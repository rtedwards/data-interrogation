import streamlit as st

from sidebar_menu import SidebarMenu
from pages.home_page import HomePage

st.set_page_config(page_title="Data Interrogations", page_icon=None, layout='wide', initial_sidebar_state='auto')

if __name__ == "__main__":
    page_selection = SidebarMenu().show()
    if page_selection is None:
        HomePage().show()
    page_selection.show()