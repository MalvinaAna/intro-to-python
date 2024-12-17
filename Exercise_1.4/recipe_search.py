import pickle

def display_recipe(recipe):
    print("\nRecipe Details:")
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}\n")

def search_ingredient(data):
    all_ingredients = data.get("all_ingredients", [])
    recipes_list = data.get("recipes_list", [])

    if not all_ingredients:
        print("No ingredients available to search.")
        return

    print("\nAvailable Ingredients:")
    for index, ingredient in enumerate(all_ingredients):
        print(f"{index + 1}. {ingredient}")

    try:
        choice = int(input("\nEnter the number of the ingredient you'd like to search for: "))
        if 1 <= choice <= len(all_ingredients):
            ingredient_searched = all_ingredients[choice - 1]
            print(f"\nSearching for recipes containing: {ingredient_searched}")
        else:
            print("Invalid selection. Please choose a valid number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    matching_recipes = [recipe for recipe in recipes_list if ingredient_searched in recipe['ingredients']]

    if matching_recipes:
        print(f"\nRecipes containing '{ingredient_searched}':")
        for recipe in matching_recipes:
            display_recipe(recipe)
    else:
        print(f"No recipes found containing the ingredient '{ingredient_searched}'.")

def main():
    print("Welcome to the Recipe Search Script!")
    filename = input("Enter the filename containing your recipe data: ").strip()

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            print("File loaded successfully!")
    except FileNotFoundError:
        print("Error: File not found. Please make sure the file exists and try again.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    else:
        search_ingredient(data)

    print("\nThank you for using the Recipe Search Script!")

if __name__ == "__main__":
    main()
