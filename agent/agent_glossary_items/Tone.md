### ⚙️ Translation Logic & Tone

**A. General UI / System Messages:**
* **Tone:** Concise, Formal, Functional, Objective (Robotic/System).
* **Constraint:** Keep text short to fit UI buttons. No filler words.
* **Context Inference:** Infer context from Key Names (e.g., 'Submit' in menu = "ยืนยัน", 'Submit' to authority = "ยอมจำนน").

**B. "EncyDesc_" Logic (Encyclopedia Entries):**
* **Target:** Keys starting with `EncyDesc_`
* **Tone:** "Alterra Sales Pitch" – Informative, persuasive, commercial yet scientific. (Describe item benefits as if selling a product).
* **Header Format:** Unless specified otherwise in [GLOSSARY], the first line MUST follow this format:
    * `Thai Name (English Name)`
    * *Example:* `"EncyDesc_Scanner": "สแกนเนอร์ (Scanner) ..."`
    * *Example:* `"EncyDesc_SolarPanel": "แผงโซลาร์เซลล์ (Solar Panel) ..."`