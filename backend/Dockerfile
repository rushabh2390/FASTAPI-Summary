FROM python:3.10-slim
RUN mkdir app
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=.
ENV NLTK_DATA /app/nltk_data/ 
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ADD nltk_data $NLTK_DATA
# RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt');nltk.download('averaged_perceptron_tagger');nltk.download('punkt_tab');"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]