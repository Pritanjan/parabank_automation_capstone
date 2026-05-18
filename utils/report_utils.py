"""
utils/report_utils.py
Custom HTML Report Generator for Banking Automation Suite
"""

import os
import json
from datetime import datetime


class ReportUtils:

    REPORTS_DIR = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "reports"
    )

    @staticmethod
    def ensure_reports_dir():
        os.makedirs(ReportUtils.REPORTS_DIR, exist_ok=True)

    @staticmethod
    def log_test_result(test_name: str, status: str, message: str = ""):

        ReportUtils.ensure_reports_dir()

        log_file = os.path.join(
            ReportUtils.REPORTS_DIR,
            "test_log.json"
        )

        entry = {
            "test": test_name,
            "status": status,
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        logs = []

        if os.path.exists(log_file):

            try:
                with open(log_file, "r") as f:
                    logs = json.load(f)

            except (json.JSONDecodeError, FileNotFoundError):
                logs = []

        logs.append(entry)

        with open(log_file, "w") as f:
            json.dump(logs, f, indent=4)

    @staticmethod
    def generate_summary_report():

        log_file = os.path.join(
            ReportUtils.REPORTS_DIR,
            "test_log.json"
        )

        if not os.path.exists(log_file):
            print("No test log found.")
            return

        with open(log_file, "r") as f:
            logs = json.load(f)

        passed = sum(
            1 for log in logs
            if log["status"].upper() == "PASS"
        )

        failed = sum(
            1 for log in logs
            if log["status"].upper() == "FAIL"
        )

        total = len(logs)

        html_content = f"""
        <html>
        <head>
            <title>Banking Automation Report</title>
        </head>

        <body style="font-family: Arial; padding: 20px;">

            <h1>Parabank Automation Summary</h1>

            <h3>
                Total Tests: {total}
            </h3>

            <h3 style="color:green;">
                Passed: {passed}
            </h3>

            <h3 style="color:red;">
                Failed: {failed}
            </h3>

            <table border="1" cellpadding="10" cellspacing="0">

                <tr>
                    <th>Test Name</th>
                    <th>Status</th>
                    <th>Message</th>
                    <th>Timestamp</th>
                </tr>
        """

        for log in logs:

            color = "green" if log["status"].upper() == "PASS" else "red"

            html_content += f"""
                <tr>
                    <td>{log['test']}</td>

                    <td style="color:{color};">
                        <b>{log['status']}</b>
                    </td>

                    <td>{log['message']}</td>

                    <td>{log['timestamp']}</td>
                </tr>
            """

        html_content += """
            </table>
        </body>
        </html>
        """

        summary_path = os.path.join(
            ReportUtils.REPORTS_DIR,
            "summary.html"
        )

        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"\n📊 Summary report generated: {summary_path}")