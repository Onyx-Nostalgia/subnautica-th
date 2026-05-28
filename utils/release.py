import json
import shutil
from pathlib import Path
from typing import List, Optional

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel

import config
from utils.file_io import save_json

console = Console()


def build_final_translation():
    """
    Merges all translation phases and creates the final JSON files.
    Writes decoded version (for git tracking) and delegates encoding to
    the standalone release script.
    """
    config.RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    console.print("[bold blue]Building Final Translation...[/bold blue]")

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
    merge_sources: List[Path] = [
        config.CLEANED_THAI_PATH,
        config.PHASE_1.COMPLETE_PATH,
        config.PHASE_2.COMPLETE_PATH,
        config.PHASE_3.COMPLETE_PATH,
        config.PHASE_4.COMPLETE_PATH,
        config.PHASE_5.COMPLETE_PATH,
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
    
    # Write decoded file (Readable UTF-8) for Git tracking
    save_json(merged_data, config.FINAL_DECODED_PATH)

    # Write encoded file (ASCII safe for game)
    config.FINAL_BUILD_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with open(config.FINAL_ENCODED_PATH, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=True, indent=4)
        console.print(f"[bold green]✓ Created Game File:[/bold green] {config.FINAL_ENCODED_PATH}")
    except IOError as e:
        console.print(f"[bold red]Error writing final file:[/bold red] {e}")

def deploy_to_game(source: Optional[Path] = None, destination: Optional[Path] = None):
    """
    Copies the translation to the game directory.
    Args:
        source: Source file path. If None, uses config default (FINAL_ENCODED_PATH).
        destination: Target file path (e.g., .../Thai.json). If None, uses config default.
    """
    console.print("[bold blue]Deploying to game...[/bold blue]")
    
    source_file = source if source else config.FINAL_ENCODED_PATH
    
    if not source_file.exists():
        console.print(f"[bold red]Error:[/bold red] File not found: {source_file}")
        console.print("Please provide a valid source file or run 'Build Final Translation' first.")
        return
    
    # Use provided destination or fallback to config
    final_dest = destination if destination else config.GAME_LANGUAGE_ROOT / "Thai.json"
    
    # Validate destination directory
    if not final_dest.parent.exists():
        console.print("[bold red]Error:[/bold red] Destination directory not found at:")
        console.print(f"{final_dest.parent}")
        return

    console.print(f"Source: [blue]{source_file}[/blue]")
    console.print(f"Destination: [blue]{final_dest}[/blue]")
    
    try:
        shutil.copy2(source_file, final_dest)
        console.print("[bold green]Successfully deployed to game![/bold green]")
    except IOError as e:
        console.print(f"[bold red]Deployment failed:[/bold red] {e}")