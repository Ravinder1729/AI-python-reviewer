from openai import OpenAI
import streamlit as st
st.image(r"C:\Users\ravin\Downloads\innomatics-footer-logo (1).webp")
f = open(r"D:\GenAI\key\key.txt")
key = f.read()
client = OpenAI(api_key = key)
#st.snow()
st.title("AI code reviewer")
#st.subheader("GenAi")

prompt = st.text_area('Enter your python code')
if st.button("Generate"):
    #st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role":"system","content":"""You are a helpful AI assistant.
                                        please fix bugs in given python code"""},
            {"role":"user","content":prompt}
    ]
    )

    if response.choices:
        st.write(response.choices[0].message.content)