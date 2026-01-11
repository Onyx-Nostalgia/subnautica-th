from pathlib import Path


class TranslationPhase:
    """
    Helper class to manage translation paths for each phase.
    Reduces repetition and ensures consistency.
    """
    def __init__(self, directory: str):
        self.DIR = Path(directory)
        self.KEY_PATH = self.DIR / 'translation_key.json'
        self.PROGRESS_PATH = self.DIR / 'translation_progress.json'
        self.REVIEW_PATH = self.DIR / 'translation_review.json'
        self.COMPLETE_PATH = self.DIR / 'translation_complete.json'
        self.APPROVED_REVIEW_PATH = self.DIR / 'translation_approved_review.json'
        self.UNAPPROVED_REVIEW_PATH = self.DIR / 'translation_unapproved_review.json'

# Original File Paths
ORIGINAL_ENGLISH_PATH = Path('data/Original/English.json')
ORIGINAL_THAI_PATH = Path('data/Original/Thai.json')

# Pre-processing Paths
PRE_PROCESSING_DIR = Path('data/pre_processing')
PARSED_PATH = PRE_PROCESSING_DIR / 'English_parsed.json'
CLEANED_PATH = PRE_PROCESSING_DIR / 'English_cleaned.json'
DECODED_THAI_PATH = PRE_PROCESSING_DIR / 'Thai_decoded.json'
CLEANED_THAI_PATH = PRE_PROCESSING_DIR / 'Thai_cleaned.json'
SORTED_BY_TH_PATH = PRE_PROCESSING_DIR / 'English_sorted_by_th.json'
SORTED_BY_EN_PATH = PRE_PROCESSING_DIR / 'Thai_sorted_by_en.json'

# Classification Paths
CLASSIFICATION_DIR = Path('data/classification')
CLASSIFIED_PATH = CLASSIFICATION_DIR / 'categories.json'
CLASSIFIED_TREE_PATH = CLASSIFICATION_DIR / 'category_tree.txt'

# Phase Mapping
PHASE_DIR = Path('data/phase_mapping')
PHASE_STATS = PHASE_DIR / 'phase_stats.txt'
PHASE_MAPPING_PATH = PHASE_DIR / 'phase_mapping.json'
PHASE_1_PATH = PHASE_DIR / '1_Core_System_UI.json'
PHASE_2_PATH = PHASE_DIR / '2_Glossary_Items.json'
PHASE_3_PATH = PHASE_DIR / '3_Story_The_Awakening.json'
PHASE_4_PATH = PHASE_DIR / '4_The_Journey_Lore.json'
PHASE_5_PATH = PHASE_DIR / '5_The_Encyclopedia.json'

# ==========================================
# Phase Contexts
# ==========================================
# Usage: config.PHASE_3.KEY_PATH, config.PHASE_3.PROGRESS_PATH, etc.

# Phase 1: Core System & UI
PHASE_1 = TranslationPhase('data/1_core_system_ui')

# Phase 2: Glossary Items
PHASE_2 = TranslationPhase('data/2_glossary_items')

# Phase 3: Story - The Awakening
PHASE_3 = TranslationPhase('data/3_story_the_awakening')

# Phase 4: The Journey Lore
PHASE_4 = TranslationPhase('data/4_the_journey_lore')

# Phase 5: The Encyclopedia
PHASE_5 = TranslationPhase('data/5_the_encyclopedia')


# Temporary Paths
## example manual paths; adjust as needed
# DECODED_THAI_V2_PATH = 'data/tmp/Decoded_Thai_v2.json'

# Game Configuration
# TODO: Make this configurable via environment variable or user input
GAME_TRANSLATION_PATH = Path('/mnt/d/Epic Games/Subnautica/Subnautica_Data/StreamingAssets/SNUnmanagedData/LanguageFiles/Thai.json')
