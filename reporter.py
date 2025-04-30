import pandas as pd

def generate_report(comparison_results, report_path="comparison_report.csv"):
    df = pd.DataFrame(comparison_results)
    df.to_csv(report_path, index=False)
    print(f"Report saved to {report_path}")
