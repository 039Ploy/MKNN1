import streamlit as st
import pandes as pd

st.title("❤️🧸Website Developing using Python🧸❤️")
st.header("🎈🎈Website Developing using Python🎈🎈")

st.imsge('./img/Thipnapa.jpg')
st.subheader("🌼Thipnapa Natsawang🌼") 

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.erite(dt.head(10))