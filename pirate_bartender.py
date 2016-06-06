import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": [
        {"name": "glug of rum", "stock": 32},
        {"name": "slug of whisky", "stock": 17},
        {"name": "splash of gin", "stock": 12},
    ],
    "salty": [
        {"name": "olive on a stick", "stock": 11},
        {"name": "salt-dusted rim", "stock": 52},
        {"name": "rasher of bacon", "stock": 5},
    ],
    "bitter": [
        {"name": "shake of bitters", "stock": 15},
        {"name": "splash of tonic", "stock": 3},
        {"name": "twist of lemon peel", "stock": 74},
    ],
    "sweet": [
        {"name": "sugar cube", "stock": 65},
        {"name": "spoonful of honey", "stock": 135},
        {"name": "splash of cola", "stock": 4},
    ],
    "fruity": [
        {"name": "slice of orange", "stock": 12},
        {"name": "dash of cassis", "stock": 6},
        {"name": "cherry on top", "stock": 89},
    ],
}

def taste_questions(questions):
    tastes = {}
    for taste in questions:
        valid_answer = False
        while not(valid_answer):
            value = str(input(questions[taste] + ' (yes or no): ')).lower()
            if (value == 'y') or (value == 'yes'):
                tastes[taste] = True
                valid_answer = True
            elif (value == 'n') or (value == 'no'):
                tastes[taste] = False
                valid_answer = True
    return tastes
    
def mix_drink(tastes, ingredients):
    drink = []
    for taste in tastes:
        if tastes[taste]:
            stocked_ingredient = ''
            while not(stocked_ingredient):
                ingredient = random.choice(ingredients[taste])
                if ingredient['stock'] > 0:
                    stocked_ingredient = ingredient
                    for ingredient_from_stock in ingredients[taste]:
                        print(ingredient_from_stock)
                        if ingredient['name'] == ingredient_from_stock['name']:
                            ingredient_from_stock['stock'] -= 1
                            print('There are', ingredient_from_stock['stock'], 'of', ingredient['name'], 'left.')
                else:
                    print('Order some more', ingredient, '!')
            drink.append(stocked_ingredient)
    return drink
    
def drink_name():
    adjectives = ['Salty', 'Sassy', 'Fluffy', 'Drowned', 'Scuttled', 'Crusty', 'Sandy']
    nouns = ['Shrimp', 'Plank', 'Squid', 'Davy Jones', 'Whisker', 'Kraken']
    drink = random.choice(adjectives) + ' ' + random.choice(nouns)
    return drink
                
if __name__ == '__main__':
    customers = {}
    name = ''
    while True:
        menu_selection = ''
        while (menu_selection != 'g') and (menu_selection != 's') and (menu_selection != 'w'):
            menu_selection = input('Bar tender, re(s)tock the bar, (g)reet ye customer, or (w)alk the plank? ').lower()
            if menu_selection == 'g':
                name = ''
                while (len(name) < 1):
                    name = input('What should I call ye? (or "empty" bar) :')
                if name == 'empty':
                    exit()
                elif not(name in customers.keys()):
                    customers[name] = taste_questions(questions)
                drink = mix_drink(customers[name], ingredients)
                print('Your ' + drink_name() + ' is made of:')
                for ingredient in drink:
                    print(ingredient['name'])
            elif menu_selection == 's':
                print('Here\'s all ye ingredients and ye stock levels:')
                for taste in ingredients:
                    for ingredient in ingredients[taste]:
                        print(ingredient['name'], ':', ingredient['stock'])
                ingredient_to_restock = input("Which thing do ye need more of? ")
                for taste in ingredients:
                    for ingredient in ingredients[taste]:
                        if ingredient['name'] == ingredient_to_restock:
                            ingredient['stock'] += 10
                            print('10 more', ingredient['name'], 'added.')
            elif menu_selection == 'w':
                exit()