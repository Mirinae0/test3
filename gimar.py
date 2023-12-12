import streamlit as st
import numpy as np
import pandas as pd

import os
os.system('cls')

import matplotlib.pyplot as plt

"### <이승재 포트폴리오>"
col1, col2 = st.columns([1, 2])
with col1:
    st.image('이승재.jpg')
with col2:
    "### :green[[저는 이런 사람입니다!]]"
    '이 나라에 필요한 인재! (이승재, 24세(만 23세),군필)'
    '전화번호(📞) : 010-9660-7178'
    '대표 이메일(📧) : dlsrks7178@gmail.com'
    '주소(🏠) : 충남 논산시 은진면 와야2길 39-11 해피룸'

''
'-----------------------'
st.sidebar.write('# 01 : 나는 누구인가?')
st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.write('# 02 : 나의 학교생활')
st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.write('# 03 : 나의 군생활과 경력')
st.sidebar.write(' ')
st.sidebar.write(' ')
st.sidebar.write(' ')

col = st.sidebar.columns(2)
with col[0]:
    " "
    " "
    " "
    " "
    "### SMS ADDRESS"
    st.link_button("Instagram(🌐)", "https://instagram.com/lsjae_1003")
with col[1]:
    " "
    " "
    " "
    " "
    "### THE OTHER"
    "### NAVER✅:"
    "ghj01003@naver.com"


" "
" "
"## :orange[자기소개]"
"## 01"
"##### 저는 서울에서 1남 1녀의 집안에서 태어나 살아가고 있습니다. 제 학력은 대학교 3학년 재학중이며, 군필입니다."
"##### 저의 집안은 부모님 두분과 저와 누나로 이루어진 4인 가족입니다. 저의 집안은 가족끼리 매우 화목하며 소통이 활발하게 이루어진, 좋은 집안입니다."
" "
"## 02"
"##### 저는 2019년도에 건양대학교 재난안전 소방학과에 입학하였으며, 2023년 올해 한 해 동안 부학회장으로 부임했습니다."
"##### 또한 저는 2023학년도 1학기에 과탑을 달성함으로써 전액장학금으로 등록금이 면제되었습니다."
" "
"##### 군복무는 25사단 공병대대 병장 만기전역으로 마쳤습니다."
" " 
"## 03"
"##### 제 경력을 설명드리겠습니다."
" " 
"##### 삼성전자 전주센터에서 아르바이트로 에어컨 수리를 약 5개월간 하였으며, 스키장에서 아르바이트로 약 3개월 근무 했습니다."
"##### 그리고 현재는 대학가 앞의 먹자골목안에 있는 '석쇠한판'에서 아르바이트를 진행중입니다."



