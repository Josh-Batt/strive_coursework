import cv2
import numpy as np

path = '/solidWhiteCurve.jpg'

GREEN = (0, 255, 0)
kernel = np.ones((3, 3), np.uint8)

def get_image(path):
    image_dir = 'test_images'
    image = cv2.imread(image_dir + path)
    return image

test_image = get_image(path)
test_image_copy = test_image.copy()

blurred = cv2.GaussianBlur(test_image, (3, 3), 1)

width = test_image_copy[:, 280:750]

gray_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
inv_gray_image = ~gray_image
#image_enhanced = cv2.equalizeHist(inv_gray_image)

cropped = inv_gray_image[:, 280:750]
cropped_colour = test_image_copy[:, 280:750]

thresh_hold_image = cv2.adaptiveThreshold(inv_gray_image, 200, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 10)

closed = cv2.morphologyEx(thresh_hold_image, cv2.MORPH_OPEN, kernel)
dilated = cv2.dilate(closed, kernel, iterations=2)
cannyed = cv2.Canny(dilated, 100, 200)
#----------------------------------------------------------------
print(cannyed.shape)

cannyed_crop = cannyed[:, 280:750]
my_cropped_colour = test_image_copy[:, 280:750]
#----------------------------------------------------------------
contours, h = cv2.findContours(cannyed_crop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours_sorted = sorted(contours, key=cv2.contourArea, reverse=True)
contours_drawn = cv2.drawContours(my_cropped_colour, contours_sorted, -1, GREEN, 4, cv2.LINE_8)

canvas = np.zeros(my_cropped_colour.shape)


cv2.imshow('test', blurred)
cv2.waitKey()
cv2.destroyAllWindows()


#================================================================
# test_image_copy = test_image_copy[:, 280:750] * canvas
# test_image_copy = test_image_copy[:, 280:750] + my_cropped_colour


# def combine_two_color_images(image1, image2):
#     foreground, background = image1.copy(), image2.copy()
    
#     foreground_height = foreground.shape[0]
#     foreground_width = foreground.shape[1]
#     alpha =0.5
    
#     # do composite on the upper-left corner of the background image.
#     blended_portion = cv2.addWeighted(foreground,
#                 alpha,
#                 background[:foreground_height,:foreground_width,:],
#                 1 - alpha,
#                 0,
#                 background)
#     background[:foreground_height,:foreground_width,:] = blended_portion
#     cv2.imshow('composited image', background)

# combine_two_color_images(contours_drawn, test_image_copy)