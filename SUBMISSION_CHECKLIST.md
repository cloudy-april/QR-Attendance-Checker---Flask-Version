# 📋 SUBMISSION CHECKLIST - CSEC 3 Final Project

## What to Submit to Your Professor

Your submission consists of **ONE GitHub Repository Link** that contains all deliverables.

---

## ✅ REPOSITORY REQUIREMENTS

### A. Directory Structure
```
QR-Attendance-Checker---Flask-Version/
├── diagram/
│   └── architecture.png                    ← Deliverable 1: Architecture Diagram (20 pts)
├── deployment/
│   ├── README.md                          ← Deployment instructions
│   └── screenshots/                       ← 10+ labeled Azure Portal screenshots
│       ├── 01-resource-group.png
│       ├── 02-sql-database.png
│       ├── 03-storage-account.png
│       ├── 04-app-service-plan.png
│       ├── 05-app-service-instance-1.png
│       ├── 06-app-service-instance-2.png
│       ├── 07-app-gateway.png
│       ├── 08-autoscale-rules.png
│       ├── 09-application-insights.png
│       └── ...more as needed
├── report/
│   └── cost-estimate.md                   ← Deliverable 3: Cost Report (15 pts)
├── CHANGELOG.md                           ← Deliverable 2: Team contributions (part of 30 pts)
├── README.md                              ← Project overview + video link
└── app/
    └── (your Flask application code)
```

---

## 📦 DELIVERABLE 1: ARCHITECTURE DIAGRAM (20 Points)

### Requirements
- [ ] Professional diagram showing all Azure resources
- [ ] Clear labels for each service (App Service, SQL DB, Storage, etc.)
- [ ] Connection arrows showing data flow
- [ ] Security boundary identified (public vs. private)
- [ ] Cloud optimizations highlighted (autoscale, load balancer, AZs, monitoring)
- [ ] Saved as PNG in `/diagram/architecture.png`

### How to Create
**Option 1: Draw.io (Recommended & Free)**
1. Go to https://draw.io
2. Import Azure architecture icons:
   - File → Import from URL → https://jgraph.github.io/drawio-libs/libs/azure_svg.xml
3. Drag icons to design your architecture
4. Add labels, colors, arrows for clarity
5. Export as PNG (File → Export as → PNG)
6. Save to `/diagram/architecture.png`

**Option 2: Azure Architecture Center**
- Download official Azure icons: https://learn.microsoft.com/en-us/azure/architecture/icons/
- Use PowerPoint or Visio
- Create diagram with all resources
- Export as PNG

**Option 3: Lucidchart**
- Professional diagram tool
- Free trial available
- Create, save, export as PNG

### What to Show in Diagram
```
BASELINE ARCHITECTURE:
[Users] 
  ↓
[Application Gateway (Load Balancer)]
  ↓
[App Service Plan: ASP-mascarqr]
  ├─ Instance 1: mascan-qr
  └─ Instance 2: mascan-qr-2
  ↓
[Azure SQL Database: mascan-db]
[Azure Storage: mascanstorage]
  ├─ Blob Container: uploads (CSV, PDF)

OPTIMIZATIONS HIGHLIGHTED:
✓ Multi-instance for fault tolerance
✓ Autoscale rules (CPU-based)
✓ Application Insights monitoring
✓ Firewall & security rules
```

---

## 📄 DELIVERABLE 2: DEPLOYMENT DOCUMENTATION (30 Points)

### Part A: Deployment Steps (20 pts)
- [ ] `/deployment/README.md` exists
- [ ] Covers all resources created:
  - Resource Group creation
  - Azure SQL Database setup
  - Storage Account setup
  - App Service Plan creation
  - App Service instances (2+)
  - Application Gateway configuration
  - Autoscale rules
  - Application Insights integration
- [ ] Screenshots folder organized and labeled
- [ ] Clear, step-by-step instructions

### Part B: Screenshots (10 pts)
- [ ] **9-10 high-quality screenshots** in `/deployment/screenshots/`
- [ ] Each screenshot clearly labeled (01-..., 02-..., etc.)
- [ ] Screenshots show:
  1. Resource Group overview
  2. SQL Database configuration
  3. Storage Account with blob container
  4. App Service Plan settings
  5. Both App Service instances running
  6. Application Gateway configuration
  7. Autoscale rules
  8. Application Insights dashboard
  9. Live app running in browser
  10. Application functioning (login, event creation, QR scanning)

### How to Take & Organize Screenshots
```powershell
# 1. Open Azure Portal
# 2. Navigate to each resource
# 3. Take screenshot (Shift + Windows + S)
# 4. Save to deployment/screenshots/
# 5. Rename: 01-resource-group.png, 02-sql-database.png, etc.
# 6. Add brief captions in README.md pointing to each screenshot
```

### CHANGELOG.md Requirements (10 pts)
- [ ] File exists at `/CHANGELOG.md`
- [ ] Uses "Keep a Changelog" format
- [ ] All 4 team members have entries
- [ ] Minimum 5 entries per team member
- [ ] All entries dated (YYYY-MM-DD format)
- [ ] Entries are specific, not vague
- [ ] Covers architecture, deployment, code changes, bug fixes
- [ ] Updated regularly (not filled last-minute)

