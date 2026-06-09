look_for = "color = map"

root = "E:/SteamLibrary/steamapps/common/Europa Universalis V/game/in_game/common"
target = "C:/Users/ofgag/Documents/Paradox Interactive/Europa Universalis V/mod/eu5_urban_rights/colors.txt"

import os
from pathlib import Path

def extract_colors(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    colors = []
    for line in lines:
        if look_for in line:
            color_value = line.split('=')[1].strip()
            if "#" in color_value:
                color_value = color_value.split("#")[0].strip()
            colors.append(color_value)
    
    return colors

def main():
    all_colors = []
    for root_dir, _, files in os.walk(root):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root_dir, file)
                colors = extract_colors(file_path)
                all_colors.extend(colors)
    
    with open(target, 'w', encoding='utf-8') as output_file:
        for color in all_colors:
            output_file.write(color + '\n')

if __name__ == "__main__":
    main()