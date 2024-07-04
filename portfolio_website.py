import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Adem Dikkaya")

with col2:
    st.image("images/a1.jfif")

st.title(" ")

persona = ''' You are Adem AI bot. You help people answer questions about your self (i.e Adem)
Answer as if you are responding . dont answer in second or third person. If you don't know they answer you simply say "That's a secret"
Here is more info about Adem: studied in Eastern Mediterranean '''

st.title("Adem's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader(" Adem's favorite Song ")
    st.write("- Happy")
with col2:
    st.video("https://www.youtube.com/watch?v=ZbZSe6N_BXs")
st.title(" ")

st.title("My Setup")
st.image("images/setup.jfif")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 75)
st.slider("Robotics", 0, 100, 60)

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/i1.jfif")
    st.image("images/i2.jfif")

with col2:
    st.image("images/i3.jfif")
    st.image("images/i4.jfif")

with col3:
    st.image("images/i5.jfif")
    st.image("images/i6.jfif")

st.write("  ")
st.write("CONTACT")
st.title("for any inquiries, please contact me ")
st.subheader("01ademdikkaya@gmail.com")
