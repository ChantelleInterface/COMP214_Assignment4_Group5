import tkinter as tk
from tkinter import messagebox
import mysql.connector

def create_job():

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

# Create the Tkinter window
root = tk.Tk()
root.title("Create Job")

labels = ['Job ID', 'Title', 'Minimum Salary']
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

entry_job_id = tk.Entry(root)
entry_job_id.grid(row=0, column=1, padx=10, pady=5)

entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1, padx=10, pady=5)

entry_min_salary = tk.Entry(root)
entry_min_salary.grid(row=2, column=1, padx=10, pady=5)

create_button = tk.Button(root, text="CREATE JOB", command=create_job)
create_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
