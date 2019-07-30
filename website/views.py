from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.
def index(request):
    #essa página vai cadatrar uma pessoa
    args = { }
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        args = {'msg': 'Parabéns, agora so colocar seu e-mail'}
        return render(request, 'index.html', args)
    
    return render(request, 'index.html', args)

def sobre(request):
    #essa pagina vai listar as ideia e seus criadores
    ideias = Ideias.objectos.filter(ativo=True).all
    args = {
        'ideias':ideias
    }
    return render(request,'sobre.html', args)

def login(request):
    '''
    Essa página irá conferir se existe um usuário
    cadastro, se sim retornará para página sobre
    se não, retornara para página de cadastro com
    uma mensagem s "Cadastre-se para criar uma ideia 
    '''
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objectos.filter(email=email_form).firts()

        print('Iae meu bom amigo ', pessoa )

        if pessoa is None:
            #mandar para página de cadastro
            args = {'msg': 'Cadastre-se para criar uma ideia'}
            return render(request, 'index.html', args)
        else:
            args = {'pessoa': pessoa}
            return render(request, 'ideias.html', args)
        
    return render(request, 'login.html', {})

def cadastrar_ideia(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email_pessoa).firts()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('uhuuuuuu')

            return redirect('/sobre')
        
        return redirect(request, 'ideias.html', {})

def remover_ideia(request, id):
    ideia = Ideia.objects.filter(id=id)
    if ideia is not None:
        ideia.ativo = False
        ideia.save()
        return redirect('/sobre')
    return render(request, 'sobre.html',{ 'msg': 'Ops, deu ruim'})