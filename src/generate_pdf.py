import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PDF_PATH = os.path.join(BASE_DIR, "paper", "research_paper.pdf")
FIG_DIR = os.path.join(BASE_DIR, "paper", "figures")

doc = SimpleDocTemplate(
    PDF_PATH,
    pagesize=letter,
    leftMargin=54,
    rightMargin=54,
    topMargin=50,
    bottomMargin=50
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "DocTitle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=16,
    leading=20,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#0f172a")
)

subtitle_style = ParagraphStyle(
    "DocSubtitle",
    parent=styles["Normal"],
    fontName="Helvetica-Oblique",
    fontSize=11,
    leading=15,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#334155"),
    spaceAfter=6
)

author_style = ParagraphStyle(
    "AuthorStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10.5,
    leading=14,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#1e293b")
)

affil_style = ParagraphStyle(
    "AffilStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=8.5,
    leading=12,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#475569")
)

h1_style = ParagraphStyle(
    "H1Style",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=12,
    leading=16,
    textColor=colors.HexColor("#0f172a"),
    spaceBefore=12,
    spaceAfter=5,
    keepWithNext=True
)

h2_style = ParagraphStyle(
    "H2Style",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=10,
    leading=14,
    textColor=colors.HexColor("#1e293b"),
    spaceBefore=8,
    spaceAfter=4,
    keepWithNext=True
)

body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9,
    leading=13,
    alignment=TA_JUSTIFY,
    textColor=colors.HexColor("#1e293b"),
    spaceAfter=5
)

abstract_style = ParagraphStyle(
    "AbstractStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Oblique",
    fontSize=8.5,
    leading=12,
    alignment=TA_JUSTIFY,
    textColor=colors.HexColor("#1e293b")
)

caption_style = ParagraphStyle(
    "CaptionStyle",
    parent=styles["Normal"],
    fontName="Helvetica-Oblique",
    fontSize=8,
    leading=10.5,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#475569"),
    spaceBefore=3,
    spaceAfter=6
)

table_header_style = ParagraphStyle(
    "TableHeader",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8,
    leading=10,
    textColor=colors.white,
    alignment=TA_CENTER
)

table_body_style = ParagraphStyle(
    "TableBody",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.5,
    leading=9.5,
    textColor=colors.HexColor("#1e293b"),
    alignment=TA_CENTER
)

story = []

# Title & Metadata
story.append(Paragraph("The Whack-a-Mole Effect in AI Code Repair: Static-Analysis Findings and Code Complexity After Scanner-Guided Fixes", title_style))
story.append(Spacer(1, 3))
story.append(Paragraph("A Preliminary Pilot Study and Empirical Feasibility Assessment", subtitle_style))
story.append(Paragraph("<b>Anunay Naman</b>", author_style))
story.append(Paragraph("Department of Computer Science & Engineering<br/>Punjab Engineering College (Deemed to be University), Chandigarh, India<br/>Email: anunaynaman@pec.edu.in | Repository: github.com/jackyhitter/AI_security_report", affil_style))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#cbd5e1"), spaceAfter=8))

# Abstract Box
abstract_text = (
    "<b>Abstract—</b>Large language models specialized for software engineering frequently generate code containing security weaknesses. "
    "A widely proposed mitigation strategy is <i>scanner-guided repair</i>, wherein a static analysis tool inspects generated code and feeds diagnostic "
    "alerts back to the model for iterative fixing. In this preliminary working paper, we empirically investigate the <b>'Whack-a-Mole' hypothesis</b>: "
    "when an AI model repairs Python code using actual static-analysis findings, does it eliminate original alerts, leave findings unresolved, "
    "introduce new secondary findings, or increase structural code complexity? We deploy an automated pipeline integrating LLMSecEval, official GitHub CodeQL CLI "
    "(52 security and taint-tracking queries), and the open-weight <b>Qwen2.5-Coder-1.5B-Instruct</b> model across three controlled conditions: "
    "<i>(A) Baseline</i>, <i>(B) Security-aware prompt prefixing</i>, and <i>(C) Closed-loop scanner-guided repair</i>. "
    "Before execution, we validate the CodeQL harness against ground-truth positive (Flask untrusted redirect in debug mode) and negative controls, confirming identical detection across CSV and SARIF outputs. "
    "In an initial pilot evaluation (<i>N</i> = 3 Python tasks from LLMSecEval), we find that: (1) security-aware prompting was completely ineffective at suppressing baseline alerts (100% alert persistence across all 4 baseline alert instances); "
    "(2) scanner-guided repair resolved a localized configuration flaw (<code>py/flask-debug</code>, 1/4 alerts, 25.0% resolution rate), but failed to eliminate dataflow taint-tracking alerts (<code>py/url-redirection</code>, 3/4 alerts, 75.0% persistence rate); "
    "(3) no new secondary findings were introduced in evaluable cases (New = 0); and (4) Radon cyclomatic complexity and logical lines of code remained unchanged (ΔCC = 0, ΔLOC = 0). "
    "While limited by pilot sample size, these preliminary findings suggest that naive diagnostic feedback enables models to patch literal configuration flags but fails to prompt architectural sanitization for dataflow vulnerabilities.<br/><br/>"
    "<b>Keywords—</b>AI Code Generation, Automated Program Repair, Static Analysis, CodeQL, Vulnerability Remediation, Whack-a-Mole Effect."
)

