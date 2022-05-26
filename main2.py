from platform import python_branch
from turtle import st
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 入門')

st.write("Display Image")

# if st.checkbox('Show Image'):
#   img = Image.open('/Users/kobayashimika/Desktop/work/sample_lesson.jpeg')
#   st.image(img, caption = 'Kobayashi', use_column_width = True)

option = st.selectbox(
  'あなたが好きな数字を教えてください、',
  list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'



