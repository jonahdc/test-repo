from valid_file import hello_world

# Test with a string input
try:
    hello_world("Test input")
except Exception as e:
    print(f"Error occurred: {str(e)}")

# Test without input (original behavior)
try:
    hello_world()
except Exception as e:
    print(f"Error occurred: {str(e)}")