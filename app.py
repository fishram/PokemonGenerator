from flask import Flask, render_template

import requests
from random import randint

app: Flask = Flask(__name__)

type_compare: dict[str, dict[str, float]] = {
    "normal": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 0.5, "ghost": 0.0, "dragon": 1.0, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
    "fire": {"normal": 1.0, "fire": .5, "water": .5, "electric": 1.0, "grass": 2.0, "ice": 2.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 2.0, "rock": 0.5, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 2.0, "fairy": 1.0},
    "water": {"normal": 1.0, "fire": 2.0, "water": .5, "electric": 1.0, "grass": .5, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 2.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 2.0, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 0.0, "fairy": 1.0},
    "electric": {"normal": 1.0, "fire": 1.0, "water": 2.0, "electric": 1.0, "grass": 0.5, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 0.0, "flying": 2.0, "psychic": 1.0, "bug": 1.0, "rock": 1.0, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 1.0, "fairy": 1.0},
    "grass": {"normal": 1.0, "fire": 0.5, "water": 2.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 1.0, "poison": 0.5, "ground": 2.0, "flying": 0.5, "psychic": 1.0, "bug": 0.5, "rock": 2.0, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
    "ice": {"normal": 1.0, "fire": .5, "water": .5, "electric": 1.0, "grass": 2.0, "ice": .5, "fighting": 1.0, "poison": 1.0, "ground": 2.0, "flying": 2.0, "psychic": 1.0, "bug": 1.0, "rock": 1.0, "ghost": 1.0, "dragon": 2.0, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
    "fighting": {"normal": 2.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 2.0, "fighting": 1.0, "poison": 0.5, "ground": 1.0, "flying": 0.5, "psychic": 0.5, "bug": 0.5, "rock": 2.0, "ghost": 0.0, "dragon": 1.0, "dark": 2.0, "steel": 2.0, "fairy": 0.5},
    "poison": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 2.0, "ice": 1.0, "fighting": 1.0, "poison": 0.5, "ground": 0.5, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": .5, "ghost": 0.5, "dragon": 1.0, "dark": 1.0, "steel": 0.0, "fairy": 1.0},
    "ground": {"normal": 1.0, "fire": 2.0, "water": 1.0, "electric": 2.0, "grass": 0.5, "ice": 1.0, "fighting": 1.0, "poison": 2.0, "ground": 1.0, "flying": 0.0, "psychic": 1.0, "bug": 0.5, "rock": 2.0, "ghost": 1.0, "dragon": 1.0, "dark": 1.0, "steel": 2.0, "fairy": 1.0},
    "flying": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 0.5, "grass": 2.0, "ice": 1.0, "fighting": 2.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 2.0, "rock": 0.5, "ghost": 1.0, "dragon": 1.0, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
    "psychic": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 2.0, "poison": 2.0, "ground": 1.0, "flying": 1.0, "psychic": 0.5, "bug": 1.0, "rock": 1.0, "ghost": 1.0, "dragon": 1.0, "dark": 0.0, "steel": 0.5, "fairy": 1.0},
    "bug": {"normal": 1.0, "fire": 0.5, "water": 1.0, "electric": 1.0, "grass": 2.0, "ice": 1.0, "fighting": 0.5, "poison": 0.5, "ground": 1.0, "flying": 0.5, "psychic": 2.0, "bug": 1.0, "rock": 1.0, "ghost": 0.5, "dragon": 1.0, "dark": 2.0, "steel": 0.5, "fairy": 0.5},
    "rock": {"normal": 1.0, "fire": 2.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 2.0, "fighting": 0.5, "poison": 1.0, "ground": 0.5, "flying": 2.0, "psychic": 1.0, "bug": 2.0, "rock": 1.0, "ghost": 1.0, "dragon": 1.0, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
    "ghost": {"normal": 0.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 2.0, "bug": 1.0, "rock": 1.0, "ghost": 2.0, "dragon": 1.0, "dark": 0.5, "steel": 1.0, "fairy": 1.0},
    "dargon": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 1.0, "ghost": 1.0, "dragon": 2.0, "dark": 1.0, "steel": 0.5, "fairy": 0.0},
    "dark": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 0.5, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 2.0, "bug": 1.0, "rock": 1.0, "ghost": 2.0, "dragon": 1.0, "dark": 0.5, "steel": 1.0, "fairy": 0.5}, 
    "steel": {"normal": 1.0, "fire": 0.5, "water": 0.5, "electric": 0.5, "grass": 1.0, "ice": 2.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 2.0, "ghost": 1.0, "dragon": 1.0, "dark": 1.0, "steel": 0.5, "fairy": 2.0},
    "fairy": {"normal": 1.0, "fire": 0.5, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 2.0, "poison": 0.5, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 1.0, "ghost": 1.0, "dragon": 2.0, "dark": 2.0, "steel": 0.5, "fairy": 1.0}
}


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generated_pokemon")
def generate_pokemon():
    generated: Pokemon = Pokemon(id = randint(1,905))
    pokemon_name: str = generated.get_name()
    pokemon_type: list[str] = generated.get_type()
    pokemon_height: int = generated.get_height()
    pokemon_image: str = generated.get_image()
    id = generated.id
    generated2: Pokemon = Pokemon(id = randint(1,905))
    pokemon_name2: str = generated2.get_name()
    pokemon_type2: list[str] = generated2.get_type()
    pokemon_height2: int = generated2.get_height()
    pokemon_image2: str = generated2.get_image()
    id2 = generated2.id
    generated.type = pokemon_type
    generated2.type = pokemon_type2
    generated.name = pokemon_name
    generated2.name = pokemon_name2
    battle_result = battle(generated, generated2)

    return render_template('generated_pokemon.html', pokemon_name = pokemon_name.capitalize(), pokemon_type = pokemon_type, pokemon_height = pokemon_height, pokemon_image = pokemon_image, id = id, pokemon_name2 = pokemon_name2.capitalize(), pokemon_type2 = pokemon_type2, pokemon_height2 = pokemon_height2, pokemon_image2 = pokemon_image2, id2 = id2, battle_result = battle_result)



