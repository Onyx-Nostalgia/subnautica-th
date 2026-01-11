# Subnautica Thai Localization: Glossary & Formatting Rules

เอกสารนี้รวบรวมคำศัพท์เฉพาะ (Glossary) และกฎการจัดรูปแบบ (Formatting Rules) เพื่อใช้เป็นมาตรฐานอ้างอิงในการแปลภาษาไทย

---

## 1. 📏 Formatting & Translation Patterns (รูปแบบและกฎการแปล)

กฎเหล่านี้ใช้สำหรับการแปลงประโยคที่มีโครงสร้างซ้ำๆ หรือคำศัพท์เฉพาะทางเทคนิค

| English Pattern | Thai Format / Rule | Example |
| :--- | :--- | :--- |
| **{ITEM} blueprint** | พิมพ์เขียว {ITEM} | "Bioreactor blueprint" -> "พิมพ์เขียว เครื่องปฏิกรณ์ชีวภาพ" // มี space ด้วย|
| **{ITEM} fragment** | ชิ้นส่วน {ITEM} | "Seamoth fragment" -> "ชิ้นส่วน ซีมอธ" // มี space ด้วย|
| **{ITEM} sample** | ตัวอย่าง {ITEM} | "Brain coral sample" -> "ตัวอย่าง ปะการังสมอง" // มี space ด้วย|
| **Break {ITEM}** | ทุบ{ITEM} | "Break limestone outcrop" -> "ทุบชั้นหินปูน" |
| **Plans for building a {ITEM}** | แผนผังสร้าง {ITEM} |  "Plans for building a bioreactor" -> "แผนผังสร้าง เครื่องปฏิกรณ์ชีวภาพ" // มี space ด้วย|
| **{ITEM} hatch from these.** | {ITEM} ฟักออกมาแล้ว | "Bonesharks hatch from these." -> "ฉลามกระดูก ฟักออกมาแล้ว" // มี space ด้วย|
| **Use {ITEM}** | ใช้{ITEM} | "Use fabricator" -> "ใช้เครื่องประดิษฐ์" |
| **Enter {VEHICLE}** | เข้า{VEHICLE} | "Enter prawn" -> "เข้าชุด PRAWN" |

### กฎเพิ่มเติม
*   **Parentheses in Headers:** สำหรับหัวข้อ (Title) ของสิ่งมีชีวิต, ไบโอม, หรือเทคโนโลยีสำคัญ สามารถคงวงเล็บชื่อภาษาอังกฤษไว้ได้ เพื่อความชัดเจนในการอ้างอิงกับข้อมูลในเกม (เช่น "งูปู (Crabsnake)")
*   **EncyDesc_ Header Rules:**
    *   **✅ ใส่ Header เมื่อ:**
        *   เป็นศัพท์เฉพาะทางเทคนิค/ชื่อเฉพาะมากๆ (Proper Noun/Technical Term) ที่ควรรู้ชื่ออังกฤษ (เช่น ชื่อปลา, พืช, เทคโนโลยี)
        *   เป็นชื่อสถานที่สำคัญ (Major Locations) เช่น เขตไบโอม
        *   เป็นข้อมูลวิจัย/รายงานทางเทคนิค (Research Data/Reports) เช่น "ข้อมูลการวิจัย... (Research Data)", "รายงานความเสียหาย (Damage Report)"
    *   **❌ ไม่ใส่ Header เมื่อ:**
        *   เป็นคำทั่วไป/เข้าใจง่าย (Common Terms) เช่น "ไข่...", "ซาก...", "กระดูก..."
        *   Logs/Emails/Transmissions เช่น "บันทึกของ...", "เมนูวันนี้"
        *   รายงานสถานะ/การอัปเดตข้อมูล (Status Updates) ที่ไม่ใช่การอธิบายรายละเอียดสิ่งนั้นๆ โดยตรง
