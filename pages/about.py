from typing import Dict
import pandas as pd
import streamlit as st
st.info('this is kero')
st.success('koko')
name = st.text_input ('enter your name')
age = st.number_input ('enter ur num')
height = st.slider ('enter ur height', min_value=0,max_value=200 , step = 10)
Dic = {'name' : name , 'age' : age}
df = pd.DataFrame(Dic,index=[0])
st.write(df)

def get_data():
    return pd.DataFrame ('name' : name , 'age' : age)
