from cmath import exp
from platform import python_branch
from turtle import left, st
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 入門')

st.write("Interactive Widgets")

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')


expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3回答')
expander4 = st.beta_expander('問い合わせ4')
expander4.write('問い合わせ4回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condetion = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condetion


