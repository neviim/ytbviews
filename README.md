# ytbviews

Captura views e subscritos de um canal especificado.

  - Utiliza Python3.5

  - Baixa o arquivo do github para sua maquina, instale o pacotes de dependencia.

        $ pip3 install requests

  - Na pasta ./data tem dois arquivos entrada.json e saida.json

        entrada.json => contem os nomes dos canais ao qual se quer obter os dados.
        saida.json   => contem a saida processada das informações determinada pelo algoritino.

  - Entra na pasta src

        $ cd src
        $ python3 main.py

        Isso ira gerar um arquivo de saida na pasta ./data/saida.json com o resultado da operação. 
