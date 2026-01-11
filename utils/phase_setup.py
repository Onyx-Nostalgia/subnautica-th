import json
import os

from rich import print

import config
from utils.file_io import save_json


def is_thai(text):
    """Check if the text contains Thai characters."""
    if not text:
        return False
    for char in text:
        if '\u0E00' <= char <= '\u0E7F':
            return True
    return False

def setup_phase(phase_obj, source_data_path):
    """
    General function to setup translation forms for any phase.
    
    Args:
        phase_obj (TranslationPhase): The phase configuration object (e.g., config.PHASE_3).
        source_data_path (Path): Path to the source JSON file for this phase (e.g., config.PHASE_3_PATH).
                                 Expected structure: { "Category": { "Key": "English Text" } }
    """
    print(f"[bold blue]Setting up phase for:[/bold blue] {phase_obj.DIR}")

    # Load Source Data (Phase Mapping)
    with open(source_data_path, 'r', encoding='utf-8') as f:
        category_data = json.load(f)
    
    # Load Thai Reference Data
    with open(config.CLEANED_THAI_PATH, 'r', encoding='utf-8') as f:
        thai_data = json.load(f)

    # Load Legacy Thai Data (Low confidence source)
    legacy_data = {}
    if hasattr(config, 'CLEANED_LAGACY_THAI_PATH') and config.CLEANED_LAGACY_THAI_PATH.exists():
        try:
            with open(config.CLEANED_LAGACY_THAI_PATH, 'r', encoding='utf-8') as f:
                legacy_data = json.load(f)
        except Exception as e:
            print(f"[yellow]Warning:[/yellow] Could not load legacy data: {e}")

    # Load Manual Updates (Optional/Legacy support + Extra sources)
    manual_data = {}
    manual_paths = [
        config.DECODED_THAI_V2_PATH,
    ]

    for path in manual_paths:
        file_path = str(path) # Ensure string for os.path operations if needed, though open() handles Path
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    manual_data.update(data)
                print(f"[green]Loaded manual data from:[/green] {file_path} ({len(data)} items)")
            except Exception as e:
                print(f"[red]Error loading {file_path}:[/red] {e}")
        else:
            print(f"[yellow]Warning:[/yellow] Manual data file not found at {file_path}. Skipping.")

    # 1. Create Key File (Flattened)
    print("Creating phase key file...")
    keys = category_data.values()
    # Handle case where category_data might be flat or nested differently if needed, 
    # but assuming standard structure {Category: {Key: Value}}
    phase_keys = {k: v for d in keys for k, v in d.items()}
    
    print(f"Keys: {len(phase_keys.keys())} keys")
    save_json(phase_keys, phase_obj.KEY_PATH)
    
    # 2. Create Progress Form
    print("Creating progress form file...")
    progress_data = {}
    
    # Check if progress file already exists to preserve work
    if phase_obj.PROGRESS_PATH.exists():
        print(f"[yellow]Note:[/yellow] Progress file {phase_obj.PROGRESS_PATH} already exists. Merging/Overwriting based on logic (currently overwriting structure but could be enhanced).")
        # For this refactor, we stick to the original behavior: create fresh based on categories
        # If preservation is needed, we would load it here.
    
    for category, item in category_data.items():
        for key, value in item.items():
            # Current Thai translation from cleaned data
            thai_text = thai_data.get(key, "")
            if not is_thai(thai_text):
                thai_text = ""
            
            form = {
                "Category": category,
                "English": value,
                "Thai": thai_text,
            }
            progress_data[key] = form.copy()
            
            # Check manual data
            _result = manual_data.get(key, "")
            legacy_val = legacy_data.get(key, "")
            
            norm_result = _result.strip().replace(" ", "")
            norm_value = value.strip().replace(" ", "")
            norm_thai = thai_text.strip().replace(" ", "")
            norm_legacy = legacy_val.strip().replace(" ", "")
            
            # Logic 2: Standard Validation
            if norm_result == norm_value or norm_result == norm_thai or norm_result == norm_legacy:
                 # If result matches English exactly, it's likely untranslated or placeholder -> Clear it
                _result = ""
            
            progress_data[key].update({"Result": _result, "Approved": False})
            
    print(f"Progress Keys: {len(progress_data.keys())} keys")
    save_json(progress_data, phase_obj.PROGRESS_PATH)
    
    print(f"[bold green]Setup complete for phase:[/bold green] {phase_obj.DIR}")