*   **O₂ Symbol:** อนุญาตให้ใช้สัญลักษณ์ **"O₂"** ในชื่อไอเท็มหรือข้อความที่ต้องการความกระชับ (เช่น "ถัง O₂ มาตรฐาน")
*   **Color "Blue":** ให้พิจารณาบริบทภาพในเกม
    *   ส่วนใหญ่ใช้ **"สีฟ้า"** (Cyan/Light Blue) โดยเฉพาะกับเทคโนโลยีต่างดาว, พืช, ปะการัง (เช่น "แท็บเล็ตสีฟ้า", "ปะการังโต๊ะสีฟ้า")
    *   ใช้ **"สีน้ำเงิน"** (Dark Blue) กับวัตถุที่เป็นสีน้ำเงินเข้มจริงๆ (เช่น "หมวกสีน้ำเงิน")
*   **Cut Content:** หากพบเนื้อหาที่ถูกตัดออกจากเกม (Cut Content) เช่น **Terraformer**, **Transfuser** ไม่จำเป็นต้องสนใจความถูกต้องของการแปล หรือจะทับศัพท์ไปเลยก็ได้ ขอเพียงแค่ **ไม่ใช่ค่าว่าง**
*   **Prawn Suit Notifications:** คำแจ้งเตือนหรือคำทักทายจากชุด Prawn (เช่น `ExosuitWelcomeAboard`) ไม่ต้องเปลี่ยน "PRAWN:" เป็น "ชุด PRAWN:" ให้คงเดิมไว้ หรือหากเป็นป้ายชื่อ (Sign_) ก็ไม่ต้องแก้
*   **Specific Item Names:**
    *   **Tank Names:** ไม่ต้องแก้ชื่อถังออกซิเจน ให้ใช้ชื่อเดิมที่กระชับเหมาะสมแล้ว (เช่น "ถัง O₂ มาตรฐาน")
*   อย่าแปล **indigenous** ว่า "พื้นเมือง" ❌ ให้ใช้เป็นคำว่า "พื้นถิ่น" ✅ เช่น "สิ่งมีชีวิตพื้นถิ่น" ✅
*   เพิ่ม space แบ่งประโยคไม่ให้ยาวจนเกินไป ป้องกันการทำให้ UI แสดงผลไม่สวยงาม เช่นกรณี "เลือกส่วนประกอบพื้นฐานจากเมนูและวางในตำแหน่งที่เหมาะสม" คือยาวเกินไป ต้องมีการเว้นวรรคบ้าง อาจจะแบ่งเป็น "เลือกส่วนประกอบพื้นฐานจากเมนู และวางในตำแหน่งที่เหมาะสม" เป็นต้น 
*   **บริบทคำว่า Health:**
    *   **สุขภาพ** (สำหรับสิ่งมีชีวิต, ผู้เล่น)
    *   **ความทนทาน** (สำหรับยานพาหนะ, ฐาน, สิ่งก่อสร้าง)

---

## 2. 🚀 Vehicles (ยานพาหนะ)

| English | Thai Translation |
| :--- | :--- |
| **Cyclops** | ไซคลอปส์ |
| **Seamoth** | ซีมอธ |
| **Prawn suit / Exo suit** | ชุด PRAWN |
| **Neptune** | เนปจูน |
| **Lifepod / Escapepod** | ยานชูชีพ |
| **Mobile vehicle bay** | อู่ต่อยานฉบับพกพา |
| **Vehicle upgrade console** | คอนโซลอัพเกรดยานพาหนะ |
| **Sunbeam** | Sunbeam (ทับศัพท์) |
| **Aurora** | Aurora (ทับศัพท์) |
| **Degasi** | Degasi (ทับศัพท์) |

---

## 3. 🏠 Base Building & Components (การสร้างฐานและส่วนประกอบ)

**กฎ:** ในบริบทสิ่งก่อสร้าง ให้ใช้คำว่า **"ผนัง"** แทน "กำแพง"

