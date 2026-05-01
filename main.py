from report_generator import ReportGenerator
from test_cases import test_switch_to_netflix, test_volume_increase

class TestRunner:
    def __init__(self):
        self.results = []

    def run_test(self, test_function, test_name):
        print(f"\nExecuting: {test_name}")
        result = test_function()
        self.results.append((test_name, result))

    def summary(self):
        print("\n========== TEST SUMMARY ==========")
        for name, result in self.results:
            print(f"{name}: {result}")

        total = len(self.results)
        passed = len([r for r in self.results if r[1] == "PASS"])

        print("\nTotal Tests:", total)
        print("Passed:", passed)
        print("Failed:", total - passed)


if __name__ == "__main__":
    print("Starting Test Execution...\n")

    runner = TestRunner()

    runner.run_test(test_switch_to_netflix, "Switch to Netflix")
    runner.run_test(test_volume_increase, "Volume Increase")

    runner.summary()

report = ReportGenerator(runner.results)
report.generate_html_report()

