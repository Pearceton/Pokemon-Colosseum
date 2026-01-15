from functions.ParseCSV import ParsePokemonData, ParsePokemonMoves
from Pokemon import AssignPokemon

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