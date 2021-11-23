import cv2 
import numpy as np


def neighbours1(x,y,image):
    """Return 8-neighbours of image point P1(x,y), in a clockwise order"""
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1;
    img[x_1][y]=0
    img[x_1][y1]=0
    img[x][y1]=0
    img[x1][y1]=0
    img[x1][y]=0
    img[x1][y_1]=0
    img[x][y_1]=0
    img[x_1][y_1]=0

def neighbours(x,y,image):
    """Return 8-neighbours of image point P1(x,y), in a clockwise order"""
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1;
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1], img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]   


def getSkeletonIntersection(skeleton):
    """ Given a skeletonised imag,e it will give the coordinates of the intersections of the skeleton.

    Keyword arguments:
    skeleton -- the skeletonised image to detect the intersections of

    Returns: 
    List of 2-tuples (x,y) containing the intersection coordinates
    """
    # A biiiiiig list of valid intersections             2 3 4
    # These are in the format shown to the right         1 C 5
    #                                                    8 7 6 
    validIntersection = [[0,1,0,1,0,0,1,0],[0,0,1,0,1,0,0,1],[1,0,0,1,0,1,0,0],
                         [0,1,0,0,1,0,1,0],[0,0,1,0,0,1,0,1],[1,0,0,1,0,0,1,0],
                         [0,1,0,0,1,0,0,1],[1,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,1],
                         [0,1,0,1,0,0,0,1],[0,1,0,1,0,1,0,0],[0,0,0,1,0,1,0,1],
                         [1,0,1,0,0,0,1,0],[1,0,1,0,1,0,0,0],[0,0,1,0,1,0,1,0],
                         [1,0,0,0,1,0,1,0],[1,0,0,1,1,1,0,0],[0,0,1,0,0,1,1,1],
                         [1,1,0,0,1,0,0,1],[0,1,1,1,0,0,1,0],[1,0,1,1,0,0,1,0],
                         [1,0,1,0,0,1,1,0],[1,0,1,1,0,1,1,0],[0,1,1,0,1,0,1,1],
                         [1,1,0,1,1,0,1,0],[1,1,0,0,1,0,1,0],[0,1,1,0,1,0,1,0],
                         [0,0,1,0,1,0,1,1],[1,0,0,1,1,0,1,0],[1,0,1,0,1,1,0,1],
                         [1,0,1,0,1,1,0,0],[1,0,1,0,1,0,0,1],[0,1,0,0,1,0,1,1],
                         [0,1,1,0,1,0,0,1],[1,1,0,1,0,0,1,0],[0,1,0,1,1,0,1,0],
                         [0,0,1,0,1,1,0,1],[1,0,1,0,0,1,0,1],[1,0,0,1,0,1,1,0],
                         [1,0,1,1,0,1,0,0]]
    image = skeleton.copy();
    image = image/255;
    intersections = list();
    for x in range(1,len(image)-1):
        for y in range(1,len(image[x])-1):
            # If we have a white pixel
            if image[x][y] == 1:
                nb= neighbours(x,y,image);
                valid = True;
                if nb in validIntersection:
                    intersections.append((y,x));
    # Filter intersections to make sure we don't count them twice or ones that are very close together
    for point1 in intersections:
        for point2 in intersections:
            if (((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) < 10**2) and (point1 != point2):
                intersections.remove(point2);
    # Remove duplicates
    intersections = list(set(intersections));
    return intersections;


img=cv2.imread('fishdemo.png',0)
img1=cv2.imread('fishdemo.png',0)

res = cv2.resize(img,(1000,500), interpolation = cv2.INTER_CUBIC)

##cv2.imshow("original image before",img)
##cv2.imshow("resize image",res)

img=res

cv2.imshow("original image",img1)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)
 
##ret,img = cv2.threshold(img,127,255,0)
ret,img = cv2.threshold(img,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
 
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
 
    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True
 
##cv2.imshow("skel",skel)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
points=getSkeletonIntersection(skel)
cv2.imshow("skel",skel)
rows,cols=skel.shape

for i in range(0,rows):
    for j in range(0,cols):
        if(skel[i,j]!=0):
            print(i,j,skel[i,j])
        if ((j,i) in points):
            neighbours1(i,j,img)
            y= np.zeros((rows,cols,3),np.uint8)
            print ('hello')
##            skel[i,j]=0


##cv2.imshow("zero-img",skel)
       
print('points',points)

##for j in points:
##    print(j[0],j[1],skel[j[1],j[0]])
##    skel[j[1],j[0]]=0
##    print(skel[j[1],j[0]])
##cv2.imshow("hoperesult",skel)
##cv2.imwrite("bshape-1write.png", skel)
cv2.imwrite("fish-demo-zero-pixel.png",img)
