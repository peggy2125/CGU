import cv2
import numpy as np
import os
import time
from tkinter import Tk
from tkinter.filedialog import askdirectory
import pyautogui
import keyboard

def main():
    # 隱藏主 tkinter 視窗
    Tk().withdraw()
    

    # 打開文件對話框以選擇資料夾
    save_folderdirc = askdirectory(title="選擇存放截圖的資料夾")

    if not save_folderdirc:
        print("未選擇資料夾，程式結束。")
        return
        
    

    # 設置截圖的頻率(秒)
    screenshot_frequency = float(input("enter the screenshot frequency:"))
    screenshot_period=1/screenshot_frequency
    # 設置截圖的座標範圍
    x1, y1 = 239, 0
    
    number=0
    print("按下空白鍵開始截圖，再次按下即結束")
    
    # 等待空白鍵被按下
    keyboard.wait('space')  # 等待空白鍵按下
    #print("截圖開始，按下空白鍵停止截圖...")


      # 設置一個標誌來控制截圖循環

    while True:
        starttime=time.perf_counter()

        # 截取螢幕
        screenshot_pil = pyautogui.screenshot(region=( x1, y1, 1442, 1080))
        
        #PIL(BRG)轉換為RGB(opencv默認)
        screenshot_numpy = cv2.cvtColor(np.array(screenshot_pil), cv2.COLOR_RGB2BGR)
        
        number+=1
        # 獲取當前時間戳
        #timestamp = time.strftime("%Y%m%d_%H%M%S")
        
        # 保存截圖
        save_path = os.path.join(save_folderdirc, f"{number}.png")
        cv2.imwrite(save_path, screenshot_numpy)
        
        #print(f"已保存截圖: {save_path}")
        endtime=time.perf_counter()

        waitingtime=screenshot_period-endtime+starttime
        
        # 等待指定時間後繼續
        if waitingtime > 0:
            time.sleep(waitingtime)
        
                # 等待指定時間後繼續
                
        # 檢查是否按下空白鍵以停止截圖
        if keyboard.is_pressed('space'):
            print("截圖程序結束")
            print("截圖數量:",number)
            break



if __name__ == "__main__":
    main()
