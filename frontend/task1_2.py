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

# Task2_1
def identify_job_description():
    def search_job():
        job_id_value = job_id_entry.get()

        connection = None
        username = 'COMP214_W24_ers_77'
        password = 'passwords'
        dsn = '199.212.26.208:1521/SQLD'
        encoding = 'UTF-8'

        try:
            connection = cx_Oracle.connect(username, password, dsn, encoding=encoding)
            cursor = connection.cursor()

            cursor.execute("SELECT job_title FROM jobs WHERE job_id = :job_id", {"job_id": job_id_value})
            result = cursor.fetchone()

            if result:
                job_description_label.config(text=result[0])
            else:
                job_description_label.config(text="Job ID not found")

        except cx_Oracle.Error as error:
            print(f"Error retrieving job description: {error}")
        finally:
            if connection:
                connection.close()

    identify_job_window = tk.Toplevel()
    identify_job_window.title("Identify Job Description")
    identify_job_window.geometry("400x200")  

    job_id_label = tk.Label(identify_job_window, text="Enter Job ID:")
    job_id_label.pack(pady=10)

    job_id_entry = tk.Entry(identify_job_window)
    job_id_entry.pack(pady=5)

    search_button = tk.Button(identify_job_window, text="Search", command=search_job)
    search_button.pack(pady=10)

    job_description_label = tk.Label(identify_job_window, text="")
    job_description_label.pack(pady=10)

def create_job():
    def create():
        job_id = entry_job_id.get()
        title = entry_title.get()
        min_salary = float(entry_min_salary.get())
        max_salary = min_salary * 2

        # Connect to MySQL database
        try:
            conn = mysql.connector.connect(
            connection = None,
            user="COMP214_W24_ers_77",
            password="passwords",
            dsn = "199.212.26.208:1521/SQLD",
            encoding = "UTF-8"
            )
            cursor = conn.cursor()

            # Call the stored procedure
            cursor.callproc('new_job', (job_id, title, min_salary, max_salary))
            conn.commit()

            messagebox.showinfo("Success", "A new job has been created")

            entry_job_id.delete(0, tk.END)
            entry_title.delete(0, tk.END)
            entry_min_salary.delete(0, tk.END)

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            cursor.close()
            conn.close()

    create_job_window = tk.Toplevel()
    create_job_window.title("Create Job")

    labels = ['Job ID', 'Title', 'Minimum Salary']
    for i, label_text in enumerate(labels):
        label = tk.Label(create_job_window, text=label_text)
        label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entry_job_id = tk.Entry(create_job_window)
    entry_job_id.grid(row=0, column=1, padx=10, pady=5)

    entry_title = tk.Entry(create_job_window)
    entry_title.grid(row=1, column=1, padx=10, pady=5)

    entry_min_salary = tk.Entry(create_job_window)
    entry_min_salary.grid(row=2, column=1, padx=10, pady=5)

    create_button = tk.Button(create_job_window, text="CREATE JOB", command=create)
    create_button.grid(row=3, columnspan=2, padx=10, pady=10)

def create_menu():
    root = tk.Tk()
    root.title("HR Application")
    root.geometry("500x300")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    employee_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Employee Main Menu", menu=employee_menu)
    employee_menu.add_command(label="Hire Employee", command=hire_employee)
    employee_menu.add_command(label="Placeholder", command=hire_employee)
    
    jobs_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Jobs Main Menu", menu= jobs_menu)
    jobs_menu.add_command(label="Identify JOB Description", command=identify_job_description)
    jobs_menu.add_command(label="Create Job", command=create_job)
    
    dept_menu = tk.Menu(menubar, tearoff=False)
    menubar.add_cascade(label="Departments Main Menu", menu= dept_menu)
    dept_menu.add_command(label="Department Types", command=create_job)
    dept_menu.add_command(label="Placeholder", command=hire_employee)

    root.mainloop()

if __name__ == "__main__":
    create_menu()