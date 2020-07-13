from django.shortcuts import render

# Create your views here.
def serv(request):
    return render(request, 'serv/services.html', {'Services':'active'})
