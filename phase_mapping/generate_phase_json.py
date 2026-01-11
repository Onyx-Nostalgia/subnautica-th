import json
import os
import sys

from rich import print
from rich.console import Console

# import config from previous folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import (
    CLASSIFIED_PATH,
    PHASE_1_PATH,
    PHASE_2_PATH,
    PHASE_3_PATH,
    PHASE_4_PATH,
    PHASE_5_PATH,
    PHASE_MAPPING_PATH,
    PHASE_STATS,
)
from utils.file_io import save_json

# Define Phase Mappings (Root Categories)
PHASE_MAPPING = {
    "1_Core_System_UI": [
        "Main menu", "Save games", "Options screen", "Language names", "Input names", 
        "Loading, intro", "In-Game UI", "Ingame menu", "HUD", "Item Selector","Input and actions", "Generic Deploy",
    ],
    "2_Glossary_Items": [
        "Tech Categories","PDA", "Tech groups (builder tool menu tabs)", "Tech types", 
        "Ping labels", "Scanner", "Fragment analyzer", "Builder tool", 
        "Charger", "BatteryCharger", "PowerCellCharger", "Beacon", 
        "Propulsion Cannon", "Dive Reel", "Air Bladder", 
        "Sub & rocket editing console", "Submersible editing console", "Sign",
        "BaseBioReactor", "BaseNuclearReactor", "Decoration", 
        "Cyclops", "cyclops launch bay", "Cyclops Decoy Tube", 
        "Tool upgrades", "TOOLTIPS", "TECH","SIGN LABELS"
    ],
    "3_Story_The_Awakening": [
        "Intro hints", "Hints", "Escape pod", "LIFEPOD SCREEN", 
        "PDA VOICE - AURORA EXPLOSION", "INTRO PDA VO", "PDA VO ITEMS", 
        "STARTING ENTRIES", "LIFEPOD TEXTS", "RADIO", "RADIO ALTS CLUES NOT SIGNALS"
    ],
    "4_The_Journey_Lore": [
        "Rocket", "Time Capsule", "Time Capsule status", "SUNBEAM", 
        "PDA VO BIOMES", "AURORA PDA VO", "CRASHED SHIP LORE TEXTS (ONBOARD AURORA)", 
        "FLOATING ISLAND SEABASE", "JELYSHROOM SEABASE", "DEEP GRAND REEF SEABASE", 
        "PRECURSOR STORY", "PRECURSOR GUN", "LOSTRIVER BASE", 
        "Lost River Biome Scannables", "LAVA CASTLE BASE", 
        "EMPEROR PRISON - External Rooms", "TERMINALS ANTECHAMBER", 
        "EMPEROR PRISON - Aquarium", "Emperor VOs", "PRECURSOR CACHES"
    ],
    "5_The_Encyclopedia": [
        "ENCYCLOPEDIA HEADERS", "WRECKAGE LORE TEXTS (INNER BIOMES)", 
        "WRECKAGE LORE TEXTS (OUTER BIOMES)", "OUTCROPS", "UNIQUE CREATURES", 
        "RAYS", "EDIBLE FISH", "LEVIATHANS", "SHARKS", "SCAVENGERS", 
        "PLANTS", "EGGS", "LAND PLANTS", "SEA PLANTS"
    ]
}

def main():
    if not os.path.exists(CLASSIFIED_PATH):
        print(f"Error: {CLASSIFIED_PATH} not found.")
        return

    with open(CLASSIFIED_PATH, 'r', encoding='utf-8') as f:
        classified_data = json.load(f)

    # Invert mapping for easier lookup (lower case key -> phase)
    # Also keep track of roots to handle dot notation
    root_to_phase = {}
    for phase, roots in PHASE_MAPPING.items():
        for root in roots:
            root_to_phase[root.lower()] = phase

    output_data = {phase: {} for phase in PHASE_MAPPING.keys()}
    output_data["Uncategorized"] = {}

    total_categories = 0
    stats = {phase: {"total_categories": 0, "total_keys": 0} for phase in PHASE_MAPPING.keys()}
    
    for category,keys in classified_data.items():            
        total_categories += 1
        
        # 1. Exact match (case-insensitive)
        phase = root_to_phase.get(category.lower())
        
        # 2. Dot notation parent match (e.g. "TOOLTIPS.Fragments" -> "TOOLTIPS")
        if not phase and "." in category:
            parent = category.split(".")[0]
            phase = root_to_phase.get(parent.lower())
            
        # 3. Fallback: manual fixes or catch-all if needed
        # (For now, let it fall to Uncategorized so we can see what's missing)

        if phase:
            output_data[phase][category] = keys
            stats[phase]["total_categories"] += 1
            stats[phase]["total_keys"] += len(keys)
        else:
            output_data["Uncategorized"][category] = keys

    # Write output
    save_json(output_data,PHASE_MAPPING_PATH)
    
    phase_path = [PHASE_1_PATH,PHASE_2_PATH,PHASE_3_PATH,PHASE_4_PATH,PHASE_5_PATH]
    for i,(phase,data) in enumerate(output_data.items()):
        if phase == "Uncategorized":
            continue
        save_json(data,phase_path[i])
    
    # Print stats
    console = Console(record=True)
    console.print("=" * 30)
    console.print(f"🔹 Total Categories Processed: {total_categories}")
    for phase,stat in stats.items():
        console.print(f"🔹 Phase: [green bold]{phase}")
        console.print(f"  - Total Categories: {stat['total_categories']}")
        console.print(f"  - Total Keys: {stat['total_keys']}")
        console.print()
    
    if len(output_data["Uncategorized"]) > 0:
        console.print("[red]🟥 Uncategorized:", len(output_data["Uncategorized"]))
        for category,keys in output_data["Uncategorized"].items():
            console.print(f"  - {category}: {len(keys)}")
    console.print("=" * 30)
    console.save_text(PHASE_STATS)
    print(f"✅ บันทึกไฟล์ {PHASE_STATS} เรียบร้อย")

if __name__ == "__main__":
    main()
