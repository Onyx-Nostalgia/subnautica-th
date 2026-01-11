# Translation Guide (คู่มือการแปล)

เอกสารนี้รวบรวมขั้นตอนการทำงาน (Step-by-step Journey) สำหรับการแปลเกม Subnautica โดยใช้เครื่องมือในโปรเจกต์นี้ ตั้งแต่การตั้งค่าเริ่มต้น ไปจนถึงการนำไฟล์เข้าเกม

---

## 🚀 1. เริ่มต้นใช้งาน (Initialization)

ก่อนที่จะเริ่มงานแปลในแต่ละ Phase เราต้องเตรียมข้อมูลตั้งต้นให้พร้อมก่อน

1.  รันโปรแกรมหลัก:
    ```bash
    uv run main.py
    ```
2.  เลือกเมนู **`0. Initialization & Setup`**
3.  ทำตามขั้นตอนย่อยในเมนูนั้นให้ครบ:
    *   **Clone Data:** ดึงไฟล์ภาษาต้นฉบับจากเกม
    *   **Pre-processing:** เตรียมไฟล์และตรวจสอบความถูกต้อง
    *   **Classification:** จัดหมวดหมู่ข้อความ
    *   **Generate Phase Mapping:** สร้างไฟล์แบ่งงานตาม Phase

---

## 📝 2. กระบวนการแปล (Translation Process)

เมื่อเตรียมข้อมูลเสร็จแล้ว เราจะเริ่มแปลโดยแบ่งงานออกเป็น 5 Phases (เลือกทำทีละ Phase)

### ขั้นตอนการทำงาน (Workflow)

#### 1. Setup Phase
เลือกเมนูหมวด 1-5 ตาม Phase ที่ต้องการทำ (เช่น `1. Setup Phase 1`) โปรแกรมจะสร้างไฟล์สำคัญ 2 ไฟล์ในโฟลเดอร์ `data/[PHASE_NAME]/`:
*   `translation_key.json`: เก็บ Key ทั้งหมดของ Phase นั้น (อ้างอิงจากต้นฉบับ)
*   `translation_progress.json`: **ไฟล์หลักในการทำงาน** ใช้เก็บสถานะการแปล

#### 2. แปลภาษา (Editing)
เราจะใช้เวลาส่วนใหญ่กับไฟล์ `translation_progress.json` โดยใช้ `editor.py` หรือแก้ไฟล์ JSON โดยตรง

**การใช้งาน Editor:**
*   เปิด Terminal ใหม่ แล้วรันคำสั่ง:
    ```bash
    uv run streamlit run editor.py
    ```
    *(สามารถดูคำสั่งนี้ได้จากเมนู 19 ในโปรแกรมหลัก)*

*   **แก้ไขเฉพาะ field `Result` เท่านั้น**
*   **Special Tags:**
    *   `[thai]` หรือ `[THAI]`: ใช้แทนค่าจาก field `Thai` (ของเดิม)
    *   `[english]` หรือ `[ENGLISH]`: ใช้แทนค่าจาก field `English` (ต้นฉบับ)
    *   *ใช้ tag เหล่านี้เพื่อลด Human Error จากการ Copy-Paste*
*   **การ Approve:** หากประโยคไหนแปลสมบูรณ์แล้ว ให้แก้ field `Approved` เป็น `true`

#### 3. ตรวจสอบและใช้ AI (Review & AI Assistance)
เลือกเมนูหมวด 6-10 (Create Review Form) เพื่อสร้างไฟล์สำหรับตรวจสอบ:
*   `translation_review.json`: ไฟล์ที่แปลง Tags (`[thai]`/`[english]`) เป็นข้อความจริงแล้ว (ห้ามแก้ไฟล์นี้ ให้กลับไปแก้ที่ progress)
*   `translation_unapproved_review.json`: รวมข้อความที่ **ยังไม่ผ่าน** การ Approve (ใช้ส่งต่อให้ AI ช่วยแปล)
*   `translation_approved_review.json`: รวมข้อความที่ **ผ่าน** การ Approve แล้ว (ใช้เป็นตัวอย่าง Context ให้ AI)

**เทคนิคสำหรับ Phase 2 (Glossary Items):**
*   Phase นี้มีคำศัพท์เยอะมาก ควรให้ความสำคัญกับการกำหนด **Glossary / Rule** ที่ชัดเจนด้วยมนุษย์ เพื่อใช้เป็นมาตรฐานสำหรับ Phase อื่นๆ และสร้าง [`agent/agent_glossary_items/glossary_format_rule.md`](/agent/agent_glossary_items/glossary_format_rule.md) ของตัวเองขึ้นมา (อาจมีได้หลายไฟล์ แล้วแต่รูปแบบการแบ่งหมวด)
*   ควรคัดกรองเฉพาะ Glossary ที่เกี่ยวข้องส่งให้ AI เพื่อลด Token และเพิ่มความแม่นยำ อย่างเช่น
    *   แยกคำศัพท์ตามหมวด (เช่น ชื่อสิ่งมีชีวิต, ชื่อวัตถุ, ชื่อสถานที่) 
    *   หรือเขียน code ทำเป็น Keyword search ตรวจสอบว่า phase ใช้ glossary ไหนบ้าง แล้วคัดกรองส่งให้ AI

#### 4. สร้างไฟล์แปลฉบับสมบูรณ์ (Phase Complete)
เมื่อแปลครบและตรวจสอบเสร็จแล้ว ให้เลือกเมนูหมวด 11-15 (Create Translation Complete)
*   โปรแกรมจะสร้างไฟล์ `translation_complete.json` ของ Phase นั้นๆ
*   ไฟล์นี้จะดึงข้อมูลจาก `translation_approved_review.json` เท่านั้น

---

## 📦 3. รวมไฟล์และติดตั้ง (Build & Deploy)

เมื่อได้ไฟล์แปลครบตามต้องการแล้ว (ไม่จำเป็นต้องครบทุก Phase ก็ได้)

1.  **รวมไฟล์ (Build Final):**
    *   เลือกเมนู **`16. Build Final Translation`**
    *   โปรแกรมจะรวม `translation_complete.json` จากทุก Phase มารวมเป็นไฟล์เดียว

2.  **นำเข้าเกม (Deploy):**
    *   เลือกเมนู **`17. Deploy to Game`**
    *   โปรแกรมจะนำไฟล์ที่รวมเสร็จแล้ว ไปวางในโฟลเดอร์เกมให้ทันที

---

## 🛠️ 4. การตรวจสอบและแก้ไข (Audit & Update)

ทำขั้นตอนนี้หลังจากได้ไฟล์ `translation_complete.json` ของ Phase นั้นๆ แล้ว (จบข้อ 2.4) แต่ต้องการตรวจสอบความถูกต้องอีกครั้งก่อนนำไปรวมไฟล์

1.  ใช้ Agent (เช่น `agent_auditor`) ช่วยตรวจสอบไฟล์ `translation_complete.json`
2.  บันทึกผลการแก้ไขเป็นไฟล์ JSON (เช่น `fixed_1.json`) ไว้ใน `agent/agent_auditor/phase_[N]_review/`
3.  เลือกเมนู **`18. Update Complete from Fixed`**
4.  ระบุ Phase และ Version ของไฟล์ Fixed เพื่ออัปเดตข้อมูลกลับเข้าสู่ `translation_complete.json`
5.  เมื่อมั่นใจแล้ว ค่อยไปทำขั้นตอน **3. รวมไฟล์และติดตั้ง (Build & Deploy)** ต่อไป