### โครงสร้างหลัก (Structure)
| English | Thai Translation |
| :--- | :--- |
| **Habitat builder** | เครื่องมือก่อสร้าง |
| **Foundation** | ฐาน |
| **Multipurpose room** | ห้องอเนกประสงค์ |
| **Scanner Room** | ห้องสแกนเนอร์ |
| **Moonpool** | มูนพูล |
| **Observatory** | โดมสังเกตการณ์ |
| **Bulkhead** | ประตูกั้นน้ำ |
| **Reinforce hull** | ผนังเสริมแกร่ง |
| **Hatch** | ประตูทางเข้า |
| **Ladder** | บันได |
| **Wall** | ผนัง |

### เครื่องใช้ภายใน (Interior Modules)
| English | Thai Translation |
| :--- | :--- |
| **Fabricator** | เครื่องประดิษฐ์ |
| **Radio** | วิทยุ |
| **Medical Kit Fabricator** | ตู้ผลิตอุปกรณ์การแพทย์ |
| **Battery charger** | แท่นชาร์จแบตเตอรี่ |
| **Power cell charger** | แท่นชาร์จเซลล์พลังงาน |
| **Modification station** | เครื่องปรับแต่ง |
| **BioReactor** | เครื่องปฏิกรณ์ชีวภาพ |
| **Nuclear reactor** | เครื่องปฏิกรณ์นิวเคลียร์ |
| **Water filtration machine** | เครื่องกรองน้ำ |
| **Alien containment** | ตู้กักกันต่างดาว |
| **Aquarium** | ตู้ปลา |
| **Locker** | ล็อคเกอร์ |
| **Wall locker** | ล็อคเกอร์ติดผนัง |

### พลังงาน (Power)
| English | Thai Translation |
| :--- | :--- |
| **Solar panel** | แผงโซลาร์เซลล์ |
| **Thermal Plant** | เครื่องผลิตไฟพลังความร้อน |
| **Power transmitter** | เสาส่งพลังงาน |
| **Nuclear reactor rod** | แท่งปฏิกรณ์นิวเคลียร์ |

---

## 4. 🪑 Furniture & Decorations (เฟอร์นิเจอร์และของตกแต่ง)

| English | Thai Translation |
| :--- | :--- |
| **Desk** | โต๊ะ |
| **Chair** | เก้าอี้ / เก้าอี้หมุน |
| **Bar table** | โต๊ะบาร์ |
| **Bed** | เตียง |
| **Bench** | ม้านั่ง |
| **Trash can** | ถังขยะ |
| **Vending machine** | ตู้ขนมอัตโนมัติ |
| **Coffee vending machine** | เครื่องชงกาแฟอัตโนมัติ |
| **Counter** | เคาน์เตอร์ |
| **Sign** | ป้าย |
| **Picture Frame** | กรอบรูป |
| **Plant shelf** | กระถางติดผนัง |
| **Wall planter** | ผนังพุ่มไม้ |
| **Pot / Planter** | กระถาง / กระถางปลูกพืช |

---

## 5. 🛠️ Tools & Equipment (อุปกรณ์)

### เครื่องมือ (Handheld)
**หมายเหตุ:** คำว่า **"Stasis"** ให้แปลว่า **"หยุดเวลา"** เมื่อใช้กับปืน (Stasis Rifle) แต่ให้ทับศัพท์เมื่อเป็นชื่อเฉพาะทางเทคนิค เช่น **"Stasis Sphere"**

| English | Thai Translation |
| :--- | :--- |
| **Scanner** | สแกนเนอร์ |
| **Repair tool / Welder** | อุปกรณ์ซ่อมแซม |
| **Laser cutter** | เครื่องตัดเลเซอร์ |
| **Survival Knife** | มีดพก |
| **Thermoblade / Heatblade** | มีดทำความร้อน |
| **Flashlight** | ไฟฉาย |
| **Seaglide** | ซีไกลด์ |
| **Propulsion Cannon** | ปืนแรงโน้มถ่วง |
| **Repulsion Cannon** | ปืนแรงผลัก |
| **Stasis rifle** | ปืนหยุดเวลา |
| **Pathfinder tool** | เครื่องนำทาง |
| **Flare** | พลุไฟ |
| **Beacon** | เครื่องส่งสัญญาณ |
| **Air bladder** | ถุงลมลอยน้ำ |
| **Grav trap** | บอลแรงโน้มถ่วง |
| **Light stick** | แท่งไฟ |
| **Camera drone** | โดรนกล้อง |

