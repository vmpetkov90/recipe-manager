# 📖 Recipe Manager — Python CLI App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![CLI](https://img.shields.io/badge/Interface-CLI-blue?style=for-the-badge)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/vmpetkov90/recipe-manager)

A simple, interactive **Recipe Manager** built in **Python**, designed to store, search, edit, and manage recipes directly from the command line.  
All data is saved locally in a JSON file, making the app lightweight, portable, and easy to extend.

---

## 🚀 Features

- **View All Recipes**  
  Quickly list every recipe stored in the cookbook.

- **View a Specific Recipe**  
  Displays ingredients and step‑by‑step instructions.

- **Search Functionality**  
  Look up recipes by:
  - Title  
  - Any ingredient  

- **Add New Recipes**  
  Interactive prompts for:
  - Title  
  - Ingredients  
  - Instructions  

- **Edit Existing Recipes**  
  Update:
  - Title  
  - Ingredients (add/remove)  
  - Instructions (add/remove)

- **Delete Recipes**  
  Remove any recipe from the cookbook.

- **Automatic File Handling**  
  If `cook_book.json` doesn’t exist, it’s created with starter recipes.

---

## ▶️ How to Run the Recipe Manager

### **1. Make sure you have Python installed**
The project requires **Python 3.8+**.  
Check your version:

```
python --version
```

or:

```
python3 --version
```

---

### **2. Clone the repository**

```
git clone https://github.com/your-username/recipe-manager.git
```

Then navigate into the project folder:

```
cd recipe-manager
```

---

### **3. Run the program**

```
python main.py
```

or:

```
python3 main.py
```

---

### **4. Use the interactive menu**

Once the program starts, you’ll see:

```
Please, choose one of the following options:

1. View all recipes.
2. View a recipe
3. Search for a recipe by title or ingredients
4. Add a new recipe.
5. Edit a recipe
6. Delete a recipe
```

Type the number of the action you want to perform.

---

## 📂 Project Structure

```
recipe-manager/
│
├── cook_book.json        # Auto‑generated storage file
└── main.py               # Full CLI application
```

---

## 🧠 How It Works

### **Data Storage**
All recipes are stored in a JSON file as a list of objects:

```json
{
  "title": "tuna mayo rice bowl",
  "ingredients": ["1 can tuna", "cooked rice", "mayo", "soy sauce"],
  "instructions": ["flake tuna...", "add soy sauce...", "serve over rice"]
}
```

The app automatically loads this file on startup and updates it whenever changes are made.

---

## 🧩 Main Functionalities

### **`create_file()`**
- Generates the initial JSON file with three starter recipes.

### **`open_file()`**
- Loads the cookbook safely  
- Creates the file if missing

### **`update_file(message)`**
- Saves all changes back to JSON  
- Prints a confirmation message

### **`view_all_recipes()`**
- Lists all recipe titles

### **`view_recipe()`**
- Shows ingredients and instructions for a chosen recipe

### **`add_new_recipe()`**
- Adds a new recipe through guided prompts  
- Prevents duplicate titles

### **`search_recipe()`**
- Searches by title or ingredient substring

### **`delete_recipe()`**
- Removes a recipe by exact title match

### **`edit_recipe()`**
- Allows editing:
  - Title  
  - Ingredients  
  - Instructions  
- Handles add/remove logic interactively

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON (for data persistence)**
- **Command Line Interface**

---

## 📸 Example Interaction

```
Please, choose one of the following options:

1. View all recipes.
2. View a recipe
3. Search for a recipe by title or ingredients
4. Add a new recipe.
5. Edit a recipe
6. Delete a recipe

Please select the number of the chosen option: 1
Tuna mayo rice bowl
Cheesy quesadilla
Garlic butter pasta
```

---

## 🔮 Future Improvements

- **Export & Import Recipes**  
  Allow users to back up or load recipes from external JSON files.

- **Sorting & Filtering**  
  Sort recipes alphabetically or filter by ingredient count.

- **Categories / Tags**  
  Add recipe categories such as *breakfast*, *quick meals*, *vegetarian*, etc.

- **Better Error Handling**  
  More descriptive messages for invalid inputs or corrupted JSON files.

- **Unit Tests**  
  Add automated tests to ensure reliability as the project grows.

- **Optional GUI Version**  
  A simple Tkinter or web‑based interface for non‑CLI users.

---

## 📜 License

This project was created as part of ongoing Python development practice.  
It is open‑source and free for anyone to explore, modify, or build upon.
