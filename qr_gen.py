import qrcode
import time
import streamlit as st
from io import BytesIO

# Generate a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border size around the QR code
)

def createqr():
    # Data to be encoded in the QR code
    data = st.text_input("Enter what you want a QR Code for:")
    # Add data to the QR code instance
    qr.clear()  # Clear the QR code data in case this function is called multiple times
    qr.add_data(data)
    qr.make(fit=True)
    
    create = st.button("Create QRcode")
    if create:
        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Display the image in Streamlit
         # Save the image to a BytesIO object
        img_bytes_io = BytesIO()
        img.save(img_bytes_io, format="PNG")
        st.image(img_bytes_io)

        # Download the image
        timestamp = int(time.time())
        image_filename = f"my_qr_code_{timestamp}.png"

       

        # Create a download button for the image
        st.download_button("Download QRcode", img_bytes_io.getvalue(), file_name=image_filename)

#if __name__ == "__main__":
    #createqr()
