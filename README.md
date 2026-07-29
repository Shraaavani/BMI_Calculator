# 🩺 BMI Calculator (Python GUI)

A user-friendly **Body Mass Index (BMI) Calculator** built with **Python**, featuring a graphical user interface (GUI), BMI classification, SQLite database storage, and BMI trend visualization using Matplotlib.

This application allows multiple users to calculate and store their BMI records, making it easy to monitor health progress over time.

---

## 📌 Features

- ✅ Interactive GUI built with Tkinter
- ✅ Calculate BMI using weight and height
- ✅ Automatic BMI classification:
  - Underweight
  - Normal Weight
  - Overweight
  - Obese
- ✅ Color-coded BMI result
- ✅ Multi-user support
- ✅ Store BMI history in SQLite database
- ✅ Display BMI trend graph using Matplotlib
- ✅ Input validation and error handling
- ✅ Clear input fields with one click

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter
- SQLite3
- Matplotlib

---

## 📂 Project Structure

```
BMI_Calculator/
│
├── bmi_calculator.py      # Main application
├── bmi.db                 # SQLite database
├── README.md
└── screenshots/           # (Optional) Project screenshots
```

---

## 🧮 BMI Formula

```
BMI = Weight (kg) / Height² (m²)
```

### BMI Categories

| BMI Range | Category |
|------------|-----------|
| Less than 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25 – 29.9 | Overweight |
| 30 and above | Obese |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/BMI_Calculator.git
```

### 2. Navigate to the Project Folder

```bash
cd BMI_Calculator
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install matplotlib
```

### 6. Run the Application

```bash
python bmi_calculator.py
```

---

## 📊 How It Works

1. Enter your name.
2. Enter your weight (kg).
3. Enter your height (m).
4. Click **Calculate BMI**.
5. View your BMI value and health category.
6. Your record is automatically saved to the SQLite database.
7. Click **Show BMI Trend** to visualize your BMI history.

---

## 💾 Database

The application uses an **SQLite database (`bmi.db`)** to store:

- Name
- Weight
- Height
- BMI
- Date & Time

This enables users to track BMI history over multiple sessions.

---

## 📈 BMI Trend Visualization

The application generates a line graph using **Matplotlib** to display BMI changes over time for each user.

---

## ⚠️ Input Validation

The application checks for:

- Empty fields
- Non-numeric input
- Negative or zero values
- Invalid height and weight entries

Appropriate error messages are displayed using dialog boxes.

---

## 🎯 Learning Outcomes

This project demonstrates:

- GUI development using Tkinter
- Python functions and event handling
- SQLite database operations (CRUD)
- Data visualization using Matplotlib
- Input validation
- Exception handling
- Multi-user data management

---

## 🔮 Future Enhancements

- Export BMI history to CSV/PDF
- User login system
- Dark mode
- BMI health recommendations
- Diet and exercise suggestions
- Height input in feet & inches
- Delete/Edit BMI records

---

## 👩‍💻 Author

**Shravani Santosh Kamble**

- GitHub: https://github.com/Shraaavani
- LinkedIn: https://www.linkedin.com/in/shravani-kamble-9b9345346/

---

## ⭐ If you found this project helpful, consider giving it a star!