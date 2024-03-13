import streamlit as st
from PIL import Image
from deoldify import device
from deoldify.device_id import DeviceId
from deoldify.visualize import *

# Set device
device.set(device=DeviceId.GPU0)

# Streamlit app
def main():
    st.title("Image Colorization App")
    st.write("Upload a black and white image to colorize.")

    # Upload image
    uploaded_file = st.file_uploader("Choose a black and white image...", type=["jpg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Colorize image on button click
        if st.button("Colorize"):
            with st.spinner("Colorizing..."):
                # Colorize the image
                colorizer = get_image_colorizer(artistic=True)
                colorized_image = colorizer.get_transformed_image(image)

                # Display colorized image
                st.image(colorized_image, caption="Colorized Image", use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
