class Recipe:
    all_ingredients = set()

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cooking_time(self, time):
        self.cooking_time = time
        self.calculate_difficulty()

    def get_cooking_time(self):
        return self.cooking_time

    def add_ingredients(self, *args):
        self.ingredients.extend(args)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10:
            if len(self.ingredients) < 4:
                self.difficulty = "Easy"
            else:
                self.difficulty = "Medium"
        else:
            if len(self.ingredients) < 4:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"

    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    def __str__(self):
        return (f"Recipe: {self.name}\n"
                f"Ingredients: {', '.join(self.ingredients)}\n"
                f"Cooking Time: {self.cooking_time} minutes\n"
                f"Difficulty: {self.difficulty}")

    def recipe_search(data, search_term):
        print(f"Searching for recipes with ingredient: {search_term}\n")
        found = False
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)
                print("\n")
                found = True
        if not found:
            print(f"No recipes found with the ingredient: {search_term}\n")

def main():
    tea = Recipe("Tea")
    tea.add_ingredients("Tea Leaves", "Sugar", "Water")
    tea.set_cooking_time(5)

    coffee = Recipe("Coffee")
    coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
    coffee.set_cooking_time(5)

    cake = Recipe("Cake")
    cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
    cake.set_cooking_time(50)

    banana_smoothie = Recipe("Banana Smoothie")
    banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
    banana_smoothie.set_cooking_time(5)

    recipes_list = [tea, coffee, cake, banana_smoothie]

    for recipe in recipes_list:
        print(recipe)
        print("\n")

    Recipe.recipe_search(recipes_list, "Water")
    Recipe.recipe_search(recipes_list, "Sugar")
    Recipe.recipe_search(recipes_list, "Bananas")

if __name__ == "__main__":
    main()