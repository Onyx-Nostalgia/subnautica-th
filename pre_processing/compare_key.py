import json
import os
import sys

from rich.console import Console

# import config from previous folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import ORIGINAL_THAI_PATH, PARSED_PATH

console = Console()

def run_comparison():
    # Read Files
    with open(PARSED_PATH, "r", encoding="utf-8") as f:
        en_data = json.load(f)

    with open(ORIGINAL_THAI_PATH, "r", encoding="utf-8") as f:
        th_data = json.load(f)

    # Merge Keys
    th_keys = set(th_data.keys())
    en_keys = set(en_data.keys())

    # Compare Keys
    missing_in_th = en_keys - th_keys
    extra_in_th = th_keys - en_keys
    comparison_result = {"missing_in_th": list(missing_in_th), "extra_in_th": list(extra_in_th)}

    # Print comparison_result
    console.print("=== Key Comparison Result ===")
    console.print(comparison_result)

if __name__ == "__main__":
    run_comparison()

