import cv2
import numpy as np
import time
import os


def process_image(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Failed to load image: {image_path}")
    scale_percent = 50  # 缩放比例
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    start_time = time.time()
    
    # Apply Gaussian blur to smooth the image
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply threshold
    _, binary = cv2.threshold(blurred, 75, 255, cv2.THRESH_BINARY)
    #binary = cv2.adaptiveThreshold(bg_sub, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)
       # 缩放图像
    binary_resized = cv2.resize(binary, dim, interpolation=cv2.INTER_AREA)

    # 显示缩放后的图像
    cv2.imshow('resized_binary', binary_resized)


 
    end_time = time.time()
    dif_time = end_time - start_time
    print(dif_time)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return binary

# Set the directory containing your files
directory = "D:/CGU/odep_cellarray/gray_whole_rawimage_and_json"
# # Get a list of all tiff files
num=0
files = [f for f in os.listdir(directory) if f.endswith('.png')]
for image in files:
    num+=1
    image_path = os.path.join(directory, image)
    print(num)
    binary=process_image(image_path)
    base_filename = os.path.basename(image_path)  # 获取原文件名
    output_folder = "D:\\CGU\\odep_cellarray\\binaryimage_and_json\\binary_threshold(75)"
    output_path = os.path.join(output_folder, base_filename)  # 指定输出路径
    cv2.imwrite(output_path, binary)  # 保存图像
    print(f"Saved resized image to {output_path}")