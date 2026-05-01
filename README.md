# 📊 Smart TV & iPad Testing Framework

A modern GUI-based automation dashboard built using Python and Tkinter to execute test cases, monitor results, and generate reports for Smart TV and iPad applications.

---

## 🚀 Features

- ✅ Execute multiple automated test cases
- 📊 Real-time dashboard with statistics
- 🧾 Generate HTML test reports
- 🎨 Modern UI with sidebar and console logs
- 🔄 Reset and rerun test sessions
- 🟢 Color-coded logs (PASS / FAIL)

---

## 🛠️ Tech Stack

- **Language:** Python  
- **GUI Framework:** Tkinter  
- **Modules Used:**
  - tkinter
  - scrolledtext
  - time

---

## 📂 Project Structure

project/
│
├── main.py                # Main dashboard application
├── test_cases.py         # Contains all test functions
├── report_generator.py   # Generates HTML reports
└── README.md             # Project documentation

---

## ⚙️ How It Works

The application provides a graphical dashboard to run predefined automation tests.

- Clicking **Run Tests** executes test cases:
  - Switch to Netflix
  - Sync Failure Scenario
  - Volume Increase  

- Results are:
  - Logged in the console
  - Displayed in stat cards (Total, Passed, Failed, Time)

- Clicking **Generate Report** creates an HTML report.

---

## 🧪 Test Cases Included

| Test Case Name           | Description                      |
|------------------------|----------------------------------|
| Switch to Netflix      | Verifies app switching behavior  |
| Sync Failure Scenario  | Handles sync failure conditions  |
| Volume Increase        | Checks volume control feature    |

---

## 🖥️ UI Components

- **Sidebar**
  - Run Tests
  - Generate Report
  - Reset Dashboard  

- **Main Dashboard**
  - Title Header
  - Stat Cards:
    - Total Tests
    - Passed
    - Failed
    - Execution Time  

- **Console**
  - Displays logs with colored output:
    - Green → PASS
    - Red → FAIL

---

## 📄 Report Generation

The system generates an HTML report using:

ReportGenerator(self.results)

This includes:
- Test summary
- Pass/Fail status
- Execution details

---

## ▶️ How to Run

1. Install Python (3.x)
2. Clone or download the project
3. Run the application:

python main.py

---

## 🔄 Dashboard Functionalities

### Run Tests
- Executes all test cases
- Updates UI with results

### Generate Report
- Creates HTML report
- Requires tests to be executed first

### Reset
- Clears results and logs
- Resets all stats

---

## 🎯 Use Cases

- QA Automation Dashboard  
- Smart TV Application Testing  
- iPad App Testing  
- Manual + Automated Testing Hybrid Tools  

---

## 🔮 Future Enhancements

- Integration with Selenium / Playwright  
- Export reports to PDF/Excel  
- Add test scheduling  
- Cloud-based test execution  
- Database integration for history tracking  

---

## 👨‍💻 Author

Garv Mehra  
B.Tech CSE | QA & Automation Enthusiast  