### ชุดและอุปกรณ์สวมใส่ (Suits & Gear)
| English | Thai Translation |
| :--- | :--- |
| **Radiation Suit** | ชุดกันรังสี |
| **Reinforced Dive Suit** | ชุดเสริมแกร่ง |
| **Water Filtration Suit / Stillsuit** | ชุดกรองน้ำ |
| **Rebreather** | หมวกฟอกอากาศ |
| **Compass** | เข็มทิศ |
| **Thermometer** | เครื่องวัดอุณหภูมิ |
| **Fins** | ตีนกบ |
| **Tank** | ถังออกซิเจน (ใช้ "ถัง O₂" ในชื่อไอเท็มได้) |

---

## 6. 📦 Materials & Resources (วัสดุและทรัพยากร)

แปลเป็นภาษาไทย หากพบอะนไหนทับศัพท์เหมาะกว่า ให้ทับศัพท์เป็นภาษาไทย

| English | Thai Translation |
| :--- | :--- |
| **Titanium** | ไทเทเนียม |
| **Copper** | ทองแดง |
| **Silver** | เงิน |
| **Gold** | ทอง |
| **Diamond** | เพชร |
| **Lead** | ตะกั่ว |
| **Lithium** | ลิเธียม |
| **Magnetite** | แม่เหล็ก |
| **Quartz** | ควอตซ์ |
| **Glass** | กระจก |
| **Silicone rubber** | ยางซิลิโคน |
| **Lubricant** | สารหล่อลื่น |
| **Bleach** | ยาฟอกขาว |
| **Enameled Glass** | กระจกเคลือบ / กระจกเสริมแกร่ง |
| **Plasteel Ingot** | แท่งพลาสติล |
| **Aerogel** | แอโรเจล |

---

## 7. 📱 PDA & UI Terms

| English | Thai Translation |
| :--- | :--- |
| **PDA** | PDA |
| **Inventory** | ช่องเก็บของ |
| **Blueprints** | พิมพ์เขียว |
| **Beacon Manager** | เครื่องส่งสัญญาณ (ในบริบทแท็บจัดการ) |
| **Gallery / Photo Manager** | รูปภาพ |
| **Log / Voice Log** | บันทึก / บันทึกเสียง |
| **Databank / Encyclopedia** | DATABANK |
| **Time Capsule** | ไทม์แคปซูล |
| **Ping / Signal** | สัญญาณ |

### กฎการแปลสัญญาณ (Ping / Signal Rules) & HUD 📡
เนื่องจากข้อความสัญญาณและ HUD มีพื้นที่จำกัด ให้เน้นความ **กระชับ สั้น และได้ใจความ (Compact & Concise)**
*   ตัดคำฟุ่มเฟือย: เช่น "ที่", "ซึ่ง", "อัน", "กำลัง" หากตัดแล้วความหมายยังคงเดิม
*   ใช้คำย่อมาตรฐานสำหรับหน่วยวัดใน HUD/Signal:
    *   **Meter:** ใช้ **ม.**
    *   **Seconds:** ใช้ **วิ**
    *   **Percent:** ใช้ **%** (พิมพ์ติดตัวเลข เช่น 100%)
*   **ตัวอย่าง:**
    *   *Source:* "Lifepod 17 (100m) - Stranded near a cave system and under attack"
    *   *Target:* "ยานชูชีพ 17 (100ม.) - ติดใกล้ถ้ำและถูกโจมตี"
    *   *Source:* "Proposed Degasi Habitat (250m)"
    *   *Target:* "ฐานที่พัก Degasi (250ม.)"

---

