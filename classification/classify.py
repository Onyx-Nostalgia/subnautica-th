import json
import os
import re
import sys

from rich import print

# import config from previous folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import CLASSIFIED_PATH, CLEANED_PATH, ORIGINAL_ENGLISH_PATH
from utils.file_io import save_json

with open(ORIGINAL_ENGLISH_PATH, 'r', encoding='utf-8') as f:
    source_code = f.read()

# --- 1. Regex Definitions ---
regex_decoration = re.compile(r"^\s*\/{2,}\s*$")
regex_big = re.compile(r"^\s*\/{2,}\s*(?!https?:\/\/|\/\/)(.*?)\s*\/{2,}\s*$")
regex_normal = re.compile(r"^\s*\/{2,}(?!\/)\s*(?!https?:\/\/|\/\/)(.*?)\s*$")

# [แก้จุดที่ 1] เอา ^ ออก เพื่อให้หาเจอได้ทุกที่ในบรรทัด ไม่ใช่แค่ต้นบรรทัด
regex_key = re.compile(r'"([^"]+)"\s*:') 

# --- 2. Processing Loop ---
raw_data = {}           
current_parent = None
current_category = "Uncategorized"

# Init first category
if current_category not in raw_data:
    raw_data[current_category] = []

lines = source_code.strip().split('\n')

for line in lines:
    line = line.strip()
    
    # Skip Empty & Decoration
    if not line or regex_decoration.match(line):
        continue

    # Case: Big Topic (Parent)
    match_big = regex_big.match(line)
    if match_big:
        title = match_big.group(1).strip()
        if title:
            current_parent = title
            current_category = title
            if current_category not in raw_data:
                raw_data[current_category] = []
        continue

    # Case: Normal Topic (Child/Root)
    match_normal = regex_normal.match(line)
    if match_normal:
        title = match_normal.group(1).strip()
        if title:
            if current_parent:
                current_category = f"{current_parent}.{title}"
            else:
                current_category = title
            
            if current_category not in raw_data:
                raw_data[current_category] = []
        continue

    # [แก้จุดที่ 2] ใช้ findall เพื่อหาทุก Key ที่ซ่อนอยู่ในบรรทัดนั้น
    found_keys = regex_key.findall(line)
    if found_keys:
        # found_keys จะได้ list เช่น ['Locked_Door', 'Sealed_Door']
        # ใช้ extend เพื่อยัดทั้งก้อนเข้าไปใน list ของ category นั้นเลย
        raw_data[current_category].extend(found_keys)

# --- 3. Prepare Output ---
output_list = []
output_json = {}
total_categories = 0
total_keys = 0

with open(CLEANED_PATH, 'r', encoding='utf-8') as f:
    cleaned_data = json.load(f)

cleaned_keys = set(cleaned_data.keys())

for category, keys in raw_data.items():
    if keys:
        _keys = list(set(keys).intersection(cleaned_keys))
        _keys = sorted(_keys, key=lambda x: keys.index(x))
        if _keys:
            output_list.append({
                "category": category,
                "count": len(keys),
                "keys": _keys
            })
            
            total_categories += 1
            total_keys += len(_keys)
            for k in _keys:
                if category not in output_json:
                    output_json[category] = {}
                output_json[category][k] = cleaned_data[k]

# --- 4. Write to File ---
output_filename = CLASSIFIED_PATH
save_json(output_json, output_filename)
# save_json(output_list, output_filename_old)


# --- 5. Statistics ---
print("-" * 30)
print("📊 สรุปผลข้อมูล (Summary)")
print("-" * 30)
print(f"🔹 จำนวนหมวดหมู่ (Categories): {total_categories:,} หมวด")
print(f"🔹 จำนวนคีย์ทั้งหมด (Total Keys): {total_keys:,} คีย์")
print("-" * 30)
print("Verifying...")
print("Expect Key Count: {:,} keys".format(len(cleaned_keys)))
if total_keys != len(cleaned_keys):
    print("❌ จำนวน Keys ไม่ถูกต้อง (Actual: {:,} vs Expected: {:,})".format(total_keys, len(cleaned_keys)))
else:
    print("✅ จำนวน Keys ถูกต้อง")
print("=" * 30)