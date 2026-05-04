prompt = "\nPlease enter the name of a topping you'll add that topping to their pizza:"
prompt += "\n(Enter 'Quit' when you finished.)"
while True:
    pizza = input(prompt)
    if pizza == 'quit':
        break
    else:
        print(f"I'd love to add topping to the pizza{pizza.title()}")


