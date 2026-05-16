# How to Run and Test the QR Attendance Checker App

## 📋 Quick Start (30 seconds)

### Step 1: Install Dependencies
```powershell
cd app
pip install -r requirements.txt
```

### Step 2: Run the App
```powershell
python src/flask_app.py
```

### Step 3: Open in Browser
Go to: **http://localhost:5000**

**Default Credentials:**
- Username: `admin`
- Password: `Admin@123`

---

## 🔧 Detailed Setup Instructions

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git (optional, if cloning from GitHub)

### Verify Python Installation
```powershell
python --version
pip --version
```

### Navigate to App Directory
```powershell
cd "c:\Users\Fred\Desktop\QR-Attendance-Checker---Flask-Version-main\app"
```

### Install Required Dependencies
```powershell
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- Flask-CORS (cross-origin requests)
- Flask-Session (session management)
- OpenCV (QR code scanning)
- ReportLab (PDF generation)
- bcrypt (password hashing)
- And more...

**⏱️ Installation takes 2-5 minutes depending on internet speed**

---

## 🚀 Running the Application

### Start the Flask Server
```powershell
cd app
python src/flask_app.py
```

### Expected Output
```
Creating default admin user
Default admin user created
...
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.43.170:5000
Press CTRL+C to quit
 * Debugger is active!
```

### Access the App
- **Local Machine**: http://localhost:5000
- **Other Machine on Network**: http://YOUR_IP:5000

### Stop the Server
Press `Ctrl+C` in the PowerShell terminal

---

## 🧪 Testing the Features

### 1. **Login**
1. Go to http://localhost:5000
2. Enter credentials:
   - Username: `admin`
   - Password: `Admin@123`
3. Click "Login"

### 2. **Test Online Status Feature** (NEW!)
1. After logging in, click **"Online Users"** in the navigation menu
2. You should see the admin user listed as online
3. Click **"Refresh Status"** button to manually refresh

### 3. **Test API Endpoint**
Open a new PowerShell and run:

```powershell
# Login and test the API
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
Invoke-WebRequest -Uri "http://localhost:5000/login" -Method POST -WebSession $session `
  -Body @{username="admin"; password="Admin@123"} | Out-Null

# Get online status as JSON
$response = Invoke-WebRequest -Uri "http://localhost:5000/api/online-status" -WebSession $session
$response.Content | ConvertFrom-Json | ConvertTo-Json -Depth 10
```

**Expected Response:**
```json
{
  "total_online": 1,
  "admins_online": 1,
  "scanners_online": 0,
  "active_users": [
    {
      "username": "admin",
      "full_name": "Administrator",
      "role": "admin",
      "login_time": "2026-05-13T21:44:39",
      "status": "Online"
    }
  ],
  "admins": [...],
  "scanners": [...]
}
```

### 4. **Test Multiple Users**
Create additional test users:

1. Go to **"Users"** section (admin only)
2. Click **"Add New User"**
3. Fill in:
   - Username: `scanner1`
   - Full Name: `John Scanner`
   - Password: `Scanner@123`
   - Role: `scanner`
4. Click **"Create User"**
5. Repeat for more users

Then open different browser windows/tabs and login as different users to see them appear in the online status!

### 5. **Test Logout**
1. Click **"Logout"** button in top-right
2. User should disappear from "Online Users" page

### 6. **Test QR Scanner**
1. Click **"Start Scanning"** from dashboard
2. Allow camera access when prompted
3. Show a QR code to your webcam
4. System should automatically record attendance

### 7. **Test Events**
1. Click **"Events"** in navigation
2. Click **"Create Event"**
3. Fill event details and create
4. Event should appear in the list

### 8. **Test Attendance History**
1. Click **"Attendance History"** (from dashboard)
2. View all attendance records
3. Filter by event if desired

---

## 🔍 Troubleshooting

### Port Already in Use
If you get "Port 5000 is already in use":

```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F
```

Or run on a different port:
```powershell
# Edit src/flask_app.py and change:
# app.run(debug=True, host='0.0.0.0', port=5001)
```

### Module Not Found Error
```powershell
# Make sure you're in the right directory
cd app
pip install -r requirements.txt

# If still failing, upgrade pip
pip install --upgrade pip
pip install -r requirements.txt
```

### Database Issues
The app automatically creates `mascan_attendance.db` on first run. If you have issues:

```powershell
# Delete the old database to start fresh
rm mascan_attendance.db

# Restart the app
python src/flask_app.py
```

### Camera/Webcam Not Working
- Allow camera permissions when asked
- Make sure no other app is using your webcam
- Try refreshing the browser (F5)

### Can't Connect to http://localhost:5000
- Make sure Flask is running (check PowerShell output)
- Try http://127.0.0.1:5000 instead
- Check if firewalls are blocking port 5000

---

## 📊 Testing Checklist

