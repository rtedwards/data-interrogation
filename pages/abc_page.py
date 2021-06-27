from abc import ABC, abstractmethod

import streamlit as st

class ABCPage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def show(self):
        """Shows the page of the class."""
