import streamlit as st
st.header('このファイルはテストです')
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

from streamlit_extras.stylable_container import stylable_container
with st.form(key='profile_form1'):
    value = st.text_input('値(スペースで区切って入力してください)')
    name = st.selectbox('分析', ('平均', '分散','標準偏差'))
    submit_btn = st.form_submit_button('入力した値で実行')
    if value:
        try:
            value_list = value.split()
            value = [float(number) for number in value_list]
        except ValueError:
            st.write("有効な数値を入力してください。")
    if  submit_btn:
        if len(value) == 0:
            st.write("値が入力されていません。")
        else:
            if name == ('平均'):

                value_mean = np.mean(value)
                st.text(f'平均＝{value_mean}')

            elif name == ('分散'):

                value_var = np.var(value)
                st.text(f'分散＝{value_var}')
            else:

                value_std = np.std(value)
                st.text(f'標準偏差＝{value_std}')

