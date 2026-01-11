import json
import os

from rich import print

from utils.file_io import save_json


def create_review_form(phase_obj):
    """
    General function to create review forms for any phase.
    
    Args:
        phase_obj (TranslationPhase): The phase configuration object (e.g., config.PHASE_3).
    """
    print(f"[bold blue]Creating review form for:[/bold blue] {phase_obj.DIR}")

    if not phase_obj.PROGRESS_PATH.exists():
        print(f"[bold red]Error:[/bold red] Progress file not found at {phase_obj.PROGRESS_PATH}")
        return

    with open(phase_obj.PROGRESS_PATH, 'r', encoding='utf-8') as f:
        progress_data = json.load(f)
    
    # Review form
    print("Creating review form file...")
    review_data = {}
    approved_review_data = {}
    unapproved_review_data = {}
    
    for key, item in progress_data.items():
        result = item.get("Result", "")
        
        # Handle special placeholder tags if they exist
        match str(result).lower():
            case "[english]": 
                result = item["English"]
            case "[thai]": 
                result = item["Thai"]
        
        review_data[key] = {
            "Category": item.get("Category", ""),
            "English": item.get("English", ""),
            "Thai": item.get("Thai", ""),
            "Result": result,
            "Approved": item.get("Approved", False)
        }
        
        if item.get("Approved", False):
            approved_review_data[key] = {
                "Category": item.get("Category", ""),
                "English": item.get("English", ""),
                "Result": result
            }
        else:
            unapproved_review_data[key] = {
                "Category": item.get("Category", ""),
                "English": item.get("English", ""),
            }
            
    print(f"Review Keys: {len(review_data.keys())} keys")
    save_json(review_data, phase_obj.REVIEW_PATH)
    
    print(f"Approved Review Keys: {len(approved_review_data.keys())} keys")
    if len(approved_review_data.keys()) > 0:
        save_json(approved_review_data, phase_obj.APPROVED_REVIEW_PATH)
    elif phase_obj.APPROVED_REVIEW_PATH.exists():
        print("No approved review data found.")
        os.remove(phase_obj.APPROVED_REVIEW_PATH)
        print("✅ Removed empty approved review file")
    
    print(f"Unapproved Review Keys: {len(unapproved_review_data.keys())} keys")
    if len(unapproved_review_data.keys()) > 0:
        save_json(unapproved_review_data, phase_obj.UNAPPROVED_REVIEW_PATH)
    elif phase_obj.UNAPPROVED_REVIEW_PATH.exists():
        print("No unapproved review data found.")
        os.remove(phase_obj.UNAPPROVED_REVIEW_PATH)
        print("✅ Removed empty unapproved review file")

    print(f"[bold green]Review form creation complete for:[/bold green] {phase_obj.DIR}")
