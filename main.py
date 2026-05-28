from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

import config
from classification.category_tree import run_category_tree
from classification.classify import run_classification
from phase_mapping.generate_phase_json import main as generate_phase_main
from pre_processing.compare_key import run_comparison
from pre_processing.preprocess import clean_thai, pre_proccess
from utils import (
    build_final_translation,
    create_phase_complete,
    deploy_to_game,
    generate_inspection_files,
    setup_phase,
    update_complete_from_fixed,
)
from utils.setup_project import setup_workspace

console = Console()

def ask_phase():
    """
    Helper to ask for phase number and return config objects.
    Returns: (phase_obj, phase_path, phase_num_str) or None if cancelled.
    """
    phase_num = Prompt.ask("\nEnter Phase Number", choices=["1", "2", "3", "4", "5", "b"], default="b")
    
    if phase_num == "b":
        return None
        
    phase_obj = getattr(config, f"PHASE_{phase_num}")
    phase_path = getattr(config, f"PHASE_{phase_num}_PATH")
    
    return phase_obj, phase_path, phase_num

def main():
    while True:
        console.clear()
        console.print("[bold blue]Subnautica Thai Localization Tool[/bold blue]")
        console.print("\n[bold]Main Menu:[/bold]")
        
        main_choices = {
            "0": "Initialization & Setup (Clone Data, Preprocess, Classify)",
            "1": "Setup Phase (Prepare files for translation)",
            "2": "Generate Inspection Files (Approved/Unapproved)",
            "3": "Create Translation Complete (Finalize Phase)",
            "4": "Build Final Translation (Merge all phases)",
            "5": "Deploy to Game",
            "6": "Utilities / Tools (Editor, Fix)",
            "q": "Quit"
        }

        for key, desc in main_choices.items():
            console.print(f"[cyan]{key}.[/cyan] {desc}")

        action = Prompt.ask("\nSelect an action", choices=list(main_choices.keys()), default="q")
        
        if action == "q":
            break

        console.print(f"\n[bold]Selected:[/bold] {main_choices[action]}")

        match action:
            case "0":
                # --- Initialization ---
                sub_choices = [
                    "1. Clone Data from Game",
                    "2. Run Pre-processing (Clean & Parse)",
                    "3. Run Classification (Categorize Keys)",
                    "4. Generate Phase Mapping",
                    "b. Back"
                ]
                while True:
                    console.print("\n[bold cyan]--- Initialization & Setup ---[/bold cyan]")
                    for sc in sub_choices:
                        console.print(sc)
                    
                    sub_action = Prompt.ask("Enter choice", choices=["1", "2", "3", "4", "b"], default="b")
                    
                    if sub_action == "b":
                        break
                    
                    match sub_action:
                        case "1": setup_workspace()
                        case "2": 
                            pre_proccess()
                            clean_thai()
                            run_comparison()
                        case "3": 
                            run_classification()
                            run_category_tree()
                        case "4": generate_phase_main()
                    
                    if sub_action != "b":
                        console.input("\n[dim]Press Enter to continue...[/dim]")

            case "1":
                # --- Setup Phase ---
                res = ask_phase()
                if res:
                    phase_obj, phase_path, _ = res
                    setup_phase(phase_obj, phase_path)

            case "2":
                # --- Generate Inspection Files ---
                res = ask_phase()
                if res:
                    phase_obj, _, _ = res
                    generate_inspection_files(phase_obj)

            case "3":
                # --- Create Translation Complete ---
                res = ask_phase()
                if res:
                    phase_obj, _, _ = res
                    create_phase_complete(phase_obj)

            case "4":
                # --- Build Final ---
                build_final_translation()

            case "5":
                # --- Deploy ---
                source_path = None
                abort = False
                default_source = config.FINAL_ENCODED_PATH
                console.print(f"\nDefault Source: [cyan]{default_source}[/cyan]")
                
                if Prompt.ask("Use default source?", choices=["y", "n"], default="y") == "n":
                    while True:
                        user_src_str = Prompt.ask("Enter full path to the source Thai.json file")
                        user_src_str = user_src_str.strip('"').strip("'")
                        user_src = Path(user_src_str)
                        
                        if user_src.is_file():
                            source_path = user_src
                            break
                        else:
                            console.print(f"[bold red]Error:[/bold red] File not found: {user_src}")
                            if Prompt.ask("Try again?", choices=["y", "n"], default="y") == "n":
                                abort = True
                                break
                
                if abort:
                    console.print("[yellow]Deployment aborted.[/yellow]")
                else:
                    default_dest = config.GAME_LANGUAGE_ROOT / "Thai.json"
                    console.print(f"\nDefault Destination: [cyan]{default_dest}[/cyan]")
                    
                    use_default = Prompt.ask("Deploy to this path?", choices=["y", "n"], default="y")
                    final_dest = default_dest

                    if use_default == "n":
                        while True:
                            user_path_str = Prompt.ask("Enter 'LanguageFiles' folder or full file path")
                            user_path_str = user_path_str.strip('"').strip("'")
                            user_path = Path(user_path_str)
                            
                            if user_path.is_dir():
                                final_dest = user_path / "Thai.json"
                            else:
                                final_dest = user_path
                                
                            if final_dest.parent.exists():
                                break
                            else:
                                console.print(f"[bold red]Error:[/bold red] Directory not found: {final_dest.parent}")
                                if Prompt.ask("Try again?", choices=["y", "n"], default="y") == "n":
                                    final_dest = None
                                    break
                    
                    if final_dest:
                        deploy_to_game(source=source_path, destination=final_dest)

            case "6":
                # --- Utilities ---
                while True:
                    console.print("\n[bold cyan]--- Utilities / Tools ---[/bold cyan]")
                    util_choices = {
                        "1": "Update Complete from Fixed (Audit Fix)",
                        "2": "Open Translation Editor (Instructions)",
                        "b": "Back"
                    }
                    for k, v in util_choices.items():
                        console.print(f"[cyan]{k}.[/cyan] {v}")
                    
                    util_action = Prompt.ask("Select tool", choices=list(util_choices.keys()), default="b")
                    
                    if util_action == "b":
                        break
                        
                    match util_action:
                        case "1":
                            res = ask_phase()
                            if res:
                                _, _, phase_num = res
                                version = Prompt.ask("Enter fixed version number", default="1")
                                update_complete_from_fixed(int(phase_num), int(version))
                        case "2":
                            console.print(Panel(
                                "[bold yellow]To start the Translation Editor:[/bold yellow]\n\n"
                                "Please open a [bold]NEW TERMINAL[/bold] window and run the following command:\n\n"
                                "[bold green]uv run streamlit run editor.py[/bold green]\n\n"
                                "This will launch the editor in your default web browser.\n"
                                "You can keep this main menu open while using the editor.",
                                title="📝 Translation Editor",
                                expand=False
                            ))
                    
                    console.input("\n[dim]Press Enter to continue...[/dim]")
                    console.clear()
        
        # Centralized Pause for main actions (excluding sub-menus and quit)
        if action not in ["0", "6", "q"]:
            console.input("\n[dim]Press Enter to continue...[/dim]")

    console.print("[bold green]Goodbye![/bold green]")

if __name__ == "__main__":
    main()
