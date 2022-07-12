import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('Streamlit')
st.write('progress bar')
'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'(Iteration {i+1})')
    bar.progress(i+1)
    time.sleep(0.1)
    

# left_column,right_column = st.beta_columns(2)
# button = left_column.button('右からむに文字を表示')
# if button:
#     right_column.write('ここは右からむ')

# expander = st.beta_expander('問合せ')
# expander.write('問い合わせ内容を書く')
# text = st.text_input('あなたの趣味は？')
# 'あなたの趣味は',text,'です。'

# condition = st.slider('あなたの調子は？',0,100,50)
# 'コンディション',condition

# if st.checkbox('show image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='ishii',use_column_width=True)

