import os
import tkinter as tk
from tkinter import filedialog, simpledialog

def select_folder():
    """打开文件对话框以选择文件夹"""
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory(title="选择包含图片的文件夹")
    return folder_path

def create_file_list(selected_folder, file_type):
    """根据选择的文件夹和类型创建 train.txt 或 val.txt 文件"""
    # 获取所有图片文件
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp')  # 支持的图片格式
    images = [f for f in os.listdir(selected_folder) if f.endswith(image_extensions)]
    
    if not images:
        print("所选文件夹中没有找到图片。")
        return
    
    # 生成相对路径
    relative_paths = [os.path.relpath(os.path.join(selected_folder, img), start=os.path.dirname(selected_folder)) for img in images]
    
    # 确定保存的文件名
    file_name = f"{file_type}.txt"
    
    # 将路径写入文本文件
    with open(os.path.join(selected_folder, file_name), 'w') as f:
        for path in relative_paths:
            f.write(f"{path}\n")
    
    print(f"{file_name} 已创建，包含 {len(relative_paths)} 张图片的路径。")

def main():
    # 选择要创建的文件类型
    file_type = simpledialog.askstring("输入", "请输入要创建的文件类型 (train 或 val):")
    
    if file_type not in ["train", "val"]:
        print("无效输入，请输入 'train' 或 'val'。")
        return
    
    # 选择包含图片的文件夹
    selected_folder = select_folder()
    
    if selected_folder:
        create_file_list(selected_folder, file_type)

if __name__ == "__main__":
    main()