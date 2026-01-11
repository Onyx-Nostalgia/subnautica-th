import json
import os
import re
import sys

from rich.console import Console

# import other from previous folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import (
    CLEANED_PATH,
    CLEANED_THAI_PATH,
    DECODED_THAI_PATH,
    ORIGINAL_ENGLISH_PATH,
    ORIGINAL_THAI_PATH,
    PARSED_PATH,
)
from utils.file_io import save_json

console = Console()


def clean_and_parse_json(text):
    # 1. ลบ Comment
    text = re.sub(r'^\s*//.*', '', text, flags=re.MULTILINE)

    # 2. Logic การซ่อม String (Value)
    # Pattern: Group(1) คือ Separator (: + whitespace), Group(2) คือ "เนื้อหา"
    pattern = r'(:\s*)("((?:[^"\\]|\\.)*)")'

    def fix_string_content(match):
        # แยกส่วนประกอบออกจากกัน
        separator = match.group(1)  # เช่น " :\t" (ห้ามไปยุ่งกับอันนี้!)
        content_block = match.group(2) # เช่น "Aurora...\n..." (ซ่อมแค่อันนี้)

        # ซ่อมเฉพาะเนื้อหา
        fixed_content = content_block.replace('\n', '\\n').replace('\r', '')
        fixed_content = fixed_content.replace('\t', ' ') # แก้ Tab ในเนื้อหา
        fixed_content = fixed_content.replace('\f', '\\f')

        # เอามาต่อกันเหมือนเดิม
        return separator + fixed_content

    text = re.sub(pattern, fix_string_content, text)

    # 3. Clean up
    text = text.strip().strip(',')

    # 4. เติมปีกกา
    if not text.startswith('{'):
        text = "{" + text + "}"

    # 5. ลบ Trailing Comma
    text = re.sub(r',\s*}', '}', text)

    # 6. Parse
    try:
        data = json.loads(text, strict=False)
        return data
    except json.JSONDecodeError as e:
        console.print(f"❌ Error parsing JSON: {e}",style="red")
        start = max(0, e.pos - 50)
        end = min(len(text), e.pos + 50)
        console.print(f"บริเวณที่ Error: ...{text[start:end]}...")
        return None

def clean_none_value(data):
    if isinstance(data, dict):
        return {k: clean_none_value(v) for k, v in data.items() if v}
    elif isinstance(data, list):
        return [clean_none_value(item) for item in data if item]
    else:
        return data

def pre_proccess():
    console.print("\nPre-processing...\n",style="bold green")
    with open(ORIGINAL_ENGLISH_PATH, 'r', encoding='utf-8') as f:
        raw_data = f.read()
    console.print(" - Parse json",style="bold yellow")
    parsed_json = clean_and_parse_json(raw_data)
    console.print(f"✅ สำเร็จ! อ่านได้ {len(parsed_json)} keys")
    save_json(parsed_json, PARSED_PATH)
    
    console.print(" - Clean none value",style="bold yellow")
    cleaned_json = clean_none_value(parsed_json)
    console.print(f"✅ สำเร็จ! เหลือ {len(cleaned_json)} keys")
    save_json(cleaned_json, CLEANED_PATH)
    
def decode_thai():
    console.print("\nDecode Thai",style="bold green")
    # Decode Original Thai JSON to verify
    with open(ORIGINAL_THAI_PATH, 'r', encoding='utf-8') as f:
        thai_data = json.load(f)

    console.print(f"อ่านได้ {len(thai_data)} keys")
    with open(DECODED_THAI_PATH, 'w', encoding='utf-8') as f:
        json.dump(thai_data, f, indent=4, ensure_ascii=False)
        console.print(f"✅ บันทึกไฟล์ {DECODED_THAI_PATH} เรียบร้อย")

def clean_thai():
    decode_thai()
    console.print("\nClean Thai",style="bold green")
    with open(DECODED_THAI_PATH, 'r', encoding='utf-8') as f:
        thai_data = json.load(f)
    cleaned_data = clean_none_value(thai_data)
    console.print(f"✅ สำเร็จ! เหลือ {len(cleaned_data)} keys")
    save_json(cleaned_data, CLEANED_THAI_PATH)

if __name__ == "__main__":
    pre_proccess()
    clean_thai()