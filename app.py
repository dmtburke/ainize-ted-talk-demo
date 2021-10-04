import streamlit as st
import requests


def send_request(text, length):
    api_url = 'https://master-ainize-gpt2-tedtalk-dmtburke.endpoint.ainize.ai'
    files = {
        'base_text': (None, text),
        'length': (None, length),
    }
    response = requests.post(api_url, files=files)
    status_code = response.status_code

    return status_code, response


st.title("GPT-2 Ted Talk Demo")
st.header("Generate a Ted Talk presentation using GPT-2 model")

length_slider = st.sidebar.slider("Length", 0, 300)

base_story = st.text_input("Base text", "My name is Dalton and I've been studying machine learning")
if st.button("Submit"):
    if length_slider == 0:
        st.warning("Please define the length")
    else:
        status_code, response = send_request(base_story, length_slider)
        if status_code == 200:
            prediction = response.json()
            st.success(prediction["prediction"])
        else:
            st.error(str(status_code) + " Error")

st.markdown('''
<div style="display:flex">
        <a target="_blank" href="https://github.com/dmtburke/ainize-ted-talk-demo">
            <img src="https://i.imgur.com/UnJzwth.png"/>
        </a>
        <a style="margin-left:10px" target="_blank" href="https://ainize.ai/dmtburke/ainize-ted-talk-demo?branch=main">
            <img src="https://i.imgur.com/ASkTsnj.png"/>
        </a>
<div>
    ''',
    unsafe_allow_html=True
)
