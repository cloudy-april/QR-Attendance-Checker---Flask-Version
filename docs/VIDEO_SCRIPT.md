# 🎥 Video Presentation Script — MaScan QR Attendance Checker
## CSEC 3 Cloud Computing Final Project | Target: 35/35 Points

**Total Duration**: 12–14 minutes  
**Format**: Screen recording + voice narration (all 4 members speak)  
**Upload**: YouTube (Unlisted)  
**Recording Tool**: OBS Studio / Xbox Game Bar (Win+G) / Loom

---

## 🎯 Rubric Checklist (What Gets You 35/35)

- [x] Architecture explained **confidently** with clear focus on chosen cloud optimizations
- [x] Live demo works **flawlessly** — app runs end-to-end in browser
- [x] Azure Portal resources shown
- [x] IaC command demonstrated
- [x] Cost review presented clearly
- [x] **All 4 group members speak equally and meaningfully** (~3 min each)

---

## PRE-RECORDING CHECKLIST

Before you hit record, have these ready:

### Browser Tabs (Pre-open in order)
1. **Tab 1**: Architecture diagram (`diagram/architecture.html` or the PNG)
2. **Tab 2**: Your live app URL (`http://YOUR_APP_GATEWAY_IP` or `localhost:5000`)
3. **Tab 3**: Azure Portal → Resource Group `mascan-rg` overview
4. **Tab 4**: Azure Portal → App Service Plan → Scale Out (Autoscale)
5. **Tab 5**: Azure Portal → Application Insights → Overview dashboard
6. **Tab 6**: Azure Portal → Application Gateway → Backend Health
7. **Tab 7**: Cost Estimate report (`report/cost-estimate.md`) or rendered version
8. **Tab 8**: Azure Pricing Calculator (with your config loaded)
9. **Tab 9**: Terminal / PowerShell (for IaC command demo)

### App Prep
- Log out of the app (so you can demo the login)
- Have `sample_students.csv` ready on your desktop for upload
- Create a test event in advance (or be ready to create one live)
- Have a printed QR code ready (or a phone showing one) for scanning demo

### Audio
- Use headset microphone
- Quiet room, no background noise
- Test audio levels before recording

---

## SEGMENT 1: INTRODUCTION & ARCHITECTURE WALKTHROUGH
### ⏱️ Duration: 3 minutes | 🎤 Speaker: MEMBER 1

---

### [0:00 – 0:30] Opening Introduction

**SHOW ON SCREEN**: Title slide or README.md in browser

**SAY:**
> "Good day! We are [Team Name] presenting our CSEC 3 Cloud Computing Final Project. Our project is MaScan, a QR-based Attendance Checker built with Python Flask, deployed on Microsoft Azure."
>
> "Our team members are:
> - [Member 1] — Architecture & Resource Group setup
> - [Member 2] — Database & Storage deployment  
> - [Member 3] — App Service & CI/CD pipeline
> - [Member 4] — Monitoring, Documentation & Cost Analysis"
>
> "Let me start by walking through our cloud architecture."

---

### [0:30 – 3:00] Architecture Deep Dive

**SHOW ON SCREEN**: Switch to Tab 1 — Architecture Diagram (full screen)

**SAY (point to each resource as you talk):**

> "Here is our Azure architecture diagram. Let me walk through the data flow from top to bottom."

**Point to Users at top:**
> "End users — students and staff — access MaScan through their web browser or mobile device over HTTPS on port 443."

**Point to Application Gateway:**
> "Traffic first hits our **Application Gateway**, named `mascan-gateway`, which is a Standard V2 load balancer. This distributes incoming requests across our backend instances and performs health checks every 30 seconds. If one instance goes down, traffic is automatically routed to the healthy instance — this is our **first cloud optimization: Fault Tolerance**."

**Point to App Service Plan:**
> "Inside our Azure Virtual Network, we have the **App Service Plan** `ASP-mascarqr` running on B2 Standard tier. This hosts two Flask application instances — `mascan-qr` and `mascan-qr-2` — both running Python 3.10."

**Point to Autoscale badge:**
> "This is our **second cloud optimization: Autoscaling**. We configured CPU-based autoscale rules — when CPU exceeds 70%, Azure automatically spins up additional instances, up to a maximum of 5. When CPU drops below 30%, it scales back down. This ensures we handle traffic spikes during peak attendance hours without paying for idle resources."

**Point to SQL Database:**
> "Our backend data is stored in **Azure SQL Database** — `mascan-db` running Standard S1 tier with 20 DTUs. Notice the security boundary — the SQL server is protected by firewall rules that only allow whitelisted IP addresses and Azure services. No public access."

**Point to Storage Account:**
> "File uploads — CSV student lists and exported PDF reports — are stored in **Azure Blob Storage** under the `mascanstorage` account with a container called `uploads`."

