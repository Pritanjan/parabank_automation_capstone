"""
utils/report_utils.py
Custom HTML Report Generator for Banking Automation Suite
"""

import os
import json
from datetime import datetime


class ReportUtils:
    REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")

    @staticmethod
    def ensure_reports_dir():
        os.makedirs(ReportUtils.REPORTS_DIR, exist_ok=True)

    @staticmethod
    def log_test_result(test_name: str, status: str, message: str = ""):
        """Append a test result to a JSON log."""
        ReportUtils.ensure_reports_dir()
        log_file = os.path.join(ReportUtils.REPORTS_DIR, "test_log.json")

        entry = {
            "test": test_name,
            "status": status,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }

        logs = []
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []

        logs.append(entry)
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2)

    @staticmethod
    def generate_summary_report():
        """Generate a summary HTML from test_log.json."""
        log_file = os.path.join(ReportUtils.REPORTS_DIR, "test_log.json")
        if not os.path.exists(log_file):
            return

        with open(log_file, "r") as f:
            logs = json.load(f)

        passed = sum(1 for l in logs if l["status"] == "PASS")
        failed = sum(1 for l in logs if l["status"] == "FAIL")
        total = len(logs)

        html = f"""
        <html><head><title>Banking Test Summary</title></head>
        <body style="font-family: Arial;">
        <h1>Banking Automation Summary</h1>
        <p>Total: {total} | Passed: {passed} | Failed: {failed}</p>
        <table border="1" cellpadding="5">
        <tr><th>Test</th><th>Status</th><th>Message</th><th>Time</th></tr>
        """
        for log in logs:
            color = "green" if log["status"] == "PASS" else "red"
            html += f"""
            <tr>
                <td>{log['test']}</td>
                <td style="color:{color}"><b>{log['status']}</b></td>
                <td>{log['message']}</td>
                <td>{log['timestamp']}</td>
            </tr>"""

        html += "</table></body></html>"

        summary_path = os.path.join(ReportUtils.REPORTS_DIR, "summary.html")
        with open(summary_path, "w") as f:
            f.write(html)
        print(f"\n📊 Summary report: {summary_path}")