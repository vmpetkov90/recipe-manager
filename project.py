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

# View all recipes
def view_all_recipes():
    if len(cook_book) > 0:
        for recipe in cook_book:
            print(recipe['title'].capitalize())
    else:
        print('The cook book is empty.')

# View a specific recipe
def view_recipe():
    match = False
    if len(cook_book) > 0:
        while True:
            recipe_to_view = input('Which recipe would you like to view?: ')
            if len(recipe_to_view) > 0:
                break
        for recipe in cook_book:
            if recipe['title'] == recipe_to_view.lower():
                match = True
                print('Ingredients:')
                for index, ingredient in enumerate(recipe['ingredients'], start=1):
                    print(f'{index}. {ingredient}')
                print('Instructions:')
                for index, instruction in enumerate(recipe['instructions'], start=1):
                    print(f'{index}. {instruction}')
        if match == False:
            print('This recipe is not in our cook book.')
    else:
        print('The cook book is empty')
        
# Add a new recipe
def add_new_recipe():
    while True:
        match = False
        title = input('Add a recipe title: ')
        for recipe in cook_book:
            if title.lower() == recipe['title']:
                match = True     
        if not match and len(title) > 0:
            break
        elif match :
            print('This recipe is already in the cook book.')
    print('Add ingredients (leave blank when done).')
    ingredients_list = []
    while True:
        ingredient = input(f'Ingredient №{len(ingredients_list)+1}: ')
        if len(ingredient) > 0:
            ingredients_list.append(ingredient.lower())
        elif len(ingredient) == 0 and len(ingredients_list) > 0:
            break
    print('Add instructions (leave blank when done).')
    instructions_list = []
    while True:
        instructions = input(f'Instruction №{len(instructions_list)+1}: ')
        if len(instructions) > 0:
            instructions_list.append(instructions.lower())
        elif len(instructions) == 0 and len(instructions_list) > 0:
            break
    recipe={
        'title':title.lower(),
        'ingredients': ingredients_list,
        'instructions': instructions_list
    }
    cook_book.append(recipe)
    message = f'"{title.capitalize()}" was successfully added to the recipe book'
    update_file(message)

# Search for a recipe 
def search_recipe():
    if len(cook_book) > 0:
        match = False
        while True:
            query = input('Enter what you are searching for: ')
            if len(query) > 0:
                break
        for recipe in cook_book:
            if ( query.lower() in recipe['title'].lower()
                or any(query.lower() in ingredient.lower() for ingredient in recipe['ingredients'])):
                match = True
                print(recipe['title'].capitalize())
        if not match:
            print('Nothing found')
    else:
        print('The cook book is empty.')

# Variable to store recipes
cook_book = open_file()

# Variable to stop the main program
stop = False

# Main program
while True:
    print('\nPlease, choose one of the following options:\n')
    print('1. View all recipes.')
    print('2. View a recipe')
    print('3. Search for a recipe by title or ingredients')
    print('4. Add a new recipe.')
    print('5. Edit a recipe')
    print('6. Delete a recipe\n')
    while True:
        option = input('Please select the number of the choosen option: ')
        if option in ['1','2','3','4','5','6']:
            break
    if option == '1':
        view_all_recipes()
    elif option == '2':
        view_recipe()
    elif option == '3':
        search_recipe()
    elif option == '4':
        add_new_recipe()

    while True:
        another_action = input('\nWould you like to perform another action? (yes/no): ')
        if another_action == 'no':
            stop = True
            break
        elif another_action == 'yes':
            break
    if stop:
        break
