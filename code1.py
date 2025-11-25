import streamlit as st            # Streamlit 라이브러리를 불러와 웹 앱 형태로 결과를 표시
import plotly.graph_objects as go # Plotly의 그래프 객체를 사용하기 위한 모듈
import random                     # 난수(무작위 수) 생성을 위한 모듈

# 주사위 눈 1~6 사이에서 무작위 정수 10개를 생성하여 리스트로 저장
n = 100
dice = [random.randint(1, 6) for _ in range(n)]

fig1 = go.Figure()          # 히스토그램을 위한 Figure 생성

# 히스토그램 추가: x축은 주사위 눈 리스트
fig1.add_trace(             
    go.Histogram(
        x=dice,
        nbinsx=6,               # 막대(bin)의 개수: 주사위 눈(1~6)이라 6개
        marker_color="skyblue"  # 막대 색상을 빨간색으로 설정
    )
)

# 그래프 레이아웃 설정
fig1.update_layout(         
    title="주사위 던지기 " + str(n) + "번 시행",   # 그래프 제목
    xaxis_title="주사위 눈",                      # x축 제목
    yaxis_title="빈도",                          # y축 제목(각 눈이 나온 횟수)
    bargap=0.2                      # 막대 간격 설정(0에 가까울수록 연결됨)
)
fig1.update_yaxes(dtick=1)          # y축 눈금을 정수로 맞춤

st.plotly_chart(fig1)   # Streamlit 화면에 Plotly 그래프 그리기
