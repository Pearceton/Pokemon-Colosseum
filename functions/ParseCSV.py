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
            #print(moves)
            pokemon_moves[row[0]] = ast.literal_eval(moves) # string to list

#    for key in pokemon_moves:
 #       print(key, "moves: ", pokemon_moves[key])

    return pokemon_moves

def ParsePokemonMoves():
    moves_filename = 'moves-data.csv'
    header = []
    moves_data = {}

    with open(moves_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            moves_data[row[0]] = row[1:]  # move name as key, rest as values

    return moves_data