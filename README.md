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
