print('Welcome to the Treasure Hunt!')
print('Your goal is to find the treasure.')
direction = input('You are at a crossroad. Where do you want to go? Type left or right. \n')

if direction == "left":
    wait_or_swim = input('You have come to a lake. There is an island in middle of the lake. Type "wait" to wait for a boat or "swim" to swim accross the lake? \n')
elif direction == "right":
    print('You are crushed by a truck. Game Over!')
else:
    print('You chose an option that doesn\'t exist.')

    
if wait_or_swim == "wait":
    color = input('You arrived at the island unharmed. There is a house with three doors. One red, one blue and one green. Which one will you choose? \n')
elif wait_or_swim == "swim":
    print('You have been eaten by a shark.\nGame Over.')
else:
    print('You chose an option that does not exist. ')

    
if color == "red":
    print('You fell into a room full of fire.\nGame Over.')
    
elif color == "green": 
    print('Congratulations, you have found the treasure!')
    
elif color == "blue":
    print('You fell into a ditch.\nGame Over.')
        
else:
    print('You chose a door that does not exist.\nGame Over.')
  
             
  