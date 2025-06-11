import streamlit as st
import image_CIFAR10
import regression_housing
import text_imdb

st.title("Deep Learning Model App - with Classification!")

# Menú principal
option = st.selectbox("What model would you like to use?:",
    ("Image Classifier", "Regression (Median house value)", "Text Classifier (IMDB Review Sentiments)"))

#page for selection
if option == "Image Classifier":
    image_CIFER10.main()
elif option == "Regression (Median house value)":
    regression_housing.main()
elif option == "Text Classifier (IMDB Review Sentiments)":
    text_imdb.main()
