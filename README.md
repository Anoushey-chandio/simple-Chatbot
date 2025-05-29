# simple Chatbot  Using uv, LiteLLM, and Chainlit

This project demonstrates a simple AI chatbot built with Python, leveraging three key tools:

- **uv**: A fast Python package and environment manager to streamline setup.
- **LiteLLM**: A unified interface for large language models, here used to interact with Gemini AI.
- **Chainlit**: A conversational AI framework for creating chat-based interfaces.

---

## How This Code Works

1. **Environment Setup**  
   The code loads the Gemini API key securely from a `.env` file using the `dotenv` package.

2. **Chat Session Initialization**  
   When a user starts chatting, an empty chat history is initialized and a welcome message is sent.

3. **Handling User Messages**  
   Every incoming user message is added to the chat history.  
   Then, the code calls the LiteLLM `completion` function with the Gemini model to generate a response.

4. **Sending and Updating Responses**  
   While waiting for the AI response, a “Thinking...” message is shown. Once the response is received, it updates the message with the actual content.

5. **Maintaining Conversation History**  
   Both user and assistant messages are appended to the session’s chat history, enabling context-aware conversations.

6. **Error Handling**  
   Any errors during the AI completion call are caught, and an error message is displayed to the user.

7. **Chat Session End**  
   When the chat ends, the entire conversation history is saved into a JSON file `chat_history.json` for future reference or analysis.

---

## Key Points

- The project securely manages API keys via `.env` and does not expose them in code.
- The chat history is stored in session memory and persisted on chat end.
- The chatbot uses Gemini’s latest model via LiteLLM for generating responses.
- Chainlit provides an easy interface for asynchronous messaging and session management.

---

 
