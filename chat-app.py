# Install openai and gradio if not already installed
!pip install openai gradio

import openai
import gradio as gr
import os

# Set your OpenAI API key securely in your environment
os.environ["OPENAI_API_KEY"] = "## your api key##"
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is available
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set. Please set it in your environment.")

# Initial messages setup for the system role
messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]

# Function for custom ChatGPT interaction
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})  # Append the user input to the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]  # Extract assistant's reply
    messages.append({"role": "assistant", "content": ChatGPT_reply})  # Add assistant's reply to the conversation
    return ChatGPT_reply

# Creating a Gradio interface
demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

# Launch the demo with public sharing enabled
demo.launch(share=True)
