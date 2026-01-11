import json
import pathlib

from rich.console import Console

console = Console()


def save_json(data, path):
    # Make output directory if not exists
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    # Save JSON file with utf-8 encoding
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    console.print(f"[bold green]JSON saved to:[/bold green] {path}")