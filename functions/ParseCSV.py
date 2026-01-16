import csv
import ast

def ParsePokemonData():
    pokemon_filename = 'pokemon-data.csv'
    header = []
    pokemon_moves = {}

    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            moves=''
            end_of_moves=False
            for s in row:
                if s[0]=='[':
                    end_of_moves = True
                    moves = s
                elif end_of_moves == True:
                    moves += ','+s
                    if s[-1] == ']':
                        end_of_moves = False
            pokemon_moves[row[0]] = ast.literal_eval(moves) # string to list

    return pokemon_moves

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

