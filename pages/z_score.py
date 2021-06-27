import streamlit as st

from pages.abc_page import ABCPage

class ZScorePage(ABCPage):
    def __init__(self):
        super().__init__()

    def show(self):
        st.error(f"{self.__class__} not implemented...")