import cv2
import numpy as np
import time
import os


def process_image(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    original_size = image.shape[1], image.shape[0]  # (width, height)

    cv2.imshow('raw', image)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    start_time = time.time()

    # Apply Gaussian blur to smooth the image
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    blurred_resized = cv2.resize(blurred, original_size)
    cv2.imshow('blurred', blurred_resized)


    # Apply threshold
    _, binary = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)
    #binary = cv2.adaptiveThreshold(bg_sub, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)
    cv2.imshow('binary', binary)

    # Erode and dilate to remove noise
    #dilate1 = cv2.dilate(binary, kernel, iterations = 2)
    #cv2.imshow('dilate1', dilate1)
    #erode1 = cv2.erode(dilate1, kernel, iterations = 2)
    #cv2.imshow('erode1', erode1)
    #erode2 = cv2.erode(erode1, kernel, iterations = 1)
    #cv2.imshow('erode2', erode2)
    #dilate2 = cv2.dilate(erode2, kernel, iterations = 1)
    #cv2.imshow('dilate2', dilate2)



    # Apply Canny edge detector to find edges
    #edges = cv2.Canny(erode2, 50, 150)
    #cv2.imshow('canny edges', edges)

    # Trace contours from the edge image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
    end_time = time.time()
    dif_time = end_time - start_time
    print(dif_time)

    # Prepare an image to draw the contours
    contour_image = np.zeros_like(image)

    # Draw each contour
    '''for contour in contours:
        for x, y in contour:
            contour_image[x, y] = 255

    # Show the resulting image
    cv2.imshow('Processed Image', contour_image)'''
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Set the directory containing your files
directory = 'D:/CGU/odep_cellarray/Testimage/2024.09.18'
# # Get a list of all tiff files
files = [f for f in os.listdir(directory) if f.endswith('.png')]
for image in files:
    image_path = os.path.join(directory, image)
#    print(image_path)
    process_image(image_path)