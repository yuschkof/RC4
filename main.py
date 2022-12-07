import streamlit as st
from RC4 import RC4


st.set_page_config(
    page_title="RC4 cipher",
    page_icon="🧊",
    layout="centered",
)

st.title('Шифр RC4')
st.caption("Описание из Википедии [RC4](https://ru.wikipedia.org/wiki/RC4)")

keys = st.text_input('Ключ', 'Key')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Зашифровать')
    output = ''
    word = st.text_input('Слово', 'Hello world')
    if st.button('Зашифровать'):
        rc4 = RC4(keys)
        output = rc4.encrypt(word)
    st.markdown(f"Зашифрованное слово: {output}")


with col2:
    st.subheader('Расшифровать')
    output = ''
    shifre = st.text_input('Зашифрованное слово', '')
    if st.button('Расшифровать'):
        rc4 = RC4(keys)
        output = rc4.decrypt(shifre)
    st.markdown(f"Расшифрованное слово: {output}")
