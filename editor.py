import json
import math
import os

import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(layout="wide", page_title="Subnautica Thai Localization Editor")

ITEMS_PER_PAGE = 20

# Phase Definitions
PHASE_INFO = {
    1: {"name": "Phase 1: Core System & UI", "path": "data/1_core_system_ui/translation_progress.json"},
    2: {"name": "Phase 2: Glossary Items", "path": "data/2_glossary_items/translation_progress.json"},
    3: {"name": "Phase 3: Story - The Awakening", "path": "data/3_story_the_awakening/translation_progress.json"},
    4: {"name": "Phase 4: The Journey Lore", "path": "data/4_the_journey_lore/translation_progress.json"},
    5: {"name": "Phase 5: The Encyclopedia", "path": "data/5_the_encyclopedia/translation_progress.json"},
}

def escape_newlines(text):
    return text

def unescape_newlines(text):
    return text

def load_data(file_path):
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return None
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    rows = []
    for key, value in data.items():
        row = {
            "Keyname": key,
            "Category": value.get("Category", ""),
            "English": escape_newlines(value.get("English", "")),
            "Thai": escape_newlines(value.get("Thai", "")),
            "Result": escape_newlines(value.get("Result", "")),
            "Approved": value.get("Approved", False)
        }
        rows.append(row)
    
    return pd.DataFrame(rows)

def save_data(df, file_path):
    try:
        output_data = {}
        for index, row in df.iterrows():
            key = row["Keyname"]
            output_data[key] = {
                "Category": row["Category"],
                "English": unescape_newlines(row["English"]),
                "Thai": unescape_newlines(row["Thai"]),
                "Result": unescape_newlines(row["Result"]),
                "Approved": bool(row["Approved"])
            }
            
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

# --- 1. Phase Selection Logic ---

# Check Query Params for persistence
if "phase" in st.query_params:
    try:
        st.session_state.selected_phase = int(st.query_params["phase"])
    except ValueError:
        st.query_params.clear()

if "selected_phase" not in st.session_state:
    st.title("📂 Select Phase to Edit")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        phase_choice = st.radio(
            "Choose a Phase:",
            options=[1, 2, 3, 4, 5],
            format_func=lambda x: PHASE_INFO[x]["name"]
        )
        
        if st.button("🚀 Load Editor", type="primary"):
            st.session_state.selected_phase = phase_choice
            st.query_params["phase"] = str(phase_choice)
            st.rerun()
            
    with col2:
        st.info(f"You are selecting: **{PHASE_INFO[phase_choice]['name']}**")
        st.code(f"Path: {PHASE_INFO[phase_choice]['path']}")

