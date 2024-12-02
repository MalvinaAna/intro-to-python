# into-to-python

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