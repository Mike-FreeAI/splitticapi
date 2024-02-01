import asyncio
from SplitticAPI.meowgpt import ChatModule

# Set the global API key
api_key = "your-api-key"
ChatModule.initialize(api_key)

# Create a ChatModule instance with a unique chat ID
chat_instance = ChatModule.create_chat(api_key)

# Send an asynchronous message and get a reply
async def main():
    reply = await chat_instance.async_reply("Hi")
    print(reply)

# Run the asynchronous event loop
if __name__ == "__main__":
    asyncio.run(main())
