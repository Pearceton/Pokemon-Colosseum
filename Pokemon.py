import random
from functions.ParseCSV import ParsePokemonData, ParsePokemonMoves

# Assign three random Pokémon to a team
def AssignPokemon():
   pokemon_data = ParsePokemonData()  
   random_pokemon_list = random.sample(list(pokemon_data.keys()), k=3)
   return random_pokemon_list

# Assign moves to a given Pokémon
def AssignMoves(pokemon_name):
   pokemon_data = ParsePokemonData()  
   moves = pokemon_data.get(pokemon_name, [])
   assigned_moves = random.sample(moves, k=len(moves))
   return assigned_moves

# Dictionary for type matchups
type_effectiveness = {
    "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2.0},
    "Water": {"Fire": 2.0, "Water": 0.5, "Rock": 2.0,"Grass": 0.5},
    "Electric": {"Water": 2.0, "Electric": 0.5, "Grass": 0.5},
    "Grass": {"Fire": 0.5, "Water": 2.0, "Grass": 0.5},
}