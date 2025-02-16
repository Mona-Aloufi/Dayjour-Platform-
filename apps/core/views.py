from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    return render(request, "Blay/home.html")

def login_view(request):
    return render(request, 'login.html')

def signin_view(request):
    return render(request, 'signin.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def encrypt_data_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['dataFile']
        
        # Simulate saving the uploaded file
        saved_file_path = os.path.join('path/to/save/uploaded/files', uploaded_file.name)
        
        # Save the uploaded file to the filesystem
        with open(saved_file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Show the download page with the file name
        return render(request, 'download_encrypt.html', {'encrypted_file': uploaded_file.name})

    return render(request, 'uploadData.html')

def download_encrypted_file_view(request, encrypted_file):
    file_path = os.path.join('path/to/save/uploaded/files', encrypted_file)
    
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{encrypted_file}"'
            return response

    return HttpResponse("File not found.", status=404)

def trainLocalmodel(request):
     return render(request, 'train.html')
