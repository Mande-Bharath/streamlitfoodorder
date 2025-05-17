import streamlit as st

def show_home():
    st.title("🍽️ Welcome to Foodie Express!")
    st.markdown("#### Your favorite meals delivered fast at your door.")
    st.image("/Users/mandebharath/Desktop/streamlitfoodorder/utils/banner.jpg", use_container_width=True)

    st.markdown("Enjoy delicious meals from our curated menu. Navigate using the sidebar to place your order.")
