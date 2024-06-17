import argparse

def process_message(message=None):
    if message is None:
        # Create the parser
        parser = argparse.ArgumentParser(description='Process some strings.')      
        parser.add_argument('message', type=str, help='The message to display') 
        args = parser.parse_args() # Execute the parse_args() method
        message = args.message

    # Print the message
    print(message)

# Example usage from a script or another function
if __name__ == '__main__':
    # This will print the provided message
    process_message("Hello, World!")  

