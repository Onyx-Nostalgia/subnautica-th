import json
import os

from rich import print

from utils.file_io import save_json


def generate_inspection_files(phase_obj):
    """
    General function to create inspection files for any phase.
    
    Args:
        phase_obj (TranslationPhase): The phase configuration object (e.g., config.PHASE_3).
    """
    print(f"[bold blue]Generating inspection files for:[/bold blue] {phase_obj.DIR}")

    if not phase_obj.PROGRESS_PATH.exists():
        print(f"[bold red]Error:[/bold red] Progress file not found at {phase_obj.PROGRESS_PATH}")
        return

    with open(phase_obj.PROGRESS_PATH, 'r', encoding='utf-8') as f:
        progress_data = json.load(f)
    
    # Inspection form
    print("Creating inspection files...")
    inspection_data = {}
    approved_inspection_data = {}
    unapproved_inspection_data = {}
    
    for key, item in progress_data.items():
        result = item.get("Result", "")
        
        # Handle special placeholder tags if they exist
        match str(result).lower():
            case "[english]": 
                result = item["English"]
            case "[thai]": 
                result = item["Thai"]
        
        inspection_data[key] = {
            "Category": item.get("Category", ""),
            "English": item.get("English", ""),
            "Thai": item.get("Thai", ""),
            "Result": result,
            "Approved": item.get("Approved", False)
        }
        
        if item.get("Approved", False):
            approved_inspection_data[key] = {
                "Category": item.get("Category", ""),
                "English": item.get("English", ""),
                "Result": result
            }
        else:
            unapproved_inspection_data[key] = {
                "Category": item.get("Category", ""),
                "English": item.get("English", ""),
            }
            
    print(f"Inspection Keys (Full): {len(inspection_data.keys())} keys")
    save_json(inspection_data, phase_obj.INSPECTION_PATH)
    
    print(f"Approved Keys: {len(approved_inspection_data.keys())} keys")
    if len(approved_inspection_data.keys()) > 0:
        save_json(approved_inspection_data, phase_obj.APPROVED_INSPECTION_PATH)
    elif phase_obj.APPROVED_INSPECTION_PATH.exists():
        print("No approved data found.")
        os.remove(phase_obj.APPROVED_INSPECTION_PATH)
        print("✅ Removed empty approved inspection file")
    
    print(f"Unapproved Keys: {len(unapproved_inspection_data.keys())} keys")
    if len(unapproved_inspection_data.keys()) > 0:
        save_json(unapproved_inspection_data, phase_obj.UNAPPROVED_INSPECTION_PATH)
    elif phase_obj.UNAPPROVED_INSPECTION_PATH.exists():
        print("No unapproved data found.")
        os.remove(phase_obj.UNAPPROVED_INSPECTION_PATH)
        print("✅ Removed empty unapproved inspection file")

    print(f"[bold green]Inspection files generation complete for:[/bold green] {phase_obj.DIR}")
