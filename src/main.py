"""
le e grava arquivo JSON

Processa chamada de leitura das views e subscritos de um canal do youtube
armazena os dados retornados

Instalar dependencias:
    $ pip3 install requests

    executar:
        $ cd src/
        $ python3 main.py
"""

import json
import controles
import datetime

lista_canais = []

def ler_arquivo_json():
    """
    Le as informações do arquivo JSON especificado.

    Preenche a lista lista_canais com instancias da classe Canais
    com os valores que vem do arquivo JSON.
    """

    global lista_canais

    def pega_dados(obj):
        """
        Cria uma nova instancia de canais

        utiliza os dados recebidos do json através do objeto 'obj'
        para tvid, views e subscritos.
        retorna a instancia Canal()

        Como ter acesso as informações do obj instancia

            valor <= instancia.tvid

        """
        instancia = controles.Canais(
            tvid = obj['tvid'],
            views = obj['views'],
            subscritos = obj['subscritos']
            )

        contaID = instancia.tvid
        yc = controles.Countyt(contaID)

        instancia.views = yc.getViews()
        instancia.subscritos = yc.getSubscritos()

        return instancia

    # ler um arquivo JSON
    try:
        arquivo_json = open('../data/entrada.json', 'r') # Abre o arquivo no disco
        dados_json = json.load(arquivo_json) # Converte dicionario Json => python
        canais = dados_json['canais']

        # na funcao pega_dados, instancia a classe controles.Canais.
        lista_canais = [ pega_dados(canal) for canal in canais ]
    except Exception as erro:
        print("Erro ocorrrido: {}".format(erro))


def grava_arquivo_json():
    """
    Grava as informaçoes em um arquivo de saida JSON

    O registro ligo e atualizado do canal com suas views e sudcritos
    sera gravado em um outro arquivo de saida no forma JSON

    Cria uma lista no formato: [{tvid=obj.tvid, views=obj.views, subscritos=obj.subscritos}]
    Transforma a lista em um dicionário: { "canais": lista_salvar }
    """

    lista_salvar = [
        dict(tvid=obj.tvid, views=obj.views, subscritos=obj.subscritos)
        for obj in lista_canais
    ]
    lista_salvar.append(dict(data=str(datetime.date.today())))
    dict_salvar = { "canais": lista_salvar }
    dict_salvar = json.dumps(dict_salvar, indent=4, sort_keys=False)

    try:
        arquivo_json = open('../data/saida.json', 'w') # Abre o arquivo no formato de escrita
        arquivo_json.write(dict_salvar) # Escreve os dados no arquivo
        arquivo_json.close() # Fecha e grava o arquivo JSON
    except Exception as erro:
        print("Erro ocorrrido: {}".format(erro))


def main():
    """
     Definição que inicializa as chamadas do progrma

     Chama as duas funções definida acima.
    """
    ler_arquivo_json()
    grava_arquivo_json()
    print('Arquivo "saida.json" foi recriado.')


if __name__ == '__main__':
    main()