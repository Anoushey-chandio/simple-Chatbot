import os
import json
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion

# Load the environment variables from the .env file
load_dotenv()

# Get the Gemini API key from the environment
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

@cl.on_chat_start
async def start():
    """Set up the chat session when a user connects."""
    cl.user_session.set("chat_history", [])
    await cl.Message(content="Welcome to the simple AI Assistant! Created by Anoushey 🤖\nHow can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    # Show a temporary "Thinking..." message
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Retrieve chat history
    history = cl.user_session.get("chat_history") or []

    # Add the user's message to history
    history.append({"role": "user", "content": message.content})

    try:
        # Get a response from LiteLLM using Gemini
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=gemini_api_key,
            messages=history
        )

        response_content = response.choices[0].message.content

        # Update the message with actual response
        msg.content = response_content
        await msg.update()

        # Save the response to chat history
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")

    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")

@cl.on_chat_end
async def on_chat_end():
    """Save chat history when the session ends."""
    history = cl.user_session.get("chat_history") or []
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=2)
    print("Chat history saved.")

# ✅ Run the Chainlit app with correct port and host (important for Railway)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    cl.run(port=port, host="0.0.0.0")

