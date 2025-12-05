from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


def basic_platypus_pdf(filename):

    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph("First Generated Pdf using Platypus", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 20)) # Add space after title

    body = Paragraph(
        "This is a simple PDF document generated using ReportLab's Platypus library. ", styles["Normal"]
    )
    elements.append(body)

    doc.build(elements)

basic_platypus_pdf("generated_document.pdf")    

