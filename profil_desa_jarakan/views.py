# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from profil_desa_jarakan.module_helper import replace_text_in_docx, docx2pdf

FORM_NAMES = {
    'sktm': SKTMForm,
    
}

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            field_names = list(form.fields.keys())
            replacement_data = {item.upper():form.cleaned_data[item] for item in field_names}

            doc_path = replace_text_in_docx('contoh', replacement_data)
            response = HttpResponse(open(doc_path, 'rb').read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            
            
            response['Content-Disposition'] = f'attachment; filename=document.docx'
            
            return response            
            # return render(request, 'contact.html', {'form': form, 'message': 'DONE'})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def generate_surat(request):
    
    if request.method == 'POST':
        form_name = request.POST['form_type']
        form_type = FORM_NAMES[form_name]
        form = form_type(request.POST)

        if form.is_valid():

            field_names = list(form.fields.keys())
            replacement_data = {item.upper():form.cleaned_data[item] for item in field_names}

            pdf_path, cmd_output = docx2pdf(replace_text_in_docx('sktm', replacement_data))
            response = HttpResponse(open(pdf_path, 'rb').read(), content_type='application/pdf')
            
            response['Content-Disposition'] = f'attachment; filename={form_name}.pdf'
            
            return response                 
        else:
            replacement_data = {'ERROR': form.errors.as_text()}
            pdf_path, cmd_output = docx2pdf(replace_text_in_docx('gagal', replacement_data))
            response = HttpResponse(open(pdf_path, 'rb').read(), content_type='application/pdf')
            
            response['Content-Disposition'] = f'attachment; filename=gagal.pdf'
            
            return response                 

    