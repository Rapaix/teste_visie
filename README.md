## Teste Técnico da Visie

Clona o repositorio e depois instala o python 3.8 ou superior.
depois de instalar o python agora  instale a virtualenv.

```bash
pip install virtualenv 
```

depois de instalar, vai na raiz do projeto e digita no terminal:
```bash
python3 -m venv env 
```

Depois de criado o ambiente ative com o seguinte comando.


linux
```bash
source env/bin/activate` 
```

windows
```bash
\env\Scripts\activate
```

entra no diretorio do projeto 
```
cd teste_visie
```
instale as depedências do projeto e rode o servidor
``` bash
# install dependencies
pip install -r  requirements.txt

# run server
python3 run.py

```