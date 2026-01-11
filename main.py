from rich.console import Console
from rich.prompt import Prompt

import config
from utils import (
    build_final_translation,
    create_phase_complete,
    create_review_form,
    deploy_to_game,
    setup_phase,
    update_complete_from_fixed,
)

console = Console()

def main():
    console.print("[bold blue]Subnautica Thai Localization Tool[/bold blue]")
    
    choices = [
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
        "q. Quit"
    ]
    
    console.clear() # Clear start
    
    while True:
        console.print("[bold blue]Subnautica Thai Localization Tool[/bold blue]")
        console.print("\n[bold]Select an action:[/bold]")
        for choice in choices:
            console.print(choice)
            
        action = Prompt.ask("Enter choice", choices=[
            "1", "2", "3", "4", "5", 
            "6", "7", "8", "9", "10", 
            "11", "12", "13", "14", "15","16","17", "18",
             "q"
        ], default="q")
        
        if action == "q":
            break
            
        match action:
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
                deploy_to_game()
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
