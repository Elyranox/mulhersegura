from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Denuncia
from vitimas.models import Usuario
from datetime import datetime
from django.core.files.storage import FileSystemStorage


# 🔹 Registrar Denúncia
def registrar_denuncia(request):
    cpf = request.session.get('cpf')

    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        localizacao = request.POST.get('localizacao')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        provas = request.POST.get('provas') == 'on'
        arquivo = request.FILES.get('arquivo')

        try:
            usuario = Usuario.objects.get(cpf=cpf)
            data_hora = datetime.strptime(f'{data} {hora}', '%Y-%m-%d %H:%M')

            arquivo_path = None
            if arquivo:
                fs = FileSystemStorage(location='media/provas/')
                filename = fs.save(arquivo.name, arquivo)
                arquivo_path = 'provas/' + filename

            Denuncia.objects.create(
                cpf=usuario,
                descricao=descricao,
                localizacao=localizacao,
                provas_anexadas=provas,
                data_hora=data_hora,
                arquivo=arquivo_path
            )

            messages.success(request, "Denúncia registrada com sucesso!")
            return redirect('denuncia_enviada')

        except Usuario.DoesNotExist:
            messages.error(request, "CPF não encontrado.")
        except Exception as e:
            print(f"Erro: {e}")
            messages.error(request, f"Ocorreu um erro: {e}")

    return render(request, 'denuncias/registrar_denuncia.html', {'cpf': cpf})


# 🔹 Tela de sucesso após registro
def denuncia_enviada(request):
    return render(request, 'denuncias/denuncia_enviada.html')


# 🔹 Histórico de Denúncias com Detalhes
def historico_denuncia(request):
    cpf = request.session.get('cpf')

    if not cpf:
        return render(request, 'erro.html', {'mensagem': 'Usuário não autenticado.'})

    denuncias = Denuncia.objects.filter(cpf=cpf).order_by('-data_hora')

    context = {
        'denuncias': denuncias
    }

    return render(request, 'denuncias/historico_denuncia.html', context)
