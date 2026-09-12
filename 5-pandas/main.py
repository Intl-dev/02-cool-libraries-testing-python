import pandas as pd
data = pd.read_csv("Pokemon.csv")
df = pd.DataFrame(data)
df= df.fillna({"Type2": "None"})

def search(df, column_name, value):
    result = df[df[column_name] == value]
    return result

option_chosen = input("Select an option to search, 1 for a specific pokemon, 2, for a stat, 3 for a type: ")
if option_chosen == "1":
    specific_pokemon = input("Enter 1 to use the pokemon name, or 2 for the index number of the pokemon: ")
    if specific_pokemon == "1":
        pokemon_name = input("Enter pokemon name: ")
        print(search(df, "Pokemon", pokemon_name).to_string())

    if specific_pokemon == "2":
        pokemon_ndex = int(input("Enter the index number of the pokemon (first 100 pokemon start with 00 or 0, for example 001 for bulbasaur: "))
        print(search(df, "Ndex", pokemon_ndex).to_string())
if option_chosen == "2":
    pokemon_stat = input("Enter 1 for HP,2 for attack, 3 for special attack, 4 for defense, 5 for special defense, and 6 for speed: ")
    if pokemon_stat == "1":
        HP = int(input("Enter HP value: "))
        print(search(df, "Hp", HP).to_string())