- [ ] **Setup & Installation**
  - [ ] Python 3.10+ installed
  - [ ] Dependencies installed successfully
  - [ ] No errors during startup

- [ ] **Core Features**
  - [ ] Can login with admin credentials
  - [ ] Dashboard displays correctly
  - [ ] Can create events
  - [ ] Can create users
  - [ ] Can view all users

- [ ] **Online Status Feature** (NEW!)
  - [ ] "Online Users" appears in menu
  - [ ] Online users page loads
  - [ ] Current user shows as online
  - [ ] Multiple users show as online
  - [ ] Users disappear when logging out
  - [ ] API endpoint `/api/online-status` returns JSON
  - [ ] Auto-refresh works (30-second updates)
  - [ ] Manual refresh button works

- [ ] **Scanner**
  - [ ] Scanner page loads
  - [ ] Camera access works
  - [ ] Can scan QR codes
  - [ ] Attendance records correctly

- [ ] **Attendance & History**
  - [ ] Attendance records are created
  - [ ] Can view attendance history
  - [ ] Can filter by event
  - [ ] Can export to PDF

- [ ] **User Management** (Admin Only)
  - [ ] Can view all users
  - [ ] Can create new users
  - [ ] Can delete users
  - [ ] Roles are correctly assigned

---

## 🐛 Debug Mode

The app runs in **debug mode** by default. This means:
- ✅ Auto-reloads when you change code
- ✅ Shows detailed error messages
- ✅ Interactive debugger available
- ⚠️ NOT for production use

### Disable Debug Mode
Edit `src/flask_app.py` and change:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

---

## 📱 Test on Other Devices

### Same Network
1. Find your PC's IP address:
   ```powershell
   ipconfig
   # Look for "IPv4 Address"
   ```

2. Access from another device:
   ```
   http://YOUR_IP:5000
   ```

### Mobile Device Testing
- Works on smartphones and tablets
- Responsive design adapts to screen size
- Camera works on mobile devices

---

## 📈 Performance Testing

### Quick Performance Check
```powershell
# Test API response time
$sw = Measure-Command {
  Invoke-WebRequest -Uri "http://localhost:5000/api/online-status" | Out-Null
}
Write-Host "API Response Time: $($sw.TotalMilliseconds)ms"
```

### Load Testing (advanced)
For load testing, install Apache Bench or similar:
```powershell
# Example: 100 requests, 10 concurrent
ab -n 100 -c 10 http://localhost:5000/
```

---

## 📝 Common Test Scenarios

### Scenario 1: Complete Workflow
1. Login as admin
2. Create an event
3. Create a scanner user
4. Login as scanner (new tab/window)
5. View online users (both see each other)
6. Scanner logs out
7. Admin sees scanner disappeared from online users

### Scenario 2: Attendance Taking
1. Event is created
2. Multiple users logged in
3. Scanner starts scanning QR codes
4. Attendance records appear
5. Can view attendance history

### Scenario 3: Role-Based Access
1. Login as admin - see all menu items
2. Create scanner user
3. Login as scanner - limited menu items
4. Verify scanner can't access admin features

---

## 📚 Database Inspection

### View Database Contents
```powershell
# Install sqlite3 if needed
choco install sqlite

# Open database
sqlite3 mascan_attendance.db

# View users
SELECT * FROM users;

# View login history
SELECT * FROM login_history;

# View active sessions
SELECT u.username, u.full_name, u.role, lh.login_time 
FROM login_history lh 
JOIN users u ON lh.username = u.username 
WHERE lh.logout_time IS NULL;
```

---

## 🎓 Code Structure for Testing

```
app/
├── src/
│   ├── flask_app.py          # Main app initialization
│   ├── routes/
│   │   ├── auth_routes.py     # Login/Logout
│   │   ├── dashboard_routes.py # Dashboard & Online Users (NEW!)
│   │   ├── attendance_routes.py
│   │   └── ...
│   ├── database/
│   │   └── db_manager.py      # Database operations + get_online_stats()
│   ├── templates/
│   │   ├── online_users.html  # Online Users Page (NEW!)
│   │   └── ...
│   └── static/
│       ├── css/
│       └── js/
```

---

## 🆘 Need Help?

### Check Logs
Look at the PowerShell output when running the app for:
- Error messages
- Database issues
- Module loading errors

### Enable Verbose Logging
Edit `src/flask_app.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Module not found | Run `pip install -r requirements.txt` again |
| Port in use | Kill the process or use different port |
| Can't login | Check admin user exists in database |
| Camera not working | Allow permissions, restart browser |
| Database locked | Restart Flask app |
| Slow performance | Reduce auto-refresh interval in JS |

---

## 🎉 You're Ready!

Now you can:
- ✅ Run the application
- ✅ Test all features
- ✅ View online users
- ✅ Use the API
- ✅ Debug issues

Happy testing! 🚀
