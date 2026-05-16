# MaScan - QR Attendance Checker (Flask)
## CSEC 3 Cloud Computing - Final Project (Azure Deployment)

MaScan is a Flask web app for attendance tracking using QR codes. It supports event-based attendance, QR generation from CSV, scanning, attendance history, and PDF export.

**This project has been deployed to Microsoft Azure as a production-grade cloud application with fault tolerance, autoscaling, and advanced monitoring.**

---

## 🎯 Project Submission (CSEC 3 Final Project)

### Team Members
- **Member 1**: [Name] - Role
- **Member 2**: [Name] - Role
- **Member 3**: [Name] - Role
- **Member 4**: [Name] - Role

### Live Demo & Video Presentation
📹 **[Watch Video Presentation (YouTube Unlisted)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)**

Video includes:
- Architecture walkthrough (3 min)
- Live demo in browser (5 min)
- Azure Portal walkthrough
- Cost review & optimization strategies
- Team Q&A

### Access Live Application
🌐 **[Click Here to Access Deployed App](http://YOUR_APPLICATION_GATEWAY_IP)**

**Credentials:**
- Username: `admin`
- Password: `Admin@123`

### Project Deliverables
- ✅ **[Architecture Diagram](./diagram/architecture.png)** - Baseline + optimized design
- ✅ **[Deployment Documentation](./deployment/README.md)** - Step-by-step Azure setup with screenshots
- ✅ **[Cost Estimate Report](./report/cost-estimate.md)** - Monthly cost analysis & optimization
- ✅ **[CHANGELOG.md](./CHANGELOG.md)** - Team contribution tracking
- ✅ **Video Presentation** - YouTube link above

### Azure Services Used (Minimum 3 ✓)
1. **Azure App Service** - Flask web application (2 instances for redundancy)
2. **Azure SQL Database** - Production database (replaced SQLite)
3. **Azure Storage (Blob)** - File uploads & PDF exports
4. **Application Gateway** - Load balancing
5. **Azure Application Insights** - Monitoring & telemetry

### Cloud Optimizations Implemented (Minimum 2 ✓)
1. **Fault Tolerance** - Multi-instance App Service across Availability Zones with health checks
2. **Scalability** - Autoscale rules (2-5 instances based on CPU > 70%)
3. **Advanced Monitoring** - Application Insights for performance tracking
4. **Security** - SQL firewall rules, managed identity, NSG configuration

---

## Features
- QR scanning for attendance check-in
- Bulk QR generation from CSV uploads
- Event management (create, edit, list, view)
- Attendance history and activity logs
- User authentication and role-based access
- PDF export of attendance records

## Tech Stack
- Python, Flask
- SQLite
- HTML/CSS/JavaScript
- OpenCV + pyzbar (QR scanning)
- ReportLab (PDF export)

## Project Structure
```text
QR-Attendance-Checker---Flask-Version/
|-- README.md
|-- sample_students.csv
|-- app/
|   |-- app.py
|   |-- requirements.txt
|   |-- src/
|   |   |-- flask_app.py
|   |   |-- routes/
|   |   |-- templates/
|   |   |-- static/
|   |   |-- database/
|   |   |-- utils/
```

## Prerequisites
- Python 3.10+
- pip
- Webcam (for live scanning)

## Setup and Run

### 1. Open project root
```powershell
git clone https://github.com/thebaynal/QR-Attendance-Checker---Flask-Version.git
cd QR-Attendance-Checker---Flask-Version
```

### 2. Create virtual environment
```powershell
python -m venv .venv
```

### 3. Activate virtual environment
Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```powershell
pip install -r app/requirements.txt
```

### 5. Run the app
From project root:
```powershell
python app/app.py
```

The app runs at:
- http://127.0.0.1:5000
- http://localhost:5000

## Default Login
- Username: admin
- Password: Admin@123

## How to Use
1. Log in with the default admin account.
2. Create an event in Events.
3. Go to QR Management.
4. Upload a CSV file (see format below) to generate QR codes.
5. Open Scanner and select an event.
6. Scan generated QR codes to mark attendance.
7. View attendance history and export PDF reports.

## CSV Format for QR Generation
Use this header row:
```csv
School ID,Name,First Name,Last Name,Middle Initial,Year,Section,Course
```

A ready-to-use mock file is included:
- sample_students.csv

Example rows:
```csv
STU101,Alex Cruz,Alex,Cruz,M,1,A,BS Computer Science
STU102,Bianca Reyes,Bianca,Reyes,L,1,B,BS Information Technology
```

## Screenshots

### App Preview

#### Dashboard

![Dashboard](https://raw.githubusercontent.com/thebaynal/QR-Attendance-Checker---Flask-Version/main/docs/screenshots/dashboard.png)

#### Events Management

![Events](https://raw.githubusercontent.com/thebaynal/QR-Attendance-Checker---Flask-Version/main/docs/screenshots/events.png)

#### Login

![Login](https://raw.githubusercontent.com/thebaynal/QR-Attendance-Checker---Flask-Version/main/docs/screenshots/login.png)

#### QR Scanner

![QR Scanner](https://raw.githubusercontent.com/thebaynal/QR-Attendance-Checker---Flask-Version/main/docs/screenshots/qr_scan.png)

#### QR Management

![QR Management](https://raw.githubusercontent.com/thebaynal/QR-Attendance-Checker---Flask-Version/main/docs/screenshots/qr-management.png)


## Troubleshooting

### Port already in use
```powershell
$env:FLASK_RUN_PORT=5001
python app/app.py
```

### Dependency install fails (Windows)
```powershell
python -m pip install --upgrade pip
pip install -r app/requirements.txt
```

### Scanner not detecting QR
- Ensure webcam permission is allowed in browser.
- Improve lighting and keep QR within frame.
- Check camera is not used by another app.

### Reset local data
If needed, remove local DB/session files and rerun the app.

## Notes
- QR import supports required and optional columns; include School ID and Name at minimum.
- Keep your virtual environment activated while running the app.
