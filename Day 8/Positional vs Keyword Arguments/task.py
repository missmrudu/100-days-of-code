# Functions with input

#def greet_with_name(name):
#    print(f"Hello {name}")
#   print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

def greet_with (name , location):
    print("Hello, " + name + "!")
    print("What is it like in", location, "?")

greet_with("Jack Bauer","Nowhere")

greet_with(location ="Nowhere",name ="Jack Bauer")
