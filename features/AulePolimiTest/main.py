import datetime
import urllib
import urllib.request
# noinspection PyUnresolvedReferences
import lxml
from bs4 import BeautifulSoup


def f1(url):
    contents = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(contents, 'html.parser')
    mydivs = soup.findAll("table", {"class": "BoxInfoCard"})[1]
    mydivs2 = mydivs.findAll("table", {"class": "scrollTable"})[0]
    mydivs3 = mydivs2.findAll("td", {"class": "dove"})

    aula_da_trovare = "N.0.2"

    head = soup.findAll("head", {})[0]

    for aula in mydivs3:
        if str(aula.text).__contains__(aula_da_trovare):
            return f2(aula, head)

    return None


def f3(aula2):
    list = []
    temp = aula2
    while True:
        prec = temp.previous_sibling
        e1 = None
        try:

            e1 = prec.findAll("td", {"class": "innerEdificio"})
        except:
            pass

        list.append(prec)

        if (e1 is not None) and len(e1) == 1:
            return list

        temp = prec

    return None


def f4(aula, intestazione, head):
    html = "<html>"
    html += head.prettify()
    html += "<style>td {border: #333 1px solid; width: 50px;}</style>"
    html += "<body>"
    html += "<table>"

    intestazione2 = reversed(intestazione)
    for int35 in intestazione2:
        html += "<tr>"
        html += int35.prettify()
        html += "</tr>"

    html += aula.prettify()

    html += "</table>"
    html += "</body>"
    html += "</html>"
    return html


def f2(aula, head):
    aula2 = aula.parent
    intestazione = f3(aula2)
    # todo: unire intestazione e aula per fare l'output
    return f4(aula2, intestazione, head)


def f5(day, month, year):
    url = "https://www7.ceda.polimi.it/spazi/spazi/controller/OccupazioniGiornoEsatto.do?" \
          "csic=MIA" \
          "&categoria=tutte" \
          "&tipologia=tutte" \
          "&giorno_day=" + str(day) + \
          "&giorno_month=" + str(month) + \
          "&giorno_year=" + str(year) + \
          "&jaf_giorno_date_format=dd%2FMM%2Fyyyy&evn_visualizza="

    return f1(url)


datetime_object = datetime.datetime.now()
result = f5(datetime_object.day, datetime_object.month, datetime_object.year)
pass
