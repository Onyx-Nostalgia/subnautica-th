import json
import re
import shutil
from pathlib import Path
from typing import List, Optional

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

import config
from utils.file_io import save_json

console = Console()

FINAL_DIR = Path("final/")

def get_next_version() -> int:
    """
    Scans the final directory to determine the next version number.
    Returns 1 if no files exist.
    """
    if not FINAL_DIR.exists():
        return 1
    
    latest_version = 0
    # Look for files matching Thai_v{number}.json (excluding _decode.json)
    for file_path in FINAL_DIR.glob("Thai_v*.json"):
        if "_decode.json" in file_path.name:
            continue
        
        # Extract number using regex
        match = re.search(r'Thai_v(\d+)\.json', file_path.name)
        if match:
            version = int(match.group(1))
            if version > latest_version:
                latest_version = version
                
    return latest_version + 1

def get_latest_version_number() -> int:
    """Returns the highest version number found in the final directory."""
    version = get_next_version() - 1
    return version if version > 0 else 0

def build_final_translation():
    """
    Merges all translation phases and creates the final JSON files.
    Generates both an encoded version (for the game) and a decoded version (for reference).
    """
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    
    next_version = get_next_version()
    final_path = FINAL_DIR / f"Thai_v{next_version}.json"
    final_decode_path = FINAL_DIR / f"Thai_v{next_version}_decode.json"
    
    console.print(f"[bold blue]Building Final Translation v{next_version}...[/bold blue]")

    # Load base English file
    if not config.PARSED_PATH.exists():
        console.print(f"[bold red]Error:[/bold red] Base file not found at {config.PARSED_PATH}")
        return

    try:
        with open(config.PARSED_PATH, 'r', encoding='utf-8') as f:
            merged_data = json.load(f)
    except json.JSONDecodeError:
        console.print(f"[bold red]Error:[/bold red] Failed to decode base file at {config.PARSED_PATH}")
        return

    # Define the order of files to merge (later files overwrite earlier ones)
    # Using Path objects from config
    merge_sources: List[Path] = [
        config.CLEANED_THAI_PATH,
        config.PHASE_1.COMPLETE_PATH,
        config.PHASE_2.COMPLETE_PATH,
        config.PHASE_3.COMPLETE_PATH,
        config.PHASE_4.COMPLETE_PATH,
        config.PHASE_5.COMPLETE_PATH,
        Path(config.DECODED_THAI_V1_PATH),
    ]
    
    processed_sources = []
    
    for source_path in merge_sources:
        if not source_path.exists():
            continue
            
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # filter data to only include keys present in merged_data
                _data = {k: v for k, v in data.items() if k in merged_data}
                merged_data.update(_data)
                processed_sources.append(str(source_path))
        except json.JSONDecodeError:
            console.print(f"[bold yellow]Warning:[/bold yellow] Skipping corrupt file: {source_path}")

    # Display summary
    items = [Panel(f"[bold green]Merged[/bold green]\n{Path(item).name}", expand=True) for item in processed_sources]
    console.print("[bold bright_cyan]Merged data from:[/bold bright_cyan]")
    console.print(Columns(items))
    
    # Write encoded file (ASCII safe for game)
    try:
        with open(final_path, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=True, indent=4)
        console.print(f"[bold green]✓ Created Game File:[/bold green] {final_path}")
    except IOError as e:
        console.print(f"[bold red]Error writing final file:[/bold red] {e}")
        return

    # Write decoded file (Readable UTF-8)
    save_json(merged_data, final_decode_path)

def deploy_to_game(version: Optional[int] = None, destination: Optional[Path] = None):

    """

    Copies the specified (or latest) translation version to the game directory.

    Args:

        version: Specific version to deploy. If None, finds latest.

        destination: Target file path (e.g., .../Thai.json). If None, uses config default.

    """

    console.print("[bold blue]Deploying to game...[/bold blue]")

    

    if version is None:

        version = get_latest_version_number()

        if version == 0:

            console.print("[bold red]No final translation files found.[/bold red]")

            return

        console.print(f"Latest version detected: [bold green]v{version}[/bold green]")

    

    source_file = FINAL_DIR / f"Thai_v{version}.json"

    

    if not source_file.exists():

        console.print(f"[bold red]Error:[/bold red] File not found: {source_file}")

        console.print("Please check the version number.")

        return

    

    # Use provided destination or fallback to config

    final_dest = destination if destination else config.GAME_TRANSLATION_PATH

    

    # Validate destination directory

    if not final_dest.parent.exists():

        console.print("[bold red]Error:[/bold red] Destination directory not found at:")

        console.print(f"{final_dest.parent}")

        return



    console.print(f"Source: [blue]{source_file}[/blue]")

    console.print(f"Destination: [blue]{final_dest}[/blue]")

    

    try:

        shutil.copy2(source_file, final_dest)

        console.print(f"[bold green]Successfully deployed v{version} to game![/bold green]")

    except IOError as e:

        console.print(f"[bold red]Deployment failed:[/bold red] {e}")


