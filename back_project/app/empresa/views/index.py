from django.shortcuts import render


def index(request):
     
    if request.session['operador'] :
        
        context = {'objeto':"Você está logado"}
    
        return render(request, 'index.html', context)
    
    else:
        
        context = {'objeto':"Você NÃO está logado"}

    
        return render(request, 'index.html', context)

