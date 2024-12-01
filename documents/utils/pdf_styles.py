from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def get_title_style():
    styles = getSampleStyleSheet()
    return ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        textColor=colors.darkblue,
    )

def get_content_style():
    styles = getSampleStyleSheet()
    return styles["Normal"]