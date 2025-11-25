# code1
import streamlit as st

st.title("Hello Streamlit 👋")                       	# 제목
st.write("파이선 코드가 웹페이지로 바뀌었어요!")      	# 내용
x = st.slider("슬라이더를 움직여볼까요?", 0, 100, 50)	# 슬라이더
st.write("현재 값은:", x)
