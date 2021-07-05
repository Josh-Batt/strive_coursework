import cv2
import numpy as np

path = '/solidWhiteCurve.jpg'

GREEN = (0, 255, 0)
kernel = np.ones((3, 3), np.uint8)

def get_image(path):
    image_dir = 'test_images'
    image = cv2.imread(image_dir + path)
    return image

def imshow(title, img):
    cv2.imshow(title, img)
    cv2.waitKey()
    cv2.destroyAllWindows()

test_image = get_image(path)
test_image_copy = test_image.copy()

gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
image_enhanced = cv2.equalizeHist(gray_image)

imshow('hello0', gray_image)
#================================================================

#-----Converting image to LAB Color model----------------------------------- 
# lab= cv2.cvtColor(test_image, cv2.COLOR_BGR2LAB)

# #-----Splitting the LAB image to different channels-------------------------
# l, a, b = cv2.split(lab)
# imshow('l_channel', l)
# imshow('a_channel', a)
# imshow('b_channel', b)

# #-----Applying CLAHE to L-channel-------------------------------------------
# clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
# cl = clahe.apply(l)
# imshow('CLAHE output', cl)

# #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
# limg = cv2.merge((cl,a,b))
# imshow('limg', limg)

# #-----Converting image from LAB Color model to RGB model--------------------
# final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
# imshow('final', final)

#================================================================

blurred = cv2.GaussianBlur(test_image, (3, 3), 1)
height = int(test_image.shape[0] * .67)

inv_gray_image = ~gray_image
imshow('asd', inv_gray_image)

cropped = inv_gray_image[height:, :]
cropped_colour = test_image_copy[height:, :]

thresh_hold_image = cv2.adaptiveThreshold(cropped, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 10)

closed = cv2.morphologyEx(thresh_hold_image, cv2.MORPH_OPEN, kernel)
dilated = cv2.dilate(closed, kernel, iterations=2)
cannyed = cv2.Canny(dilated, 100, 200)

cannyed_crop = cannyed[:, 280:750]
my_cropped_colour = cropped_colour[:, 280:750]

contours, h = cv2.findContours(cannyed_crop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_sorted = sorted(contours, key=cv2.contourArea, reverse=True)
contours_drawn = cv2.drawContours(my_cropped_colour, contours_sorted, -1, GREEN, 4, cv2.LINE_8)

canvas = np.zeros(my_cropped_colour.shape)

# test_image_copy = test_image_copy[:, 280:750] * canvas
# test_image_copy = test_image_copy[:, 280:750] + my_cropped_colour