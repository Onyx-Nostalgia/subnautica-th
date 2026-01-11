Audit

หน้าที่ของคุณในวันนี้คือ @data/auditor_agent.md ใช้ Rule ร่วมกับ @data/glossary_format_rule.md เพื่อแก้ไข @data/translation_unapproved_review.json และเขียนผลลัพธ์ลง @data/fixed_after_review.json หาก Key ที่ต้องตรวจสอบมีมากเกินกว่าที่จะทำจบได้ในรอบเดียว ให้แบ่งตรวจสอบเป็นชุดๆ จนกว่าจะตรวจครบทุก Key

ใช้ python code เพื่อ นำ @data/fixed_after_review.json ไป update ลง @data/translation_progress.json map แต่ละ Key แก้ไขเฉพาะ Value ของ Key "Result"  