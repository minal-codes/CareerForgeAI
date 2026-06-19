from flask import Flask, render_template, request, send_file
import os

from document_parser import extract_resume_text
from career_analyzer import analyze_resume

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Latest analysis store karne ke liye
latest_analysis = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload_page():

    global latest_analysis

    if request.method == "POST":

        file = request.files["resume"]

        if file and file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            # Resume Text Extract
            resume_text = extract_resume_text(filepath)

            # Career Analysis
            analysis = analyze_resume(resume_text)

            # PDF ke liye data save
            latest_analysis = {
                "filename": file.filename,
                "resume_text": resume_text,
                "analysis": analysis
            }

            return render_template(
                "dashboard.html",
                filename=file.filename,
                resume_text=resume_text,
                analysis=analysis
            )

    return render_template("upload.html")


@app.route("/download-report")
def download_report():

    global latest_analysis

    if not latest_analysis:
        return "Please upload a resume first."

    pdf_file = "CareerForge_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "CareerForge AI Career Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    analysis = latest_analysis["analysis"]

    content.append(
        Paragraph(
            f"Career Readiness Score: {analysis['score']}/100",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Strengths",
            styles["Heading2"]
        )
    )

    for item in analysis["strengths"]:
        content.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    for item in analysis["missing"]:
        content.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Recommended Certifications",
            styles["Heading2"]
        )
    )

    for item in analysis["certifications"]:
        content.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Recommended Projects",
            styles["Heading2"]
        )
    )

    for item in analysis["projects"]:
        content.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            "Learning Roadmap",
            styles["Heading2"]
        )
    )

    for item in analysis["roadmap"]:
        content.append(
            Paragraph(f"• {item}", styles["BodyText"])
        )

    doc.build(content)

    return send_file(
        pdf_file,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)