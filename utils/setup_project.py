import shutil
import os
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt

import config

console = Console()

def setup_workspace():
    console.print("[bold blue]Initial Setup: Clone Data from Game[/bold blue]")
    
    # Check if files already exist
    if config.ORIGINAL_ENGLISH_PATH.exists() and config.ORIGINAL_THAI_PATH.exists():
        console.print("[yellow]Original data files already exist.[/yellow]")
        override = Prompt.ask("Do you want to overwrite them?", choices=["y", "n"], default="n")
        if override == "n":
            return

    # Ask for game path
    default_path = "/mnt/d/Epic Games/Subnautica/Subnautica_Data/StreamingAssets/SNUnmanagedData/LanguageFiles"
    
    console.print(f"\nDefault Game Path: [cyan]{default_path}[/cyan]")
    use_default = Prompt.ask("Use default path?", choices=["y", "n"], default="y")
    
    game_path = Path(default_path)
    
    if use_default == "n":
        while True:
            user_path = Prompt.ask("Enter full path to 'LanguageFiles' folder")
            # Remove quotes if user copied them
            user_path = user_path.strip('"').strip("'")
            temp_path = Path(user_path)
            
            if temp_path.exists():
                game_path = temp_path
                break
            else:
                console.print(f"[bold red]Error:[/bold red] Path does not exist: {user_path}")
                retry = Prompt.ask("Try again?", choices=["y", "n"], default="y")
                if retry == "n":
                    return

    # Source files
    src_thai = game_path / "Thai.json"
    src_english = game_path / "English.json"

    # Destination files
    config.ORIGINAL_THAI_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    # Copy
    try:
        if src_thai.exists():
            shutil.copy(src_thai, config.ORIGINAL_THAI_PATH)
            console.print(f"[green]Copied:[/green] {src_thai} -> {config.ORIGINAL_THAI_PATH}")
        else:
            console.print(f"[red]Not Found:[/red] {src_thai}")

        if src_english.exists():
            shutil.copy(src_english, config.ORIGINAL_ENGLISH_PATH)
            console.print(f"[green]Copied:[/green] {src_english} -> {config.ORIGINAL_ENGLISH_PATH}")
        else:
            console.print(f"[red]Not Found:[/red] {src_english}")
            
    except Exception as e:
        console.print(f"[bold red]Error copying files:[/bold red] {e}")

if __name__ == "__main__":
    setup_workspace()
