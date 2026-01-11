from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from pathlib import Path

import config
from utils import (
    build_final_translation,
    create_phase_complete,
    create_review_form,
    deploy_to_game,
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

def main():
    console.print("[bold blue]Subnautica Thai Localization Tool[/bold blue]")
    
    choices = [
        "0. Initialization & Setup (Clone Data, Preprocess, Classify)",
        "------------------------------------",
        "1. Setup Phase 1 (Core System & UI)",
        "2. Setup Phase 2 (Glossary Items)",
        "3. Setup Phase 3 (Story - The Awakening)",
        "4. Setup Phase 4 (The Journey Lore)",
        "5. Setup Phase 5 (The Encyclopedia)",
        "------------------------------------",
        "6. Create Review Form Phase 1",
        "7. Create Review Form Phase 2",
        "8. Create Review Form Phase 3",
        "9. Create Review Form Phase 4",
        "10. Create Review Form Phase 5",
        "------------------------------------",
        "11. Create Translation Complete Phase 1",
        "12. Create Translation Complete Phase 2",
        "13. Create Translation Complete Phase 3",
        "14. Create Translation Complete Phase 4",
        "15. Create Translation Complete Phase 5",
        "------------------------------------",
        "16. Build Final Translation",
        "17. Deploy to Game",
        "18. Update Complete from Fixed",
        "------------------------------------",
        "19. Open Translation Editor (Instructions)",
        "------------------------------------",
        "q. Quit"
    ]
    
    console.clear() # Clear start
    
    while True:
        console.print("[bold blue]Subnautica Thai Localization Tool[/bold blue]")
        console.print("\n[bold]Select an action:[/bold]")
        for choice in choices:
            console.print(choice)
            
        action = Prompt.ask("Enter choice", choices=[
            "0",
            "1", "2", "3", "4", "5", 
            "6", "7", "8", "9", "10", 
            "11", "12", "13", "14", "15","16","17", "18", "19",
             "q"
        ], default="q")
        
        if action == "q":
            break
            
        match action:
            case "0":
                console.clear()
                console.print("[bold cyan]--- Initialization & Setup ---[/bold cyan]")
                sub_choices = [
                    "1. Clone Data from Game",
                    "2. Run Pre-processing (Clean & Parse)",
                    "3. Run Classification (Categorize Keys)",
                    "4. Generate Phase Mapping",
                    "b. Back"
                ]
                while True:
                    console.print("\n[bold]Setup Menu:[/bold]")
                    for sc in sub_choices:
                        console.print(sc)
                    
                    sub_action = Prompt.ask("Enter choice", choices=["1", "2", "3", "4", "b"], default="b")
                    
                    if sub_action == "b":
                        break
                    
                    match sub_action:
                        case "1":
                            setup_workspace()
                        case "2":
                            pre_proccess()
                            clean_thai()
                            run_comparison()
                        case "3":
                            run_classification()
                            run_category_tree()
                        case "4":
                            generate_phase_main()
                    
                    console.input("\n[dim]Press Enter to continue...[/dim]")
                    console.clear()

            case "1":
                setup_phase(config.PHASE_1, config.PHASE_1_PATH)
            case "2":
                setup_phase(config.PHASE_2, config.PHASE_2_PATH)
            case "3":
                setup_phase(config.PHASE_3, config.PHASE_3_PATH)
            case "4":
                setup_phase(config.PHASE_4, config.PHASE_4_PATH)
            case "5":
                setup_phase(config.PHASE_5, config.PHASE_5_PATH)
            case "6":
                create_review_form(config.PHASE_1)
            case "7":
                create_review_form(config.PHASE_2)
            case "8":
                create_review_form(config.PHASE_3)
            case "9":
                create_review_form(config.PHASE_4)
            case "10":
                create_review_form(config.PHASE_5)
            case "11":
                create_phase_complete(config.PHASE_1)
            case "12":
                create_phase_complete(config.PHASE_2)
            case "13":
                create_phase_complete(config.PHASE_3)
            case "14":
                create_phase_complete(config.PHASE_4)
            case "15":
                create_phase_complete(config.PHASE_5)
            case "16":
                build_final_translation()
            case "17":
                # Ask for version (Optional)
                deploy_version = None
                if Prompt.ask("Deploy specific version?", choices=["y", "n"], default="n") == "y":
                    deploy_version = int(Prompt.ask("Enter version number"))

                # Ask for destination path logic
                default_dest = config.GAME_TRANSLATION_PATH
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
                                final_dest = None # Cancelled
                                break
                
                if final_dest:
                    deploy_to_game(version=deploy_version, destination=final_dest)

            case "19":
                console.print(Panel(
                    "[bold yellow]To start the Translation Editor:[/bold yellow]\n\n"
                    "Please open a [bold]NEW TERMINAL[/bold] window and run the following command:\n\n"
                    "[bold green]uv run streamlit run editor.py[/bold green]\n\n"
                    "This will launch the editor in your default web browser.\n"
                    "You can keep this main menu open while using the editor.",
                    title="📝 Translation Editor",
                    expand=False
                ))
            case "18":
                phase_num = Prompt.ask("Enter phase number", choices=["1", "2", "3", "4", "5"])
                version = Prompt.ask("Enter fixed version number", default="1")
                update_complete_from_fixed(int(phase_num), int(version))
        

        # Pause and Clear
        console.input("\n[dim]Press Enter to continue...[/dim]")
        console.clear()

            
    console.print("[bold green]Goodbye![/bold green]")

if __name__ == "__main__":
    main()
