import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'abilities': [ability['ability']['name'] for ability in pokemon['abilities']],
    }


def run():
    num_rounds = 3
    player_wins = 0
    opponent_wins = 0
    round_outcomes = []

    for round_number in range(1, num_rounds + 1):
        my_pokemon = random_pokemon()
        print('Your Pokemon ID is:', my_pokemon['id'])  # Print the ID of the player's Pokemon
        print('You were given {}'.format(my_pokemon['name']))
        stat_choice = input('Which stat do you want to use? (id, height, weight, abilities) ')
        opponent_pokemon = random_pokemon()
        print('The opponent chose {}'.format(opponent_pokemon['name']))
        opponent_stat = opponent_pokemon.get(stat_choice)
        my_stat = my_pokemon.get(stat_choice)

        if my_stat is not None and opponent_stat is not None:
            if my_stat > opponent_stat:
                print('You Win!')
                player_wins += 1
                round_outcomes.append('win')
            elif my_stat < opponent_stat:
                print('You Lose!')
                opponent_wins += 1
                round_outcomes.append('lose')
            else:
                print('Draw!')
                round_outcomes.append('draw')
        else:
            print('Invalid stat choice!')

    print("\nRound Outcomes:", round_outcomes)

    if player_wins > opponent_wins:
        print("Congratulations! You're the overall winner!")
    elif player_wins < opponent_wins:
        print("Sorry, you didn't win enough rounds to be the overall winner.")
    else:
        print("It's a tie! No overall winner.")

        # prompt user(player) to choose to play again or quit game Deborahs part
        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again == 'yes':  # if user decides to play again, run function is called
            run()
        else:
            print('Thanks for playing, see you soon!')  # farewell message to be printed if user decides to exit game

run()

