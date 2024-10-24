import json
import os
import numpy as np

def load_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def load_txt(txt_path):
    circles = []
    with open(txt_path, 'r') as f:
        for line in f:
            x, y = map(float, line.strip().split(','))
            circles.append((x, y))
    return circles

def is_point_in_circle(px, py, cx, cy, radius):
    return (px - cx) ** 2 + (py - cy) ** 2 <= radius ** 2

def compare_circles(json_path, txt_path):
    # Load JSON and TXT data
    json_data = load_json(json_path)
    txt_circles = load_txt(txt_path)

    json_circles = []
    for shape in json_data['shapes']:
        if shape['shape_type'] == 'circle':
            # Extract circle center and radius from JSON
            x1, y1 = shape['points'][0]
            x2, y2 = shape['points'][1]
            radius = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            json_circles.append((x1, y1, radius))

    # Compare circles
    txt_in_json_count = 0
    txt_not_in_json_count = 0
    json_missed_count = 0
    checked_json = [False] * len(json_circles)

    for txt_x, txt_y in txt_circles:
        found_in_json = False
        for i, (json_x, json_y, radius) in enumerate(json_circles):
            if is_point_in_circle(txt_x, txt_y, json_x, json_y, radius):
                found_in_json = True
                checked_json[i] = True
                break
        if found_in_json:
            txt_in_json_count += 1
        else:
            txt_not_in_json_count += 1

    json_missed_count = len(json_circles) - sum(checked_json)

    print(f"JSON circles: {len(json_circles)}")
    print(f"TXT circles: {len(txt_circles)}")
    print(f"Correctly matched circles: {txt_in_json_count}")
    print(f"TXT circles not in JSON: {txt_not_in_json_count}")
    print(f"JSON circles missed in TXT: {json_missed_count}")

# Example usage
json_folder = "D:\\CGU\\odep_cellarray\\detecting_testing_data\\binaryimage_and_json\\json"
txt_folder = "D:\\CGU\\odep_cellarray\\detecting_testing_data\\binaryimage_and_json\\binary_threshold(75)\\FIND_CPARTICLES_TXT"
filename = "2024.09.19_001"  # without extension

json_path = os.path.join(json_folder, f"{filename}.json")
txt_path = os.path.join(txt_folder, f"{filename}.txt")

compare_circles(json_path, txt_path)
