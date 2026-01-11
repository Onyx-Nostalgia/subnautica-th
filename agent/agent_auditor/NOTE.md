Audit

หน้าที่ของคุณในวันนี้คือ @glossary_items/auditor_agent.md ใช้ Rule ร่วมกับ @glossary_items/agent_workspace/glossary_format_rule.md เพื่อแก้ไข @glossary_items/agent_workspace/translation_unapproved_review.json และเขียนผลลัพธ์ลง @glossary_items/agent_workspace/fixed_after_review.json หาก Key ที่ต้องตรวจสอบมีมากเกินกว่าที่จะทำจบได้ในรอบเดียว ให้แบ่งตรวจสอบเป็นชุดๆ จนกว่าจะตรวจครบทุก Key

ใช้ python code เพื่อ นำ @glossary_items/agent_workspace/fixed_after_review.json ไป update ลง @glossary_items/agent_workspace/translation_unapproved_review.json map แต่ละ Key แก้ไขเฉาพาะ Value ของ Key "Result"  