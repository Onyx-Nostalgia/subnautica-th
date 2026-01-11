import os
import pathlib
import re
import sys

# import config from previous folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rich import print

from config import CLASSIFIED_TREE_PATH, ORIGINAL_ENGLISH_PATH

def run_category_tree():
    with open(ORIGINAL_ENGLISH_PATH, 'r', encoding='utf-8') as f:
        source_code = f.read()

    # --- 1. Regex & Parsing Logic ---
    regex_decoration = re.compile(r"^\s*\/{2,}\s*$")
    regex_big = re.compile(r"^\s*\/{2,}\s*(?!https?:\/\/|\/\/)(.*?)\s*\/{2,}\s*$")
    regex_normal = re.compile(r"^\s*\/{2,}(?!\/)\s*(?!https?:\/\/|\/\/)(.*?)\s*$")

    output_structure = []
    current_parent = None

    lines = source_code.strip().split('\n')

    for line in lines:
        line = line.strip()
        
        if not line or regex_decoration.match(line):
            continue
            
        match_big = regex_big.match(line)
        if match_big:
            title = match_big.group(1).strip()
            if title:
                new_parent = {"title": title, "type": "parent", "children": []}
                output_structure.append(new_parent)
                current_parent = new_parent
                continue

        match_normal = regex_normal.match(line)
        if match_normal:
            content = match_normal.group(1).strip()
            if content:
                if current_parent:
                    current_parent["children"].append(content)
                else:
                    output_structure.append({"title": content, "type": "root"})
                    

    # --- 2. Logic การ Save ลงไฟล์ (output.txt) ---

    # Make sure the directory exists
    pathlib.Path(os.path.dirname(CLASSIFIED_TREE_PATH)).mkdir(parents=True, exist_ok=True)

    # ใช้ encoding='utf-8' เพื่อรองรับภาษาไทย
    with open(CLASSIFIED_TREE_PATH, "w", encoding="utf-8") as f:
        
        # ส่วนที่ 1: เขียนโครงสร้าง Tree
        f.write("--- Structure Report ---\n")
        for item in output_structure:
            if item['type'] == 'root':
                f.write(f"- {item['title']}\n")
            elif item['type'] == 'parent':
                f.write(f"- {item['title']}\n")
                for child in item['children']:
                    f.write(f"    - {child}\n")
        
        f.write("\n" + "="*40 + "\n\n")

        # ส่วนที่ 2: เขียนสถิติ (Statistics)
        total_parents = 0
        total_children = 0
        total_roots = 0

        f.write("--- Statistics ---\n")
        for item in output_structure:
            if item['type'] == 'parent':
                total_parents += 1
                child_count = len(item['children'])
                total_children += child_count
                f.write(f"Category: {item['title']:<20} | Count: {child_count}\n")
            elif item['type'] == 'root':
                total_roots += 1
                
        f.write("-" * 30 + "\n")
        f.write(f"Total Parents:  {total_parents}\n")
        f.write(f"Total Children: {total_children}\n")
        f.write(f"Total Roots:    {total_roots}\n")
        f.write(f"Total Items:    {total_parents + total_children + total_roots}\n")

    print(f"✅ บันทึกข้อมูลเรียบร้อยแล้วที่ไฟล์: {CLASSIFIED_TREE_PATH}")

    # --- 3. Print ดูคร่าวๆ หน้าจอ (Optional) ---
    print(f"Total found: {total_parents + total_children + total_roots} items.")

if __name__ == "__main__":
    run_category_tree()