import tkinter as tk
from tkinter import scrolledtext
import time
from test_cases import (
    test_switch_to_netflix,
    test_volume_increase,
    test_sync_failure
)
from report_generator import ReportGenerator


class ModernTestDashboard:

    def __init__(self, root):
        self.root = root
        self.root.title("Smart TV & iPad Testing Framework")
        self.root.geometry("1100x700")
        self.root.configure(bg="#1a1a2e")

        self.results = []
        self.start_time = None

        self.create_layout()

    # ------------------ LAYOUT ------------------
    def create_layout(self):

        # ================= SIDEBAR =================
        sidebar = tk.Frame(self.root, bg="#111122", width=240)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Label(sidebar,
                 text="Automation\nDashboard",
                 bg="#111122",
                 fg="white",
                 font=("Segoe UI", 18, "bold"),
                 justify="center").pack(pady=40)

        self.create_button(sidebar, "Run Tests", self.run_tests)
        self.create_button(sidebar, "Generate Report", self.generate_report)
        self.create_button(sidebar, "Reset", self.reset_dashboard)

        # ================= MAIN AREA =================
        main = tk.Frame(self.root, bg="#1a1a2e")
        main.pack(side="right", fill="both", expand=True)

        tk.Label(main,
                 text="Smart TV & iPad Testing Framework",
                 bg="#1a1a2e",
                 fg="white",
                 font=("Segoe UI", 24, "bold")).pack(pady=30)

        # ================= STAT CARDS =================
        stats_frame = tk.Frame(main, bg="#1a1a2e")
        stats_frame.pack(pady=10)

        self.total_card = self.create_stat_card(stats_frame, "Total Tests", "0", "#4e73df")
        self.pass_card = self.create_stat_card(stats_frame, "Passed", "0", "#1cc88a")
        self.fail_card = self.create_stat_card(stats_frame, "Failed", "0", "#e74a3b")
        self.time_card = self.create_stat_card(stats_frame, "Execution Time", "0s", "#f6c23e")

        # ================= CONSOLE =================
        self.console = scrolledtext.ScrolledText(
            main,
            height=18,
            font=("Consolas", 11),
            bg="#0f0f1a",
            fg="white",
            insertbackground="white",
            borderwidth=0
        )
        self.console.pack(padx=50, pady=30, fill="both", expand=True)

        # 🔥 Color Tags for PASS / FAIL
        self.console.tag_config("PASS", foreground="#1cc88a")  # Green
        self.console.tag_config("FAIL", foreground="#e74a3b")  # Red
        self.console.tag_config("INFO", foreground="white")    # Normal

    # ------------------ BUTTON ------------------
    def create_button(self, parent, text, command):
        btn = tk.Button(parent,
                        text=text,
                        command=command,
                        bg="#4e73df",
                        fg="white",
                        font=("Segoe UI", 11, "bold"),
                        relief="flat",
                        padx=10,
                        pady=12,
                        activebackground="#2e59d9",
                        activeforeground="white",
                        cursor="hand2")
        btn.pack(pady=15, fill="x", padx=25)

    # ------------------ STAT CARD ------------------
    def create_stat_card(self, parent, title, value, color):
        card = tk.Frame(parent,
                        bg=color,
                        width=220,
                        height=110)
        card.pack_propagate(False)
        card.pack(side="left", padx=20)

        tk.Label(card,
                 text=title,
                 bg=color,
                 fg="white",
                 font=("Segoe UI", 12, "bold")).pack(pady=(20, 5))

        label = tk.Label(card,
                         text=value,
                         bg=color,
                         fg="white",
                         font=("Segoe UI", 22, "bold"))
        label.pack()

        return label

    # ------------------ LOG ------------------
    def log(self, message, tag="INFO"):
        self.console.insert(tk.END, message + "\n", tag)
        self.console.see(tk.END)

    # ------------------ RUN TESTS ------------------
    def run_tests(self):
        self.console.delete("1.0", tk.END)
        self.results.clear()

        self.start_time = time.time()

        self.log("🚀 Running Automation Tests...\n", "INFO")

        tests = [
            ("Switch to Netflix", test_switch_to_netflix),
            ("Sync Failure Scenario", test_sync_failure),
            ("Volume Increase", test_volume_increase)
        ]

        for name, test in tests:
            result = test()
            self.results.append((name, result))

        self.update_dashboard()

    # ------------------ UPDATE DASHBOARD ------------------
    def update_dashboard(self):
        total = len(self.results)
        passed = len([r for r in self.results if r[1] == "PASS"])
        failed = total - passed
        execution_time = round(time.time() - self.start_time, 2)

        self.total_card.config(text=str(total))
        self.pass_card.config(text=str(passed))
        self.fail_card.config(text=str(failed))
        self.time_card.config(text=f"{execution_time}s")

        self.log("\n===== TEST SUMMARY =====", "INFO")

        for name, result in self.results:
            if result == "PASS":
                self.log(f"✅ {name}: {result}", "PASS")
            else:
                self.log(f"❌ {name}: {result}", "FAIL")

        if failed == 0:
            self.log("\n✅ All Tests Passed Successfully!", "PASS")
        else:
            self.log("\n❌ Some Tests Failed!", "FAIL")

    # ------------------ GENERATE REPORT ------------------
    def generate_report(self):
        if not self.results:
            self.log("⚠️ Run tests before generating report.", "INFO")
            return

        report = ReportGenerator(self.results)
        report.generate_html_report()
        self.log("📄 Report Generated Successfully.", "INFO")

    # ------------------ RESET ------------------
    def reset_dashboard(self):
        self.results.clear()
        self.console.delete("1.0", tk.END)

        self.total_card.config(text="0")
        self.pass_card.config(text="0")
        self.fail_card.config(text="0")
        self.time_card.config(text="0s")

        self.log("Dashboard Reset Completed.", "INFO")


if __name__ == "__main__":
    root = tk.Tk()
    app = ModernTestDashboard(root)
    root.mainloop()
