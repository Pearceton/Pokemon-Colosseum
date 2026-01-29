import random
from functions.ParseCSV import ParsePokemonData, ParsePokemonMoves

class Pokemon:    
    def __init__(self, name):

        pokemon_data = ParsePokemonData()
        
        if name not in pokemon_data:
            raise ValueError(f"Pokemon '{name}' not found in database")
        
        data = pokemon_data[name]
        
        self.name = name
        self.type = data['Type']
        self.hp = data['HP']
        self.attack = data['Attack']
        self.defense = data['Defense']
        self.height = data['Height']
        self.weight = data['Weight']
        self.moves = data['Moves']

# Assign Pokemon to a team
def AssignPokemon():
   pokemon_data = ParsePokemonData()
   all_six = random.sample(list(pokemon_data.keys()), k=6)
   return all_six[:3], all_six[3:]  # Returns two lists of 3

# Assign moves to a given Pokémon
def AssignMoves(pokemon_name):
   pokemon_data = ParsePokemonData()  
   moves = pokemon_data.get(pokemon_name, {}).get('Moves', [])
   assigned_moves = random.sample(moves, k=len(moves))
   return assigned_moves

# Type matchup table
type_effectiveness = {
    "Fire": {"Fire": 0.5, "Water": 0.5, "Grass": 2.0},
    "Water": {"Fire": 2.0, "Water": 0.5, "Rock": 2.0,"Grass": 0.5},
    "Electric": {"Water": 2.0, "Electric": 0.5, "Grass": 0.5},
    "Grass": {"Fire": 0.5, "Water": 2.0, "Grass": 0.5},
}

# Function to calculate damage based on move and defense
def Damage(move, pokemon_A, pokemon_B):

   moves_data = ParsePokemonMoves()
   pokemon_data = ParsePokemonData()

   # Get details on Pokemon and moves
   move_details = moves_data.get(move, {})
   pokemon_details_A = pokemon_data.get(pokemon_A, {})
   pokemon_details_B = pokemon_data.get(pokemon_B, {})

   # Get power and attack from attacker and defense from defender
   power = int(move_details.get('Power', 0))
   attack = int(pokemon_details_A.get('Attack', 0))
   defense = int(pokemon_details_B.get('Defense', 0))

   # Prevent division by zero
   if defense == 0:
      defense = 1

   # Get STAB (Same Type Attack Bonus)
   if(move_details.get('Type') == pokemon_details_A.get('Type')):
      STAB = 1.5
   else:
      STAB = 1.0

   # Get Type Effectiveness
   move_type = move_details.get('Type', 'Normal')
   defender_type = pokemon_details_B.get('Type')
   
   if move_type in type_effectiveness:
      TE = type_effectiveness[move_type].get(defender_type, 1.0)
   else:
      TE = 1.0  # "Others" row default

   # Formula for Damage Calculation
   damage = round(power * attack/defense * STAB * TE * random.uniform(0.5, 1.0))

   return int(damage)