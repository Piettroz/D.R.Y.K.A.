import pyttsx3
import datetime

texto_fala = pyttsx3.init()

def falar(*audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate", 160)              #alteração da velocidade da fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[2].id)    #alteração de voz
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    falar("Agora são")
    falar(Tempo)

def data():
    Data = datetime.datetime.now()
    ano = int(Data.year)
    mes = int(Data.month)
    dia = int(Data.day)
    falar("a data atual é")
    falar(f" dia {dia}. do mês {mes}. de {ano}")

tempo()
data()

