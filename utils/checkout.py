import streamlit as st

def show_checkout():
    st.title("💳 Checkout")
    cart = st.session_state.get('cart', [])
    if not cart:
        st.warning("Please add items to your cart first.")
        return

    total = sum(item[1] for item in cart)
    st.write(f"Total to pay: ₹{total:.2f}")
    name = st.text_input("Name")
    address = st.text_area("Delivery Address")
    if st.button("Place Order"):
        if name and address:
            st.success(f"Thank you {name}! Your order has been placed.")
            st.session_state['cart'] = []
        else:
            st.error("Please fill out all fields.")
