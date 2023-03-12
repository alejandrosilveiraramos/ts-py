from django.shortcuts import render


def logout(request):
    
    request.session['operador'] = None
    
    return render(request, 'login.html')

