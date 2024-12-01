from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Document
from .forms import DocumentForm
from .utils.pdf_generator import PDFGenerator

def document_list(request):
    documents = Document.objects.all().order_by('-created_at')
    return render(request, 'documents/document_list.html', {'documents': documents})

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('documents:document_list')
    else:
        form = DocumentForm()
    return render(request, 'documents/document_form.html', {'form': form})

def generate_pdf(request, pk):
    document = get_object_or_404(Document, pk=pk)
    
    # Generate PDF
    pdf_generator = PDFGenerator(document)
    pdf = pdf_generator.generate()
    
    # Create the HTTP response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.title}.pdf"'
    response.write(pdf)
    
    return response