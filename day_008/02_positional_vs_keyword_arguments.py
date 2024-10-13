# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it life in {location}")


# Positional arguments
greet_with("Cuong", "Nowhere")
greet_with("Nowhere", "Cuong")

# Keyword arguments
greet_with(location="Nowhere", name="Cuong")
