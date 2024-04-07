# task1_2.py

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import cx_Oracle

def hire_employee():
    def hire():
        # Get the data from the entry fields
        first_name_value = first_name.get()
        last_name_value = last_name.get()
        email_value = email.get()
        phone_value = phone.get()
        hire_date_value = hire_date.get()
        salary_value = salary.get()
        job_id_value = job_id.get()
        manager_value = manager.get()
        department_value = department.get()

        # Retrieve the department ID based on the selected department
        department_ids = {
            "Administration": 10,
            "Marketing": 20
        }
        department_id = department_ids.get(department_value)
        
        connection = None
        username = 'COMP214_W24_ers_77'
        password = 'passwords'
        dsn = '199.212.26.208:1521/SQLD'
        encoding = 'UTF-8'
        
        try:
            connection = cx_Oracle.connect(username, password, dsn, encoding=encoding)
        
            cursor = connection.cursor()
            
            cursor.callproc('Employee_hire_sp', (first_name_value, last_name_value, email_value, phone_value, 
                                                 hire_date_value, salary_value, job_id_value, 
                                                 manager_value, department_value))
            connection.commit()

            print("Employee record created successfully!")

        except cx_Oracle.Error as error:
            print(f"Error creating procedure: {error}")
        finally:
            if connection:
                connection.close()


    hire_window = tk.Toplevel()
    hire_window.title("Employee Hiring Form")

    labels = ["First Name", "Last Name:", "Email", "Phone", "Hire Date: ",  "Salary: ", "Job ID", "Manager", "Department"]
    for i, label_text in enumerate(labels):
        label = tk.Label(hire_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    # Variables to store entry values
    first_name = tk.StringVar()
    last_name = tk.StringVar()
    email = tk.StringVar()
    phone = tk.StringVar()
    hire_date = tk.StringVar(value=date.today())
    salary = tk.StringVar()
    job_id = tk.StringVar()
    manager = tk.StringVar()
    department = tk.StringVar()

    # Entry fields
    entries = [
        ttk.Entry(hire_window, textvariable=first_name),
        ttk.Entry(hire_window, textvariable=last_name),
        ttk.Entry(hire_window, textvariable=email),
        ttk.Entry(hire_window, textvariable=phone),
        ttk.Entry(hire_window, textvariable=hire_date),
        ttk.Entry(hire_window, textvariable=salary),
    ]
    for i, entry in enumerate(entries):
        entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

    # Dropdown for Job
    jobs = {
        "ACCOUNTANT": "FI_ACCOUNT",
        "Sales Representative": "SA_REP",
        "Sales Manager": "SA_MAN"
    }
    job_dropdown = ttk.Combobox(hire_window, textvariable=job_id, values=list(jobs.keys()), state="readonly", width=20)
    job_dropdown.grid(row=len(labels)-3, column=1, padx=10, pady=5, sticky=tk.W)

    # Dropdown for Manager
    managers = ["100", "101"]  # List of managers
    manager_dropdown = ttk.Combobox(hire_window, textvariable=manager, values=managers, state="readonly", width=20)
    manager_dropdown.grid(row=len(labels)-2, column=1, padx=10, pady=5, sticky=tk.W)

    # Dropdown for Department
    departments = ["75", "77"]
    department_dropdown = ttk.Combobox(hire_window, textvariable=department, values=departments, state="readonly", width=20)
    department_dropdown.grid(row=len(labels)-1, column=1, padx=10, pady=5, sticky=tk.W)

    hire_button = tk.Button(hire_window, text="Hire", command=hire, bd=3)
    hire_button.grid(row=len(labels), columnspan=2, pady=10)



def create_menu():
    root = tk.Tk()
    root.title("HR Application")
    root.geometry("500x300")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    employee_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Employee Main Menu", menu=employee_menu)
    employee_menu.add_command(label="Hire Employee", command=hire_employee)
    employee_menu.add_command(label="List and Update Employees", command=list_update_employees)
    
    jobs_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Jobs Main Menu", menu= jobs_menu)
    jobs_menu.add_command(label="Job Types", command=hire_employee)
    jobs_menu.add_command(label="Placeholder", command=hire_employee)
    
    dept_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Departments Main Menu", menu= dept_menu)
    dept_menu.add_command(label="Department Types", command=hire_employee)
    dept_menu.add_command(label="Placeholder", command=hire_employee)
    
    

    root.mainloop()

#Task1_3
def list_update_employees():
    list_window = tk.Toplevel()
    list_window.title("List and Update Employees")

    tree = ttk.Treeview(list_window, columns=("First Name", "Last Name", "Email", "Phone", "Hire Date", "Salary", "Job ID", "Manager", "Department"))
    tree.heading("#0", text="Employee ID")
    tree.heading("#1", text="First Name")
    tree.heading("#2", text="Last Name")
    tree.heading("#3", text="Email")
    tree.heading("#4", text="Phone")
    tree.heading("#5", text="Hire Date")
    tree.heading("#6", text="Salary")
    tree.heading("#7", text="Job ID")
    tree.heading("#8", text="Manager")
    tree.heading("#9", text="Department")
    tree.pack()

    def update_employee():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an employee to update.")
            return

        
        employee_id = tree.item(selected_item)['text']

        update_window = tk.Toplevel(list_window)
        update_window.title("Update Employee")


        try:
            username = 'COMP214_W24_ers_77'
            password = 'passwords'
            dsn = '199.212.26.208:1521/SQLD'

            connection = cx_Oracle.connect(username, password, dsn)
            cursor = connection.cursor()

            
            cursor.execute("SELECT * FROM Employees WHERE employee_id = :id", {"id": employee_id})
            employee_data = cursor.fetchone()

            
            labels = ["First Name", "Last Name:", "Email", "Phone", "Hire Date: ",  "Salary: ", "Job ID", "Manager", "Department"]
            for i, label_text in enumerate(labels):
                label = tk.Label(update_window, text=label_text)
                label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            
            first_name = tk.StringVar(value=employee_data[1])
            last_name = tk.StringVar(value=employee_data[2])
            email = tk.StringVar(value=employee_data[3])
            phone = tk.StringVar(value=employee_data[4])
            hire_date = tk.StringVar(value=employee_data[5])
            salary = tk.StringVar(value=employee_data[6])
            job_id = tk.StringVar(value=employee_data[7])
            manager = tk.StringVar(value=employee_data[8])
            department = tk.StringVar(value=employee_data[9])

            
            entries = [
                ttk.Entry(update_window, textvariable=first_name),
                ttk.Entry(update_window, textvariable=last_name),
                ttk.Entry(update_window, textvariable=email),
                ttk.Entry(update_window, textvariable=phone),
                ttk.Entry(update_window, textvariable=hire_date),
                ttk.Entry(update_window, textvariable=salary),
            ]
            for i, entry in enumerate(entries):
                entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)

            
            jobs = {
                "ACCOUNTANT": "FI_ACCOUNT",
                "Sales Representative": "SA_REP",
                "Sales Manager": "SA_MAN"
            }
            job_dropdown = ttk.Combobox(update_window, textvariable=job_id, values=list(jobs.keys()), state="readonly", width=20)
            job_dropdown.grid(row=len(labels)-3, column=1, padx=10, pady=5, sticky=tk.W)

            
            managers = ["100", "101"]  
            manager_dropdown = ttk.Combobox(update_window, textvariable=manager, values=managers, state="readonly", width=20)
            manager_dropdown.grid(row=len(labels)-2, column=1, padx=10, pady=5, sticky=tk.W)

            
            departments = ["75", "77"]
            department_dropdown = ttk.Combobox(update_window, textvariable=department, values=departments, state="readonly", width=20)
            department_dropdown.grid(row=len(labels)-1, column=1, padx=10, pady=5, sticky=tk.W)

            def save_changes():
               
                try:
                    cursor.execute("""
                        UPDATE HR_Employees 
                        SET first_name = :first, last_name = :last, email = :email, phone = :phone, 
                        hire_date = :hire, salary = :salary, job_id = :job, manager_id = :manager, 
                        department_id = :department
                        WHERE employee_id = :id""",
                        {
                            "first": first_name.get(),
                            "last": last_name.get(),
                            "email": email.get(),
                            "phone": phone.get(),
                            "hire": hire_date.get(),
                            "salary": salary.get(),
                            "job": job_id.get(),
                            "manager": manager.get(),
                            "department": department.get(),
                            "id": employee_id
                        }
                    )
                    connection.commit()
                    messagebox.showinfo("Success", "Employee record updated successfully!")
                    update_window.destroy()
                except cx_Oracle.Error as error:
                    messagebox.showerror("Error", f"Error updating employee record: {error}")

           
            save_button = tk.Button(update_window, text="Save Changes", command=save_changes)
            save_button.grid(row=len(labels), columnspan=2, pady=10)

        except cx_Oracle.Error as error:
            messagebox.showerror("Error", f"Error fetching employee data: {error}")

        finally:
            if connection:
                connection.close()

   
    update_button = tk.Button(list_window, text="Update", command=update_employee)
    update_button.pack()

    try:
        username = 'COMP214_W24_ers_77'
        password = 'passwords'
        dsn = '199.212.26.208:1521/SQLD'

        connection = cx_Oracle.connect(username, password, dsn)
        cursor = connection.cursor()

       
        cursor.execute("SELECT * FROM HR_Employees")

        for row in cursor.fetchall():
            tree.insert("", "end", text=row[0], values=row[1:])

    except cx_Oracle.Error as error:
        messagebox.showerror("Error", f"Error fetching employees: {error}")

    finally:
        if connection:
            connection.close()
    

if __name__ == "__main__":
    create_menu()