import streamlit as st
import numpy as np
import pandas as pd

import os
os.system('cls')

import matplotlib.pyplot as plt


col1, col2 = st.columns([1, 2])
with col1:
    st.image('이승재.jpg')
with col2:
    '이 나라에 필요한 인재! (이승재, 24세(만 23세),군필)'
    '전화번호(📞) : 010-9660-7178'
    '이메일(📧) : dlsrks7178@gmail.com'
    '주소(🏠) : 충남 논산시 은진면 와야2길 29-11 해피룸'

''
'-----------------------'
col = st.columns(4)
with col[0]:
    st.link_button("Instagram(🌐)", "https://instagram.com/lsjae_1003")

" "
" "
"## :orange[자기소개]"
"### 저는 서울에서 1남 1녀의 집안에서 태어나 살아가고 있습니다. 제 학력은 대학교 3학년 재학중이며, 군필입니다. 군대는 25사단 공병대대 만기전역을 했으며, 제 경력은 삼성전자 전주센터에서 아르바이트로 에어컨 수리를 약 5개월간 하였으며,"