t_abstract = Table([[Paragraph(abstract_text, abstract_style)]], colWidths=[500])
t_abstract.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#94a3b8")),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(t_abstract)
story.append(Spacer(1, 10))

# Section 1
story.append(Paragraph("1. Introduction", h1_style))
story.append(Paragraph(
    "Large Language Models (LLMs) accelerate code production but regularly generate security defects, with foundational studies reporting that "
    "approximately 40% of generated snippets contain Common Weakness Enumerations (CWEs) (Pearce et al., 2022; Tony et al., 2023). "
    "To address this, developers deploy <i>Security-Aware Prompting</i> or <i>Scanner-Guided Repair</i>, wherein static analysis diagnostics "
    "are fed back to the LLM. However, program repair practitioners observe a potential drawback termed the <b>'Whack-a-Mole' effect</b>: "
    "fixing one static alert may cause models to introduce secondary bugs, shift taint sinks, or inflate code complexity without eliminating the underlying weakness. "
    "This preliminary working paper investigates this phenomenon in an initial feasibility pilot ($N=3$ Python tasks from LLMSecEval).",
    body_style
))
story.append(Paragraph("<b>Research Questions:</b>", h2_style))
story.append(Paragraph("• <b>RQ1 (Resolution vs. Persistence):</b> To what extent does feeding authentic CodeQL static-analysis findings back to the model eliminate versus preserve original alert instances?", body_style))
story.append(Paragraph("• <b>RQ2 (Secondary Findings):</b> Does scanner-guided repair introduce new, distinct static-analysis findings not present in baseline code?", body_style))
story.append(Paragraph("• <b>RQ3 (Structural Code Complexity):</b> Does scanner-guided repair alter structural complexity, measured by Cyclomatic Complexity (CC) and Logical Lines of Code (LOC)?", body_style))

# Section 2 & 3
story.append(Paragraph("2. Experimental Methodology and Ground-Truth Controls", h1_style))
story.append(Paragraph(
    "We evaluate three conditions: <b>Condition A (Baseline)</b> generates code directly from the natural language prompt; "
    "<b>Condition B (Security-Aware)</b> appends an explicit security constraint; and "
    "<b>Condition C (Scanner-Guided Repair)</b> provides authentic CodeQL static-analysis diagnostics (rule IDs, descriptions, line numbers) back to the model to repair Condition A code. "
    "Evaluations use the standalone <b>GitHub CodeQL CLI</b> (v2.24.x) executing the official <code>python-security-extended.qls</code> suite (52 rules). "
    "Before experimental runs, we verified the scanner against ground-truth controls: the known-positive control (Flask untrusted redirect in debug mode) triggered exactly 2 alerts (<code>py/flask-debug</code> and <code>py/url-redirection</code>) verified across both SARIF and CSV outputs; "
    "the known-negative control (static internal redirect) triggered 0 alerts, confirming 100% precision on baseline controls.",
    body_style
))
story.append(Paragraph(
    "<b>Model Attribution:</b> Local feasibility was evaluated using <b>Qwen/Qwen2.5-Coder-1.5B-Instruct</b> (revision: main, $T=0.2$, seed=42). "
    "This model was selected during local host execution due to 15 GB contiguous RAM allocation thresholds for 32-bit float loading of 7B models on CPU. "
    "All reported findings stem strictly from this 1.5B model run; results from different model sizes are never conflated.",
    body_style
))

