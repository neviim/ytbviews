"""
Modulo com a classe Canais

Esta classe é para instanciar e ler cada canal no youtube
o qual sera especificado em um arquivo json de reverencia
de leitura, para o processamento

Os dados desta instancia sera usado para gerar e gravar um
arquivo de saida com as novas referncias capturadas no youtube.
"""

import datetime
import requests
import json

class Canais():
    """ Classe Canais"""

    def __init__(self, tvid="", views=0, subscritos=0):
        """
        Entra com os valores iniciais. váriaveis de sistema:

            tvid       => nome do canal no youtube
            views      => quantidade de views do canal
            subscritos => quantidade de inscritos no canal.
        """
        super(Canais, self).__init__()
        self.tvid = tvid
        self.views = views
        self.subscritos = subscritos

    def ler_tvid(self):
        """ Retorna o nome do canal do youtube """
        return self.tvid

    def __str__(self):
        """ Retorna uma descrição amigável do objeto """
        return "{}/{}/{}".format(self.tvid, self.views, self.subscritos)

    def __repr__(self):
        """ Retorna uma descrição precisa e única do objeto """
        return "tvid()={} views()=int({}) sudscritos()=int({})".format(self.tvid, self.views, self.subscritos)


class Countyt():
    """
    Classe para capturar dados do site youtube

        Captura de variaveis:

            views      => visualizações
            subscritos => inscritos
    """

    html_string = ""

    def __init__(self, contaID):
        """ Variaveis de uso do sistema """
        url = "http://youtube.de/user/" + contaID + "/about"
        html = requests.get(url)
        self.html_string = html.text

    def getSubscritos(self):
        """ Captura subscritos de um canal especifico """
        abo = self.html_string.find("Abonnenten")
        raw = self.html_string[(abo - 10):abo]
        abonnenten = ""
        for x in raw:
            if (x.isdigit()):
                abonnenten += x
        return int(abonnenten)

    def getViews(self):
        """ Capitura views de um canal especifico """
        abo = self.html_string.find("Aufrufe")
        raw = self.html_string[(abo - 16):abo]
        aufrufe = ""
        for x in raw:
            if (x.isdigit()):
                aufrufe += x
        return int(aufrufe)


class DatetimeEncoder(json.JSONEncoder):
    '''
    Classe para formatar datatime

        Transforma data em:
            ano => %Y
            mes => %m
            dia => %s

        Transforma data hora:
            ano     => %Y
            mes     => %m
            dia     => %dT
            hora    => %H:
            minuto  => %M:
            segundo => %SZ

        clamada para uso: json.dumps(dict,cls=DatetimeEncoder)
    '''
    def default(self, obj):
        ''' chamada por default, defini se é uma instancia de datatime ou data '''
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # base class default caso não tenha as opções retorna TypeError
        return json.JSONEncoder.default(self, obj)

