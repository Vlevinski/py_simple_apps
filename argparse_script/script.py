import argparse

def process_message(message=None):
    if message is None:
        # Create the parser
        parser = argparse.ArgumentParser(description='Process some strings.')
        # Add the argument
        parser.add_argument('message', type=str, help='The message to display')
        # Execute the parse_args() method
        args = parser.parse_args()
        message = args.message

    # Print the message
    print(message)

if __name__ == '__main__':
    # Example usage: This will use argparse to get the message from the command line
    # If you want to test the function with a predefined message, uncomment the following line
    # process_message("Hello, World!")
    
    # This will use argparse to get the message from the command line
    process_message() 

