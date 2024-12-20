import importlib.util
spec = importlib.util.spec_from_file_location("valid_file", "./valid-file.py")
valid_file = importlib.util.module_from_spec(spec)
spec.loader.exec_module(valid_file)
hello_world = valid_file.hello_world

print("Test 1: No arguments (default case)")
hello_world()

print("\nTest 2: Empty string")
hello_world("")

print("\nTest 3: String with whitespace")
hello_world("   Bob   ")

print("\nTest 4: None value")
hello_world(None)