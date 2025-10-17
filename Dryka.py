import pyttsx3
import datetime
import speech_recognition as sr
import pause

texto_fala = pyttsx3.init()

def texto_para_numero(texto):
    """Converte números por extenso em português para inteiros."""
    numeros = {
        "zero": 0, "um": 1, "uma": 1, "dois": 2, "duas": 2, "três": 3, "tres": 3,
        "quatro": 4, "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9,
        "dez": 10, "onze": 11, "doze": 12, "treze": 13, "quatorze": 14,
        "quinze": 15, "dezesseis": 16, "dezessete": 17, "dezoito": 18, "dezenove": 19,
        "vinte": 20, "trinta": 30, "quarenta": 40, "cinquenta": 50, "sessenta": 60
    }

    texto = texto.lower().replace(" e ", " ")  # remove "e" entre números
    palavras = texto.split()
    total = 0

    for palavra in palavras:
        if palavra in numeros:
            total += numeros[palavra]
        elif palavra.isdigit():
            total += int(palavra)
    return total if total > 0 else None


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
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language='pt-br')
        print(comando)
    
    except Exception as e:
        print(e)
        falar("por favor repita!")

        return None
    
    return comando

if __name__ == "__main__":
    bem_vindo()

    while True:
        print("Escutando...")

        comando = microfone()
        if comando is None or comando == "none":
            continue  # volta a escutar de novo
        comando = comando.lower()

        if 'como você está' in comando:
            falar('Não é da sua conta.    estou bem')
            falar('o que posso fazer para ajudá-lo. mestre')

        elif 'hora' in comando:
            tempo()

        elif 'data' in comando:
            data()


        #Criar um determinada resposta para cada um tipo minutos, segundos e horas!!
        elif 'pare de escutar' in comando:
            falar("por quantos minutos queres que eu pare de escutar?")
            resposta = microfone()

            if resposta:
                minutos = texto_para_numero(resposta)
                if minutos:
                    falar(f"disseste-me para parar de escutar por {minutos} minutos.")
                    pause.seconds(minutos)
                    falar("estou de volta mestre.")
                else:
                    falar("não entendi o número, mestre.")
            else:
                falar("não ouvi nada mestre.")

        elif 'adeus' in comando or 'tchau' in comando:
            falar("adeus mestre!")
            quit()


