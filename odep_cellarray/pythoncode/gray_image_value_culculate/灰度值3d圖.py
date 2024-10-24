import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askdirectory
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

def select_png_directory():
    # 隱藏主 tkinter 視窗
    Tk().withdraw()
    
    # 打開文件對話框以選擇資料夾
    folder_path = askdirectory(title="選擇含有圖片的資料夾")
    return folder_path

# Function to read images from a specified folder and plot 3D grayscale values as a surface
def plot_grayscale_surface(folder_path):
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

    # Convert list of images to a 3D numpy array (number of images, height, width)
    gray_stack = np.array(gray_values)

    # Only use the first image for plotting (if multiple images exist)
    z = gray_stack[0]  # Assuming we use the first image in the folder

    # Get dimensions for plotting
    height, width = z.shape

    # Create a meshgrid for x and y coordinates
    x = np.linspace(0, width, width)
    y = np.linspace(0, height, height)
    x, y = np.meshgrid(x, y)

    # Plotting the image's grayscale values in 3D as a surface
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface with z representing the grayscale value, and color mapping to show height
    surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')  # 'viridis' colormap for colorful 3D surface

    # Add a color bar to map the grayscale values to colors
    fig.colorbar(surf)

    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.set_zlabel('Grayscale Value')
    plt.title('3D Grayscale Surface from Image with Color')
    plt.show()


    x = np.arange(width)
    y = np.arange(height)
    x, y = np.meshgrid(x, y)
    # Filtering points with z (grayscale values) < 100
    filtered_points = np.column_stack(np.where(z < 100)& (y >= 45) & (y <= 1013))

    print("Coordinates with grayscale value < 100:")
    for point in filtered_points:
        print(f"X: {point[1]}, Y: {point[0]}")

# Specify the folder path containing the images
folder_path = select_png_directory()
plot_grayscale_surface(folder_path)
