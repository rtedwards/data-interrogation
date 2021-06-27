import streamlit as st

from pages.abc_page import ABCPage

class HomePage(ABCPage):
    def __init__(self):
        # super().__init__()
        pass

    def show(self):
        st.title("Data Interrogations")

        st.markdown("""
            ## Random Forest Multiclass Classifier

            A random forest classifier is trained to predict...
            
            - gif
            - hyperlink
            ----
        """)

        st.markdown("""
            ## SHAP: Binary Classifier

            SHAP is used to explain a binary classifier
            - gif
            - hyperlink
            ----
        """)

        st.markdown("""
            ## SHAP: Multiclass Classifier

            SHAP is used to explain a multiclass classifier
            - gif
            - hyperlink
            ----
        """)

        st.markdown("""
            ## SHAP: Regression

            SHAP is used to explain a regression model
            - gif
            - hyperlink
            ----
        """)

        st.markdown("""
            ## SHAP: Regression

            SHAP is used to explain a neural network model
            - gif
            - hyperlink
            ----
        """)



