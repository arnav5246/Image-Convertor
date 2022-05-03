#This program converts an image into pencil sketch

#pip install opencv-python

#import library

import cv2

#get image location and image file name
img_location = 'E:/SELF WORK/ARJ EXTRA PROJECTS/IMAGE SOURCES/'
file_name = 'cat_and_dog.jpg'

#read the image
img = cv2.imread(img_location + file_name)

#convert the image to gray scale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#invert the image
inverted_gray_image = 255 - gray_image

#blur the image by gaussian function
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

#invert the blurred image
inverted_blurred_img = 255 - blurred_img

#create the pencil sketch image
pencil_sketch_img = cv2.divide(gray_image, inverted_blurred_img, scale=256.0)


#show the image
cv2.imshow('Original Image', img)
cv2.imshow('New Image 1', gray_image)
cv2.imshow('New Image 2', inverted_gray_image)
cv2.imshow('New Image 3', blurred_img )
cv2.imshow('New Image 4', inverted_blurred_img)
cv2.imshow('New Image 5', pencil_sketch_img)
cv2.waitKey(0)

