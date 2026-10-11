import os
import sys
import json
import time
import shutil
import subprocess
import pandas as pd

CODEQL_DIR = r"d:\Projects\securityAI\security AI\scratch\codeql_env"
CODEQL_BIN = os.path.join(CODEQL_DIR, "codeql", "codeql.exe" if os.name == "nt" else "codeql")
QUERY_SUITE = "codeql/python-queries:codeql-suites/python-security-extended.qls"
TESTS_OUT = r"d:\Projects\securityAI\security AI\results\controls"
os.makedirs(TESTS_OUT, exist_ok=True)

# 1. Test Snippets
POSITIVE_CODE = '''from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/redirect")
def vulnerable_redirect():
    # CWE-601: URL redirection from remote source
    target = request.args.get("url")
    return redirect(target)

if __name__ == "__main__":
    # CWE-215: Flask app is run in debug mode
    app.run(debug=True)
'''

NEGATIVE_CODE = '''from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/redirect")
def safe_redirect():
    # Safe negative control: Static constant internal redirect
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=False)
'''

def run_control_test(name, code):
    print(f"\n--- Testing Control: {name} ---")
    t0 = time.time()
    src_dir = os.path.join(TESTS_OUT, f"src_{name}")
    db_dir = os.path.join(TESTS_OUT, f"db_{name}")
    sarif_file = os.path.join(TESTS_OUT, f"{name}.sarif")
    csv_file = os.path.join(TESTS_OUT, f"{name}.csv")
    
    if os.path.exists(src_dir): shutil.rmtree(src_dir)
    if os.path.exists(db_dir): shutil.rmtree(db_dir)
    os.makedirs(src_dir, exist_ok=True)
    
    with open(os.path.join(src_dir, "test.py"), "w", encoding="utf-8") as f:
        f.write(code)
        
    print(f"Creating database for {name}...")
    subprocess.run([CODEQL_BIN, "database", "create", db_dir, "--language=python", f"--source-root={src_dir}"], check=True, capture_output=True)
    
    print(f"Analyzing {name} (CSV)...")
    subprocess.run([CODEQL_BIN, "database", "analyze", db_dir, "--format=csv", f"--output={csv_file}", QUERY_SUITE, "--warnings=hide"], check=True, capture_output=True)
    
    print(f"Analyzing {name} (SARIF)...")
    subprocess.run([CODEQL_BIN, "database", "analyze", db_dir, "--format=sarif-latest", f"--output={sarif_file}", QUERY_SUITE, "--warnings=hide"], check=True, capture_output=True)
    
    # Parse SARIF
    sarif_alerts = []
    if os.path.exists(sarif_file):
        with open(sarif_file, "r", encoding="utf-8") as f:
            sarif_data = json.load(f)
        runs = sarif_data.get("runs", [])
        if runs:
            for result in runs[0].get("results", []):
                sarif_alerts.append({
                    "rule_id": result.get("ruleId"),
                    "message": result.get("message", {}).get("text"),
                    "level": result.get("level", "warning")
                })
                
    # Parse CSV
    csv_alerts = []
    if os.path.exists(csv_file):
        try:
            df = pd.read_csv(csv_file, names=["Name", "Description", "Severity", "Message", "Path", "StartLine", "StartCol", "EndLine", "EndCol"])
            for _, row in df.iterrows():
                csv_alerts.append({"rule": str(row["Name"]), "severity": str(row["Severity"]), "msg": str(row["Message"])})
        except Exception:
            pass
            
    duration = time.time() - t0
    print(f"Completed {name} in {duration:.1f}s. SARIF alerts: {len(sarif_alerts)}, CSV alerts: {len(csv_alerts)}")
    return sarif_alerts, csv_alerts, duration

if __name__ == "__main__":
    pos_sarif, pos_csv, t_pos = run_control_test("known_positive", POSITIVE_CODE)
    neg_sarif, neg_csv, t_neg = run_control_test("known_negative", NEGATIVE_CODE)
    
    print("\n" + "="*50)
    print("CONTROL VALIDATION RESULTS:")
    print("="*50)
    print(f"Known-Positive Alerts: {len(pos_sarif)} SARIF / {len(pos_csv)} CSV")
    for a in pos_sarif:
        print(f"  -> Rule: {a['rule_id']} | Message: {a['message']}")
    print(f"Known-Negative Alerts: {len(neg_sarif)} SARIF / {len(neg_csv)} CSV")
    
    # Validation checks
    assert len(pos_sarif) > 0 or len(pos_csv) > 0, "Known positive failed: Expected security findings!"
    assert len(neg_sarif) == 0 and len(neg_csv) == 0, "Known negative failed: Expected zero security findings!"
    print("\nSUCCESS: CodeQL controls passed and SARIF/CSV parser verified.")