## 8. 🗺️ Locations & Biomes (สถานที่และไบโอม)

### Biome name
* **Life Pod** : ยานชูชีพ
* **Crashed Ship** : ซากยาน Aurora
* **Crash Zone** : เขตยานตก
* **Safe Shallows** : แนวปะการังน้ำตื้น
* **Lost River** : เขตแม่น้ำที่สาบสูญ
* **The Grand Reef** : แนวปะการังยักษ์
* **The Deep Grand Reef** : แนวปะการังยักษ์เขตลึก
* **Mountains** : เขตเทือกเขาใต้น้ำ
* **The Kelp Forest** : ป่าสาหร่าย
* **Grassy Plateaus** : ที่ราบหญ้าแดง
* **Jellyshroom Caves** : ถ้ำเห็ดเยลลี่
* **Mushroom Forest** : ป่าเห็ด
* **The Bulb Zone** : เขตพุ่มกระเปาะ
* **The Floating Islands** : เกาะลอยน้ำ
* **The Floating Islands Surface** : บนเกาะลอยน้ำ
* **Underneath The Floating Islands** : ใต้เกาะลอยน้ำ
* **The Underwater Islands** : เขตหมู่เกาะใต้น้ำ
* **The Sparse Reef** : เขตปะการังร้าง
* **The Sea Treader Path** : เส้นทางอพยพ Sea Treader
* **The Dunes** : เขตเนินทรายมรณะ
* **The Blood Kelp Zone** : เขตสาหร่ายเลือด
* **The Lava Castle Tunnel** : อุโมงค์สู่ปราสาทลาวา
* **The Lava Castle Chamber** : โถงปราสาทลาวา
* **The Inactive Lava Zone Corridor** : อุโมงค์เชื่อมเขตลาวา
* **Precursor Installation** : สิ่งปลูกสร้างต่างดาว
* **Primary Containment Facility** : ศูนย์กักกันหลัก
* **Lava Pit** : หลุมลาวา
* **The Inactive Lava Chamber** : โถงลาวามอด
* **Lava Lakes** : ทะเลสาบลาวา
* **Lava Falls** : น้ำตกลาวา
* **The Void** : หุบเหวไร้ก้น
* **The Crag Field** : เนินทุ่งหินผา

### format การแปลหากพบว่าต้องบอกชื่อไบโอม
format: "สำรวจ[THAI_NAME] ([ENGLISH_NAME])" 
- [ENGLISH_NAME] ในวงเล็บจะไม่มี "The" นำหน้า
- e.g. "สำรวจป่าสาหร่าย (Kelp Forest)"

ตัวอย่าง Key:
```json
"PresenceExploring_biome_kelpforest": "Exploring The Kelp Forest",
```
จะแปลเป็น
```json
"PresenceExploring_biome_kelpforest": "สำรวจป่าสาหร่าย (Kelp Forest)",
```

**ยกเว้น! 2 ไบโอมที่ไม่จำเป็นต้องใช้ format ดังกล่าว**
- **Life Pod** จะเป็น "สำรวจยานชูชีพ"
- **Crashed Ship** จะเป็น "สำรวจซากยาน Aurora"

### สถานที่ของเหล่าต่างดาวโบราณ (Precursor Locations) ใช้ชื่อแปลไทย 
| English | Thai Translation |
| :--- | :--- |
| **quarantine enforcement platform** | แพลตฟอร์มควบคุมการกักกัน |
| **Primary Containment Facility / Primary Alien Facility** | ศูนย์กักกันหลัก |
| **Alien Sanctuary Alpha/Beta** | วิหารต่างดาว Alpha/Beta |
| **Alien Arch** | ประตูต่างดาว |
| **Thermal Power Facility / Alien Thermal Plant** | โรงไฟฟ้าพลังงานความร้อน |
| **Alien Disease Research Facility / Disease Research Facility** | ศูนย์วิจัยโรคต่างดาว/ศูนย์วิจัยโรค |


---

## 9. 🐟 Flora & Fauna (พืชและสัตว์)

