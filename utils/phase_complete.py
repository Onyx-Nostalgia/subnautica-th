import json

from rich.console import Console

import config
from utils.file_io import save_json

console = Console()

def create_phase_complete(phase_obj):
    """
    Reads approved reviews, extracts the 'Result', and updates the complete translation file for the given phase.
    
    Args:
        phase_obj (TranslationPhase): The phase configuration object (e.g., config.PHASE_3).
    """
    
    console.print(f"[bold blue]Creating translation complete file for:[/bold blue] {phase_obj.DIR}")
    
    approved_path = phase_obj.APPROVED_REVIEW_PATH
    complete_path = phase_obj.COMPLETE_PATH

    if not approved_path.exists():
        console.print(f"[bold red]Error:[/bold red] Approved review file not found at {approved_path}")
        return

    try:
        with open(approved_path, 'r', encoding='utf-8') as f:
            approved_data = json.load(f)
    except json.JSONDecodeError:
        console.print(f"[bold red]Error:[/bold red] Failed to decode JSON from {approved_path}")
        return

    # Load existing complete data if it exists
    complete_data = {}
    if complete_path.exists():
        try:
            with open(complete_path, 'r', encoding='utf-8') as f:
                complete_data = json.load(f)
        except json.JSONDecodeError:
            console.print("[bold yellow]Warning:[/bold yellow] Failed to decode existing complete file. Starting fresh.")
            complete_data = {}

    # Update logic: complete[key] = approved[key].Result
    count = 0
    for key, value in approved_data.items():
        if isinstance(value, dict) and "Result" in value:
            complete_data[key] = value["Result"]
            count += 1
        
    console.print(f"Merged [bold green]{count}[/bold green] items from approved review.")

    # Save the updated complete file
    save_json(complete_data, complete_path)
    console.print(f"[bold green]Translation complete file updated:[/bold green] {complete_path}")


def update_complete_from_fixed(phase_num: int, version: int):
    """
    Updates the complete translation file for a given phase using a fixed JSON file from the auditor agent.
    
    Args:
        phase_num (int): The phase number (1-5).
        version (int): The version of the fixed file (e.g., 1 for fixed_1.json).
    """
    phase_map = {
        1: config.PHASE_1,
        2: config.PHASE_2,
        3: config.PHASE_3,
        4: config.PHASE_4,
        5: config.PHASE_5
    }
    
    phase_obj = phase_map.get(int(phase_num))
    if not phase_obj:
        console.print(f"[bold red]Error:[/bold red] Invalid phase number {phase_num}")
        return

    # Construct source path
    # Example: agent_auditor/phase_2_review/fixed_1.json
    source_path = f"agent_auditor/phase_{phase_num}_review/fixed_{version}.json"
    
    console.print(f"[bold blue]Updating phase {phase_num} from fixed file:[/bold blue] {source_path}")

    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            fixed_data = json.load(f)
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] Fixed file not found at {source_path}")
        return
    except json.JSONDecodeError:
        console.print(f"[bold red]Error:[/bold red] Failed to decode JSON from {source_path}")
        return

    # Load target complete file
    complete_path = phase_obj.COMPLETE_PATH
    
    complete_data = {}
    if complete_path.exists():
        try:
            with open(complete_path, 'r', encoding='utf-8') as f:
                complete_data = json.load(f)
        except json.JSONDecodeError:
            console.print("[bold yellow]Warning:[/bold yellow] Failed to decode existing complete file. Starting fresh.")
            complete_data = {}
            
    # Update data
    count = 0
    for key, value in fixed_data.items():
        if key in complete_data:
            # Optional: You might want to log if you are overwriting something different
            pass
        complete_data[key] = value
        count += 1
        
    console.print(f"Updated [bold green]{count}[/bold green] items from fixed review.")
    
    save_json(complete_data, complete_path)
    console.print(f"[bold green]Translation complete file updated:[/bold green] {complete_path}")