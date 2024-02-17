import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Prediction App

This App predicts the **Palmer Penguin** Species!

Data obtained from [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
""")

st.sidebar.header('User Input Features')
st.sidebar.markdown("""
[Example CSV input file]
""")