**Example Entry:**
```markdown
- [Member Name] - Created Resource Group 'mascan-rg' in Southeast Asia region
- [Member Name] - Set up Azure SQL Database with Standard S1 tier and configured firewall
- [Member Name] - Deployed App Service with Python 3.10 runtime and configured GitHub Actions
```

---

## 💰 DELIVERABLE 3: COST ESTIMATE REPORT (15 Points)

### Requirements
- [ ] File exists at `/report/cost-estimate.md`
- [ ] 1-2 pages (markdown or PDF)
- [ ] Includes:

**✅ Architecture Summary** (brief description of deployed resources)
```
Example:
The QR Attendance Checker is deployed on Azure using:
- App Service Plan (B2 Standard) with 2-5 autoscaling instances
- Azure SQL Database (Standard S1)
- Azure Storage Account (Standard LRS)
- Application Gateway for load balancing
- Application Insights for monitoring
```

**✅ Itemized Cost Breakdown** (for each resource)
```
| Service | Monthly Cost | Notes |
|---------|--------------|-------|
| App Service Plan (B2) | $50.00 | 2 instances |
| Autoscaling instances | +$8/ea | Up to 5 total |
| SQL Database (Standard S1) | $30.00 | |
| Storage Account | $5.88 | Blob + data transfer |
| Application Gateway | $10.50 | Load balancing |
| Application Insights | $2.99 | Monitoring |
| **TOTAL** | **$124.37** | |
```

**✅ Azure Pricing Calculator Screenshot**
1. Go to https://azure.microsoft.com/pricing/calculator/
2. Add each Azure service
3. Set region: Southeast Asia
4. Take screenshot of final cost estimate
5. Save as PNG and reference in report

**✅ Cost Optimization Strategies** (at least 1 realistic strategy)
```
Examples:
1. Reserved Instances: Save 30-40% with 1-year commitment
2. Scheduled Scaling: Scale down at nights/weekends
3. SQL Serverless: Switch to autoscaling for variable workloads
4. Storage Tier: Move old files to "Cool" tier
5. Load Balancer: Replace App Gateway with cheaper Azure LB
```

---

## 🎥 DELIVERABLE 4: VIDEO PRESENTATION (35 Points)

### Requirements
- [ ] **Duration**: 10-15 minutes
- [ ] **Format**: MP4, recorded screen + audio
- [ ] **Upload**: YouTube (unlisted)
- [ ] **Link added**: To README.md
- [ ] **All 4 members** speak equally

### Segments (Follow This Exactly)

**Segment 1: Architecture Walkthrough (3 minutes)**
- [ ] Show architecture diagram on screen
- [ ] Explain baseline deployment
- [ ] Highlight cloud optimizations (autoscale, load balancer, monitoring)
- [ ] Explain why each optimization matters
- [ ] Speaker: Any team member

**Segment 2: Live Demo (5 minutes)**
- [ ] Show Flask app running in browser
- [ ] Demonstrate key features:
  - [ ] Login (admin / Admin@123)
  - [ ] Create an event
  - [ ] Upload CSV file
  - [ ] Generate QR codes
  - [ ] Scan a QR code
  - [ ] View attendance report
  - [ ] Export PDF
- [ ] Show Azure Portal with deployed resources:
  - [ ] Resource Group overview
  - [ ] Both App Service instances running
  - [ ] Application Gateway health probes
  - [ ] Application Insights dashboard
- [ ] Speaker: Any team member

**Segment 3: Cost Review (2 minutes)**
- [ ] Show cost estimate report
- [ ] Explain itemized monthly cost
- [ ] Show Azure Pricing Calculator screenshot
- [ ] Explain cost optimization strategy
- [ ] Speaker: Any team member

**Segment 4: Conclusion (2 minutes)**
- [ ] Recap project achievements
- [ ] Challenges faced and how you solved them
- [ ] Key learnings from cloud deployment
- [ ] Future improvements (optional)
- [ ] Wrap-up and Q&A intro
- [ ] Speakers: All 4 members briefly (30 sec each)

### Video Recording Tips
1. **Record in advance** (not live during submission)
2. **Test audio** - use headset microphone
3. **Share screen** - show desktop/browser clearly
4. **Slow down** - talk clearly, don't rush
5. **Edit carefully** - trim silence, fix audio levels
6. **Use screen recording software**:
   - Windows: **OBS Studio** (free, professional)
   - Windows: **ScreenFlow** (macOS)
   - Windows: Built-in **Xbox Game Bar** (Win+G)
   - Online: **Loom** (free, browser-based)

