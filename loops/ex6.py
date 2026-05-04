team_names = ['carolina','rachel','collinson','Michal','emly']
print("Here are the first there members:")
for team in team_names[4:]:
    print(team)
my_foods = ['pizza','falafel','carrotcake']
friends_foods = my_foods[:]
print("my favorite foods are:")
for foods in my_foods:
    print(foods)
my_foods.append('icecream')
print(my_foods)
print("\n my friends favorite foods are:")
friends_foods.append('cake')
for friends in friends_foods:
    print(friends)
print(friends_foods)