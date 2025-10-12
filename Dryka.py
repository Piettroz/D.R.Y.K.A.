import pyttsx3
import datetime
import speech_recognition as sr

texto_fala = pyttsx3.init()

def falar(audio):
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

'''         TAREFA  0.0:

    trasformar o mês em um nome referente a sua data.
    e fazer a dryka pronunciar esse nome!
    ex: mês 8 == agosto

'''

def data():
    Data = datetime.datetime.now()
    ano = int(Data.year)
    mes = int(Data.month)
    dia = int(Data.day)
    falar("a data atual é")
    falar(f" {dia}. do mês {mes}. de {ano}")

def bem_vindo():
    falar("Olá mestre. bem vindo de volta!")
    tempo()
    data()

    hora = datetime.datetime.now().hour
                                                     
    if hora >= 5 and hora < 12:                         
        falar("bom dia mestre!")
    elif hora >= 12 and hora < 18:
        falar("boa tarde mestre!")
    elif hora >= 18 and hora <= 24:
        falar("boa noite mestre!")
    else:                                            
        falar("Ola Bat man")                           #jovem mocergo
  
    falar("dryka a sua disposição! diga-me, como posso ajuda-lo!")

def microfone():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language='pt-br')
        print(comando)
    
    except Exception as e:
        print(e)
        falar("por favor repita!")

        return "None"
    
    return comando

if __name__ == "__main__":
    bem_vindo()

    while True:
        print("Escutando...")
        comando = microfone().lower()


