from PIL import Image as PILImage
from reportlab.lib.units import inch
from reportlab.platypus import Image

def process_image(image_path):
    """Process and resize image for PDF generation."""
    img = PILImage.open(image_path)
    
    # Calculate aspect ratio
    aspect = img.width / img.height
    
    # Set maximum width to 6 inches
    max_width = 6 * inch
    width = max_width
    height = width / aspect
    
    return Image(image_path, width=width, height=height)