import csv
import ast

def ParsePokemonData():
    pokemon_filename = 'pokemon-data.csv'
    header = []
    pokemon_data = {}

    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            pokemon_name = row[0]
            pokemon_data[pokemon_name] = {
                'Type': row[1],
                'HP': int(row[2]),
                'Attack': int(row[3]),
                'Defense': int(row[4]),
                'Height': float(row[5]),
                'Weight': float(row[6]),
                'Moves': ast.literal_eval(row[7])

            }

    return pokemon_data

def ParsePokemonMoves():
    moves_filename = 'moves-data.csv'
    moves_data = {}

    with open(moves_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            move_name = row[0]
            accuracy = None if row[6].lower() == 'none' else int(row[6])
            moves_data[move_name] = {
                'Type': row[1],
                'Category': row[2],
                'Contest': row[3],
                'PP': int(row[4]),
                'Power': int(row[5]),
                'Accuracy': accuracy
            }

    return moves_data

