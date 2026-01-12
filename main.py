import re
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from pathlib import Path

import config
from utils import (
    build_final_translation,
    create_phase_complete,
    create_release_package,
    deploy_to_game,
    generate_inspection_files,
    re_encode_final_files,
    setup_phase,
    update_complete_from_fixed,
)
from utils.setup_project import setup_workspace
from pre_processing.preprocess import pre_proccess, clean_thai
from pre_processing.compare_key import run_comparison
from classification.classify import run_classification
from classification.category_tree import run_category_tree
from phase_mapping.generate_phase_json import main as generate_phase_main

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
            "6": "Create Release Package (ZIP)",
            "7": "Utilities / Tools (Editor, Fix, Re-encode)",
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
                deploy_version = None
                if Prompt.ask("Deploy specific version?", choices=["y", "n"], default="n") == "y":
                    deploy_version = int(Prompt.ask("Enter version number"))

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
                    deploy_to_game(version=deploy_version, destination=final_dest)

            case "6":
                # --- Create Release Package ---
                version_str = Prompt.ask("Enter Release Version String (e.g. 1.0.1, must be x.x.x)")
                if not re.fullmatch(r"^\d+\.\d+\.\d+$", version_str):
                    console.print("[bold red]Error:[/bold red] Version string must be in x.x.x format (e.g., 1.0.1). Aborting release package creation.")
                else:
                    source_ver = None
                    if Prompt.ask("Use latest translation version as source?", choices=["y", "n"], default="y") == "n":
                        source_ver = int(Prompt.ask("Enter source version number"))
                    
                    create_release_package(version_str, source_version=source_ver)

            case "7":
                # --- Utilities ---
                while True:
                    console.print("\n[bold cyan]--- Utilities / Tools ---[/bold cyan]")
                    util_choices = {
                        "1": "Update Complete from Fixed (Audit Fix)",
                        "2": "Re-Encode Final Files (Update from Decode)",
                        "3": "Open Translation Editor (Instructions)",
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
                            re_encode_final_files()
                        case "3":
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
        if action not in ["0", "7", "q"]:
            console.input("\n[dim]Press Enter to continue...[/dim]")

    console.print("[bold green]Goodbye![/bold green]")

if __name__ == "__main__":
    main()
