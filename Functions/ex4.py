def describe_pet(animal_type,pet_name):
    """ Display information about a pet."""
    print(f"I have a {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type="hammer",pet_name='harry')
describe_pet(pet_name='harry',animal_type="hammer")