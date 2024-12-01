from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.pagesizes import letter
from io import BytesIO
from .pdf_styles import get_title_style, get_content_style
from .image_processor import process_image
import json

class PDFGenerator:
    def __init__(self, document):
        self.document = document
        self.buffer = BytesIO()
        
    def _create_document(self):
        return SimpleDocTemplate(
            self.buffer,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
    def _classify(self, d):
        d*=100
        if d<30:
            return "normal"
        elif d<80:
            return "medival"
        else:
            return "critical"
    def _build_content(self):
        story = []
        
        # Add title
        title = Paragraph(self.document.title, get_title_style())
        story.append(title)
        story.append(Spacer(1, 12))
        
        # Add content
        prediction = json.loads(self.document.content)
        data = [["Differential Diagnosis", "Status"]]
        for key in prediction.keys():
            if type(prediction[key]) == type(0.0):
                a = [key, self._classify(prediction[key])]
                data.append(a)
        
        content = Table(data)
        # content = Paragraph(self.document.content, get_content_style())
        story.append(content)
        story.append(Spacer(1, 12))
        
        # Add image if present
        if self.document.image:
            image = process_image(self.document.image.path)
            story.append(image)
            
        return story

    def generate(self):
        try:
            # Create the PDF document
            doc = self._create_document()
            
            # Build the content
            story = self._build_content()
            
            # Generate the PDF
            doc.build(story)
            
            # Get the PDF content
            pdf = self.buffer.getvalue()
            return pdf
            
        finally:
            self.buffer.close()