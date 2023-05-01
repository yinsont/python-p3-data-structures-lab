spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [n.get("name") for n in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    names = [n for n in spicy_foods if n.get("heat_level") > 5]
    return names

def print_spicy_foods(spicy_foods):
  heat = '🌶'
  for n in spicy_foods:
    print(f'{n.get("name")} ({n.get("cuisine")}) | Heat Level: {heat * (n.get("heat_level"))}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
  for n in spicy_foods:
    if n.get("cuisine") == cuisine:
      return (n)

def print_spiciest_foods(spicy_foods):
    heat = '🌶'
    for n in spicy_foods:
        if n.get("heat_level") > 5:
            print(f'{n.get("name")} ({n.get("cuisine")}) | Heat Level: {heat * (n.get("heat_level"))}')

def get_average_heat_level(spicy_foods):
    overallHeat = 0
    for n in spicy_foods:
       overallHeat += n.get("heat_level")
    return(overallHeat/len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
  new_spicy_food = spicy_foods
  new_spicy_food.append(spicy_food)
  return(new_spicy_food)
