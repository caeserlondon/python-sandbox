from django.shortcuts import render
from basicApp import forms_model

# Create your views here.
def index(request):
    return render(request, 'basicApp/index.html')

def form_name_view(request):
    form = forms_model.FormName()

    if request.method == 'POST':
        form = forms_model.FormName(request.POST)

        if form.is_valid():
            #Do somthing code
            print("Validations successful")
            print("NAME "+form.cleaned_data['name'])
            print("EMAIL "+form.cleaned_data['email'])
            print("TEXT "+form.cleaned_data['text'])










    return render(request, 'basicApp/form_page.html', {'form': form})
