# task1_2.py

import tkinter as tk
from tkinter import messagebox

def hire_employee():
    # Implement the logic to call the stored procedure and insert employee data here


    # Assuming the procedure inserts successfully:
    messagebox.showinfo("Success", "Employee hired successfully!")

def create_menu():
    root = tk.Tk()
    root.title("HR Application")
    root.geometry("500x300")

    # Create a menu bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    # Create Employee Main Menu
    employee_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Employee Main Menu", menu=employee_menu)
    
    # Add menu items 
    employee_menu.add_command(label="Hire Employee", command=hire_employee)
    employee_menu.add_command(label="Placeholder", command=hire_employee)
    
    # Create Employee Main Menu
    jobs_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Jobs Main Menu", menu= jobs_menu)
    
    # Add menu items 
    jobs_menu.add_command(label="Job Types", command=hire_employee)
    jobs_menu.add_command(label="Placeholder", command=hire_employee)
    
    # Create Departments Main Menu
    dept_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Departments Main Menu", menu= dept_menu)
    
    # Add menu items 
    dept_menu.add_command(label="Department Types", command=hire_employee)
    dept_menu.add_command(label="Placeholder", command=hire_employee)

    
    

    root.mainloop()

if __name__ == "__main__":
    create_menu()
