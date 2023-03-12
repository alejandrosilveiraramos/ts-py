from django.shortcuts import render


def login(request):
    """
    validacao = request.GET.get('validacao')
    
    confirme = {
        'validacao': validacao
    }"""
    
    return render(request, 'login.html')

