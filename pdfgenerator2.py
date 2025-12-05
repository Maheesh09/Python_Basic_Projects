from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def pdf_withparagraphs(filename, paragraphs):

    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Generated PDF with Multiple Paragraphs", styles['Title']))
    elements.append(Spacer(1, 20))  # Add space after title

    for text in paragraphs:
        elements.append(Paragraph(text, styles["Normal"]))
        elements.append(Spacer(1, 12))  # Add space between paragraphs

    img = Image("img1.png",width=100, height=120)
    elements.append(img)

    data = [
        ["Item", "Quantity", "Price"],
        ["Apple", "10", "$5"],
        ["Banana", "6", "$3"],
        ["Mango", "3", "$9"],
    ]

    table = Table(data)

    table.setStyle(TableStyle([ 
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey), # Header row background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), # Header row text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # Center align all cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), # Header row font
        ('FONTSIZE', (0, 0), (-1, 0), 14), # Header row font size
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12), # Header row padding
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige), # Body rows background
        ('GRID', (0, 0), (-1, -1), 1, colors.black), # Grid lines
    ]))

    elements.append(table)
    doc.build(elements)

sample_paragraphs = [
    "This is the first paragraph generated from a list.",
    "Here is another piece of content coming from Python.",
    "You can easily loop over database rows, JSON, etc."
]
pdf_withparagraphs("generated_paragraphs.pdf", sample_paragraphs)