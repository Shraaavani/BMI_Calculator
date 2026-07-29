import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# ---------------- DATABASE ---------------- #

try:
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        weight REAL,
        height REAL,
        bmi REAL,
        date TEXT
    )
    """)

    conn.commit()

except sqlite3.Error as e:
    messagebox.showerror("Database Error", str(e))


# ---------------- BMI FUNCTION ---------------- #

def calculate_bmi():

    try:

        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if name == "":
            raise ValueError("Enter your name.")

        if weight <= 0 or height <= 0:
            raise ValueError("Values must be positive.")

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"

        elif bmi < 25:
            category = "Normal"
            color = "green"

        elif bmi < 30:
            category = "Overweight"
            color = "orange"

        else:
            category = "Obese"
            color = "red"

        result.config(
            text=f"BMI : {bmi}\nCategory : {category}",
            fg=color
        )

        try:
            cursor.execute("""
            INSERT INTO bmi_records(name,weight,height,bmi,date)
            VALUES(?,?,?,?,?)
            """,
                           (
                               name,
                               weight,
                               height,
                               bmi,
                               datetime.now().strftime("%Y-%m-%d %H:%M")
                           ))

            conn.commit()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


def clear_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result.config(text="", fg="black")



# ---------------- GRAPH ---------------- #

def show_graph():

    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Enter user name")
        return

    try:

        cursor.execute("""
        SELECT date,bmi FROM bmi_records
        WHERE name=?
        ORDER BY id
        """, (name,))

        data = cursor.fetchall()

        if len(data) == 0:
            messagebox.showinfo("Info", "No records found.")
            return

        dates = [x[0] for x in data]
        bmi = [x[1] for x in data]

        plt.figure(figsize=(8,4))
        plt.plot(dates, bmi, marker="o")
        plt.title(f"{name}'s BMI Trend")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))


# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("420x380")
window.resizable(False, False)

title = tk.Label(window,
                 text="BMI Calculator",
                 font=("Arial",18,"bold"))
title.pack(pady=10)

tk.Label(window,text="Name").pack()

name_entry = tk.Entry(window,width=30,justify="center")
name_entry.pack()

tk.Label(window,text="Weight (kg)").pack(pady=5)

weight_entry = tk.Entry(window,width=30,justify="center")
weight_entry.pack()

tk.Label(window,text="Height (m)").pack(pady=5)

height_entry = tk.Entry(window,width=30,justify="center")
height_entry.pack()

tk.Button(
    window,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="lightgreen",
    width=18
).pack(pady=5)

tk.Button(
    window,
    text="Show BMI Trend",
    command=show_graph,
    bg="lightblue",
    width=18
).pack(pady=5)

result = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold")
)
result.pack(pady=8)

tk.Button(
    window,
    text="Clear",
    command=clear_fields,
    bg="lightgray",
    width=18
).pack(pady=5)

window.mainloop()