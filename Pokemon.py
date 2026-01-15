import random
from functions.ParseCSV import ParsePokemonData

def AssignPokemon():
   pokemon_data = ParsePokemonData()  # Call the function and store result
   random_pokemon_list = random.sample(list(pokemon_data.keys()), k=3)
   return random_pokemon_list