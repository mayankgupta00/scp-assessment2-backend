# SCP Directory Manager

## Project Overview

The **SCP Directory Manager** is a full-stack web application that manages SCP subjects (SCP-001 to SCP-020). It is built with:

* **React** for the frontend (UI)
* **Flask** for the backend (REST API)
* **MySQL** database for storing SCP records
* **Netlify** for cloud deployment of frontend

The application allows users to **create, read, update, and delete (CRUD)** SCP records dynamically.

---

## Live Demo

Frontend deployed on Netlify:
[https://chipper-biscotti-fd443a.netlify.app](https://chipper-biscotti-fd443a.netlify.app)

---

## Features

* CRUD operations for SCP records
* Responsive UI with React and Bootstrap
* RESTful API built with Flask
* MySQL database stores 20 SCP subjects
* Cloud deployment for frontend via Netlify

---

## Technologies Used

| Layer      | Technology                                                  |
| ---------- | ----------------------------------------------------------- |
| Frontend   | React.js, Axios, Bootstrap, React-Bootstrap                 |
| Backend    | Python, Flask, Flask-CORS                                   |
| Database   | MySQL (XAMPP or cloud)                                      |
| Deployment | Netlify (frontend), local/optional cloud server for backend |

---

## Project Structure

```
scp-assessment2/
│
├── scp-frontend/         # React frontend
│   ├── src/
│   │   ├── App.js
│   │   ├── App.css
│   │   └── components/
│   │       ├── SCPList.js
│   │       └── SCPForm.js
│   ├── package.json
│   └── build/            # Production build for deployment
│
├── scp-api/              # Flask backend
│   ├── app.py
│   └── db_config.py
│
└── database.sql           # MySQL database script (scp_directory + 20 SCP records)
```

---

## Setup Instructions

### 1. Backend (Flask API)

1. Install Python packages:

```bash
pip install Flask Flask-Cors mysql-connector-python
```

2. Configure MySQL connection in `db_config.py`:

```python
host="localhost"
user="root"
password=""
database="scp_directory"
```

3. Run Flask API:

```bash
python app.py
```

API base URL: `http://127.0.0.1:5000/api/scp`

---

### 2. Database (MySQL)

1. Open **phpMyAdmin** or MySQL CLI.
2. Import `database.sql` or run manually:

```sql
CREATE DATABASE scp_directory;
USE scp_directory;
CREATE TABLE scp_subjects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(50),
    class VARCHAR(50),
    description TEXT,
    containment TEXT
);
-- Add 20 SCP records (SCP-001 to SCP-020)
```

---

### 3. Frontend (React)

1. Install dependencies:

```bash
npm install
```

2. Start development server:

```bash
npm start
```

Open [http://localhost:3000](http://localhost:3000)

3. Build production version for deployment:

```bash
npm run build
```

4. Deploy `build/` folder to **Netlify** for a live site.

---

## API Endpoints

| Method | Endpoint        | Description               |
| ------ | --------------- | ------------------------- |
| GET    | `/api/scp`      | Retrieve all SCP records  |
| GET    | `/api/scp/<id>` | Retrieve SCP record by ID |
| POST   | `/api/scp`      | Add new SCP record        |
| PUT    | `/api/scp/<id>` | Update SCP record by ID   |
| DELETE | `/api/scp/<id>` | Delete SCP record by ID   |

---

## Notes

* Ensure Flask API is running before using React frontend.
* Frontend is cloud-deployed; backend can also be deployed to Render or PythonAnywhere for full cloud solution.
* Code is clean, organized, and well-commented for comprehension.

---



