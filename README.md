# 🗳️ Secure E-Voting with Facial Recognition using AI

## 🔒 Overview
This project aims to build a **secure and efficient electronic voting system** that uses **facial recognition** to authenticate voters.  
It eliminates the need for traditional voter IDs, reduces fraud, and ensures **one person can vote only once**, providing a transparent, AI-powered e-voting experience.

---

## 🚀 Features
- ✅ **AI-Based Face Recognition** – Identifies voters using trained facial data.
- ✅ **Real-Time Verification** – Prevents duplicate or fake votes.
- ✅ **Database Integration** – Stores voter data and results securely.
- ✅ **Admin Panel** – Manage voters, candidates, and monitor results.
- ✅ **User-Friendly Interface** – Simple and intuitive web design.
- ✅ **OTP / PIN Validation (Optional)** – Adds an extra security layer.

---

## 🧠 Tech Stack

| Layer | Technologies Used |
|:------|:------------------|
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Backend** | Python (Flask) |
| **AI / ML** | OpenCV, Face Recognition Library |
| **Database** | MySQL / SQLite |
| **Version Control** | Git, GitHub |

---

## 🧩 System Workflow
1️⃣ **Admin registers voters** and adds their face data.  
2️⃣ **Model trains** on stored facial images (`all_images` folder).  
3️⃣ During voting:
   - Captures a live face through webcam.  
   - Matches it with stored data using AI model.  
   - If matched, allows voting; otherwise denies access.  
4️⃣ Vote is recorded securely in the database.  
5️⃣ Admin can view and tally the final results.

---


---

## ⚙️ Installation & Setup

### 🧩 Prerequisites
- Python 3.8+
- Git installed
- OpenCV library
- Face Recognition library

### 🧱 Steps
# 1. Clone this repository
git clone https://github.com/SurajThoke/Secure-E-Voting-with-Facial-Recognition-with-AI.git
cd Secure-E-Voting-with-Facial-Recognition-with-AI

# 2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate      # For Windows
# or
source venv/bin/activate          # For Linux/Mac

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
