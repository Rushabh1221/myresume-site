from django.shortcuts import render

# Create your views here.
def core(request):
    return render(request, 'core1/home.html', {'Home':'active'})

def cont(request):
    return render(request, 'core1/contact.html', {'Contact':'active'})