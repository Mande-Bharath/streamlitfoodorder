import streamlit as st

def show_cart():
    st.title("🛒 Your Cart")

    cart = st.session_state.get('cart', [])
    total = sum(item[1] for item in cart)

    if cart:
        indices_to_remove = []
        for i, (item, price) in enumerate(cart):
            col1, col2 = st.columns([3, 1])
            col1.write(f"{item} - ₹{price:.2f}")
            if col2.button("❌ Remove", key=f"remove_{i}"):
                indices_to_remove.append(i)

        for i in sorted(indices_to_remove, reverse=True):
            del st.session_state['cart'][i]

        st.markdown(f"### Total: ₹{sum(p for _, p in st.session_state['cart']):.2f}")
    else:
        st.info("Your cart is empty.")




