def greet(name):
    message = ""

    if name == "Johnny":
        message = "Hello, my love!"
    else:
        message = f"Hello, {name}!"
    return message


print(greet("Alice"))