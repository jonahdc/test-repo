def hello_world(name=None):
    if name is None:
        print("hello world")
    else:
        # Handle empty strings and strip whitespace
        name = str(name).strip()
        if not name:
            print("hello world")
        else:
            print(f"hello {name}")
