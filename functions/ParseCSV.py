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
                'HP': row[2],
                'Attack': row[3],
                'Defense': row[4],
                'Height': row[5],
                'Weight': row[6],
                'Moves': row[7]

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
            moves_data[move_name] = {
                'Type': row[1],
                'Category': row[2],
                'Contest': row[3],
                'PP': row[4],
                'Power': row[5],
                'Accuracy': row[6]
            }

    return moves_data

