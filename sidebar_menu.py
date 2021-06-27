from pages.abc_page import ABCPage

import streamlit as st

from pages.home_page import HomePage
from pages.multiprocessing_page import MultiprocessingPage
from pages.mean_variance_page import MeanVariancePage
from pages.numba_page import NumbaPage
from pages.probability_page import ProbabilityPage
from pages.random_forest_page import RandomForestPage
from pages.support_vector_machine_page import SupportVectorMachinePage
from pages.z_score_page import ZScorePage
from pages.isolation_forest_page import IsolationForestPage
from pages.one_class_svm_page import OneClassSVMPage
from pages.bias_variance_tradeoff_page import BiasVarianceTradeoffPage
from pages.train_validation_test_page import TrainValidationTestPage
from pages.cross_validation_page import CrossValidationPage
from pages.dbscan_page import DBSCANPage
from pages.hdbscan_page import HDBSCANPage
from pages.shap_page import SHAPPage
from pages.lime_page import LIMEPage


from pages.abc_page import ABCPage

class SidebarMenu(ABCPage):
    def __init__(self):
        self.github_badge = "[![Star](https://img.shields.io/github/stars/rtedwards/data-interrogation.svg?logo=github&style=social)](https://github.com/rtedwards/data-interrogation)"
        self.twitter_badge = "[![Follow](https://img.shields.io/twitter/follow/bobeartoes?style=social)](https://www.twitter.com/bobeartoes)"

        self.machine_learning = {
            "Bias Variance Trade-Off": BiasVarianceTradeoffPage(),
            "Train/Validation/Test": TrainValidationTestPage(),
            "Cross Validation": CrossValidationPage()
        }
        self.supervised_learning = {
            "Random Forest": RandomForestPage(),
            "Support Vector Machine": SupportVectorMachinePage()
        }
        self.unsupervised_learning = {
            "DBSCAN": DBSCANPage(),
            "HDBSCAN": HDBSCANPage(),
        }
        self.anamoly_detection = {
            "Z-Score": ZScorePage(),
            "Isolation Forest": IsolationForestPage(),
            "One-Class SVM": OneClassSVMPage(),
        }
        self.performance = {
            "Multiprocessing": MultiprocessingPage(),
            "Numba": NumbaPage(),
        }
        self.probability = {
            "Expected Value & Variance": MeanVariancePage(),
            "Probability": ProbabilityPage(),
        }
        self.frequentist = {
            # "P-Values": PValuesPage()
            # "Hypothesis Testing": HypothesisTestingPage(),
        }
        self.bayesian = {
            # "Bayes Rule": BayesRulePage(), 
        }
        self.explainable_ai = {
            "LIME": LIMEPage(),
            "SHAP": SHAPPage(),
        }
        self.projects = {
            # "Spotify Track Reccomender": SpotifyTrackReccomenderPage(), 
            # "COVID Tracker": COVIDTrackerPage(), 
            # "Real-Time Data Streams": COVIDTrackerPage(), 
        }
    
    def show(self):
        page_selection = HomePage()

        with st.sidebar:
            with st.beta_expander("Machine Learning", expanded=False):
                st.markdown("### Machine Learning Concepts")
                for k, v in self.machine_learning.items():
                    if st.button(f"{k}"):
                        page_selection = v

                st.markdown("### Supervised Learning")
                for k, v in self.supervised_learning.items():
                    if st.button(f"{k}"):
                        page_selection = v

                st.markdown("### Unsupervised Learning")
                for k, v in self.unsupervised_learning.items():
                    if st.button(f"{k}"):
                        page_selection = v
                
                st.markdown("### Anamoly Detection")
                for k, v in self.anamoly_detection.items():
                    if st.button(f"{k}"):
                        page_selection = v
            
            with st.beta_expander("Explainable AI", expanded=False):
                for k, v in self.explainable_ai.items():
                    if st.button(f"{k}"):
                        page_selection = v

            with st.beta_expander("Performance", expanded=False):
                for k, v in self.performance.items():
                    if st.button(f"{k}"):
                        page_selection = v

            with st.beta_expander("Statistics", expanded=False):
                st.markdown("### Probability")
                for k, v in self.probability.items():
                    if st.button(f"{k}"):
                        page_selection = v

                st.markdown("### Frequentist")
                for k, v in self.frequentist.items():
                    if st.button(f"{k}"):
                        page_selection = v

                st.markdown("### Bayesian Statistics")
                for k, v in self.bayesian.items():
                    if st.button(f"{k}"):
                        page_selection = v

            with st.beta_expander("Projects", expanded=False):
                for k, v in self.projects.items():
                    if st.button(f"{k}"):
                        page_selection = v
        
            st.write(f"{self.github_badge} {self.twitter_badge}")

        return page_selection

                