import streamlit as st
import google.generativeai as genai  # Replace with the correct import

# Initialize Generative AI
genai.configure(api_key="AIzaSyBdY9bOtYv0M_-xdj6gJShZfqjpuCjE92U")
model = genai.GenerativeModel('gemini-pro')

def initiate(user_input):
    prompt = f"""
    Analyzing Car Issues:
    User Input: {user_input}
    """

    response = model.chat(messages=prompt)
    return response

def reply(prev_msg, user_input):
    prompt = f"""
    Previous AI Response: {prev_msg.last}
    User Input: {user_input}
    """

    return prev_msg.reply(prompt)

def ai_car_diagnosis():
    st.title("AI Car Diagnosis")

    # Initial interaction
    user_input = st.text_input("User Input:")
    response = initiate(user_input)
    st.text(f"AI: {response.last}")

    # Continuing the conversation
    user_input_list = [user_input]
    form = st.form("user_inputs_form")

    user_input = ""  # Initialize user_input outside the loop

    while True:
        user_input_list.append(user_input)
        response = reply(response, user_input)

        if user_input.lower() in ["exit", "quit", "stop"]:
            st.text("Exiting AI Car Diagnosis.")

    

if __name__ == "__main__":
    ai_car_diagnosis()
