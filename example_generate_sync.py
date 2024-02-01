from SplitticAPI.interdiffusion import DiffusionModule
from PIL import Image

# Set the global API key
api_key = "your-api-key"
Diff = DiffusionModule(api_key)

# Send a synchronous message and get a reply
def main():
    Diff.generate("cat")
    Image.open('output.png').show()

# Run the program
if __name__ == "__main__":
    main()