**Point to Application Insights:**
> "Our **third cloud optimization is Advanced Monitoring** with Application Insights — `mascan-insights`. This collects real-time telemetry: request rates, response times, failure rates, and dependency tracking. This lets us proactively identify performance bottlenecks."

**Point to Security Boundary:**
> "Finally, notice the red dashed line — this is our **security boundary**. Everything inside runs within a private Azure VNet. NSG firewall rules control which traffic can reach our app services. The SQL Database has its own IP-based firewall. This layered security is our **fourth optimization**."

> "That covers our architecture. Now let me hand it over to [Member 2] for the live demo."

---

## SEGMENT 2: LIVE DEMO (Part A — App Demo)
### ⏱️ Duration: 3 minutes | 🎤 Speaker: MEMBER 2

---

### [3:00 – 3:15] Transition

**SAY:**
> "Thank you, [Member 1]. I'll now demonstrate our application running live on Azure. Let me switch to the browser."

---

### [3:15 – 3:45] Login Demo

**SHOW ON SCREEN**: Switch to Tab 2 — App URL (login page)

**SAY:**
> "Here's our MaScan application, accessible through the Application Gateway's public IP. As you can see, we have a professional login page."

**ACTION**: Type username `admin`, password `Admin@123`, click Login

> "I'm logging in with the admin account. The authentication uses bcrypt password hashing for security."

**SHOW**: Dashboard loads with live clock, stats, quick actions

> "This is our dashboard. It shows real-time statistics — total events, total attendance, total users — and a live clock. The dashboard also shows today's active events with live progress bars that update every 3 seconds."

---

### [3:45 – 4:30] Create Event

**SAY:**
> "Let me demonstrate creating an event."

