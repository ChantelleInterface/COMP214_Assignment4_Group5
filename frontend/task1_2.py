# task1_2.py

import tkinter as tk
from tkinter import ttk, messagebox

#Hire Employee 
def hire_employee():
    # Implement the logic to call the stored procedure and insert employee data here


    # Assuming the procedure inserts successfully:
    def hire():
        messagebox.showinfo("Success", "Employee hired successfully!")
    
    hire_window = tk.Toplevel()
    hire_window.title("Employee Hiring Form")


    labels = ["First Name", "Last Name:", "Email", "Phone", "Hire Date: ",  "Salary: ", "Manager: ", "Department"]
    for i, label_text in enumerate(labels):
        label = tk.Label(hire_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)


    first_name = tk.StringVar()
    last_name = tk.StringVar()
    email = tk.StringVar()
    phone= tk.StringVar()
    hire_date = tk.StringVar(value="2024-04-03")
    salary = tk.StringVar()
    manager = tk.StringVar(value="Alexander Hunold")
    department = tk.StringVar(value="Administration")


    # Entry field
    entries = [
        tk.Entry(hire_window, textvariable=first_name),
        tk.Entry(hire_window, textvariable=last_name),
        tk.Entry(hire_window, textvariable=email),
        tk.Entry(hire_window, textvariable=phone),
        tk.Entry(hire_window, textvariable=hire_date),
        tk.Entry(hire_window, textvariable=salary)        
    ]
    for i, entry in enumerate(entries):
        entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)


    managers = [
        "Alexander Hunold",
        "Nancy Greenberg"
    ]
    manager_dropdown = ttk.Combobox(hire_window, textvariable=manager, values=managers, state="readonly", width=20)
    manager_dropdown.grid(row=len(labels)-2, column=1, padx=10, pady=5, sticky=tk.W)


    departments = [
        "Administration",
        "Marketing"
    ]
    manager_dropdown = ttk.Combobox(hire_window, textvariable=department, values=departments, state="readonly", width=20)
    manager_dropdown.grid(row=len(labels)-1, column=1, padx=10, pady=5, sticky=tk.W)


    hire_button = tk.Button(hire_window, text="Hire", command=hire, bd=3)
    hire_button.grid(row=len(labels), columnspan=2, pady=10)


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
