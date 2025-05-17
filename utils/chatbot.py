import streamlit as st

def get_bot_response(user_msg):
    msg = user_msg.lower()
    if "menu" in msg:
        return "Sure! We have burgers, pizzas, nuts and dries, and samosas. What would you like?"
    elif "order" in msg:
        return "You can place an order from the Menu section. What would you like to order?"
    elif "hello" in msg or "hi" in msg:
        return "Hello! How can I assist you today?"
    elif "thanks" in msg or "thank you" in msg:
        return "You're welcome! 😊"
    elif "bye" in msg or "exit" in msg:
        return "Goodbye! Have a great day!"
    else:
        return "contact: bharathytgmr@gmail.com"

def show_chatbot():
    st.title("💬 Chatbot Assistant")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Create a form for input so we can clear it on submit
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_input("You:")
        submitted = st.form_submit_button("Send")

    if submitted and user_input:
        bot_response = get_bot_response(user_input)
        st.session_state['chat_history'].append(("You", user_input))
        st.session_state['chat_history'].append(("Bot", bot_response))

    # Show chat history
    for speaker, message in st.session_state['chat_history']:
        if speaker == "You":
            st.markdown(f"**{speaker}:** {message}")
        else:
            st.markdown(
                f"<div style='background:blue; padding:8px; border-radius:5px; margin:5px 0'>"
                f"<strong>{speaker}:</strong> {message}</div>",
                unsafe_allow_html=True
            )



