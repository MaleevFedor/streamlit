import streamlit as st
from datetime import datetime


st.title('Поиск статей по дате')
date = st.date_input('Выберите дату(большая часть статей написанны 21ого-23его числа)')


k = 0
for i in open('data.csv', encoding="UTF-8").readlines()[1:]:
    i = i.split(';')
    if datetime.strptime(i[2].rstrip(), '%Y-%m-%d').date() == date:
        name = f'<p style="font-size: 20px;">{i[0]}</p>'
        theme = f'<p style="color: #8b8c89; font-size: 15px;">тема: {i[1]}</p>'
        st.markdown(name, unsafe_allow_html=True)
        st.markdown(theme, unsafe_allow_html=True)
        k += 1
st.write(f'В этот день написанно {k} статей')