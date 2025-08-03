# Chainlit Agent with External LLM (Gemini)

This project demonstrates how to create a Chainlit application that leverages an external Large Language Model (LLM), specifically Google's Gemini, using an OpenAI-compatible API endpoint.  It utilizes the `agents` library for agent management and streaming responses.
 
## Features

*   **Chainlit Integration:**  Uses Chainlit for a user-friendly chat interface.
*   **External LLM Support:** Connects to Gemini via an OpenAI-compatible API.
*   **Streaming Responses:** Provides a real-time, streamed response from the LLM to the user.
*   **Agent-Based Architecture:**  Uses the `agents` library to define and manage an agent with specific instructions.
*   **Environment Variable Configuration:** Uses `.env` for secure API key management.

## Prerequisites

*   Python 3.8+
*   [Poetry](https://python-poetry.org/) (Recommended for dependency management) or pip
*   An OpenAI-compatible API endpoint for Gemini (e.g., using [GenAIStack](https://github.com/shahules786/genai-stack)).
*   A Gemini API key.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Install dependencies:**

    **Using Poetry (Recommended):**

    ```bash
    poetry install
    ```

    **Using pip:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add the following environment variables:

    ```
    GEMINI_API_KEY=<your_gemini_api_key>
    base_url=<your_gemini_api_endpoint_url>  # e.g., "http://localhost:8000/v1" (if using GenAIStack locally)
    ```

    **Important:** Replace `<your_gemini_api_key>` with your actual Gemini API key and `<your_gemini_api_endpoint_url>` with the correct URL of your Gemini API endpoint.  Ensure this file is *not* committed to your repository (it's usually included in `.gitignore`).

## Usage

1.  **Run the Chainlit application:**

    ```bash
    chainlit run app.py
    ```

    (Assuming your main application file is named `app.py`)

2.  **Access the application:**

    Open your web browser and navigate to the URL provided by Chainlit (usually `http://localhost:8000`).

3.  **Start chatting:**

    You can now start interacting with the agent by typing messages in the chat interface.

## Code Overview

*   **`app.py`:**  The main Chainlit application file.

    *   Imports necessary libraries (`os`, `dotenv`, `openai`, `chainlit`, `agents`).
    *   Loads environment variables from the `.env` file.
    *   Configures the OpenAI client to use the Gemini API endpoint.
    *   Defines the `handle_start_chat` function to send a welcome message when the chat starts.
    *   Defines the `handle_message` function to:
        *   Create an `Agent` with a name, instructions, and the Gemini-backed model.
        *   Run the agent using `Runner.run_streamed` to get a streaming response.
        *   Stream the response to the Chainlit UI using `cl.Message.update`.

*   **`agents.py`:** (Assumed based on import statement).  This file likely contains the definitions for the `Agent`, `Runner`, and `OpenAIChatCompletionsModel` classes, likely adapted to interface with the OpenAI-compatible Gemini API.  If this is a custom file, you'll want to include it in your repository and potentially add more detail about it here.

## Environment Variables

| Variable       | Description                                                                    |
| -------------- | ------------------------------------------------------------------------------ |
| `GEMINI_API_KEY` | Your Gemini API key.  **Keep this secret!**                                   |
| `base_url`     | The base URL of your Gemini API endpoint (e.g., `http://localhost:8000/v1`). |

## Key Components and Explanation

*   **`AsyncOpenAI`:**  The OpenAI client configured to use the Gemini API endpoint.  This allows you to interact with Gemini as if it were an OpenAI model.
*   **`OpenAIChatCompletionsModel`:** A wrapper around the OpenAI Chat Completions API that allows you to specify the Gemini model to use (e.g., `"gemini-2.0-flash"`).  You might need to adjust this if your `agents` library has a different way of specifying the model.
*   **`Agent`:** An object that encapsulates the LLM, instructions, and other settings for your AI assistant.
*   **`Runner.run_streamed`:**  A function that executes the agent and returns a stream of events. This is crucial for providing a real-time response to the user.
*   **`ResponseTextDeltaEvent`:**  An event that contains a chunk of text from the LLM.  The code iterates through these events to build the complete response.
*   **`cl.Message` and `cl.Message.update`:**  Chainlit functions for displaying messages in the chat UI and updating them as the response streams in.

## Potential Improvements

*   **Error Handling:**  Add error handling to gracefully handle API errors, invalid API keys, and other potential issues.
*   **Token Management:**  Implement token counting and management to prevent exceeding API limits.  Consider using Langchain's token counters.
*   **Conversation History:**  Store and manage conversation history to provide context for subsequent turns.  Chainlit has built-in mechanisms for this.
*   **More Sophisticated Agent Design:**  Explore more advanced agent architectures, such as using tools or memory.
*   **Input Validation:**  Validate user input to prevent injection attacks and other security vulnerabilities.
*   **Configuration Options:**  Allow users to configure the agent's settings (e.g., temperature, max tokens) through the Chainlit UI.
*   **Tool Use:** Integrate tools (e.g., search, calculators) into the agent to expand its capabilities.
*   **Logging:**  Implement more comprehensive logging for debugging and monitoring.
*   **Testing:**  Add unit tests and integration tests to ensure the application is working correctly.
*   **Documentation:**  Expand this documentation with more detailed explanations and examples.

## Troubleshooting

*   **API Key Issues:**  Double-check that your Gemini API key is valid and that you have correctly set the `GEMINI_API_KEY` environment variable.
*   **API Endpoint Issues:**  Verify that the `base_url` is correct and that the Gemini API endpoint is running and accessible.
*   **Dependency Issues:**  Ensure that all required dependencies are installed correctly. If using Poetry, try running `poetry update`.
*   **Streaming Issues:** If the response is not streaming correctly, check the `stream_events` iterator and ensure that `ResponseTextDeltaEvent` objects are being processed correctly.  Also verify your API endpoint supports streaming.
*   **Rate Limiting:** If you encounter rate limiting errors, implement appropriate retry mechanisms and consider using a rate limiting library.


