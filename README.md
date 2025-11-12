---

# 🐍 Python Projects Portfolio

This repository contains Python projects and assignments completed during The Tech Academy Software Developer Bootcamp. These projects demonstrate foundational and intermediate skills in Python, using modules such as `tkinter`, `sqlite3`, and the Django web framework.

## 📁 Projects Overview
*Note: This overview highlights selected projects that best demonstrate my Python development skills. It does not include every assignment completed during the bootcamp, but feel free to explore the rest in this repository!*

### 🏨 Django Royal Hotel
A hotel website built with Django that allows admins to manage menu items and users to browse and purchase offerings.

**Features:**
- Admin interface for adding and deleting products  
- User-facing product display and purchase simulation  
- Page templates:
  - `home.html`
  - `products_page.html`
  - `createRecord.html`
  - `present_product.html`
  - `confirmDelete.html`

### 🎓 Django University
A Django-based system for managing university classes and campuses.

**Apps and Models:**
- `classApp` → `UniversityClasses` model:
  - Title (string)
  - Course Number (integer)
  - Instructor Name (string)
  - Duration (float)

- `campusApp` → `UniversityCampus` model:
  - Campus Name (string)
  - State (2-character string)
  - Campus ID (integer)

**Features:**
- Add and display university classes  
- Add and display campus details  

### 💰 Django Checkbook
A personal finance tracker built with Django for managing bank accounts and transactions.

**Features:**
- Create accounts with name and starting balance  
- Add transactions (deposit/withdrawal) with:
  - Date
  - Type
  - Amount
  - Description
  - Associated account
- View account balances and transaction history  
- Dropdown menu for selecting accounts  

### 📞 Phonebook App
  A desktop phonebook application using Tkinter and SQLite.
  
  **Features:**
  - Add, update, and delete contacts  
  - Store name, phone number, and email  
  - Persistent local database  

### 🎓 Student Tracking App
A student management system built with Tkinter and SQLite.

**Features:**
- Add and delete student records  
- Store name, phone number, email, and current course  
- Display all student data in a list view  

---

## 🧰 Tech Stack

- Python 3  
- Tkinter  
- SQLite3  
- Django (MVC framework)

---

## 🚀 Getting Started

To run any project locally:

```bash
git clone https://github.com/your-username/python-projects.git
cd python-projects
```

Then navigate to the desired project folder and follow its setup instructions (e.g., `python manage.py runserver` for Django apps).

---

## 📂 Project File Paths

```
/Python_Projects/techproject           → Django Royal Hotel
/Django_Checkbook_Project              → Django Checkbook
/DjangoUniversity                      → Django University
/project_phonebook                     → Phonebook App
/Student_Tracking_Assignment           → Student Tracking App
```

---

## 🙌 Acknowledgments

These projects were built as part of my journey to master Python development. Feedback and collaboration are always welcome!

---
