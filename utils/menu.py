import streamlit as st

# --- Simplified Menu with One Item per Category ---
menu_items = {
    "Burger": ("Classic Burger Combo", 149.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/burger.jpg"),
    "Pizza": ("Margherita Pizza Combo", 399.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/pizza.webp"),
    "Nuts and dries": ("Mixed Platter", 299.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/nuts.webp"),
    "samosa": ("Dessert Box", 159.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/samosa.jpg"),
    "Any Drinks": ("Beverage Combo", 99.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/soft-drinks.jpg"),
    "Any Snacks": ("Snack Box", 199.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/snacks.jpeg"),
    "Any Ice Cream": ("Ice Cream Delight", 129.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/cream.jpeg"),
    "Any Salad": ("Fresh Salad Bowl", 179.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/salad.jpeg"),
    "Any Soup": ("Soup of the Day", 89.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/soup.jpg"),
    "Extra Rice": ("Rice Bowl", 249.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/biryani.jpeg"),
    "Chicken combo": ("Curry Combo", 299.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/chickencurry.jpeg"),
    "Bread Omlet": ("Bread Basket", 99.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/bread.jpeg"),
    "Any Dessert": ("Dessert Platter", 199.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/dessert.jpeg"),
    "Shawarma": ("Wrap Combo", 249.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/shawarma.jpeg"),
    "Any type of Sandwich": ("Sandwich Combo", 199.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/sandwich.jpeg"),
    "Any Pasta": ("Pasta Delight", 299.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/pasta.jpeg"),
    "Mutton curry": ("one bowl", 249.99, "/Users/mandebharath/Desktop/streamlitfoodorder/utils/mutton.jpeg"),
}

def show_menu():
    st.title("📜 Food Menu")

    for category, (item_name, price, image_path) in menu_items.items():
        st.markdown(f"## 🍽️ {category}")

        cols = st.columns([1, 3])
        with cols[0]:
            st.image(image_path, use_container_width=True)

        with cols[1]:
            st.markdown(f"**{item_name}**")
            st.markdown(f"Price: ₹{price:.2f}")
            if st.button("Add", key=f"add_{category}"):
                if 'cart' not in st.session_state:
                    st.session_state['cart'] = []
                st.session_state['cart'].append((item_name, price))
                st.toast(f"✅ {item_name} added to cart!", icon="🛒")

    # Show Cart
    if 'cart' in st.session_state and st.session_state['cart']:
        st.markdown("---")
        st.header("🛒 Your Cart")
        total = sum(price for _, price in st.session_state['cart'])

        for i, (item, price) in enumerate(st.session_state['cart']):
            col1, col2, col3 = st.columns([5, 2, 1])
            col1.markdown(f"**{item}**")
            col2.markdown(f"₹{price:.2f}")
            if col3.button("❌", key=f"remove_{i}"):
                st.session_state['cart'].pop(i)
                st.experimental_rerun()

        st.markdown(f"### 🧾 Total: ₹{total:.2f}")
        if st.button("✅ Place Order"):
            st.success("Your order has been placed! 🎉")
            st.session_state['cart'] = []

if __name__ == "__main__":
    show_menu()






