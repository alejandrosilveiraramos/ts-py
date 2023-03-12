from django.shortcuts import render, redirect


def autenticar(request):
    
    email = request.POST.get('email')
    # senha = sha256(request.POST.get('senha').encode()).hexdigest()
    senha = request.POST.get('senha')
    
    # operador = operador.objects.filter(email = email).filter(senha = senha)
    operador = {'email':'email', 'senha':'senha'}

    
    if operador['email'] == email and operador['senha'] == senha:
        request.session['operador'] = operador['email']
        return redirect('index')
        
    else:
        # return redirect('/login?validacao=00')
        return render(request, 'login.html')
    
    """
    if len(operador) != 0:
        request.session['operador'] = operador[0].id
        return redirect('index')
        
    else:
        return redirect('/login?validacao=00')
    """
    
    