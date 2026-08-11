import streamlit as st
import json 

try:
    from StringIO import StringIO  # برای Python 2
except ImportError:
    from io import StringIO  # برای Python 3

st.title("Streamlit Dashboard")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based on I/O:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)
    
    data = json.loads()
    st.json(data)