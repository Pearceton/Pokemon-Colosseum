import random
from functions.ParseCSV import ParsePokemonData, ParsePokemonMoves
from Pokemon import AssignPokemon, AssignMoves

print("Welcome to Pokemon Colosseum!\n")
player_name = input("What is your name?: ")

team_rocket_pokemon = AssignPokemon()
tr_pokemon_1 = team_rocket_pokemon[0]
tr_pokemon_2 = team_rocket_pokemon[1]
tr_pokemon_3 = team_rocket_pokemon[2]

player_pokemon = AssignPokemon()
player_pokemon_1 = player_pokemon[0]
player_pokemon_2 = player_pokemon[1]
player_pokemon_3 = player_pokemon[2]

print("\nTeam Rocket enters! They come with", tr_pokemon_1 + ",", tr_pokemon_2 + ", and", tr_pokemon_3 + "!\n")
print("Team", player_name + " enters! They come with", player_pokemon_1 + ",", player_pokemon_2 + ", and", player_pokemon_3 + "!\n")

print("Let the battle begin!\n")

# Flip a coin to decide who goes first
coin_flip = random.choice(["Team Rocket", player_name])
print(coin_flip, "will go first!\n")

print("Commence battle!\n")

"""
moves = (AssignMoves(tr_pokemon_1))
# Get all move details
moves_data = ParsePokemonMoves()


# Test: Print assigned moves and their details
for move_name in moves:
    details = moves_data[move_name]
    print(f"{move_name}: Type={details['Type']}, Power={details['Power']}, Accuracy={details['Accuracy']}")
"""

# Add Pokemon from each team to a queue
tr_pokemon_queue = [tr_pokemon_1, tr_pokemon_2, tr_pokemon_3]
player_pokemon_queue = [player_pokemon_1, player_pokemon_2, player_pokemon_3]

# Assign values to track whose turn it is
is_player_turn = (coin_flip == player_name)
current_turn = "Player" if is_player_turn else "Team Rocket"

def switch_turn(is_player_turn):
    return not is_player_turn

### Battle logic

# While loop to continue battle until one team runs out of Pokemon
while tr_pokemon_queue and player_pokemon_queue:
    if is_player_turn:
        current_pokemon = player_pokemon_queue[0]
        print(f"{player_name}'s turn! {current_pokemon} is ready to attack.")
        
        # Logic for player's attack
    else:
        current_pokemon = tr_pokemon_queue[0]
        print(f"Team Rocket's turn! {current_pokemon} is ready to attack.")
        
        # Logic for Team Rocket's attack

    # Switch turns
    is_player_turn = switch_turn(is_player_turn)