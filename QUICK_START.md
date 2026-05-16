# Quick Start Guide - 30 Second Setup

## 🚀 Super Quick (Copy & Paste)

Open **PowerShell** and run these commands:

```powershell
cd "c:\Users\Fred\Desktop\QR-Attendance-Checker---Flask-Version-main\app"
pip install -r requirements.txt
python src/flask_app.py
```

Then open your browser: **http://localhost:5000**

**Login:** 
- Username: `admin`
- Password: `Admin@123`

Done! ✅

---

## 📺 What You'll See

### Step 1: Installation Output
```
Successfully installed Flask-3.0.0
Successfully installed flask-cors-4.0.0
...
```

### Step 2: Server Starting
```
 * Running on http://127.0.0.1:5000
```

### Step 3: Browser
Visit **http://localhost:5000** → See login page

### Step 4: Dashboard
After login → See dashboard with "Online Users" button

---

## 🧪 Quick Tests (Copy & Paste)

### Test 1: Check if App Works
```powershell
Invoke-WebRequest -Uri "http://localhost:5000" -ErrorAction SilentlyContinue | Select-Object StatusCode
# Should show: StatusCode : 200
```

### Test 2: Check Online Users API
```powershell
# Create session and login
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
Invoke-WebRequest -Uri "http://localhost:5000/login" -Method POST -WebSession $session `
  -Body @{username="admin"; password="Admin@123"} -ErrorAction SilentlyContinue | Out-Null

# Get online status
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/online-status" -WebSession $session -ErrorAction SilentlyContinue
$response.Content | ConvertFrom-Json | ConvertTo-Json
```

**Expected Output:**
```json
{
  "total_online": 1,
  "admins_online": 1,
  "scanners_online": 0,
  ...
}
```

---

## 🎯 Key Features to Try

| Feature | How to Test | Expected Result |
|---------|-------------|-----------------|
| **Online Users** | Click "Online Users" in menu | See admin listed as Online |
| **Login/Logout** | Logout → Check Online Users | Admin disappears from list |
| **Dashboard** | Login → See dashboard | Shows stats and recent activity |
| **Attendance** | Click "Scanner" → Show QR code | Records attendance |
| **Events** | Click "Events" → Create event | Event appears in list |

---

## 🛑 Stop the App

Press `Ctrl+C` in PowerShell

---

## ❌ Troubleshooting

### "Module not found"
```powershell
pip install -r requirements.txt
```

### "Port already in use"
```powershell
netstat -ano | findstr :5000
taskkill /PID <number> /F
```

### Can't access localhost:5000
- Make sure Flask is running
- Try: http://127.0.0.1:5000
- Check Windows Firewall

### Stuck? Read Full Guide
Open `RUN_AND_TEST_GUIDE.md` for detailed instructions

---

## 📖 What's New - Online Status Feature

✨ **New Feature: See who's online!**

- Navigate to `/online-users` or click "Online Users" button
- Shows all logged-in admins and users
- Auto-refreshes every 30 seconds
- API available at `/api/online-status`

**Example:**
```
👑 Administrators Online
- Administrator (@admin) - Logged in: 2026-05-13 21:44:39

🔐 Scanners Online
(none currently)
```

---

## 💾 Database

Automatically created on first run:
- `mascan_attendance.db` - SQLite database
- Contains: users, events, attendance, login history

To reset:
```powershell
rm mascan_attendance.db
python src/flask_app.py
```

---

## 🎓 Learn More

Read these files:
- `README.md` - Project overview
- `RUN_AND_TEST_GUIDE.md` - Detailed guide (this file)
- `ONLINE_STATUS_FEATURE.md` - Online status documentation
- `CHANGELOG.md` - What's changed

---

## ✅ You're All Set!

Run the app and enjoy! 🎉

```powershell
cd app
python src/flask_app.py
```

Open browser → http://localhost:5000
