import enum
import nltk
import os
from nltk import tag
import re
from nltk.corpus import stopwords
from nltk.corpus.reader import tagged, wordlist
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from line import line
from term import Term
stop_words = set(stopwords.words('english'))
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Folder Path
# path = "test"

# Change the directory
# os.chdir(path)
weight_dict = {
    "noun": 0.2,
    "adjective": 0.1,
    "adverb": 0.1,
    "verb": 0.1
}
NOUN = ["NN", "NNS", "NNP", "NNPS"]
ADVERB = ["RB", "RBS", "RBR"]
ADJECTIVE = ["JJ", "JJR", "JJS"]
VERB = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]


def generate_metadata_summary(countriesStr):
    lines_object = []
    words_object = []
    file_content_length = 0
    probable_metadata = []
    NOUNTERM = []
    ADVERBTERM = []
    VERBTERM = []
    ADJECTIVETERM = []
    remove_newline = []
    lines = re.split('[.!\?]', countriesStr)
    lines = [x.replace("\n", "") for x in lines]
    lines = [x.strip() for x in lines]
    for idx, l in enumerate(lines):
        if l == "":
            remove_newline.append(idx)
    remove_newline.reverse()
    for l in remove_newline:
        lines.pop(l)

    for x in lines:
        xindex = 0
        line_obj = line()
        line_obj.set(x, countriesStr.find(x), countriesStr.find(x)+len(x)-1)
        file_content_length += len(x)
        lines_object.append(line_obj)
        wordsList = nltk.word_tokenize(x)
        tagged = nltk.pos_tag(wordsList)
        stopword_ind = []
        for idx, tag in enumerate(tagged):
            if tag[0].lower() in stop_words or tag[0] in ['.', ',', ':']:
                stopword_ind.append(idx)
        stopword_ind.reverse()
        for l in stopword_ind:
            tagged.pop(l)
        ps = PorterStemmer()
        for tag in tagged:
            stem_word = ps.stem(tag[0])
            if len(words_object) > 0:
                is_found = False
                for idx, elem in enumerate(words_object):
                    if elem.stem_word == stem_word:
                        is_found = True
                        is_tag_match = False
                        # elem.words.append(tag[0].lower())
                        if tag[0].lower() in elem.words:
                            for ind, item in enumerate(elem.words):
                                if tag[0].lower() == item:
                                    if tag[1] == elem.grammar_term[ind]:
                                        is_tag_match = True
                                        elem.grammar_word_count[ind] = int(
                                            elem.grammar_word_count[ind]) + 1
                                        indposition = xindex+line_obj.getstartindex()
                                        break
                            if is_tag_match is False:
                                elem.words.append(tag[0].lower())
                                elem.grammar_term.append(tag[1])
                                elem.grammar_word_count.append(1)
                                indposition = xindex+line_obj.getstartindex()

                            elem.addindex(indposition)
                            elem.count += 1
                if is_found is False:
                    t = Term()
                    t.setproperty(stem_word, tag[0].lower(), tag[1])
                    indposition = xindex+line_obj.getstartindex()
                    t.addindex(indposition)
                    words_object.append(t)
            else:
                t = Term()
                t.setproperty(stem_word, tag[0].lower(), tag[1])
                indposition = xindex
                t.index.append(indposition)
                words_object.append(t)
            xindex += 1
    max_word = max(x.count for x in words_object)
    for wordelem in words_object:
        wordelem.word_weight = wordelem.count/max_word
        for idx, gt in enumerate(wordelem.grammar_term):
            if gt in NOUN:
                if wordelem not in NOUNTERM:
                    wordelem.word_weight += (
                        wordelem.grammar_word_count[idx] * weight_dict["noun"])
                    NOUNTERM.append(wordelem)
            elif gt in ADVERB:
                if wordelem not in ADVERBTERM:
                    wordelem.word_weight += (
                        wordelem.grammar_word_count[idx] * weight_dict["adverb"])
                    ADVERBTERM.append(wordelem)
            elif gt in ADJECTIVE:
                if wordelem not in ADJECTIVETERM:
                    wordelem.word_weight += (
                        wordelem.grammar_word_count[idx] * weight_dict["adjective"])
                    ADJECTIVETERM.append(wordelem)
            elif gt in VERB:
                if wordelem not in VERBTERM:
                    wordelem.word_weight += (
                        wordelem.grammar_word_count[idx] * weight_dict["verb"])
                    VERBTERM.append(wordelem)

    words_object = sorted(
        words_object, key=lambda x: x.word_weight, reverse=True)
    NOUNTERM = sorted(NOUNTERM, key=lambda x: x.word_weight, reverse=True)
    VERBTERM = sorted(VERBTERM, key=lambda x: x.word_weight, reverse=True)
    ADVERBTERM = sorted(ADVERBTERM, key=lambda x: x.word_weight, reverse=True)
    ADJECTIVETERM = sorted(
        ADJECTIVETERM, key=lambda x: x.word_weight, reverse=True)
    probable_metadata_index = []

    for i in range(5):
        if i < len(NOUNTERM):
            probable_metadata.extend(NOUNTERM[i].getword())
            probable_metadata_index.extend(NOUNTERM[i].index)
        if i < len(VERBTERM):
            probable_metadata.extend(VERBTERM[i].getword())
            probable_metadata_index.extend(VERBTERM[i].index)
        if i < len(ADVERBTERM):
            probable_metadata.extend(ADVERBTERM[i].getword())
            probable_metadata_index.extend(ADVERBTERM[i].index)
        if i < len(ADJECTIVETERM):
            probable_metadata.extend(ADJECTIVETERM[i].getword())
            probable_metadata_index.extend(ADJECTIVETERM[i].index)

    probable_metadata_index.sort()
    probable_metadata = set(probable_metadata)
    probable_summmary = ""
    for ind in probable_metadata_index:
        for l in lines_object:
            if ind >= l.getstartindex() and ind <= l.getendindex():
                l.metadatacount += 1
    lines_object = sorted(
        lines_object, key=lambda x: x.metadatacount, reverse=True)
    summary_line_limit = len(lines_object)//3
    for i in range(summary_line_limit):
        if probable_summmary == "":
            probable_summmary = lines_object[i].getlinecontent()+"."
        else:
            probable_summmary += lines_object[i].getlinecontent()+"."
    return ', '.join(probable_metadata), probable_summmary
