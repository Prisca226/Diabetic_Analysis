import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns


#import my csv file
st.title("Diabetes Analysis")
df = pd.read_csv("diabetes.csv")
st.markdown("# FIRST FIVE")
st.write(df.head())


df = pd.read_csv("diabetes.csv")
st.markdown("# LAST FIVE")
st.write(df.tail())

