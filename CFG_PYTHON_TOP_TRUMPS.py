import random, requests


def random_pokemon():
    opponent_pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(opponent_pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'order': pokemon['order']
    }
#I am creating a best of 5 games between the player and the computer
player_wins = 0 
computer_wins = 0

for wins in range(5):
    print()
    player_pokemon_number = input("Choose a pokemon number between 1 and 151 to pick a pokemon: ")
    print()
  
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(player_pokemon_number)
    response = requests.get(url)
    player_pokemon_number = response.json()
    print("Name: " + player_pokemon_number['name'])
    print("ID: " + str(player_pokemon_number['id']))
    print("Height: " + str(player_pokemon_number['height']))
    print("Weight: " + str(player_pokemon_number['weight']))
    print("Order: " + str(player_pokemon_number['order']))

    poke_stat = {
        'name': player_pokemon_number['name'],
        'id': player_pokemon_number['id'],
        'height': player_pokemon_number['height'],
        'weight': player_pokemon_number['weight'],
        'order': player_pokemon_number['order']
    }
  
    print()
    choose_stat: str = input('Select one stat you would like to compare between >> "id, height, weight, order: " ')


    opponent_pokemon_number = random_pokemon()
    print ()
    print('The opponent chose {}'.format(opponent_pokemon_number['name']))

    print("Name: " + opponent_pokemon_number['name'])
    print("ID: " + str(opponent_pokemon_number['id']))
    print("Height: " + str(opponent_pokemon_number['height']))
    print("Weight: " + str(opponent_pokemon_number['weight']))
    print("Order: " + str(opponent_pokemon_number['order']))

    player_stat = player_pokemon_number[choose_stat]
    opponent_stat = opponent_pokemon_number[choose_stat]

    #CALCULATIONS
    if player_stat > opponent_stat:
      player_wins += 1
      print("You win")

    elif player_stat < opponent_stat:
      computer_wins += 1
      print("You lost")

    else:
        print('Draw!')
#FINAL RESULTS
print("Your final results:")
if player_wins >= 3:
  print('CONGRATULATIONS You won {} out of 5 games'.format(player_wins))
elif computer_wins >= 3:
  print('You lost, The computer won {} out of 5 games :(, try again!'.format(computer_wins))
else:
  print("You won 2 games and The comuputer won 2 games, You drew")