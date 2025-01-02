# intro-to-python

## **Objective**
This project is a command-line Recipe app designed to manage, store, and search for recipes. It serves as a foundation for a future web app, focusing on Python fundamentals, object-oriented programming, and database interaction.

---

## **Features**
- Manage recipes with ingredients, cooking time, and difficulty.
- Search for recipes based on specified ingredients.
- Automatically calculate and display recipe difficulty.

---

## **Technical Requirements**
- Python 3.6+ installed locally.
- Ability to handle user-friendly error messages for common input errors.
- Interaction with locally hosted MySQL databases (to be implemented in later exercises).
- Well-structured and documented code with meaningful comments.

---

## **Setup**
1. **Install Python 3.6+**  
   - Download and install Python from [python.org](https://www.python.org/).

2. **Set up a Virtual Environment**  
   - Create and activate a virtual environment:
     ```bash
     python -m venv myenv
     source myenv/bin/activate  # For macOS/Linux
     myenv\Scripts\activate.bat  # For Windows
     ```

3. **Install Required Packages**  
   - Use `pip` to install necessary dependencies (defined later in the `requirements.txt` file):
     ```bash
     pip install -r requirements.txt
     ```

---

## **Exercises Structure**

### **Exercise 1: Intro to Python Programming**
- Installed Python on macOS, Windows, and Linux.
- Created and managed virtual environments.
- Used `pip` to install and manage Python packages.

### **Exercise 2: Data Structures for Recipe Management**

#### **Storing Recipe Data**
To represent the attributes of a recipe, a **dictionary** is the most suitable data structure. Each recipe is stored as a dictionary, where the keys represent the attributes (e.g., "name," "cooking_time," and "ingredients") and the values contain the corresponding information. 

This approach allows for:
- **Clear attribute representation**: Dictionary keys explicitly describe each attribute, making the structure self-documenting.
- **Ease of access and modification**: Values can be easily retrieved or updated by referring to their corresponding keys.

Example:
```python
recipe = {
    "name": "Pasta Alfredo",
    "cooking_time": 30,
    "ingredients": ["pasta", "cream", "parmesan", "butter"]
}
```

### **Exercise 3: Functions and Other Operations in Python**
In this exercise, we created our first script in Python as a `.py` file. The script uses `if-elif-else` statements, loops, and functions to build a command-line interface for adding recipes and displaying them.

The script:
- Asks the user for recipe details such as name, cooking time, and ingredients.
- Uses functions to store recipes and display them in a readable format.
- Includes input validation to ensure the data entered is correct.

### **Exercise 4: File Handling in Python**
Here, we explored reading and writing data to files using Python's file handling features. The project included:
- A script to collect recipes from the user and save them in a binary file.
- Another script to read the binary file and list all available ingredients.
- The user could select an ingredient to display recipes containing it.
- We implemented exception handling to manage common errors, such as file not found or invalid data.

### **Exercise 5: Object-Oriented Programming in Python**
This exercise introduced object-oriented programming. We:
- Built a custom `Recipe` class with attributes for name, cooking time, ingredients, and difficulty.
- Added methods to calculate the difficulty of a recipe based on cooking time and the number of ingredients.
- Implemented methods for displaying recipe details and returning ingredients as a list.

### **Exercise 6: Connecting to Databases in Python**
In this exercise, we connected our Python scripts to a MySQL database. The app was extended to:
- Create, read, update, and delete recipes stored in the database.
- Search for recipes by a single ingredient.
- Use SQL queries for efficient data retrieval and manipulation.

### **Exercise 7: Finalizing Your Python Program**
The final exercise brought all the components together to build a complete application. We:
- Used SQLAlchemy as an Object Relational Mapper (ORM) to simplify database interactions.
- Designed a user-friendly menu for entering, searching, and managing recipes and ingredients.
- Stored recipe and ingredient data in a MySQL database.
- Implemented a feature for searching recipes by user-defined ingredients.
- Enhanced the display of recipes, showing detailed information for the selected recipe.

With these features, the app is now a functional command-line tool for managing recipes efficiently.