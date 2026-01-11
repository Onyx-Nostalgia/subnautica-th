import json
import math
import os

import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(layout="wide", page_title="Subnautica Thai Localization Editor")

FILE_PATH = "data/5_the_encyclopedia/translation_progress.json"
ITEMS_PER_PAGE = 20

def escape_newlines(text):
    return text

def unescape_newlines(text):
    return text

def load_data():
    if not os.path.exists(FILE_PATH):
        st.error(f"File not found: {FILE_PATH}")
        return None
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
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

def save_data(df):
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
            
        with open(FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)
        
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False

# Initialize Session State
if "df" not in st.session_state:
    st.session_state.df = load_data()
if "page_number" not in st.session_state:
    st.session_state.page_number = 1

st.title("Translation Editor: Phase 5")

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
        if save_data(st.session_state.df):
            st.toast("✅ Saved successfully!", icon="💾")
            st.success("Saved to JSON.")
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
