from datetime import datetime
import os
import webbrowser


class ReportGenerator:
    def __init__(self, results):
        self.results = results

    def generate_html_report(self):
        total = len(self.results)
        passed = len([r for r in self.results if r[1] == "PASS"])
        failed = total - passed

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        readable_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create reports folder if not exists
        os.makedirs("reports", exist_ok=True)

        filename = f"reports/test_report_{timestamp}.html"

        html_content = f"""
        <html>
        <head>
            <title>Smart TV Test Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f7;
                    padding: 30px;
                }}
                h2 {{
                    color: #2c3e50;
                }}
                table {{
                    border-collapse: collapse;
                    width: 80%;
                    background-color: white;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 12px;
                    text-align: center;
                }}
                th {{
                    background-color: #34495e;
                    color: white;
                }}
                .pass {{
                    color: green;
                    font-weight: bold;
                }}
                .fail {{
                    color: red;
                    font-weight: bold;
                }}
                .summary {{
                    margin-top: 20px;
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>
            <h2>Smart TV & iPad Automation Test Report</h2>
            <p><strong>Execution Time:</strong> {readable_time}</p>

            <table>
                <tr>
                    <th>Test Case</th>
                    <th>Status</th>
                </tr>
        """

        # Add test results
        for name, result in self.results:
            css_class = "pass" if result == "PASS" else "fail"
            html_content += f"""
                <tr>
                    <td>{name}</td>
                    <td class="{css_class}">{result}</td>
                </tr>
            """

        # Add summary
        html_content += f"""
            </table>

            <div class="summary">
                <h3>Summary</h3>
                <p>Total Tests: {total}</p>
                <p>Passed: {passed}</p>
                <p>Failed: {failed}</p>
            </div>

        </body>
        </html>
        """

        # Write HTML file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)

        # Convert to absolute Windows-safe path
        absolute_path = os.path.abspath(filename)
        file_url = "file:///" + absolute_path.replace("\\", "/")

        # Open in default browser
        webbrowser.open_new_tab(file_url)

        print("HTML Report Generated:", absolute_path)
