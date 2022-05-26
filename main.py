from platform import python_branch
from turtle import st
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 入門')

st.write("Display Image")

img = Image.open('/Users/kobayashimika/Desktop/work/sample_lesson.jpeg')
st.image(img, caption = 'Kobayashi', use_column_width = True)


# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns = ['lat', 'lon']
# )
# df

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# st.table(df.style.highlight_max(axis=0))

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#st.map(df)