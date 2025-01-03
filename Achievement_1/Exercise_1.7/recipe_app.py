from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create engine object to connect to database
engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Model Definition
class Recipe(Base):
    __tablename__ = 'final_recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    ingredients = Column(String(255), nullable=False)
    cooking_time = Column(Integer, nullable=False)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')>"

    def __str__(self):
        return (f"\n{'-'*40}\n"
                f"Recipe ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Ingredients: {self.ingredients}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.difficulty}\n"
                f"{'-'*40}\n")

    def calculate_difficulty(self):
        num_ingredients = len(self.return_ingredients_as_list())
        if self.cooking_time < 10 and num_ingredients <= 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients > 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients <= 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(", ")

# Create the table
Base.metadata.create_all(engine)

# Main Menu operations
def create_recipe():
    name = input("Enter the recipe name: ")
    while len(name) > 50:
        name = input("Name too long. Please enter a name up to 50 characters: ")

    cooking_time = input("Enter the cooking time in minutes: ")
    while not cooking_time.isnumeric():
        cooking_time = input("Invalid input. Please enter a numeric value for cooking time: ")
    cooking_time = int(cooking_time)

    ingredients = []
    num_ingredients = input("How many ingredients does this recipe have? ")
    while not num_ingredients.isnumeric():
        num_ingredients = input("Invalid input. Please enter a numeric value: ")
    for _ in range(int(num_ingredients)):
        ingredients.append(input("Enter an ingredient: "))
    ingredients_str = ", ".join(ingredients)

    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time)
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe added successfully!")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("No recipes found.")
        return
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for row in results:
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    print("Ingredients available:")
    for idx, ingredient in enumerate(all_ingredients, start=1):
        print(f"{idx}: {ingredient}")

    selections = input("Enter the numbers of the ingredients you'd like to search for (separated by spaces): ").split()
    if not all(s.isnumeric() and 1 <= int(s) <= len(all_ingredients) for s in selections):
        print("Invalid selection.")
        return

    search_ingredients = [all_ingredients[int(s) - 1] for s in selections]
    conditions = [Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients]

    recipes = session.query(Recipe).filter(*conditions).all()
    if recipes:
        for recipe in recipes:
            print(recipe)
    else:
        print("No recipes found with the selected ingredients.")

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for id, name in results:
        print(f"{id}: {name}")

    recipe_id = input("Enter the ID of the recipe you'd like to edit: ")
    if not recipe_id.isnumeric() or not session.query(Recipe).filter_by(id=int(recipe_id)).first():
        print("Invalid ID.")
        return

    recipe_to_edit = session.query(Recipe).get(int(recipe_id))
    print(f"1. Name: {recipe_to_edit.name}\n2. Ingredients: {recipe_to_edit.ingredients}\n3. Cooking Time: {recipe_to_edit.cooking_time}")

    choice = input("Which attribute would you like to edit (1/2/3)? ")
    if choice == "1":
        new_name = input("Enter the new name: ")
        recipe_to_edit.name = new_name
    elif choice == "2":
        ingredients = []
        num_ingredients = input("How many ingredients does this recipe have? ")
        while not num_ingredients.isnumeric():
            num_ingredients = input("Invalid input. Please enter a numeric value: ")
        for _ in range(int(num_ingredients)):
            ingredients.append(input("Enter an ingredient: "))
        recipe_to_edit.ingredients = ", ".join(ingredients)
    elif choice == "3":
        new_time = input("Enter the new cooking time: ")
        while not new_time.isnumeric():
            new_time = input("Invalid input. Please enter a numeric value: ")
        recipe_to_edit.cooking_time = int(new_time)
    else:
        print("Invalid choice.")
        return

    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")

def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes available.")
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for id, name in results:
        print(f"{id}: {name}")

    recipe_id = input("Enter the ID of the recipe you'd like to delete: ")
    if not recipe_id.isnumeric() or not session.query(Recipe).filter_by(id=int(recipe_id)).first():
        print("Invalid ID.")
        return

    recipe_to_delete = session.query(Recipe).get(int(recipe_id))
    confirmation = input(f"Are you sure you want to delete the recipe '{recipe_to_delete.name}'? (yes/no): ").lower()
    if confirmation == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Deletion canceled.")

# Main Menu
while True:
    print("\nRecipe Manager")
    print("1. Create a new recipe")
    print("2. View all recipes")
    print("3. Search for a recipe by ingredients")
    print("4. Edit a recipe")
    print("5. Delete a recipe")
    print("Type 'quit' to exit the application")

    choice = input("Enter your choice: ").lower()
    if choice == "1":
        create_recipe()
    elif choice == "2":
        view_all_recipes()
    elif choice == "3":
        search_by_ingredients()
    elif choice == "4":
        edit_recipe()
    elif choice == "5":
        delete_recipe()
    elif choice == "quit":
        session.close()
        engine.dispose()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")