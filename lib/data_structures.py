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
    names=[]
    for food in spicy_foods:
        names.append(food["name"])
        return names

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level") > 5]

def print_spicy_foods(spicy_foods):
   for food in spicy_foods:
    name = food.get("name", "Unknown")
    cuisine = food.get("cuisine", "unknown")
    heat_level = food.get("heat_level", 0)
    heat_level_icon = '🌶' * heat_level

    print (F"{name} | {cuisine} | Heat Level:{heat_level_icon}" )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get('heat_level') for food in spicy_foods)
    average_heat = total_heat_level / len(spicy_foods)
    return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
