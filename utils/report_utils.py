"""
utils/report_utils.py
Simple HTML Report Generator
"""

import os
import json

from datetime import datetime


class ReportUtils:

    REPORTS_DIR = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "reports"
    )

    LOG_FILE = os.path.join(
        REPORTS_DIR,
        "test_log.json"
    )

    REPORT_FILE = os.path.join(
        REPORTS_DIR,
        "summary.html"
    )

    @staticmethod
    def ensure_reports_dir():

        os.makedirs(
            ReportUtils.REPORTS_DIR,
            exist_ok=True
        )

    @staticmethod
    def log_test_result(
            test_name,
            status,
            message=""
    ):

        ReportUtils.ensure_reports_dir()

        logs = []

        if os.path.exists(
                ReportUtils.LOG_FILE
        ):

            try:

                with open(
                        ReportUtils.LOG_FILE,
                        "r"
                ) as file:

                    logs = json.load(file)

            except json.JSONDecodeError:

                logs = []

        logs.append({
            "test": test_name,
            "status": status.upper(),
            "message": message,
            "time": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        })

        with open(
                ReportUtils.LOG_FILE,
                "w"
        ) as file:

            json.dump(
                logs,
                file,
                indent=4
            )

    @staticmethod
    def generate_summary_report():

        if not os.path.exists(
                ReportUtils.LOG_FILE
        ):

            return

        with open(
                ReportUtils.LOG_FILE,
                "r"
        ) as file:

            logs = json.load(file)

        passed = sum(
            1 for log in logs
            if log["status"] == "PASS"
        )

        failed = sum(
            1 for log in logs
            if log["status"] == "FAIL"
        )

        html = f"""
        <html>

        <head>
            <title>
                Parabank Report
            </title>
        </head>

        <body style="font-family:Arial;">

            <h1>
                Parabank Automation Report
            </h1>

            <h3>
                Total: {len(logs)}
            </h3>

            <h3 style="color:green;">
                Passed: {passed}
            </h3>

            <h3 style="color:red;">
                Failed: {failed}
            </h3>

            <table border="1" cellpadding="10">

                <tr>
                    <th>Test</th>
                    <th>Status</th>
                    <th>Message</th>
                    <th>Time</th>
                </tr>
        """

        for log in logs:

            color = (
                "green"
                if log["status"] == "PASS"
                else "red"
            )

            html += f"""
                <tr>

                    <td>{log['test']}</td>

                    <td style="color:{color};">
                        {log['status']}
                    </td>

                    <td>{log['message']}</td>

                    <td>{log['time']}</td>

                </tr>
            """

        html += """

            </table>

        </body>

        </html>
        """

        with open(
                ReportUtils.REPORT_FILE,
                "w",
                encoding="utf-8"
        ) as file:

            file.write(html)

        print(
            f"\n📊 Report Generated:"
            f"\n{ReportUtils.REPORT_FILE}"
        )