**ACTION**: Click "Create Event" button → Fill in:
- Event Name: `CSEC 3 Final Demo`
- Date: (today's date)
- Description: `Live demonstration for cloud computing project`
- Click Create

> "I've created a new event called 'CSEC 3 Final Demo'. You can see it now appears in our events list."

---

### [4:30 – 5:15] Upload CSV & Generate QR Codes

**ACTION**: Navigate to QR Management

**SAY:**
> "Now I'll upload a CSV file of students to generate QR codes."

**ACTION**: Click Upload CSV → Select `sample_students.csv` → Upload

> "I'm uploading our sample student CSV file. The system parses School ID, Name, Year, Section, and Course from the CSV, then generates unique QR codes for each student."

**SHOW**: QR codes generated, scroll through the list

> "As you can see, QR codes have been generated for all students. Each QR code contains the student's school ID encoded for scanning."

---

### [5:15 – 6:00] QR Scanning Demo

**ACTION**: Navigate to Scanner → Select the event you just created

**SAY:**
> "Now let me demonstrate the core feature — QR code scanning."

**ACTION**: Hold up a printed QR code or show one on phone to the webcam

> "I'm scanning a student's QR code. The system identifies the student, records their attendance with a timestamp, and marks them as 'Checked In' for the morning time slot."

**SHOW**: Success notification, attendance recorded

> "The attendance is recorded in real-time. If I try to scan the same student again for the same time slot, the system will show they're already checked in — preventing duplicate entries."

> "Let me now hand over to [Member 3] to show our Azure Portal resources and Infrastructure as Code."

---

## SEGMENT 3: LIVE DEMO (Part B — Azure Portal & IaC)
### ⏱️ Duration: 3.5 minutes | 🎤 Speaker: MEMBER 3

---

### [6:00 – 6:10] Transition

**SAY:**
> "Thank you, [Member 2]. Now let me show you our actual Azure resources deployed in the portal."

---

### [6:10 – 7:00] Resource Group Overview

**SHOW ON SCREEN**: Switch to Tab 3 — Azure Portal → Resource Group

**SAY:**
> "Here's our Azure Portal. I'm inside our Resource Group `mascan-rg`, deployed in the Southeast Asia region."

**ACTION**: Scroll through the resource list slowly

> "As you can see, we have all the resources we discussed in the architecture:
> - Our **App Service Plan** — ASP-mascarqr on B2 Standard tier
> - Two **App Service instances** — mascan-qr and mascan-qr-2
> - The **Azure SQL Database** — mascan-db  
> - Our **Storage Account** — mascanstorage
> - The **Application Gateway** — mascan-gateway
> - And **Application Insights** — mascan-insights
>
> All resources are running and healthy."

---

### [7:00 – 7:45] Autoscale Rules

**SHOW ON SCREEN**: Switch to Tab 4 — App Service Plan → Scale Out

**SAY:**
> "Let me show our autoscale configuration. Here in the App Service Plan under 'Scale Out', you can see our autoscale rules."

**ACTION**: Click into the autoscale settings, show the rules

> "We have two rules configured:
> 1. **Scale Out**: When average CPU percentage exceeds 70% over 10 minutes, increase instance count by 1, up to maximum 5 instances
> 2. **Scale In**: When average CPU percentage drops below 30% over 10 minutes, decrease instance count by 1, minimum 2 instances
>
> This ensures our application handles traffic spikes automatically — for example, during a large seminar when hundreds of students scan simultaneously."

---

### [7:45 – 8:15] Application Insights

**SHOW ON SCREEN**: Switch to Tab 5 — Application Insights

**SAY:**
> "Here is our Application Insights dashboard. You can see live metrics:
> - **Server response times** — averaging under 200 milliseconds
> - **Request rates** — showing the traffic we just generated during the demo
> - **Failure rates** — currently at zero, confirming our app is healthy
>
> This monitoring allows us to proactively detect issues before they impact users."

---

### [8:15 – 8:45] Application Gateway Backend Health

**SHOW ON SCREEN**: Switch to Tab 6 — Application Gateway → Backend Health

**SAY:**
> "Here's our Application Gateway backend health. Both instances — mascan-qr and mascan-qr-2 — show as **Healthy**. The health probes are running every 30 seconds, checking that our application responds correctly."

---

### [8:45 – 9:30] IaC Command Demonstration

**SHOW ON SCREEN**: Switch to Tab 9 — Terminal / PowerShell

**SAY:**
> "Now let me demonstrate an Infrastructure as Code command using the Azure CLI. Instead of clicking through the portal, we can manage resources programmatically."

**ACTION**: Type and run the following commands (you DON'T need to actually create resources — just show the commands):

```powershell
# Show current resource group resources
az resource list --resource-group mascan-rg --output table
```

> "This `az resource list` command shows all resources in our resource group in table format. This is the same view we saw in the portal but managed through code."

**ACTION**: Show another IaC example:

```powershell
# Autoscale command example
az monitor autoscale show --resource-group mascan-rg --name ASP-mascarqr-autoscale
```

> "And here we can query our autoscale settings through the CLI — this confirms our scale-out rule at 70% CPU and scale-in at 30%."

> "These CLI commands can be scripted into deployment pipelines for repeatable, version-controlled infrastructure. Now I'll hand over to [Member 4] for the cost review."

---

## SEGMENT 4: COST REVIEW & CONCLUSION  
### ⏱️ Duration: 3.5 minutes | 🎤 Speaker: MEMBER 4

---

### [9:30 – 9:40] Transition

**SAY:**
> "Thank you, [Member 3]. I'll now present our cost analysis for this Azure deployment."

---

### [9:40 – 10:45] Cost Breakdown

**SHOW ON SCREEN**: Switch to Tab 7 — Cost Estimate Report (or show the rendered markdown)

**SAY:**
> "We prepared a detailed cost estimate report for our Azure deployment. Let me walk through the itemized breakdown."

**ACTION**: Scroll through the cost table

> "Our monthly costs break down as follows:
>
> | Service | Monthly Cost |
> |---------|-------------|
> | App Service Plan B2 with autoscaling | $75 |
> | Azure SQL Database Standard S1 | $30 |
> | Azure Storage Account | approximately $6 |
> | Application Gateway Standard v2 | $10.50 |
> | Application Insights | approximately $3 |
>
> That gives us a **total estimated monthly cost of $124.37 USD**."

---

### [10:45 – 11:15] Azure Pricing Calculator

**SHOW ON SCREEN**: Switch to Tab 8 — Azure Pricing Calculator

**SAY:**
> "Here is the Azure Pricing Calculator where we configured each resource. You can see each service listed — App Service, SQL Database, Storage, Application Gateway, and Application Insights — all set to the Southeast Asia region with the specifications matching our deployment."

**ACTION**: Scroll to the total at bottom

> "The calculator confirms our estimated total aligns with our report."

---

### [11:15 – 12:00] Cost Optimization Strategy

**SHOW ON SCREEN**: Switch back to the cost report, scroll to optimization section

**SAY:**
> "We also identified realistic cost optimization strategies. Our primary recommendation is **Reserved Instances**."
>
> "By purchasing a 1-year reservation for our App Service Plan and SQL Database, we can save 30 to 40 percent — reducing our monthly cost from $124 down to approximately $85 per month."
>
> "Our second strategy is **Scheduled Scaling**. Since attendance tracking is only active during school hours — roughly 8 AM to 6 PM — we can use Azure Automation to scale down to a single instance during off-hours. This would save an additional $15 to $20 per month."
>
> "Combined, these optimizations bring our estimated monthly cost down to approximately **$60 to $75** — a 40% reduction from our baseline deployment."

---

### [12:00 – 13:00] Conclusion (ALL MEMBERS)

**SAY (Member 4 starts, then each member speaks ~15-20 seconds):**

**MEMBER 4:**
> "To wrap up, let me summarize what we achieved. We successfully deployed MaScan — a full-stack QR Attendance Checker — to Microsoft Azure with production-grade cloud architecture."

**MEMBER 1:**
> "From an architecture perspective, we designed a multi-tier deployment with clear security boundaries, using Application Gateway for load balancing and NSG firewall rules for access control."

**MEMBER 2:**
> "The biggest challenge we faced was migrating from SQLite to Azure SQL Database. We had to restructure our database connection handling and ensure our Flask application could handle connection pooling properly in a cloud environment."

**MEMBER 3:**
> "We implemented three key cloud optimizations — autoscaling for elastic capacity, fault tolerance with multi-instance deployment, and advanced monitoring with Application Insights. These are patterns we can apply to any future cloud project."

**MEMBER 4:**
> "Thank you for watching our presentation. Our GitHub repository, deployment documentation, architecture diagram, and cost report are all available at the link in our README. We're happy to answer any questions."

---

### [13:00 – 13:10] End Screen

**SHOW ON SCREEN**: README.md with GitHub link and YouTube link

**SAY:**
> "Thank you!"

---

## 📝 POST-RECORDING CHECKLIST

- [ ] Video is 10–15 minutes long (aim for 12–13)
- [ ] All 4 members spoke approximately equally (~3 min each)
- [ ] Audio is clear and audible throughout
- [ ] Screen recording shows all tabs clearly (no tiny fonts)
- [ ] Architecture diagram was fully explained with optimizations
- [ ] Live demo showed: login → create event → upload CSV → generate QR → scan → attendance
- [ ] Azure Portal showed: Resource Group, Autoscale, App Insights, App Gateway health
- [ ] IaC command was demonstrated (az CLI)
- [ ] Cost breakdown was presented clearly with pricing calculator
- [ ] At least one cost optimization strategy was explained with estimated savings
- [ ] No credentials/secrets visible (except demo login which is in README)

## 📤 UPLOADING TO YOUTUBE

1. Go to [youtube.com](https://www.youtube.com) → Click **Create** (camera icon)
2. Upload your MP4 file
3. **Title**: `CSEC 3 Final Project - MaScan QR Attendance Checker Azure Deployment`
4. **Description**:
   ```
   CSEC 3 – Cloud Computing Final Project
   Team Members: [Member 1, Member 2, Member 3, Member 4]
   GitHub Repository: https://github.com/thebaynal/QR-Attendance-Checker---Flask-Version
   
   Demonstrating:
   - Azure cloud architecture with autoscaling & fault tolerance
   - Live QR attendance scanning application
   - Multi-instance App Service with Application Gateway
   - Cost estimation and optimization strategies
   ```
5. **Visibility**: Set to **Unlisted**
6. Copy the video URL
7. Update `README.md` with the YouTube link

## 🎙️ SPEAKING TIPS FOR FULL MARKS

| Do ✅ | Don't ❌ |
|-------|---------|
| Speak naturally, like explaining to a colleague | Read from a script word-for-word |
| Point at/highlight what you're discussing on screen | Stare at the camera ignoring the screen |
| Use "we configured", "we deployed" (team language) | Say "I did everything" |
| Pause briefly between sections | Rush through with no pauses |
| Each member introduces the next ("Now [Name] will...") | Awkward silences between speakers |
| Explain *why* (not just what) each optimization does | Just list services without context |
| Show actual Azure Portal resources running | Only show diagrams/docs |
| Demo the IaC CLI command actually running | Skip the IaC requirement |

## 🔧 IaC COMMANDS CHEAT SHEET

Have these ready to copy-paste into your terminal during recording:

```powershell
# 1. List all resources in the resource group
az resource list --resource-group mascan-rg --output table

# 2. Show autoscale settings
az monitor autoscale show --resource-group mascan-rg --name ASP-mascarqr-autoscale --output json

# 3. Show App Service configuration
az webapp show --resource-group mascan-rg --name mascan-qr --output table

# 4. Show SQL Database status
az sql db show --resource-group mascan-rg --server mascan-server --name mascan-db --output table

# 5. Show Application Gateway health
az network application-gateway show-backend-health --resource-group mascan-rg --name mascan-gateway --output table

# 6. Create resource (example IaC — DON'T run this, just SHOW it)
az group create --name mascan-rg --location southeastasia
az appservice plan create --name ASP-mascarqr --resource-group mascan-rg --sku B2 --is-linux
az webapp create --resource-group mascan-rg --plan ASP-mascarqr --name mascan-qr --runtime "PYTHON:3.10"
```

> **TIP**: For the demo, run command #1 (`az resource list`) live. For others, you can show the command and explain what it does if you're worried about errors.

---

**Last Updated**: 2026-05-16  
**Target Score**: 35/35 — Live Demo & Video Presentation
