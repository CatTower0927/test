import streamlit as st

st.set_page_config(page_title="Mood Color App", layout="centered")

st.title("🎨 오늘의 기분색")

# 기분 - 색상 매핑
mood_colors = {
    "😊 행복해요": "#FFE066",
    "😢 슬퍼요": "#74C0FC",
    "😡 화가나요": "#FF6B6B",
    "😴 피곤해요": "#B197FC",
    "😐 그냥 그래요": "#D3D3D3"
}

# 사용자 입력
mood = st.selectbox("오늘 기분이 어떤가요?", list(mood_colors.keys()))

# 선택된 색상
selected_color = mood_colors[mood]

# CSS로 배경색 적용
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {selected_color};
        transition: background-color 0.5s ease;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.write(f"### 오늘의 기분 색은 `{selected_color}` 입니다!")

