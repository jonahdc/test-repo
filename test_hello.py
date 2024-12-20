import importlib.util
spec = importlib.util.spec_from_file_location("valid_file", "./valid-file.py")
valid_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(valid_file)
hello_world = valid_file.hello_world

# Test with string input
try:
    hello_world("John")
except Exception as e:
    print(f"Error occurred: {str(e)}")