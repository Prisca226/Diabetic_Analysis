import pandas as pd
import streamlit as st
import matplotlib.pyplot as pt
import numpy as np
import seaborn as sns


#import my csv file
st.title("*DIABETES_ANALYSIS*")
df = pd.read_csv("diabetes.csv")
st.markdown("# FIRST FIVE")
st.write(df.head())


df = pd.read_csv("diabetes.csv")
st.markdown("# LAST FIVE")
st.write(df.tail())

st.markdown("### DATA INFO")
my = df.info()
st.write(my)

st.markdown("# DATA DESCRIBE")
my = df.describe()
st.write(my)

st.markdown("# DATA SHAPE")
my = df.shape
st.write(my)

st.markdown("## UNIVARIENT ANALYSIS")

st.markdown("### Blood Pressure")
st.write(df["BloodPressure"].describe())


