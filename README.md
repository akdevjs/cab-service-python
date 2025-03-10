# 🚖 Cab Service System

_A simple ride-hailing service built in Python using file-based storage instead of a database!_

---

## 📌 Project Overview

This is a **basic cab booking system** where **Users** (passengers) can book rides, and **Drivers** can accept them.  
The system stores data using **Python File I/O** instead of a database.

---

## ⚡ Features

### 🧑‍💻 User Features

- 📝 **Register** with name, email, phone, password, and address.
- 🔐 **Login** securely using encrypted passwords.
- 🚕 **Book a ride** by selecting pickup and destination.
- ⭐ **Rate drivers** after a completed ride.
- 📜 **View ride history** and past trips.

### 🚗 Driver Features

- 📝 **Register** with car details (name, model, number, AC availability, category).
- 🔐 **Login** securely using encrypted passwords.
- ✅ **Accept or reject rides** based on availability.
- 💰 **Earn fares** and track ride history.
- ⭐ **Rate users** after a completed ride.

---

## 🏗 File Structure

The project follows a **file-based storage system** instead of using databases.

```md
📂 cab-service/
│── 📂 utils/ # Helper functions (encryption, file handling)
│── 📂 data/ # Stores all user, driver, and ride data
│ ├── users.txt # Stores registered users
│ ├── drivers.txt # Stores registered drivers
│ ├── rides.txt # Stores ride history
│── main.py # Entry point of the program
│── [other helper files] # Other files like utils.py etc
│── README.md # Project documentation
```

---

## 🔒 Security

- 🔑 **Password Encryption:** Uses a custom encryption function before storing passwords.
- 🚨 **Secure Data Storage:** Data is stored in **text files** with proper formatting and validation.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/your-username/cab-service.git
cd cab-service
```

### 1️⃣Run the Program

Make sure you have Python 3.x installed. Then, run:

```sh
python main.py
```