### กฎการแปลชื่อสิ่งมีชีวิต (Naming Conventions)

1.  **Leviathan Class & Large Creatures:** ให้ใช้ **ชื่อภาษาอังกฤษทับศัพท์** เพื่อความน่าเกรงขามและเป็นสากล
    *   *Example:* Reefback, Ghost Leviathan, Sea Dragon, Sea Emperor, Reaper Leviathan , Gargantuan
2.  **Fish (ปลา):** ให้ใช้คำว่า **"ปลา"** นำหน้า แล้วตามด้วยชื่อทับศัพท์ภาษาอังกฤษเสมอ
    *   *Example:* Peeper -> ปลา Peeper
    *   *Example:* Hoopfish -> ปลา Hoopfish
    *   *Example:* Bladderfish -> ปลา Bladderfish
    *   *Example:* Garryfish -> ปลา Garryfish
3.  **Ray (กระเบน):** ให้ **แปลเป็นภาษาไทย** โดยใช้คำว่า "กระเบน..." นำหน้า
    *   *Example:* Rabbit Ray -> กระเบนกระต่าย
    *   *Example:* Jellyray -> กระเบนวุ้น
    *   *Example:* Ghostray -> กระเบนผี
4.  **Coral (ปะการัง):** ให้ **แปลเป็นภาษาไทย** โดยใช้คำว่า "ปะการัง..." นำหน้า
    *   *Example:* Brain Coral -> ปะการังสมอง
    *   *Example:* Table Coral -> ปะการังโต๊ะ
5.   **เห็ด**: ให้ **แปลเป็นภาษาไทย** โดยใช้คำว่า "เห็ด..." นำหน้า
    *   *Example:* Jellyshroom -> เห็ดเยลลี่
    *   *Example:* Deep Shroom / White Mushroom -> เห็ดน้ำลึก

7.  **Age/Stage (ช่วงวัย):**
    *   **Juvenile:** วัยเยาว์ (เช่น "Ghost Leviathan วัยเยาว์")
    *   **Baby:** ลูก... (เช่น "ลูก Reefback")
    *   **Exception:** **Sea Emperor Baby** ให้ใช้คำว่า **"เด็ก"** (เช่น "Sea Emperor เด็ก" หรือ "Sea Emperor Leviathan เด็ก") เนื่องจากลักษณะ

### รายการคำศัพท์สัตว์ (Fauna)

| English | Thai Translation / Rule |
| :--- | :--- |
| **Reefback** | Reefback |
| **Ghost Leviathan** | Ghost Leviathan |
| **Sea Dragon Leviathan** | Sea Dragon Leviathan |
| **Sea Emperor** | Sea Emperor |
| **Reaper Leviathan** | Reaper Leviathan |
| **Sea Treader** | Sea Treader |
| **Ampeel / Shocker** | Ampeel |
| **Stalker** | Stalker |
| **Peeper** | ปลา Peeper |
| **Hoopfish** | ปลา Hoopfish |
| **Bladderfish** | ปลา Bladderfish |
| **Garryfish** | ปลา Garryfish |
| **Reginald** | ปลา Reginald |
| **Spadefish** | ปลา Spadefish |
| **Boomerang** | ปลา Boomerang |
| **Red Eyeye** | ปลา Eyeye สีแดง |
| **Oculus** | ปลา Oculus |
| **Holefish** | ปลา Holefish |
| **Spinefish** | ปลา Spinefish |
| **Cuddlefish** | หมึก Cuddlefish (ข้อยกเว้น: Cuddlefish มีลักษณะคล้ายหมึก) |
| **Crabsquid** | หมึกปู |
| **Mesmer** | ปลา Mesmer |
| **Rabbit Ray** | กระเบนกระต่าย |
| **Jellyray** | กระเบนวุ้น |
| **Ghostray** | กระเบนผี |
| **Bonesharks** | ฉลามกระดูก |
| **Sand Shark** | ฉลามทราย |
| **Lava Lizards** | กิ้งก่าลาวา |
| **Lava larva** | หนอนลาวา |
| **Crabsnake** | งูปู |
| **Shuttlebugs / Jumper** | แมงกระโดด |
| **Warper** | Warper |
| **Blood crawler** | ปูเลือด |
| **Cave crawler** | ปูถ้ำ |

