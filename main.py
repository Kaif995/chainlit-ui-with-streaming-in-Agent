import os
from dotenv import load_dotenv
from openai.types.responses import ResponseTextDeltaEvent
from openai import AsyncOpenAI

from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import chainlit as cl

# Load env vars
load_dotenv()
set_tracing_disabled(disabled=True)

# External LLM setup (e.g., Gemini)
gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("base_url")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

@cl.on_chat_start
async def handle_start_chat():
    await cl.Message(content="Hello, how can I help you today?").send()
# Chainlit handler
@cl.on_message
async def handle_message(message: cl.Message):
    agent = Agent(
        name="Kaif Shamim",
        instructions="You are a helpful assistant.",
        model=model
    )

    response = Runner.run_streamed(agent, input=message.content)

    # Stream and display response in Chainlit
    stream_response = cl.Message(content="")
    await stream_response.send()

    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            stream_response.content += event.data.delta
            await stream_response.update()
