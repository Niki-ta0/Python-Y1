# Python-Y1
# Python-Y1
# Land Rental System – Techno Property Nepal

This project is a beginner-friendly Python-based **Land Rental Management System** developed for Techno Property Nepal. It allows users to **rent** and **return** land via a text-based interface. The system handles invoice generation, availability tracking, and fine calculation using `.txt` files for data storage.

---

## Features

-  View available lands (kitta no., address, direction, area, price).
-  Rent land and generate a rental invoice.
-  Return rented land with fine calculation (if returned late).
-  Auto-updates land availability in file.
-  Input validation for phone number, kitta no., and other fields.
-  Data stored using Python 2D lists in `.txt` format.
-  Modular design using:
  - `main.py`
  - `operation.py`
  - `read_file.py`
  - `write_file.py`

---

##  Fine Policy

- If the land is **returned after the agreed rental duration**, a **10% fine per extra month** is charged based on the land price.
- If the land is returned **on time or earlier**, **no fine** is applied.
- All fines and totals are shown in the return invoice.

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Place `Coursework.txt` in the same folder as the code files.
3. Run the system using:
   ```bash
   python main.py
