import pickle

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

def take_recipe():
    print("\nEnter Recipe Details")
    name = input("Recipe name: ").strip()
    valid_input = False
    while not valid_input:
        try:
            cooking_time = int(input("Cooking time (in minutes): "))
            valid_input = True
        except ValueError:
            print("Please enter a valid integer for cooking time.")

    ingredients = input("Enter ingredients (comma-separated): ").strip().split(',')
    ingredients = [ingredient.strip().lower() for ingredient in ingredients if ingredient.strip()]
    
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }
    return recipe

def main():
    print("Welcome to the Recipe Input Script!")
    filename = input("Enter the filename to save or load recipes: ").strip()

    data = {"recipes_list": [], "all_ingredients": []}
    recipes_list = []
    all_ingredients = []

    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            print("File loaded successfully!")
    except FileNotFoundError:
        print("File not found. Creating a new file...")
        data = {"recipes_list": [], "all_ingredients": []}
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Creating a new file...")
        data = {"recipes_list": [], "all_ingredients": []}
    else:
        print("File contains existing recipes.")
    finally:
        recipes_list = data.get("recipes_list", [])
        all_ingredients = data.get("all_ingredients", [])

    num_recipes = -1
    while num_recipes < 1:
        try:
            num_recipes = int(input("How many recipes would you like to add? "))
            if num_recipes < 1:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

    for _ in range(num_recipes):
        recipe = take_recipe()
        recipes_list.append(recipe)
        
        for ingredient in recipe['ingredients']:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

    try:
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
            print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Failed to save data: {e}")

    print("\nThank you for using the Recipe Input Script!")

if __name__ == "__main__":
    main()