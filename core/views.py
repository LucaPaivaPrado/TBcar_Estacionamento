from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import FormCliente, FormVeiculo, FormTabela, FormMarca, FormMensalista, FormRotativo
from core.models import Cliente, Marca, Veiculo, Tabela, Mensalista, Rotativo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


def home(request):
    return render(request, 'core/index.html')


@login_required
def cadastroCliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('url_principal')
        contexto = {'form': form, 'txt_titulo': 'cad_cli', 'txt_descricao': 'Cadastro de cliente'}
        return render(request, 'core/cadastro_cliente_dividido.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroVeiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_veiculo')
        contexto = {'form': form, 'txt_titulo': 'cad_veic', 'txt_descricao': 'Cadastro de veiculo', 'addmarca': True}
        return render(request, 'core/cadastro_veiculo_dividido.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroTabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'txt_titulo': 'cad_tabela', 'txt_descricao': 'Cadastro Tabela'}
        return render(request, 'core/cadastro_tabela_dividido.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroMarca(request):
    if request.user.is_staff:
        form = FormMarca(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {"form": form, "txt_titulo": "cad_marca", 'txt_descricao': 'Cadastro Marca'}
        return render(request, 'core/cadastro_marca_dividido.html', contexto)


@login_required
def cadastroRotativo(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_rotativo')
        contexto = {'form': form, 'txt_titulo': 'cad_rot', 'txt_descricao': 'Cadastro de rotativos'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroMensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_mensalista')
        contexto = {'form': form, 'txt_titulo': 'cad_mensa', 'txt_descricao': 'Cadastro de mensalistas'}
        return render(request, 'core/cadastro_mensalista_dividido.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemCliente(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__contains=request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente','listagem':'listagem'}
        return render(request, 'core/listagem_cliente.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemVeiculo(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Veiculo.objects.filter(placa__contains=request.POST['input_pesquisa'])
        else:
            dados = Veiculo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a placa do carro','listagem':'listagem'}
        return render(request, 'core/listagem_veiculo.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemTabela(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Tabela.objects.filter(descricao__contains=request.POST['input_pesquisa'])
        else:
            dados = Tabela.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a descrição','listagem':'listagem'}
        return render(request, 'core/listagem_tabela.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemMarcas(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Marca.objects.filter(nome__contains=request.POST['input_pesquisa'])
        else:
            dados = Marca.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a marca','listagem':'listagem'}
        return render(request, 'core/listagem_marca.html', contexto)
    return render(request, 'aviso.html')



@login_required
def listagemMensalista(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Mensalista.objects.filter(id_veiculo__placa__contains=request.POST['input_pesquisa'])
        else:
            dados = Mensalista.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a observação do veiculo','listagem':'listagem'}
        return render(request, 'core/listagem_mensalista.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemRotativo(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Rotativo.objects.filter(id_veiculo__placa__contains=request.POST['input_pesquisa'])
        else:
            dados = Rotativo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a entrada','listagem':'listagem'}
        return render(request, 'core/listagem_rotativo.html', contexto)
    return render(request, 'aviso.html')


@login_required
def altera_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados do cliente alterado com sucesso!')
                return redirect('url_listagem_cliente')
        contexto = {'form': form, 'txt_titulo': 'EditCliente', 'txt_descrição': 'Altera Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required
def altera_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_mensalista')
        contexto = {'form': form, 'txt_titulo': 'EditMensalista', 'txt_descrição': 'Altera Mensalista'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required
def altera_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                obj.calcula_total()
                form.save()
                return redirect('url_listagem_rotativo')
        contexto = {'form': form, 'txt_titulo': 'EditRotativo', 'txt_descrição': 'Altera Rotativo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required
def altera_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_veiculo')
        contexto = {'form': form, 'txt_titulo': 'EditVeiculo', 'txt_descrição': 'Altera Veiculo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required
def altera_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        form = FormTabela(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_tabela')
        contexto = {'form': form, 'txt_titulo': 'EditTabela', 'txt_descrição': 'Altera Tabela'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required
def altera_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        form = FormMarca(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
            return redirect('url_listagem_marcas')
    contexto = {'form': form, 'txt_titulo': 'editMarca', 'txt_descrição': 'Altera Marca'}
    return render(request, 'core/cadastro.html', contexto)
    return render(request, 'core/aviso.html')


@login_required
def exclui_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        contexto = {'txt_info': obj.nome, 'txt_url': '/listagemCliente/'}
        if request.POST:
            obj.delete()
            messages.success(request, 'Cliente excluído com sucesso!')
            contexto.update({'txt_tipo': 'Cliente'})
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def exclui_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        contexto = {'txt_info': obj.id_veiculo, 'txt_url': '/listagemMensalista/'}
        if request.POST:
            obj.delete()
            contexto.update({'txt_tipo': 'Mensalista'})
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def exclui_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        contexto = {'txt_info': obj.id_veiculo, 'txt_url': '/listagemRotativo/'}
        if request.POST:
            obj.delete()
            contexto.update({'txt_tipo': 'Mensalista'})
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def exclui_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        contexto = {'txt_info': obj.placa, 'txt_url': '/listagemVeiculo/'}
        if request.POST:
            obj.delete()
            contexto.update({'txt_tipo': 'Veiculo'})
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def exclui_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        contexto = {'txt_info': obj.nome, 'txt_url': '/listagemMarcas/'}
        if request.POST:
            obj.delete()
            contexto.update({'txt_tipo': 'Marca'})
            return render(request, 'core/aviso_exclusao.html', contexto)
        else:
            return render(request, 'core/confirma_exclusao.html', contexto)
