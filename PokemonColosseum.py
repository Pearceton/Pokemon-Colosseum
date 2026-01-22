import random
from functions.ParseCSV import ParsePokemonData, ParsePokemonMoves
from Pokemon import AssignPokemon, AssignMoves, Damage

# Get player name and welcome message
print("Welcome to Pokemon Colosseum!\n")
player_name = input("What is your name?: ")

# Assign Pokemon to each team
team_rocket_pokemon = AssignPokemon()
tr_pokemon_1 = team_rocket_pokemon[0]
tr_pokemon_2 = team_rocket_pokemon[1]
tr_pokemon_3 = team_rocket_pokemon[2]

player_pokemon = AssignPokemon()
player_pokemon_1 = player_pokemon[0]
player_pokemon_2 = player_pokemon[1]
player_pokemon_3 = player_pokemon[2]

# Display teams
print("\nTeam Rocket enters! They come with", tr_pokemon_1 + ",", tr_pokemon_2 + ", and", tr_pokemon_3 + "!\n")
print("Team", player_name + " enters! They come with", player_pokemon_1 + ",", player_pokemon_2 + ", and", player_pokemon_3 + "!\n")

print("Let the battle begin!\n")

# Flip a coin to decide who goes first
coin_flip = random.choice(["Team Rocket", player_name])
print(coin_flip, "will go first!\n")


# Add Pokemon from each team to a queue
tr_pokemon_queue = [tr_pokemon_1, tr_pokemon_2, tr_pokemon_3]
player_pokemon_queue = [player_pokemon_1, player_pokemon_2, player_pokemon_3]

# Assign values to track whose turn it is
is_player_turn = (coin_flip == player_name)
current_turn = "Player" if is_player_turn else "Team Rocket"

# Function to switch turns
def switch_turn(is_player_turn):
    return not is_player_turn

### Battle logic
current_pokemon = player_pokemon_queue[0]
tr_pokemon = tr_pokemon_queue[0]
current_tr_health = ParsePokemonData()[tr_pokemon]['HP']
current_player_health = ParsePokemonData()[current_pokemon]['HP']

# While loop to continue battle until one team runs out of Pokemon
while tr_pokemon_queue and player_pokemon_queue:

    if is_player_turn:

        print(f"{player_name}'s turn! {current_pokemon} is ready to attack.")
        
        # Logic for player's attack
        print(f"Choose the move for {current_pokemon}:")

        # Display assigned moves
        i = 1
        for move in AssignMoves(current_pokemon):
            print(f"{i}. {move}")
            i += 1

        # Get player's move choice, with input validation
        try:
            selected_move = int(input(f"Team {player_name} selects: "))

            if selected_move < 1 or selected_move > len(AssignMoves(current_pokemon)):
                print("Invalid move selection. Please choose a valid move number.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number corresponding to the move.")
            continue

        move_to_use = AssignMoves(current_pokemon)[selected_move - 1]

        # Execute the move and update opponent's health
        print(f"{current_pokemon} cast {move_to_use} to {tr_pokemon}:\n")
        damage = Damage(move_to_use, current_pokemon, tr_pokemon)
        current_tr_health = current_tr_health - damage
        print(f"Damage to {tr_pokemon} is {damage} points!")

        if(current_tr_health <= 0):
            print(f"Now {tr_pokemon} faints back to the pokeball! {current_pokemon} has {current_player_health} HP!\n")
            tr_pokemon_queue.pop(0)
            
            # If Team Rocket has no more Pokemon, player wins
            if not tr_pokemon_queue:
                print(f"Team Rocket has no more Pokémon left! Team {player_name} wins!")
                break
            
            # Switch to next Team Rocket Pokemon
            tr_pokemon = tr_pokemon_queue[0]
            current_tr_health = ParsePokemonData()[tr_pokemon]['HP']
            print(f"Now {tr_pokemon} enters the battle!")
        else:
            print(f"{tr_pokemon} now has {current_tr_health} HP! {current_pokemon} has {current_player_health} HP!\n")

        # Switch turns
        is_player_turn = switch_turn(is_player_turn)

    else:
        print(f"Team Rocket's turn! {tr_pokemon} is ready to attack.")
        
        # Logic for Team Rocket's attack
        move_to_use = random.choice(AssignMoves(tr_pokemon))
        print(f"Team Rocket's {tr_pokemon} uses {move_to_use}:\n")
        damage = Damage(move_to_use, tr_pokemon, current_pokemon)
        current_player_health = current_player_health - damage
        print(f"Damage to {current_pokemon} is {damage} points!")

        if(current_player_health <= 0):
            print(f"Now {current_pokemon} faints back to the pokeball! {tr_pokemon} has {current_tr_health} HP! \n")
            player_pokemon_queue.pop(0)
            
            # If player has no more Pokemon, Team Rocket wins
            if not player_pokemon_queue:
                print(f"Team {player_name} has no more Pokémon left! Team Rocket wins!")
                break
            
            # Switch to next player Pokemon
            current_pokemon = player_pokemon_queue[0]
            current_player_health = ParsePokemonData()[current_pokemon]['HP']
            print(f"Now {current_pokemon} enters the battle!")
        else:
            print(f"{current_pokemon} now has {current_player_health} HP! {tr_pokemon} has {current_tr_health} HP!\n")

        # Switch turns
        is_player_turn = switch_turn(is_player_turn)

    