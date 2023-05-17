from app import Pokemon

type_compare: dict[str, dict[str, float]] = {
    "normal": {"normal": 1.0, "fire": 1.0, "water": 1.0, "electric": 1.0, "grass": 1.0, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 0.5, "ghost": 0.0, "dragon": 1.0, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
    "fire": {"normal": 1.0, "fire": .5, "water": .5, "electric": 1.0, "grass": 2.0, "ice": 2.0, "fighting": 1.0, "poison": 1.0, "ground": 1.0, "flying": 1.0, "psychic": 1.0, "bug": 2.0, "rock": 0.5, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 2.0, "fairy": 1.0},
    "water": {"normal": 1.0, "fire": 2.0, "water": .5, "electric": 1.0, "grass": .5, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 2.0, "flying": 1.0, "psychic": 1.0, "bug": 1.0, "rock": 2.0, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 0.0, "fairy": 1.0},
    "electric": {"normal": 1.0, "fire": 1.0, "water": 2.0, "electric": 0.5, "grass": 0.5, "ice": 1.0, "fighting": 1.0, "poison": 1.0, "ground": 0.0, "flying": 2.0, "psychic": 1.0, "bug": 1.0, "rock": 1.0, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 1.0, "fairy": 1.0},
    "grass": {"normal": 1.0, "fire": 0.5, "water": 2.0, "electric": 1.0, "grass": 0.5, "ice": 1.0, "fighting": 1.0, "poison": 0.5, "ground": 2.0, "flying": 0.5, "psychic": 1.0, "bug": 0.5, "rock": 2.0, "ghost": 1.0, "dragon": 0.5, "dark": 1.0, "steel": 0.5, "fairy": 1.0},
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