**กฎเสริมที่ใช้เฉพาะกับ EncyDesc** คิดชื่อที่เป็นชื่อแปลให้กับสัตว์ที่ไม่มีชื่อไทยไปด้วย ตัวอยา่าง format header อิงแบบนี้เหนือกฎ Naming Conventions เนื่องจาก เป็น EncyDesc 
- `ปลาระเบิด (Crashfish) [เนื้อหา]` <-- ในวงเล็บเป็น eng ล้วนไม่มีคำว่าปลา ชื่อปลาต่างๆ สามารถใช้ชื่อแปลไทยแบบนี้ได้เลยใน header เพิ่มเติม: `ปลา [english]` ไม่นับเป็นชื่อปลาที่แปลไทยแล้วนะ ดังนั้นต้องคิดชื่อแปลไทยด้วย 
- `Reefback Leviathan: วาฬหลังหิน, วาฬหลังปะการัง\n\n[เนื้อหา]` <-- จะเห็นว่า format ไม่ใช่วงเล็บ เนื่องจากมีชื่อได้หลายชื่อ และปิดท้ายด้วยการเว้นบรรทัด
- `สตอล์กเกอร์ (Stalker) [เนื้อหา]` <-- ชื่อไทยจะไม่ใช่ชื่อแปลเนื่องจาก ถ้าแปลแล้วอาจจะฟังดูแปลกๆ ใช้ทับศัพท์ไทยจะเหมาะสมกว่า
- กรณี Reaper ให้ระบุทั้งชื่อ แปลไทย และชื่อทับศัพท์ไทย

### รายการคำศัพท์พืชและปะการัง (Flora & Coral)

| English | Thai Translation |
| :--- | :--- |
| **Acid Mushroom** | เห็ดกรด |
| **Deep Shroom / White Mushroom** | เห็ดน้ำลึก |
| **Jellyshroom / Snake Mushroom** | เห็ดเยลลี่ |
| PurpleRattle / Speckled Rattler | เห็ดกระดิ่งลายจุด |
| **Coral shell plate** | ปะการังแผ่นกาบ |
| **Brain Coral** | ปะการังสมอง |
| **Table Coral** | ปะการังโต๊ะ |
| **Coral Tube** | ท่อปะการัง |
| **Tree Mushroom** | เห็ดต้นไม้ |
| **Anchor Pod** | บอลสมอ |
| **Membrain** | ต้นเมมเบรน |
| **HangingStinger/Drooping Stinger** | ต้นกะพรุนไฟ |
| **Sulfur Plant** | ต้นกำมะถัน |
| **Creepvine** | สาหร่าย Creepvine |
| **Bulbo tree** | ต้นบัลโบ |
| **Latern** | ต้นโคมไฟ |
| **Purple Vase Plant** | ต้นหมิง |
| **Jaffa cup** | เห็ดถ้วยจาฟฟา |
| **VegetablePlant** | ต้นมันฝรั่งจีน |
| **Marblemelon / MelonPlant** | แตงโมลายหินอ่อน |

**กฎเสริมที่ใช้เฉพาะกับ EncyDesc** คิดชื่อที่เป็นชื่อแปลให้กับพืชที่ไม่มีชื่อไทยไปด้วย ตัวอย่าง header format:
- `ปาล์มเฟิร์น (Fern Palm) [เนื้อหา]`
- `ขนนกเกบ (Gabe's feather) [เนื้อหา]`
- `Creepvine: สาหร่ายเถา, สาหร่าย Creepvine\n\n[เนื้อหา]` <-- จะเห็นว่า format ไม่ใช่วงเล็บ เนื่องจากมีชื่อได้หลายชื่อ และปิดท้ายด้วยการเว้นบรรทัด

