from SplitticAPI.meowgpt import ChatModule

# Set the global API key
api_key = "your-api-key"
ChatModule.initialize(api_key)

# Create a ChatModule instance with a unique chat ID
chat_instance = ChatModule.create_chat(api_key)

# Send a synchronous message and get a reply
def main():
    reply = chat_instance.reply("Hi")
    print(reply)

# Run the program
if __name__ == "__main__":
    main()
