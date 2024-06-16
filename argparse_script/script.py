import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some strings.')

# Add the arguments
parser.add_argument('message', type=str, help='The message to display')

# Execute the parse_args() method
args = parser.parse_args()

print(args.message)
