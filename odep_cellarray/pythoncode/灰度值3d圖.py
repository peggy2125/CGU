import cv2
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askdirectory

def select_png_directory():
    # 隱藏主 tkinter 視窗
    Tk().withdraw()
    
    # 打開文件對話框以選擇資料夾
    folder_path = askdirectory(title="選擇含有json標記檔的資料夾")
    return folder_path

# Function to read images from a specified folder and plot 3D grayscale values
def plot_grayscale_3d(folder_path):
    # List to hold grayscale values
    gray_values = []

    # Read all images from the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Check for image file extensions
            img_path = os.path.join(folder_path, filename)
            # Read the image in grayscale
            gray_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if gray_image is not None:
                # Append grayscale values to the list
                gray_values.append(gray_image)

    # Convert list of images to a 3D numpy array (height, width, number of images)
    gray_stack = np.array(gray_values)

    # Get dimensions for plotting
    height, width, num_images = gray_stack.shape

    # Create a meshgrid for x and y coordinates
    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)

    # Plotting each image's grayscale values in 3D
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    for i in range(num_images):
        z = gray_stack[i]  # Get grayscale values for the current image
        ax.plot_surface(x, y, z, cmap='gray', alpha=0.5)  # Plot with transparency

    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_zlabel('Grayscale Value')
    plt.title('3D Grayscale Values from Images')
    plt.show()


# Specify the folder path containing the images
folder_path = select_png_directory()
plot_grayscale_3d(folder_path)