class Pokemon: 
    type: str
    name: str
    height: int
    id: int
    image: str

    def __init__(self, type = "", name = "", height = 69, id = 420, image = "") -> None:
        self.type = type
        self.name = name
        self.height = height
        self.id = id
        self.image = image

    def get_name(self) -> str:
        pokemon_api_url: str = f"https://pokeapi.co/api/v2/pokemon/{self.id}"
        data = requests.get(pokemon_api_url)
        # response: dict[str,list[dict[str,str]]] = data.json()
        pokemon_dictionary = data.json()
        # is a dictionary with all the categories about the pokemon
        # list is a breakdown of the categories into name and url
        return pokemon_dictionary["name"]

    def get_type(self) -> str:
        pokemon_api_url: str = f"https://pokeapi.co/api/v2/pokemon/{self.id}"
        data = requests.get(pokemon_api_url)
        pokemon_dictionary = data.json()
        pokemon_types: str = ""
        pokemon_types = (pokemon_dictionary["types"][0]["type"]["name"])
        return pokemon_types

    def get_height(self) -> float:
        pokemon_api_url: str = f"https://pokeapi.co/api/v2/pokemon/{self.id}"
        data = requests.get(pokemon_api_url)
        pokemon_dictionary = data.json()
        return pokemon_dictionary["height"] / 10

    def get_image(self) -> str:
        if (self.id < 100 and self.id > 10):
            pokemon_image: str = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/0{self.id}.png"
        elif (self.id < 10):
            pokemon_image: str = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/00{self.id}.png"
        else:
            pokemon_image: str = f"https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{self.id}.png"
        return pokemon_image

def battle(pokemon1: Pokemon, pokemon2: Pokemon) -> str:
    result: float = 0.0
    if pokemon2.type != "":
        result = type_compare[pokemon1.type][pokemon2.type]
        if result > 1.0:
            return f"{pokemon1.name.capitalize()} Wins!"
        elif result == 1.0:
            return f"It's a tie!"
        elif result < 1.0:
            return f"{pokemon1.name.capitalize()} Loses!"
    

if __name__ == '__main__':
    app.run(debug=True)