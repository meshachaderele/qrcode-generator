import streamlit as st
from qr_gen import createqr
import qrcode
import time
import streamlit as st
from io import BytesIO

st.title('Free QRcode Generator')
st.subheader('Create a free QRcode for your links, text, events etc.')

createqr()

    

# Define the footer content
footer_content = """
<hr>
<p style="text-align:center">Made with ❤️ by Meshach Aderele</p>
"""

# Add the footer
st.markdown(footer_content, unsafe_allow_html=True)
