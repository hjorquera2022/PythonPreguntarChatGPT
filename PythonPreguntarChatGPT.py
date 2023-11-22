import openai
import pyttsx3

# Configura tus credenciales de OpenAI
openai.api_key = '190523icsa.metaproject.api'

# Configura el motor de síntesis de voz
engine = pyttsx3.init()

def generar_respuesta(texto):
    # Genera la respuesta utilizando ChatGPT
    respuesta = openai.Completion.create(
        engine='text-davinci-003',
        prompt=texto,
        max_tokens=50,
        temperature=0.7
    )
    return respuesta.choices[0].text.strip()

def reproducir_voz(texto):
    # Configura las propiedades del motor de síntesis de voz
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Elige una voz en particular (opcional)

    # Reproduce el texto utilizando síntesis de voz
    engine.say(texto)
    engine.runAndWait()

# Función principal del programa
def main():
    # Recibe el texto de entrada
    texto_entrada = input('Escribe tu mensaje: ')

    # Genera la respuesta de ChatGPT
    respuesta = generar_respuesta(texto_entrada)

    # Imprime la respuesta como texto
    print('Respuesta: ', respuesta)

    # Reproduce la respuesta como voz
    reproducir_voz(respuesta)

# Ejecuta el programa principal
if __name__ == '__main__':
    main()
