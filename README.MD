**Dependencias**
    python 3.10.12 (https://python.org.br/instalacao-linux/)
    virtualenv (https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-22-04)**
    ps.: Para instalar o django: pip install django==4.2.
    ** Se necessitar instalar o pip aqui tem o caminho.
**Preparação**
    **Criação do Virtualenv: virtualenv <nome da virtualenv>
    **Acessar a virtual env: source <nome da virtualenv>/bin/activate
    pip install -r requirements.txt
    Caso o django não seja instalado no requirements.txt: django 4.2 (https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-22-04)
    ps.: O requirements.txt está o da máquina global, não é preciso todos os recursos que ele irá instalar
**Usabilidade**
    Depois de Instalados os módulos: 
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
**Conteúdo**
    São dois perfis de acesso:
        Cliente: só vê o projeto e as tarefas atribuídas a ele
        Admin: Vê todas as informações e pode manipular todas as sessões;
    O projeto precisa de muitas melhorias como:
     * Restrições de acessos a urls(Implementação de decorators);
     * Visibilidade de tarefas e flags de acompanhamentos de projetos e de tarefas por projetos;
     * Atribuir projetos a organizações;
     * Relatórios para o gestor do projeto;
     * Proeficiência do cliente;
     * Porcentávem de completude das tasks;