# Section 4: Results
story.append(Paragraph("3. Empirical Pilot Results", h1_style))

# Table 1: Audited Summary Table
t1_data = [
    [Paragraph("<b>Condition</b>", table_header_style),
     Paragraph("<b>Tasks Evaluated</b>", table_header_style),
     Paragraph("<b>Tasks w/ Alerts</b>", table_header_style),
     Paragraph("<b>Total Alert Instances</b>", table_header_style),
     Paragraph("<b>Mean Alerts / Task</b>", table_header_style),
     Paragraph("<b>Resolution Rate</b>", table_header_style),
     Paragraph("<b>Persistence Rate</b>", table_header_style),
     Paragraph("<b>Mean CC / LOC</b>", table_header_style)],
    [Paragraph("Condition A: Baseline", table_body_style), Paragraph("3", table_body_style), Paragraph("2", table_body_style), Paragraph("4", table_body_style), Paragraph("1.33", table_body_style), Paragraph("—", table_body_style), Paragraph("—", table_body_style), Paragraph("1.33 / 11.0", table_body_style)],
    [Paragraph("Condition B: Security-Aware", table_body_style), Paragraph("3", table_body_style), Paragraph("2", table_body_style), Paragraph("4", table_body_style), Paragraph("1.33", table_body_style), Paragraph("0.0% (0/4)", table_body_style), Paragraph("100.0% (4/4)", table_body_style), Paragraph("1.33 / 11.0", table_body_style)],
    [Paragraph("Condition C: Scanner Repair", table_body_style), Paragraph("3", table_body_style), Paragraph("2", table_body_style), Paragraph("3", table_body_style), Paragraph("1.00", table_body_style), Paragraph("<b>25.0% (1/4)</b>", table_body_style), Paragraph("<b>75.0% (3/4)</b>", table_body_style), Paragraph("1.33 / 11.0", table_body_style)],
]
t1 = Table(t1_data, colWidths=[120, 50, 50, 60, 55, 65, 65, 55])
t1.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e293b")),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(Paragraph("<b>Table 1:</b> Aggregated Empirical Metrics Across Experimental Conditions (Pilot $N=3$)", h2_style))
story.append(t1)
story.append(Spacer(1, 8))

# Table 2: Task-Level Audit Table
t2_data = [
    [Paragraph("<b>Task ID</b>", table_header_style),
     Paragraph("<b>CWE</b>", table_header_style),
     Paragraph("<b>Base Alerts</b>", table_header_style),
     Paragraph("<b>Sec Alerts</b>", table_header_style),
     Paragraph("<b>Repair Alerts</b>", table_header_style),
     Paragraph("<b>Disappeared Rules</b>", table_header_style),
     Paragraph("<b>Persisted Rules</b>", table_header_style),
     Paragraph("<b>New Rules</b>", table_header_style),
     Paragraph("<b>CC / LOC</b>", table_header_style),
     Paragraph("<b>Outcome</b>", table_header_style)],
    [Paragraph("CWE-20_IIV-1a", table_body_style), Paragraph("CWE-20", table_body_style), Paragraph("0", table_body_style), Paragraph("0", table_body_style), Paragraph("0", table_body_style), Paragraph("None (0)", table_body_style), Paragraph("None (0)", table_body_style), Paragraph("0", table_body_style), Paragraph("0 / 10", table_body_style), Paragraph("Clean Baseline", table_body_style)],
    [Paragraph("CWE-20_IIV-1b", table_body_style), Paragraph("CWE-20", table_body_style), Paragraph("2", table_body_style), Paragraph("2", table_body_style), Paragraph("2", table_body_style), Paragraph("None (0)", table_body_style), Paragraph("Debug, Redirect", table_body_style), Paragraph("0", table_body_style), Paragraph("2 / 11", table_body_style), Paragraph("Unresolved (0/2 fixed)", table_body_style)],
    [Paragraph("CWE-20_IIV-1c", table_body_style), Paragraph("CWE-20", table_body_style), Paragraph("2", table_body_style), Paragraph("2", table_body_style), Paragraph("1", table_body_style), Paragraph("Debug (1)", table_body_style), Paragraph("Redirect (1)", table_body_style), Paragraph("0", table_body_style), Paragraph("2 / 12", table_body_style), Paragraph("Partial Fix (1/2 fixed)", table_body_style)],
]
t2 = Table(t2_data, colWidths=[75, 45, 40, 40, 40, 65, 75, 30, 40, 65])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e293b")),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ('TOPPADDING', (0,0), (-1,-1), 3),
    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
]))
story.append(Paragraph("<b>Table 2:</b> Granular Task-Level Empirical Audit Trail", h2_style))
story.append(t2)
story.append(Spacer(1, 10))

