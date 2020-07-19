# Inventario
Projeto pessoal de controle de inventário


# Instruções iniciais

Tenha instalado em sua máquina o python na versão 3.x

Download e instruçõe aqui: https://www.python.org/downloads/

Para uma melhor experiência, utilize a IDE de sua preferência. Particularmente gosto muito do Pycharm (que possui a versão open source e gratuita, Community)
Donwload aqui: https://www.jetbrains.com/pt-br/pycharm/download/

# Instruções básicas:
Crie um diretório com o nome que desejar
## Instruções para o linux:
No terminal, eu sugiro que crie um diretório projetos a partir do /home/<seu usuario>
``` 
 $ pwd
 /home/usuario/
 $ mkdir projetos
 $ cd projetos
 $ mkdir inventario
 $ cd inventario
```
Agora precisamos criar a virtualenv para o projeto (não sabe o que é virtualenv, veja este [artigo](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais)).
```
$ pwd
/home/usuario/projetos/inventario
$ python3 -m virtualenv <nome da venv>
$ ls
<nome da venv>
```
Para podermos utilizar a virtualenv, basta iniciá-la:
```
$ pwd
/home/usuario/projetos/inventario
$ source <nome da venv>/bin/activate
(<nome da venv>) $

```

Agora você já pode clonar o projeto para o seu computador com o comando: 
```
(<nome da venv>) $ pwd
/home/usuario/projetos/inventario
(<nome da venv>) $ git clone https://github.com/PauloViniciusBaleeiro/Inventario.git
(<nome da venv>) $ ls
<nome da venv>  Inventario
(<nome da venv> $ cd Inventario
```

## Dentro do projeto
A partir de agora você pode abrir a pasta que o comando git clone criou (Inventario) através da sua IDE, porém os seguintes comandos continuam sendo executados no termnal:

### Primeiros contatos com o Django
Primeiro precisamos instalar os pacotes do projeto
```
(<nome da venv>) $ pwd
/home/usuario/projetos/inventario/Inventario
(<nome da venv>) $ pip install -r requirements.txt
```

Agora (enquanto estamos desenvolvendo, usaremos um banco temporário em arquivo,criado automaticamente pelo Django) iremos iniciar um banco de dados:
```
(<nome da venv>) $ pwd
/home/usuario/projetos/inventario/Inventario
(<nome da venv>) $ python manage.py makemigrations
(<nome da venv>) $ python manage.py migrate
```

Precisamos criar o superusuario para acessar o sistema
```
(<nome da venv>) $ python manage.py createsuperuser
Nome: <digite um nome de usuario>
email: <opcional>
Senha: <senha>
Repetir senha: <senha>
Usuário criado com sucesso
```

Vamos à parte divertida:
```
(<nome da venv>) $ python manage.py runserver
```

Abra o seu navegador e digite:
> localhost:8000


Você deve ver um template incial informando que o Django está rodando.

Agora digite, no seu navegador:
> localhost:8000/admin

Você terá acesso à administração da aplicação, na qual, com as credenciais criadas pelo comando 'createsuperuser' terá acesso às funções criadas no site.

Por enquanto é isso. A seguir procederemos com o desenvolvimento da aplicação.
