import tkinter as tk
from tkinter import ttk
import sqlite3

# SQLite database file
DB_FILE = "pet_database.db"

class Pet:
    def __init__(self, name, age, pet_type):
        self.name = name
        self.age = age
        self.pet_type = pet_type

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_type(self, pet_type):
        self.pet_type = pet_type

    def get_type(self):
        return self.pet_type


class PetManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Management System")

        # Connect to SQLite database
        self.conn = sqlite3.connect(DB_FILE)
        self.cur = self.conn.cursor()

        # Create pets table if not exists
        self.create_table()

        # Entry widgets for input
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.type_var = tk.StringVar()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root, textvariable=self.name_var, width=20)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(root, textvariable=self.age_var, width=20)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.type_label = tk.Label(root, text="Type:")
        self.type_label.grid(row=2, column=0, padx=10, pady=10)
        self.type_entry = tk.Entry(root, textvariable=self.type_var, width=20)
        self.type_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.create_button = tk.Button(root, text="Create Pet", width=15, command=self.create_pet)
        self.create_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.display_button = tk.Button(root, text="Display Pet Info", width=15, command=self.display_info)
        self.display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.result_var = tk.StringVar()
        self.result_label = tk.Label(root, textvariable=self.result_var, font=('Arial', 12), wraplength=300)
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Add a tab for displaying all pets
        self.tab_control = ttk.Notebook(root)
        self.tab_control.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.all_pets_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.all_pets_tab, text='All Pets')

        self.pet_listbox = tk.Listbox(self.all_pets_tab, width=40, height=10, font=('Arial', 12))
        self.pet_listbox.pack(padx=10, pady=10)

        self.load_all_pets()

        self.root.mainloop()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                name TEXT,
                age INTEGER,
                pet_type TEXT
            )
        ''')
        self.conn.commit()

    def create_pet(self):
        name = self.name_var.get()
        age = self.age_var.get()
        pet_type = self.type_var.get()

        if name and age and pet_type:
            self.cur.execute('INSERT INTO pets VALUES (?, ?, ?)', (name, age, pet_type))
            self.conn.commit()
            self.result_var.set("Pet created successfully!")
            self.load_all_pets()
        else:
            self.result_var.set("Please enter all fields.")

    def display_info(self):
        self.result_var.set("")  # Clear previous result
        name = self.name_var.get()

        if name:
            self.cur.execute('SELECT * FROM pets WHERE name=?', (name,))
            pet = self.cur.fetchone()
            if pet:
                info = f"Name: {pet[0]}\nAge: {pet[1]}\nType: {pet[2]}"
                self.result_var.set(info)
            else:
                self.result_var.set("Pet not found.")
        else:
            self.result_var.set("Please enter a pet name.")

    def load_all_pets(self):
        self.pet_listbox.delete(0, tk.END)
        self.cur.execute('SELECT * FROM pets')
        pets = self.cur.fetchall()
        for pet in pets:
            pet_info = f"Name: {pet[0]}, Age: {pet[1]}, Type: {pet[2]}"
            self.pet_listbox.insert(tk.END, pet_info)

    def __del__(self):
        self.conn.close()


def main():
    root = tk.Tk()
    app = PetManagementGUI(root)

if __name__ == "__main__":
    main()
