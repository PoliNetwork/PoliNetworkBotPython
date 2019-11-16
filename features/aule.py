import datetime
import random
import urllib
import urllib.request
from bs4 import BeautifulSoup
import lxml

from features import reviews
from functions.temp_state import temp_state_main


def f1(url, aula_da_trovare):
    contents = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(contents, 'html.parser')
    mydivs = soup.findAll("table", {"class": "BoxInfoCard"})[1]
    mydivs2 = mydivs.findAll("table", {"class": "scrollTable"})[0]
    mydivs3 = mydivs2.findAll("td", {"class": "dove"})

    head = soup.findAll("head", {})[0]

    for aula in mydivs3:
        if str(aula.text).__contains__(aula_da_trovare):
            return f2(aula, head)

    return None


def f3(aula2):
    list2 = []
    temp = aula2
    while True:

        prec = temp.previous_sibling
        e1 = None
        try:
            e1 = prec.findAll("td", {"class": "innerEdificio"})
        except:
            pass

        if prec is not None:
            list2.append(prec)

        if (e1 is not None) and len(e1) == 1:
            return list2

        temp = prec

    return None


def f6(intestazione2):
    count = 0
    html = ""
    for int35 in intestazione2:

        if count >= 2:
            return html

        html += "<tr>"
        html += int35.prettify()
        html += "</tr>"

        count += 1

    return html


def f4(aula, intestazione, head):
    html = "<html>"
    html += head.prettify()
    html += "<style>td {border: #333 1px solid; width: 50px;}</style>"
    html += "<body>"
    html += "<table>"

    intestazione2 = reversed(intestazione)
    html += f6(intestazione2)

    html += aula.prettify()

    html += "</table>"
    html += "</body>"
    html += "</html>"
    return html


def f2(aula, head):
    aula2 = aula.parent
    intestazione = f3(aula2)
    return f4(aula2, intestazione, head)


def f5(day, month, year, aula_da_trovare):
    url = "https://www7.ceda.polimi.it/spazi/spazi/controller/OccupazioniGiornoEsatto.do?" \
          "csic=MIA" \
          "&categoria=tutte" \
          "&tipologia=tutte" \
          "&giorno_day=" + str(day) + \
          "&giorno_month=" + str(month) + \
          "&giorno_year=" + str(year) + \
          "&jaf_giorno_date_format=dd%2FMM%2Fyyyy&evn_visualizza="

    return f1(url, aula_da_trovare)


def f7(update):
    datetime_object = datetime.datetime.now()

    message = update.message
    text = message.text
    text = str(text)
    text = text[6:]
    text = text.strip()

    aula_da_trovare = text
    result = f5(datetime_object.day, datetime_object.month, datetime_object.year, aula_da_trovare)

    n = random.randint(1, 9999999)
    filename = 'data/aula' + str(n) + "_" + str(abs(int(update.message.chat.id))) + '.html'
    reviews.send_file(update, result, filename, aula_da_trovare)


def get_orari_aula(update, context):
    # f7(update)

    temp_state_main.create_state(module="a1", state="0", id_telegram=update.message.chat.id)
    temp_state_main.next_main(id_telegram=update.message.chat.id, update= update)

    return None
