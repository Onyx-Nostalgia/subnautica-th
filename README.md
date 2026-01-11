![Header](docs/img/Header.png)
# Subnautica Thai Localization (Subnautica ภาษาไทย 100%)

[![Nexus Mods](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2Fradj307%2Fe9a80731ee236cc67fb00b698e75201e%2Fraw%2F5230074dfb1a60fba917a1232f9382fa5cfec5db%2Fendpoint.json&style=for-the-badge)](https://www.nexusmods.com/subnautica/mods/2892)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=yellow&style=for-the-badge)](https://www.python.org/)
[![uv](https://img.shields.io/badge/uv-0.8.4-DE5FE9?logo=uv&style=for-the-badge)](https://github.com/astral-sh/uv)

Repository นี้เป็น Source Code สำหรับโปรเจกต์แปลภาษาไทยของเกม **Subnautica**
ภาคแรก แปลมือ + AI ช่วยในการแปลและเกลาภาษา แต่มีการตรวจสอบและแก้ไขโดยมนุษย์เพื่อความถูกต้องในทุกๆ บรรทัด (พิถีพิถัน)

สามารถดาวน์โหลดมอดเวอร์ชันพร้อมใช้งานได้ที่ 

[![Download on Nexus Mods](https://custom-icon-badges.demolab.com/badge/Download%20on%20Nexus%20Mods-da8e35.svg?logo=download&style=for-the-badge)](https://www.nexusmods.com/subnautica/mods/2892)

สำรอง:

[![Download ZIP](https://img.shields.io/badge/Download%20on%20google%20drive-EA4336?style=for-the-badge&logo=googledrive&logoColor=white)](https://drive.google.com/drive/folders/1tZ9Zq_m-CLiZdpOEon8qrfEmUMFf2zBy?usp=drive_link)

---

## 📺 วิธีการติดตั้ง (Installation)

ดูวิดีโอสอนการติดตั้งและรีวิวได้ที่นี่:
<div align="center">

[![Subnautica Thai Installation](https://img.youtube.com/vi/nvtfsFqSS6Y/0.jpg)](https://www.youtube.com/watch?v=nvtfsFqSS6Y)

*(คลิกที่รูปเพื่อดูวิดีโอ)*
</div>

---

## 🛠️ การพัฒนา (Development)

📖 อ่านคู่มือฉบับเต็มได้ที่: [Translation Guide](docs/translation_guide.md)

โปรเจกต์นี้ใช้ **[uv](https://github.com/astral-sh/uv)** ในการจัดการ Environment

### Setup

1.  Clone repository นี้
    ```bash
    git clone https://github.com/Onyx-Nostalgia/subnautica-th.git
    ```
3.  ติดตั้ง Dependencies:
    ```bash
    uv sync
    ```
4.  รันโปรแกรมหลัก:
    ```bash
    uv run main.py
    ```
5.  รันเครื่องมือแก้ไขคำแปล:
    ```bash
     uv run streamlit run editor.py 
     ```

### โครงสร้างโปรเจกต์

*   `main.py`: ไฟล์หลักสำหรับการรันโปรแกรม
*   `editor.py`: เครื่องมือสำหรับแก้ไขคำแปล
*   `agent/`: AI Agent ที่ช่วยในการแปลและเกลาภาษา
*   etc. อำนวยความสะดวกอื่นๆ

---

## ⚠️ Disclaimer (ข้อควรระวัง)

*   โปรเจกต์นี้เป็นผลงานที่จัดทำขึ้นโดย Fan-made เพื่อการศึกษาและเพื่อ Community เท่านั้น **ไม่มีความเกี่ยวข้องอย่างเป็นทางการ**กับ [**Unknown Worlds Entertainment**](https://unknownworlds.com/en)
