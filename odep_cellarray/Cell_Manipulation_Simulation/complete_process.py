import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog,simpledialog
import os


# getting image or cut from video
def get_image_from_ccd(frame):


#circular buffer
def

#using light bar to clean array area
def generate_light_bar(array_rectangle_size,width_of_bar, moving_pixel_in_one_frame, canvas, raw_image, frame_of_lightimage):
    particles_list=[]
    #detect particles in array area(from raw_image)
    particles_list.append[]
    while len(particles_list)!=0: #????
        while bar_x_position >= -width_of_bar-10:
                display_img = canvas.copy()
                # update light bar(moving)
                bar_x_position -=  moving_pixel_in_one_frame
                cv2.rectangle(display_img, (bar_x_position, 0), (bar_x_position + width_of_bar, array_rectangle_size), (255, 255, 255), thickness=cv2.FILLED)
                # show the frame
                cv2.imshow('Animation', display_img)
                # 每幀延遲33毫秒（約30幀每秒）
                if cv2.waitKey(frame_of_lightimage) & 0xFF == ord('q'):
                    break

        #detect particles in array area
        #update particle list
    

# particles detection
def particles_detection(raw_image)
    all_coordinates=[]
    


















#main function
def main():

#setting frame
    root = tk.Tk()
    root.withdraw()
    frame = simpledialog.askinteger("Input", "Enter the frame (integer):")
    frame=int(frame)
# getting image or cut from video and put into circular buffer
    get_image_from_ccd(frame)

#setting list
    obstacle_coordinates=[]

#setting array 
    array_rectangle_size= 150 

#create a image to displaying light image
    canvas_width = 1442
    canvas_height = 1080
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
    frame_of_lightimage=    #set the frame of showing light image
    
    #using light bar to clean array area
    width_of_bar=
    rate = #tranfer into how much pixel to move in one frame
    moving_pixel_in_one_frame=
    generate_light_bar(array_rectangle_size,width_of_bar, moving_pixel_in_one_frame,canvas,frame_of_lightimage)
    #check if the particle in array area were clear
    
    ##get image from circular buffer
    for raw_image in circular_buffer: 
        # complete process
        target_coordinates=[]
        all_coordinates=[]
        while len(target_coordinates)!=4:
        
        
    

