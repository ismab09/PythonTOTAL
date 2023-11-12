import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'

# Escuchar microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar el comienzo de la grabacion
        print('Ya comenzó la grabación')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language='es-uy')

            # Prueba de que pudo ingresar
            print('Dijiste: ' + pedido)

            # Devolver pedido
            return pedido

        # Sino no comprende el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print('Ups, no entendí')

            # Devolver error
            return 'sigo esperando'

        # En casi de no resolver el pedido
        except sr.RequestError:

            # Prueba de que no comprendio el audio
            print('Ups, no entendí')

            # Devolver error
            return 'sigo esperando'

        # Error inesperado
        except:

            # Prueba de que no comprendio el audio
            print('Ups, algo ha salido mal')

            # Devolver error
            return 'sigo esperando'

# Función para que el asisitente pueda ser escuchado
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar el día de la semana
def pedir_dia():

    # Crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear variables para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario de los días
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# Informar la hora
def pedir_hora():

    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Decir la hora
    hablar(hora)

# Saludo inicial
def saludo_inicial():

    # Crear la variable con datos de la hora
    hora = datetime.datetime.now()
    if hora.hour < 5 or hora.hour > 19:
        momento = 'Buenas noches'
    elif 5 <= hora.hour < 12:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento}, soy tu asistente de voz. Por favor, dime en qué te puedo ayudar.')

# Función central
def pedir_cosas():

    # Activar saludo inicial
    saludo_inicial()

    # Variable de corte
    comenzar = True

    # Loop central
    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Claro, ya te abriré YouTube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido or 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'qué día es' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Buscando en wikipedia')
            pedido = pedido.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            print(resultado)
            hablar(resultado)
            continue
        elif 'buscar en internet' in pedido:
            hablar('Ya mismo lo busco')
            pedido = pedido.replace('buscar en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'contar un chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, es el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la pude encontrar')
                continue
        elif 'adiós' in pedido:
            hablar('Bueno, nos vemos luego, cualquier cosa me avisas')
            break



pedir_cosas()
