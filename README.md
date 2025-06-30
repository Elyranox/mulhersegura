# Mulher Segura

Sistema web desenvolvido para auxiliar mulheres em situação de risco, com foco no registro de denúncias, acionamento de alertas emergenciais e integração com contatos e autoridades.

## 🌐 Visão Geral

O **Mulher Segura** é uma solução digital pensada para oferecer agilidade e segurança às vítimas de violência doméstica.  
Através de uma plataforma intuitiva e sigilosa, é possível registrar ocorrências, anexar provas, acionar alertas com localização e acompanhar o andamento das denúncias.

## 🔒 Funcionalidades

- Cadastro de vítimas com contatos de confiança  
- Registro de denúncias com anexos (áudios, fotos, prints)  
- Botão de emergência com geolocalização  
- Notificações automáticas para contatos e autoridades  
- Histórico de denúncias acessível pela usuária  
- Acesso administrativo para monitoramento e geração de relatórios

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Django (Python)  
- **Front-end:** HTML, CSS, JavaScript  
- **Banco de Dados:** PostgreSQL (principal), MySQL (simulação policial)  
- **APIs:** Google Maps (localização), Twilio (envio de alertas)  
- **Arquitetura:** MVC (Model-View-Controller)  
- **Segurança:** Criptografia de senhas, estrutura modular

## 🚧 Em Desenvolvimento

- Suporte a Progressive Web App (uso offline)  
- Integração com autoridades reais  
- Interface completa da polícia  
- Melhorias em notificações e rastreamento


## 📊 Relatório da Pesquisa com a Comunidade

Antes do desenvolvimento, foi realizada uma pesquisa sobre violência doméstica e medidas protetivas, que fundamentou as decisões do projeto.  
Acesse o relatório completo:  
[🔗 Resultados da Pesquisa - Google Drive](https://drive.google.com/file/d/1phS4gmrXn5UUw3lxmJlZ9XT3wBsdj1xS/view?usp=sharing)

## 🤝 Contribuições

Este projeto é aberto a sugestões e melhorias. Pull requests e issues são bem-vindos.

## 📢 Sobre

Este repositório é mantido por Elyranox como parte de uma iniciativa social voltada à proteção de mulheres.
O sistema não substitui os canais oficiais de denúncia, mas busca complementar a rede de apoio com soluções tecnológicas práticas e acessíveis.


## 🚀 Como Executar Localmente

```bash
# 1. Crie o ambiente virtual
python -m venv venv

# 2. Ative o ambiente
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# 3. Acesse o diretório do backend
cd backend

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Aplique as migrações
python manage.py makemigrations
python manage.py migrate

# 6. Execute o servidor local
python manage.py runserver
Acesse o sistema em http://127.0.0.1:8000/


