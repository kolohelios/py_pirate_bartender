import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def taste_questions(questions):
    tastes = {}
    for taste in questions:
        valid_answer = False
        while not(valid_answer):
            value = str(input(questions[taste] + ' (yes or no): '))
            if (value == 'y') or (value == 'yes') or (value == 'Y') or (value == 'YES'):
                tastes[taste] = True
                valid_answer = True
            elif (value == 'n') or (value == 'no') or (value == 'N') or (value == 'NO'):
                tastes[taste] = False
                valid_answer = True
    return tastes
    
def mix_drink(tastes, ingredients):
    drink = []
    for taste in tastes:
        if tastes[taste]:
            drink.append(random.choice(ingredients[taste]))
    return drink
                
if __name__ == '__main__':
    tastes = taste_questions(questions)
    drink = mix_drink(tastes, ingredients)
    print(drink)