# Figures
fig1_p = os.path.join(FIG_DIR, "condition_alert_comparison.png")
if os.path.exists(fig1_p):
    story.append(Image(fig1_p, width=390, height=210))
    story.append(Paragraph("<b>Figure 1:</b> CodeQL static-analysis alert counts across experimental conditions ($N=3$ pilot tasks).", caption_style))

fig2_p = os.path.join(FIG_DIR, "repair_alert_breakdown.png")
if os.path.exists(fig2_p):
    story.append(Image(fig2_p, width=320, height=205))
    story.append(Paragraph("<b>Figure 2:</b> Outcome distribution of baseline alert instances under scanner repair (Denominator $N=4$ baseline alerts across 2 evaluable tasks).", caption_style))

# Section 5 & 6
story.append(Paragraph("4. Discussion & Limitations", h1_style))
story.append(Paragraph(
    "<b>Configuration vs. Dataflow Discrepancy:</b> A key hypothesis-generating observation from this pilot is that scanner-guided repair "
    "operates asymmetrically across vulnerability categories. In task <code>CWE-20_IIV-1c</code>, the model readily fixed the configuration flaw "
    "(<code>py/flask-debug</code>) by changing literal parameters (<code>debug=False</code>). However, dataflow taint-tracking findings "
    "(<code>py/url-redirection</code>, CWE-601) persisted across all repair attempts. Repairing dataflow flaws requires inserting active validation "
    "or domain whitelisting, which naive diagnostic text fails to elicit.<br/>"
    "<b>Vulnerability Inertia:</b> In this sample, zero new distinct rules were introduced (New = 0). The primary failure mode was vulnerability inertia "
    "rather than secondary bug explosion. Complexity remained unchanged (CC = 2, LOC = 11–12), explaining why taint alerts persisted: no validation branches were added.<br/>"
    "<b>Threats to Validity:</b> This study is strictly a pilot ($N=3$). Findings cannot be generalized to the entire 83-task benchmark or other model architectures without scaled cloud GPU execution. "
    "Static-analysis alerts represent code patterns rather than confirmed dynamic exploits, and functional correctness was not evaluated via dynamic test suites.",
    body_style
))

story.append(Paragraph("5. Conclusion", h1_style))
story.append(Paragraph(
    "This preliminary pilot establishes an automated, reproducible closed-loop evaluation harness. Preliminary evidence suggests that general security "
    "prompting is ineffective, and raw SAST feedback repairs superficial configuration flags but struggles with architectural dataflow taint vulnerabilities. "
    "Future work will execute the full 83-task benchmark on cloud GPU resources and explore few-shot AST sanitizer templates.",
    body_style
))

story.append(Paragraph("References", h1_style))
refs = [
    "1. Pearce, H., et al. (2022). Asleep at the keyboard? Assessing the security of GitHub Copilot's code contributions. In <i>IEEE S&P</i>. DOI: 10.1109/SP46214.2022.9833571",
    "2. Tony, C., et al. (2023). LLMSecEval: A dataset of natural language prompts for security evaluations of LLMs. In <i>IEEE/ACM MSR</i>. DOI: 10.1109/MSR59073.2023.00084",
    "3. Siddiq, M. L., & Santos, J. C. (2022). SecurityEval: A benchmark of security-oriented code generation prompts. In <i>MSR4P&S</i>. DOI: 10.1145/3549035.3561184",
    "4. Khoury, R., et al. (2023). How secure is AI-generated code? A study of ChatGPT's security awareness. <i>IEEE Trans. Reliability</i>. DOI: 10.1109/TR.2023.3333838",
    "5. GitHub. (2024). CodeQL Documentation and CLI Query Suites. https://codeql.github.com/docs/",
    "6. Radon Documentation. (2023). Radon: Code Metrics in Python. https://radon.readthedocs.io/"
]
for r in refs:
    story.append(Paragraph(r, body_style))

doc.build(story)
print(f"Successfully generated audited {PDF_PATH}")
