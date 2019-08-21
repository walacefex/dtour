from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

def index(request):
    #essa página vai cadastrar uma pessoa
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.password = request.POST.get('password')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()

        return render(request, 'login.html', contexto)

    return render(request, 'index.html', contexto)
 
def servicos(request):

    return render(request, 'servicos.html')

def contato(request):

    return render(request, 'contato.html')

def dashboard(request):
    contexto = {}
    contexto = { "auth": 1}
    return render(request, 'dashboard.html', contexto)
    
def sobre(request):

    return render(request, 'sobre.html')

def login(request):
    # Essa página irá conferir se existe um usuário
    # cadastrado, se sim retonará para página sobre
    # se não, retornará para página de cadastro com
    # uma mensagem "Cadastre-se para criar uma ideia"
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_form).first()
        request.session['email'] = email_form

        print('Iae meu bom amigo ', pessoa)

        if pessoa is None:
            #mandar para página de cadastro
            contexto = {'msg': 'Cadastre-se para criar uma ideia'}
            return redirect('/dashboard')
        else:
            #mandar para página de ideias
            contexto = {'pessoa': pessoa}
            return redirect('/sobre')
    return render(request, 'login.html', {})

def nova_ideia(request):
    pessoa = Pessoa.objects.filter(email=request.session['email']).first()
    contexto = {'pessoa': pessoa}
    return render(request, 'ideias.html', contexto)


def cadastro(request):
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categorias = request.POST.get('categorias')
            # ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('uhuuu')

            return redirect('/sobre') 

    return render(request, 'cadastro.html', {}) 
