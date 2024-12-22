import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)
''')

# Function to calculate difficulty
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    else:
        return "Hard"

# Function to create a recipe
def create_recipe(conn, cursor):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients]

    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)

    cursor.execute('''INSERT INTO Recipes (name, ingredients, cooking_time, difficulty)
                      VALUES (%s, %s, %s, %s)''',
                   (name, ingredients_str, cooking_time, difficulty))
    conn.commit()
    print("Recipe added successfully!")

# Function to search for a recipe
def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = set()
    for row in results:
        all_ingredients.update(row[0].split(", "))

    all_ingredients = list(all_ingredients)
    print("Available ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    choice = int(input("Select an ingredient by number: "))
    search_ingredient = all_ingredients[choice - 1]

    cursor.execute('''SELECT * FROM Recipes WHERE ingredients LIKE %s''', (f"%{search_ingredient}%",))
    recipes = cursor.fetchall()

    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print("No recipes found with that ingredient.")

# Function to update a recipe
def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()

    print("Available recipes:")
    for recipe in recipes:
        print(recipe)

    recipe_id = int(input("Enter the ID of the recipe to update: "))
    column = input("Which column would you like to update? (name/cooking_time/ingredients): ")

    if column in ["name", "cooking_time", "ingredients"]:
        new_value = input("Enter the new value: ")
        if column == "cooking_time":
            new_value = int(new_value)
        elif column == "ingredients":
            new_value = ", ".join([i.strip() for i in new_value.split(",")])
            cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
            cooking_time = cursor.fetchone()[0]
            difficulty = calculate_difficulty(cooking_time, new_value.split(", "))
            cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (difficulty, recipe_id))

        cursor.execute(f"UPDATE Recipes SET {column} = %s WHERE id = %s", (new_value, recipe_id))
        conn.commit()
        print("Recipe updated successfully!")
    else:
        print("Invalid column name.")

# Function to delete a recipe
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    recipes = cursor.fetchall()

    print("Available recipes:")
    for recipe in recipes:
        print(recipe)

    recipe_id = int(input("Enter the ID of the recipe to delete: "))

    cursor.execute("DELETE FROM Recipes WHERE id = %s", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

# Main menu
def main_menu(conn, cursor):
    while True:
        print("\nMain Menu")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            conn.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu(conn, cursor)