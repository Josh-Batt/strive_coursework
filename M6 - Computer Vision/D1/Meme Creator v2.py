import cv2
#import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline

def meme(path, text):
    img = cv2.imread(path, 3)
    #rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    clone = img.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    textsize = cv2.getTextSize(text, font, 1, 2)[0]
    textX = (img.shape[1] - textsize[0]) / 2
    textY = (img.shape[0] + textsize[1]) / 2
    #org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    clone = cv2.putText(clone, text, (textX, textY), font, 
                    fontScale, color, thickness, cv2.LINE_AA)

    cv2.imshow('Meme', clone)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('/bike with flowers.jpg', 3)

print(type(img))
# cv2.imshow('123', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#meme('cropped dog.jpg', 'testing')