else:
    # Ensure query param is synced (in case it came from session state but url is empty)
    st.query_params["phase"] = str(st.session_state.selected_phase)

    # --- 2. Editor Mode ---
    current_phase_id = st.session_state.selected_phase
    current_phase_info = PHASE_INFO[current_phase_id]
    FILE_PATH = current_phase_info["path"]
    
    # Initialize Session State for Data
    # Reload logic: If phase changed OR if we want to force reload (optional)
    # Ideally, load_data happens every run if we want real-time updates from disk?
    # No, Streamlit reruns script top-to-bottom.
    # To see AI updates on refresh, we MUST reload data from disk on script run if not in session,
    # OR explicitly clear session state df when refreshing.
    
    # ISSUE: If we keep 'df' in session_state, F5 might preserve it depending on Streamlit runner.
    # Standard F5 usually clears session state UNLESS it's persisted. 
    # Actually, standard F5 CLEARS session_state. So load_data() will run again automatically!
    # That is exactly what we want.
    
    if "df" not in st.session_state or st.session_state.get("current_loaded_phase") != current_phase_id:
        st.session_state.df = load_data(FILE_PATH)
        st.session_state.current_loaded_phase = current_phase_id
        st.session_state.page_number = 1 

    st.title(f"📝 {current_phase_info['name']}")

    # 1. Define Filter Logic FIRST (Before Sidebar Controls)
    df_display = st.session_state.df

    # We need to capture the search query early if we want the button to use the filtered view
    # However, inputs are usually placed in layout. 
    # Best approach: Place Filter Input in Sidebar TOP, then define df_display, THEN the buttons.

    with st.sidebar:
        st.header("Controls")
        
        # Filter Input FIRST
        search_query = st.text_input("🔍 Search (Key/Eng):", placeholder="Type to search...")
        
        # Update df_display based on filter
        if search_query:
            df_display = st.session_state.df[
                st.session_state.df["Keyname"].str.contains(search_query, case=False) |
                st.session_state.df["English"].str.contains(search_query, case=False)
            ]
        else:
             df_display = st.session_state.df # Reset to full if no search

        st.markdown("---")

        # Save Button
        if st.button("💾 Save All Changes", type="primary", use_container_width=True):
            if save_data(st.session_state.df, FILE_PATH):
                st.toast("✅ Saved successfully!", icon="💾")
                st.success("Saved to JSON.")
                # Optional: Reload to ensure sync? Not strictly needed if save success.
            else:
                st.error("Failed to save.")
                
        # Jump Button (Now safe to use df_display)
        if st.button("⏩ Jump to First Draft", use_container_width=True):
            # Find first unapproved item in the current display (respecting filter)
            # Check if column exists and has any False values
            if "Approved" in df_display.columns:
                 # Get boolean mask of unapproved items
                 unapproved_mask = ~df_display["Approved"]
                 
                 if unapproved_mask.any():
                    # Find the integer position of the first True in the mask
                    # We iterate through the boolean series to find the first match's integer index
                    first_unapproved_pos = -1
                    for i, is_unapproved in enumerate(unapproved_mask):
                        if is_unapproved:
                            first_unapproved_pos = i
                            break
                    
                    if first_unapproved_pos != -1:
                        target_page = math.ceil((first_unapproved_pos + 1) / ITEMS_PER_PAGE)
                        st.session_state.page_number = target_page
                        st.toast(f"Jumped to page {target_page}", icon="🚀")
                        st.rerun()
                 else:
                    st.toast("🎉 All items approved!", icon="✅")
        
        st.markdown("---")
        
        if st.button("🔄 Change Phase"):
            st.query_params.clear()
            if "selected_phase" in st.session_state:
                del st.session_state.selected_phase
            if "df" in st.session_state:
                del st.session_state.df
            st.rerun()

        st.markdown("---")
        
        total_items = len(df_display)
        total_pages = math.ceil(total_items / ITEMS_PER_PAGE)
        
        # Ensure page number is valid
        if st.session_state.page_number > total_pages:
            st.session_state.page_number = max(1, total_pages)
            
        st.markdown(f"**Total Items:** {total_items}")
        
        # Pagination Controls
        col_prev, col_page, col_next = st.columns([1, 2, 1])
        with col_prev:
            if st.button("◀️", disabled=st.session_state.page_number <= 1):
                st.session_state.page_number -= 1
                st.rerun()
        with col_next:
            if st.button("▶️", disabled=st.session_state.page_number >= total_pages):
                st.session_state.page_number += 1
                st.rerun()
        with col_page:
            st.write(f"Page {st.session_state.page_number}/{total_pages}")
            
        # Jump to page
        new_page = st.number_input("Go to page", min_value=1, max_value=max(1, total_pages), value=st.session_state.page_number)
        if new_page != st.session_state.page_number:
            st.session_state.page_number = new_page
            st.rerun()

    # --- Main Content: Form View ---

    if total_items == 0:
        st.info("No items found.")
    else:
        start_idx = (st.session_state.page_number - 1) * ITEMS_PER_PAGE
        end_idx = min(start_idx + ITEMS_PER_PAGE, total_items)
        
        current_page_items = df_display.iloc[start_idx:end_idx]

        for i, (index, row) in enumerate(current_page_items.iterrows()):
            
            # Outer Container (Standard Border)
            with st.container(border=True):
                
                # 1. Colored Status Bar
                if row["Approved"]:
                    st.success(f"✅ Approved : {row['Keyname']}")
                else:
                    st.warning(f"📝 Draft : {row['Keyname']}")
                
                # 2. Controls & Metadata
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.caption(f"Category: {row['Category']}")
                with c2:
                    # Toggle
                    is_approved = st.checkbox("Approved", value=row["Approved"], key=f"check_{row['Keyname']}")
                    if is_approved != row["Approved"]:
                        st.session_state.df.at[index, "Approved"] = is_approved
                        st.rerun()

                # 3. English Content
                st.markdown("##### 🔵 English (Source)")
                st.code(row["English"], language="html") 
                
                # 4. Thai Content
                st.markdown("##### ⚪ Thai (Reference)")
                if row["Thai"]:
                    st.info(row["Thai"], icon="🇹🇭")
                else:
                    st.text("(No reference)")
                
                # 5. Result Content
                st.markdown("##### 🟢 Result (Edit)")
                
                # Calculate dynamic height
                line_count = row["Result"].count('\n') + 1
                dynamic_height = max(150, line_count * 24)
                
                new_result = st.text_area(
                    label="Result",
                    value=row["Result"],
                    label_visibility="collapsed",
                    height=dynamic_height,
                    key=f"text_{row['Keyname']}"
                )
                
                if new_result != row["Result"]:
                    st.session_state.df.at[index, "Result"] = new_result

        st.markdown("---")
        st.write(f"Showing items {start_idx + 1} to {end_idx}")
