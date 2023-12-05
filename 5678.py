import streamlit as st
import numpy as np
import pandas as pd

import os
os.system('cls')

import matplotlib.pyplot as plt


col1, col2 = st.columns([1, 2])
with col1:
    st.image('순심이.jpg')
with col2:
    '놓치면 후회할 인재 (신수인, 시급 5만원, 대박 쩔어~~)'
    '전화번호(📞) : 010-xxxx-xxxx'
    '이메일(📧) : gktjdcjf97@naver.com'
    '주소(🏠) : 충남 논산시 대학로 121'

''
'-----------------------'
col = st.columns(4)
with col[0]:
    st.link_button("Google(🌐)", "https://google.com")
with col[1]:
    st.link_button("Naver(✅)", "https://naver.com")
with col[2]:
    st.link_button("Daum(🇩)", "https://daum.net")
with col[3]:
    st.link_button("Facebook(ⓕ)", "https://facebook.com")

" "
" "
"## :orange[자기소개]"
"### 저는 서울에서 1남 1녀의 잡안에서 태어나 살아가고 있습니다."









import sys
sys.exit()

fig, ax = plt.subplots()

a = 2
b = -5
c = 3
d = -7

x = []
y = []
for i in range(-10, 11 ,1):
    x.append(i)
    y.append(a*i**3 + b*i**2 + c*i + d)

col1, col2, col3 = st.columns(3)
with col1:
    color = st.radio('색을 선택하시오.', ('red', 'green', 'blue', 'orange', 'magenta'))
with col2:
    linestyle = st.radio('선의 스타일을 선택하시오', ('-', '--', '-.', ':'))
with col3:
    marker = st.radio('마커의 스타일을 선택하시오.', ('s', '^', 'o', 'p', 'h'))

# if 'red' in color:
#     t = '-.r^'
# if 'green' in color:
#     t = '-.g^'
# if 'blue' in color:
#     t = '-.b^'

plt.plot(x, y, color = color, marker = marker, linestyle = linestyle)

st.pyplot(fig)








# import streamlit as st

# st.write('Hello, *World!* :sunglasses:')
# '# Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]'
# '## Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]'
# '### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]'
# '#### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]'
# '##### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]'
# '###### Hello, *World!* **tt** ***cc***  :red[red] :green[green] :blue[blue]'





# li = [1, 2, 3, 4]
# n = np.array(li)
# p = pd.Series(li, index = ['a', 'b', 'c', 'd'])
# li
# n
# p


import streamlit as st

gg = st.radio('선택하시오', ['오름차순', '내림차순'])
gg

list1 = list([["한빛", "남자", "20", "180"], ["한결", "남자", "21", "177"], ["김한결", "중성", "51", "155"], ["한라", "여자", "20", "160"]])
n = np.array(list1)
col_names = ['이름', '성별', '나이', '키']
df = pd.DataFrame(list1, columns = col_names, index = ['1행', '2행', '3행', '4행'])
df


genre = st.radio("선택하시오.", ["오름차순", "내림차순", "기타", "요약"], horizontal=True, index = 2)
number = st.number_input('Input a number', value = 0, step = 1)
df.iloc[3, 2] = number

if '오름' in genre:
    st.dataframe(df.sort_values(by = ('키')))
if '내림' in genre:
    st.dataframe(df.sort_values(by = ['키'], ascending = False))
if '기타' in genre:
    st.dataframe(df)
if '요약' in genre:
    st.dataframe(df.describe())





# # for i in range(4):
# #     li[i] = li[i] +3
# # li

# li = np.array([1, 2, 3, 4])
# li + 30


# a = np.array([1, 10, -5, 2])
# print(np.abs(a))
# print(np.sqrt(a))
# print(a**0.5)
# print(np.square(a))
# print(a**2)

# import turtle
# import random



# for i in range(6):
#     r = random.randint(1, 45)
#     r









# t1 = turtle.Turtle()
# t1.shape('turtle')

# t1.width(5)
# t1.color("red")
# t1.penup()
# t1.goto(-300, 100)
# t1.pendown()
# t1.forward(100)


# t2 = turtle.Turtle()
# t2.shape('turtle')

# t2.width(5)
# t2.color("blue")
# t2.penup()
# t2.goto(-300, -100)
# t2.pendown()
# t2.forward(100)

# for i in range(20):
#     d1 = random.randint(1, 60)
#     t1.forward(d1)
#     d2 = random.randint(1, 60)
#     t2.forward(d2)





# turtle.done()







# y = 6
# for i in range(1, 10):
#     y, 'X', i, '=', ' ', y*i


# list1 = [[1, 2, 3, 4], [3, 5, 7, 9]]

# for i in range(4):
#     list1[i] = list1[i] + 3
# list1

# a = np.array(list1)
# a
# a.shape
# s = a.sum(axis = 0)
# s
# mn = a.min(axis = 0)
# mn

# n = np.ones((5,5))
# n 
# n = np.zeros((5,5))
# n
# n = np.full((5,5), 3)
# n
# n = np.eye(5)
# n

# def user_eye(n):
#     arr = np.zeros((n, n))
#     for i in range(n):
#         for j in range(n):
#             if i == n - j -1:
#                 arr[i, j] = 1
#     return arr

# arr = user_eye(10)
# arr


# a.ndim
# n = np.ndim(a)
# np.size(a)
# a.size
# a.shape
# a.T






