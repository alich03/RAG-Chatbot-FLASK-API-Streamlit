import streamlit as st
import requests

import time

def chatbot():
    st.title("Chatbot")
    

    if "messages" not in st.session_state:
        st.session_state.messages = []

        with st.chat_message("assistant"):
            st.markdown("How can i help you?")

#print all conversation in session
#this is new
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

#take input from user and enter in session
    if prompt := st.chat_input("Type you message ..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role":"user","content":prompt})

        response=get_response_from_api(prompt)

#add response to session
        # response = f"Reply from bot {prompt}"


        with st.chat_message('assistant'):
            progress_text = st.empty()

            for i in range(len(response)):
                progress_text.markdown(response[:i + 1])
                time.sleep(0.05)
        # with st.chat_message("assistant"):
        #     st.markdown(response)

        st.session_state.messages.append({"role":"assistant","content":response})


url = "http://127.0.0.1:5000/chatbot"

def get_response_from_api(user_input):

    response = requests.post(url,json={"prompt": user_input})

    return  response.json()['response']







if __name__ == "__main__":
    chatbot()