---

## 10. องค์กร
**Trans-gov**: องค์กรรัฐข้ามระบบดาว

**federation**:  สหพันธ์

**Alterra**: Alterra (ทับศัพท์)

**Trans-System Federation / TSF**: สหพันธรัฐข้ามระบบดาว / TSF

---


## 11. ⛔ Do Not Translate / Transliterate (คำทับศัพท์/ไม่แปล)

คำเหล่านี้ให้คงรูปภาษาอังกฤษ หรือทับศัพท์ตามที่ระบุไว้ เพื่อความเข้าใจที่ตรงกัน

*   **Alterra**
*   **Precursor** (หรือ "ต่างดาวโบราณ" ในบางบริบทของ Tablet)
*   **Hull plate**
*   **Share**, **Steam**, **Pin**
*   **Phasegate**
*   **Kharaa**

ความสำคัญต่ำ เนื่องจากเป็น Cut Content ไปแล้ว (ไม่ต้องกังวลเรื่องคำแปล แค่ห้ามว่าง)

*   **Terraformer**
*   **Transfuser**
*   **PowerGlide**
*   **SpecimenAnalyzer** (เครื่องวิเคราะห์สายพันธุ์)
*   **FragmentAnalyzer**
*   **Slime**
*   **Grabcrab**
*   **BATHYSPHERE**
*   **Accumulator**
*   **Centrifuge**
*   **Cyclops pressure compensator**
*   **ReefbackTissue**
*   **ReefbackAdvancedStructure**
*   **HullReinforcementModule2**
*   **HullReinforcementModule3**
*   **Ion Crystal Matrix**

---

## 12. 🔄 System Status & Common States (สถานะระบบ)

การแปลคำศัพท์สถานะระบบ ให้พิจารณาบริบทการใช้งานเป็นหลัก

| English | Thai / Rule | Context |
| :--- | :--- | :--- |
| **Corrupted** | **ข้อมูลเสียหาย** | เมื่อกล่าวถึงไฟล์ ข้อมูล หรือ Downloadable Data |
| **Offline / Inactive** | **ออฟไลน์ / ไม่ทำงาน** | ใช้ในประโยคสนทนา หรือข้อความแจ้งเตือนทั่วไป |
| **Offline / Inactive** | **(คงภาษาอังกฤษ)** | **ข้อยกเว้น:** หากเป็นข้อความในหน้าจอ Console, Terminal หรือบรรทัดคำสั่ง (Code-like text) ให้คงภาษาอังกฤษไว้เพื่อให้ได้อารมณ์เทคนิค |

## 13. Items
| English | Thai |
| :--- | :--- |
| **Energy Core**|  แกนพลังงาน |
| **Tablet** | แท็บเล็ต |
| **Data Terminal** / **Terminal** | เทอร์มินัล **ข้อยกเว้น:** หากเป็นข้อความในหน้าจอ Console, Terminal หรือบรรทัดคำสั่ง (Code-like text) ให้คงภาษาอังกฤษไว้เพื่อให้ได้อารมณ์เทคนิค |
| **Ion cube** | ลูกบาศก์ไอออน |
| **Incubator** | เครื่องฟักไข่ |
| **HatchingEnzymes** | เอนไซม์ฟักไข่ |

## 14. Common Contextual Terms (คำศัพท์ตามบริบท)
| English | Thai | Context |
| :--- | :--- | :--- |
| **Skeletal Remains** | **ซากโครงกระดูก** | เพื่อป้องกันการสับสนกับ "โครงกระดูก" (Skeleton) ทั่วไป |
| **Case** | **ตู้ / ตู้จัดแสดง** | เมื่อหมายถึงตู้โชว์หรือตู้เก็บตัวอย่าง (ไม่ใช่ "กรณี") |
| **Empty** | **ว่างเปล่า** | เมื่อใช้กับ Container/Storage (เช่น ตู้ว่างเปล่า) |