### Upload to YouTube
1. Go to https://www.youtube.com
2. Click "Create" (upload icon)
3. Upload your MP4 file
4. Title: `CSEC 3 Final Project - QR Attendance Checker Azure Deployment`
5. Description:
   ```
   CSEC 3 – Cloud Computing Final Project
   Team Members: [Name, Name, Name, Name]
   GitHub Repository: [Your GitHub link]
   
   This video demonstrates:
   - Azure cloud architecture design
   - Live deployment on App Service with SQL Database
   - Autoscaling and load balancing implementation
   - Cost estimation and optimization strategies
   ```
6. **Visibility**: Set to "Unlisted" (not public, only accessible with link)
7. Copy video URL
8. Add to README.md:
   ```markdown
   ### Video Presentation
   📹 [Watch Full Presentation](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
   ```

---

## 📊 GRADING RUBRIC QUICK REFERENCE

| Deliverable | Excellent | Good | Developing | Poor |
|-------------|-----------|------|------------|------|
| **Diagram (20)** | All resources shown, connections clear, security boundary marked, optimizations highlighted | Resources shown, minor labeling gaps, security boundary marked | 1 resource missing, connections unlabeled, optimizations not clear | Resources missing, no connections, no security boundary |
| **Documentation (30)** | Screenshots flawless, organized, clear explanations, CHANGELOG detailed from all members | Good screenshots, CHANGELOG present but uneven, minor gaps | Screenshots disorganized, CHANGELOG incomplete, uneven contribution | Documentation unusable, CHANGELOG missing |
| **Cost Report (15)** | Clear summary, itemized costs for all resources, realistic optimization explained with savings | Breakdown mostly complete, missing 1-2 resources, optimization mentioned | Costs incomplete or unrealistic, optimization missing | Report missing or incomprehensible |
| **Video (35)** | Architecture explained confidently, live demo works flawlessly, all members speak equally, 10-15 min | Demo works with minor issues, all members speak but uneven, rushed on optimizations | Demo partially works, dominated by 1 member, disorganized | Demo fails, one member doesn't speak |
| **TOTAL** | **100** | **75-85** | **50-70** | **<50** |

---

## 🚀 FINAL SUBMISSION STEPS

### Step 1: Complete All Deliverables
- [ ] Architecture diagram (PNG) → `/diagram/architecture.png`
- [ ] Deployment README → `/deployment/README.md`
- [ ] Screenshots (10+) → `/deployment/screenshots/`
- [ ] Cost report → `/report/cost-estimate.md`
- [ ] CHANGELOG → `/CHANGELOG.md`
- [ ] Updated README → `/README.md` with video link

### Step 2: Git Commit Everything
```powershell
cd C:\Users\Fred\Desktop\QR-Attendance-Checker---Flask-Version-main

git add .
git commit -m "CSEC 3 Final Project: Complete Azure Deployment with Documentation"
git push origin main
```

### Step 3: Record & Upload Video
- [ ] Record 10-15 min presentation
- [ ] Upload to YouTube (Unlisted)
- [ ] Copy YouTube link
- [ ] Add to README.md

### Step 4: Submit to Professor
**What to submit:**
1. GitHub Repository Link
   - Example: `https://github.com/yourusername/QR-Attendance-Checker---Flask-Version`
2. Live Demo URL (Application Gateway IP)
   - Example: `http://40.123.45.67`
3. YouTube Video Link
   - Example: `https://www.youtube.com/watch?v=abc123xyz`

**Where to submit:**
- Email to professor OR
- Submit through course LMS (Canvas, Blackboard, etc.) OR
- Link shared during presentation

---

## 🎓 GRADING EVALUATION CRITERIA

Your professor will check:

✅ **Deliverable 1 (20 pts)**: Architecture diagram clarity and completeness  
✅ **Deliverable 2 (30 pts)**: Deployment documentation + screenshots + CHANGELOG + team contribution  
✅ **Deliverable 3 (15 pts)**: Cost report accuracy and optimization strategies  
✅ **Deliverable 4 (35 pts)**: Video quality, live demo success, all members speaking  
✅ **GitHub Repository**: Clean structure, proper commit history, professional documentation  

**Total: 100 points**

---

## ⚠️ IMPORTANT REMINDERS

1. **Delete Azure Resources After Grading**
   ```powershell
   az group delete --name mascan-rg --yes
   ```
   This prevents unexpected charges

2. **Each Member Must Understand Everything**
   - You'll be asked individual questions during Q&A
   - Be ready to explain any part of the architecture

3. **Keep It Simple But Professional**
   - Focus on cloud architecture, not complex app features
   - Clean, well-documented code wins points

4. **Update CHANGELOG Regularly**
   - Not last-minute
   - Shows professional development practice
   - Demonstrates individual contributions

5. **Test Everything Before Submitting**
   - Live demo must work flawlessly
   - Video must be clear and audible
   - All links must work

---

## 📞 SUPPORT

If you need help:
1. Check official documentation: https://learn.microsoft.com/azure/
2. Review your deployment README in `/deployment/README.md`
3. Check cost report for resource details
4. Verify CHANGELOG for who did what

---

**Good luck with your submission! 🚀**

Generated: 2026-05-12  
Project: CSEC 3 Cloud Computing Final Project  
Application: MaScan - QR Attendance Checker
