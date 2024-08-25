from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="HBD", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

lottie_coding = load_lottieurl("https://lottie.host/63fac222-e6fd-41e1-b16f-ca7a79d002e5/qwI4MyrXVW.json")
img_cover_form = Image.open("images/Screenshot 2024-08-24 174730.png")

st.subheader("Hi, Benssie :wave:")
st.title("Best wishes on your special day!")
st.write("Wishing you a wonderful and joyous birthday. May this special day be filled with happiness, and may the year ahead bring you continued success and fulfillment.")
st.write("[Tap me >](https://gifft.me/o/d/4j03ytil02vetrw15bdxx54k)")

# What I do 
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Happy Birthday, Benssie!")
        st.write("##")
        st.write(
            """
On your special day, I just want to remind you of how amazing you are and how much you mean to everyone around you. 
May this year bring you all the joy, laughter, and adventures your heart desires.

I wanted to take a moment to thank you for your support and understanding. 
Meeting you was one of the best times in my life. You showed me something different.
I appreciate how you’ve been there and the genuine care you’ve shown. 

I want to see you achieve everything you have told me before, and
thank you for being a part of me.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Projects
with st.container():
    st.write("---")
    st.header("MY PRESENT")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
       st.image(img_cover_form, caption='Thank you for your patience while waiting to this cover.')

    with text_column:
        st.subheader("HEAVEN KNOWS")
        st.write(
            """
A year ago, I told you that I knew I’d hear your name when you made it through—and here we are. 
You’ve done it, just as I knew you would. 
Congratulations on all that you’ve accomplished. Your success fills me with immense pride.

I hope you enjoy my last guitar cover. 
I wanted to perform it for you in person, but since that’s not possible, 
I hope it still brings you joy.

This cover is my birthday gift to you.

"As long as you're happy, it means the world to me."
            """
        )
    st.markdown("[heaven knows by 8282...](https://youtu.be/ljUAiBhtqS0)")
    
# Contact form
with st.container():
    st.write("---")
    st.header("See you!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/bautistavinceandrei800@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message" required></textarea><br>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
