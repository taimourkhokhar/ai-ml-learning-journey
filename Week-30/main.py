# main.py
import streamlit as st
import langchain_helper

st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍔")
st.title("Restaurant Name Generator 🍽️")

# Sidebar for cuisine selection
cuisine = st.sidebar.selectbox(
    "Pick a Cuisine",
    ("Indian", "Italian", "Mexican", "Arabic", "American")
)

if cuisine:
    with st.spinner(f"Generating creative ideas for {cuisine} cuisine..."):
        response = langchain_helper.generate_restaurent_name_and_items(cuisine)
        
        # Display Restaurant Name
        st.header(response['restaurent_name'].strip())
        
        # Display Menu Items
        st.subheader("Suggested Menu Items")
        menu_items = response['menu_items'].split(",")
        for item in menu_items:
            st.write(f"• {item.strip()}")