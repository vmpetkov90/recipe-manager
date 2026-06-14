import json

# Create a file
def create_file():
    initial_recipes = [{'title':'tuna mayo rice bowl',
     'ingredients':['1 can tuna','cooked rice','mayo','soy sauce'],
     'instructions':['flake tuna into a bowl and mix with a spoon of mayo',
     'add a splash of soy sauce','serve over warm rice']},
     {'title':'cheesy quesadilla',
      'ingredients':['tortilla','grated cheese','salsa'],
      'instructions':['heat a pan and place the tortilla in','add cheese on one half','fold and cook until golden on both sides','slice and dip in salsa']},
      {'title':'garlic butter pasta',
       'ingredients':['1 serving pasta','1–2 tbsp butter','1 clove garlic, minced'],
       'instructions':['cook pasta in salted water','melt butter in a pan and gently cook garlic until fragrant','toss in the drained pasta and season with salt and pepper']}]

    recipes_json = json.dumps(initial_recipes,indent=3)

    with open('cook_book.json','w') as file:
        file.write(recipes_json)

# Open file
def open_file():
    try:
        with open('cook_book.json') as file:
            return json.loads(file.read())
    except FileNotFoundError:
        create_file()
        return open_file()
    except:
        print('Something went wrong. Please try again')

# Update file
def update_file(message):
    try:
        with open('cook_book.json','w') as file:
            cook_book_json = json.dumps(cook_book,indent=3)
            file.write(cook_book_json)
            print(message)
    except:
        print('Something went wrong. Please try again')

# Variable to store recipes
cook_book = open_file()

