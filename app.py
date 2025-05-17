import streamlit as st
from streamlit_option_menu import option_menu

# Add any other dependencies your utils files use

# Import pages from utils
from utils.home import show_home
from utils.menu import show_menu
from utils.cart import show_cart
from utils.checkout import show_checkout
from utils.chatbot import show_chatbot  # New chatbot page

# ------------------------
# Page Configuration
# ------------------------
st.set_page_config(page_title="Foodie Express", layout="wide", page_icon="🍔")

# ------------------------
# Session State Initialization
# ------------------------
if 'cart' not in st.session_state:
    st.session_state['cart'] = []

# ------------------------
# Custom Styling
# ------------------------
st.markdown("""
    <style>
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .main > div {
        animation: fadeIn 0.8s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Sidebar Navigation
# ------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Menu", "Cart", "Checkout", "Chatbot"],
        icons=["house", "list", "cart", "credit-card", "chat-dots"],
        menu_icon="restaurant",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "5!important", "background-color": "#000000"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#fd1900",
                "color": "#D2C6C6",
            },
            "nav-link-selected": {"background-color": "#fd1900"},
        }
    )

    # Show current cart item count below menu
    st.markdown(f"🛒 Cart items: {len(st.session_state.get('cart', []))}")

# ------------------------
# Page Routing
# ------------------------
if selected == "Home":
    show_home()
elif selected == "Menu":
    show_menu()
elif selected == "Cart":
    show_cart()
elif selected == "Checkout":
    show_checkout()
elif selected == "Chatbot":
    show_chatbot()


