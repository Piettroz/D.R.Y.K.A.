# 🤖 D.R.Y.K.A — Assistente Virtual em Python

> **D.R.Y.K.A** — *Directly Real Yet Kindly Annoying*  
> “Direta, realista… mas gentilmente irritante.”

Uma assistente pessoal totalmente em **Python**, criada por **Piettro Silva**, capaz de **falar**, **entender comandos de voz** em português e **executar tarefas simples** com um toque de personalidade.

---

## ⚡ Funcionalidades

✅ **Reconhecimento de voz** (Google Speech Recognition)  
✅ **Respostas faladas** com voz natural (via `pyttsx3`)  
✅ **Informa a hora e a data atual**  
✅ **Cumprimentos automáticos** conforme o horário do dia  
✅ **Consegue “dormir” por alguns minutos** quando mandada  
✅ **Finaliza o programa** com comandos de despedida (“adeus”, “tchau”)  

---

## 🧩 Tecnologias Utilizadas

| Biblioteca | Função |
|-------------|--------|
| `pyttsx3` | Síntese de fala (voz da Dryka) |
| `speech_recognition` | Reconhecimento de fala (Google) |
| `pause` | Pausa a execução por um tempo |
| `datetime` | Captura de hora e data atual |
| `pyaudio` | Entrada de áudio pelo microfone |

---

## ⚙️ Requisitos

### 🐍 Versão do Python
> Recomenda-se **Python 3.8 ou superior**  
(⚠️ Versões antigas, como 3.6, podem causar erros no `pyttsx3`.)

### 📦 Instalação das Dependências

Execute no terminal:

```bash
pip install pyttsx3 SpeechRecognition pause pyaudio
💡 Se o pyaudio falhar na instalação:

bash
Copiar código
pip install pipwin
pipwin install pyaudio
🚀 Como Executar
Baixe ou clone este repositório:

bash
Copiar código
git clone https://github.com/SEU-USUARIO/Dryka.git
Entre na pasta:

bash
Copiar código
cd Dryka
Execute o programa:

bash
Copiar código
python Dryka.py
🎧 A Dryka saudará você e começará a escutar seus comandos!

💬 Comandos de Voz Disponíveis
Comando de voz	Resposta / Ação
"como você está"	Responde com humor
"que horas são" / "hora"	Informa a hora atual
"qual a data" / "data"	Diz o dia, mês e ano
"pare de escutar por X minutos"	Pausa o microfone por X minutos
"adeus" / "tchau"	Desliga a Dryka

🧠 Exemplo:

Você diz: “Dryka, pare de escutar por três minutos.”
Ela responde: “Disseste-me para parar de escutar por 3 minutos.”
(Fica em pausa e depois volta sozinha.)

🧠 Como Funciona
Reconhecimento de Fala:
O speech_recognition usa a API do Google para converter sua voz em texto.

Síntese de Fala:
O pyttsx3 transforma as respostas de texto da Dryka em fala.
Configurações principais:

python
Copiar código
texto_fala.setProperty("rate", 160)  # Velocidade da fala
texto_fala.setProperty("voice", voices[2].id)  # Escolha da voz
Compreensão de números:
A função texto_para_numero() converte palavras como “três”, “dez” ou “quarenta” em inteiros.

Pausa programada:
A função pause.minutes(x) é usada para “fazer a Dryka dormir” por alguns minutos.

🕐 Exemplo de Execução
kotlin
Copiar código
Olá mestre. bem vindo de volta!
Agora são 10:32
A data atual é 11 do mês 10 de 2025
Bom dia mestre!
Dryka à sua disposição! diga-me, como posso ajudá-lo!
🎙️ Você diz: “Dryka, que horas são?”
🧠 Ela responde: “Agora são dez e trinta e dois.”

🧩 Melhorias Futuras
✨ Falar o nome do mês por extenso (ex: agosto, setembro...)
✨ Adicionar novos comandos de voz (abrir sites, tocar músicas, ler notícias)
✨ Criar uma interface gráfica (GUI)
✨ Conectar com APIs externas (clima, agenda, etc.)

👨‍💻 Autor
Piettro Silva
Criador e desenvolvedor da Dryka, uma IA feita com criatividade, lógica e um toque de personalidade.

💬 “Direta, realista... mas gentilmente irritante.” 😎

🪄 Licença
Este projeto é de uso pessoal e educativo.
Sinta-se livre para estudar, modificar e evoluir a Dryka — mas lembre-se de dar os créditos 😉

⭐ Se gostou da Dryka, não esqueça de deixar uma estrela no repositório! 
