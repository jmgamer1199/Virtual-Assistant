
            # -------------------------------------- LIBRERIAS -------------------------------------- #

import speech_recognition as sr
import pyttsx3
import subprocess
import os
import re
import random
import Config
import sqlite3
import webbrowser
import math
import spotipy
import spotipy.util as util
import openai
import datetime
import openpyxl
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
            # -------------------------------------- ASISTENTE VIRTUAL -------------------------------------- #

def asistente_virtual():

    # Lista de palabras clave aceptadas para los comandos

    comando_hora = ["que hora es", "dime la hora", "qué hora es", "que hora son"]

    comando_texto = ["lee el texto", "dime el texto del archivo", "E", "EH", "que hay en el texto"]

    comando_dado = ["tira un dado", "lanza un dado"]

    comando_db = ["Que hay en la base de datos", "que hay en la base de datos", "dime la base de datos"]

    comando_web = ["busca en Google"]

    comando_abecedario = ["dime el abecedario"]

    comando_calcular = ["calcula"]

    comando_abrirtwitch = ["abre twitch", "abre el twitch"]

    comando_abriryoutube = ["abre youtube", "abre el youtube", "abre You Tube", "abre you tube", "abre YouTube", "abre el You Tube", "abre el you tube", "abre el YouTube"]

    comando_abrirtwitter = ["abre twitter", "abre Twitter", "abre tuitter", "abre tuite", "abre twite", "abre el twitter", "abre el Twitter", "abre el tuitter", "abre el tuite", "abre el twite"]

    comando_abririnsta = ["abre insta", "abre instagram", "abre istagram", "abre istagra", "abre el insta", "abre el instagram", "abre el istagram", "abre el istagra", "abre el Instagram", "abre Instagram"]

    comando_abrirtendenciastwitter = ["abre tendencias de Twitter", "abre tendencias de twitter"]

    comando_saludar = ["hola", "Hola", "ola", "buenas", "Buenas", "wenas", "Wenas", "hello", "Hello"]

    comando_webyt = ["busca en youtube"]
    
    comando_webwikipedia = ["busca en Wikipedia"]

    comando_webtwitter = ["busca en Twitter"]

    comando_webtwitch = ["busca en twitch"]

    comando_reproducirspotify = ["busca una musica", "busca una música"]

    comando_abriramino = ["abre amino", "abre el bot de amino", "abre Amino" "abre el bot de Amino", "enciende el bot de Amino", "enciende el bot de amino"]

    comando_abrirtwitchbot = ["abre twitch", "abre el bot de twitch", "abre Twitch" "abre el bot de Twitch", "enciende el bot de Twitch", "enciende el bot de twitch"]

    comando_abrirgenerador = ["abre el generador de contraseñas"]

    comando_haz_una_pregunta = ["lechugas"]

    comando_fecha = ["que dia es hoy", "en que dia estamos", "en qué día estamos", "qué día es hoy", "que día es hoy"]

    comando_excel = ["que hay en excel", "que hay en el excel"]

    comando_escribirtexto = ["escribe", "escribe un texto", "escribe esto", "escribe lo que yo diga"]

    comando_pausarmusica = ["pausa la musica", "pausa la música"]

    comando_reproducirmusica = ["reanuda la musica", "reanuda la música", "reproduce la música"]

    comando_holamundo = ["patatas"]

    # Inicializar el reconocimiento de voz
    r = sr.Recognizer()
    
    # Inicializar el motor de voz
    engine = pyttsx3.init()

    #Selecciona la voz que quieras utilizar
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Establecer la velocidad de habla
    engine.setProperty('rate', 150)
    
    # Nombre del asistente virtual
    nombre_asistente = "patata"
    
    # Presentarse
    print(f"Soy {nombre_asistente}, ¿cómo puedo ayudarte?")

            # -------------------------------------- INICIA EL BUCLE -------------------------------------- #
    
    while True:

        # Obtener entrada de audio del usuario
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = r.listen(source)

        # Reconocer la entrada de audio
        try:
            comando = r.recognize_google(audio, language='es-ES')
            print("Has dicho: " + comando)
            
            # Verificar si el usuario menciona el nombre del asistente
            if nombre_asistente.lower() in comando.lower():

            # -------------------------------------- DECIR HORA -------------------------------------- #

                # Ejecutar acción según el comando recibido
                if any(palabra in comando for palabra in comando_hora):
                    import datetime
                    ahora = datetime.datetime.now()
                    hora = ahora.strftime("%H:%M")
                    engine.say("La hora actual es " + hora)
                    engine.runAndWait()

            # -------------------------------------- ESCRIBE TEXTO QUE DIGA -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_escribirtexto):
                    recognizer = sr.Recognizer()
                    microphone = sr.Microphone()
                        
                    with microphone as source:
                        recognizer.adjust_for_ambient_noise(source)
                        engine.say("Di lo que quieres escribir:")
                        engine.runAndWait()
                        audio = recognizer.listen(source)
                    
                    try:
                        text = recognizer.recognize_google(audio, language="es-ES")
                        with open("Asistente_virtual/Texto.txt", "a") as f:
                            f.write(" " + text + "\n")
                        engine.say("Texto escrito exitosamente")
                        engine.runAndWait()
                    except sr.UnknownValueError:
                        engine.say("No se pudo reconocer el audio")
                        engine.runAndWait()

                        engine = pyttsx3.init()
                        engine.setProperty('rate', 120)

            # -------------------------------------- LEE ARCHIVO EXCEL -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_excel):
                    # Lee el archivo de Excel
                    wb = openpyxl.load_workbook(Config.EXCEL)

                    # Seleccionar la hoja de cálculo que deseas leer
                    sheet = wb['Hoja1']

                    # Recorrer las celdas en la hoja de cálculo
                    for row in sheet.iter_rows():
                        for cell in row:
                            # Comprobar si la celda está vacía
                            if cell.value:
                                engine.say(cell.value)
                                engine.runAndWait()

                    # Cerrar el archivo de Excel
                    wb.close()      

            # -------------------------------------- LEER TEXTO -------------------------------------- #

                elif any(palabra in comando for palabra in comando_texto):
                    ruta_archivo = "H:\Asistente virtual\Texto.txt"
            
                    if not os.path.exists(ruta_archivo):
                        # Crear archivo
                        with open(ruta_archivo, "w") as archivo:
                            archivo.write("")
                        engine.say(f"El archivo {ruta_archivo} ha sido creado.")
                    else:
                        # Leer contenido del archivo
                        with open(ruta_archivo, "r") as archivo:
                            contenido = archivo.read()
                        if contenido:
                            engine.say(f"Texto del archivo: {contenido}")
                        else:
                            engine.say(f"En el archivo {ruta_archivo} no se ha encontrado ningún texto.")
                    engine.runAndWait()

            # -------------------------------------- DADO -------------------------------------- #

                elif any(palabra in comando for palabra in comando_dado):
                    numeros = ["1", "2", "3", "4", "5"]
                    dado = random.choice(numeros)
                    engine.say(f'He lanzado el dado y el numero que ha salido es {dado}')
                    engine.runAndWait() 

            # -------------------------------------- Hola Mundo! -------------------------------------- #
            
                elif any(palabra in comando for palabra in comando_holamundo):
                    hortalizas = [ " patata " , "lechuga"] 
                    aleatorio = random.choice(hortalizas)
                    engine.say (f" aleaotorio")
                    engine.runAndWait ()

            # -------------------------------------- BASE DE DATOS -------------------------------------- #

                elif any(palabra in comando for palabra in comando_db):
                    conn = sqlite3.connect(Config.DB)
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM users")
                    resultados = cursor.fetchall()
                    datos = []
                    for resultado in resultados:
                        datos.append(str(resultado))
                    for dato in datos:
                        engine.say(f"En la base de datos hay: {dato}")
                        engine.runAndWait()
                    conn.close()

            # -------------------------------------- BUSCAR EN WEB -------------------------------------- #

                elif any(palabra in comando for palabra in comando_web): #"busca en Google" in comando:
                    # Utilizar el reconocimiento de voz para obtener la palabra o frase a buscar
                    palabra_busqueda = comando.split("busca en Google")[1].strip()
                    # Utilizar la palabra o frase como argumento para la función de búsqueda de Google
                    webbrowser.open(f"https://www.google.com/search?q={palabra_busqueda}")

            # -------------------------------------- ABECEDARIO -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abecedario):
                    engine.say("a b c d e f g h i j k l m n ñ o p q r s t u v w y z")
                    engine.runAndWait()

            # -------------------------------------- ABRIR BOT AMINO -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abriramino):
                    subprocess.call("start cmdAmino.bat", shell=True)

            # -------------------------------------- ABRIR BOT TWITCH -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abrirtwitchbot):
                    subprocess.call("start cmdTwitch.bat", shell=True)

            # -------------------------------------- ABRIR BOT GENERADOR DE CONTRASEÑAS -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abrirgenerador):
                    subprocess.call("start cmdGenerador.bat", shell=True)

            # -------------------------------------- REPRODUCIR MUSICA EN SPOTIFY -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_reproducirspotify):
                    r = sr.Recognizer()

                    with sr.Microphone() as source:
                        engine.say("Dime el nombre de la canción:")
                        engine.runAndWait()
                        audio = r.listen(source)

                    try:
                        song_name = r.recognize_google(audio)
                        engine.say("Buscando la canción: " + song_name)
                        engine.runAndWait()

                        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Config.SPOTI_ID,
                                                                        client_secret=Config.SPOTI_SECRET,
                                                                        redirect_uri=Config.URI,
                                                                        scope=["user-library-read", "user-library-modify", "playlist-read-private", "playlist-read-collaborative", "playlist-modify-public", "playlist-modify-private", "user-read-playback-state", "user-read-currently-playing", "app-remote-control", "user-modify-playback-state"]))

                        results = sp.search(q=song_name, type="track")
                        track_id = results["tracks"]["items"][0]["id"]

                        sp.start_playback(uris=[f"spotify:track:{track_id}"])
                        engine.say(f"Reproduciendo la canción: {song_name}")
                        engine.runAndWait()
                    except:
                        engine.say("Lo siento, no he podido reconocer el nombre de la canción.")
                        engine.runAndWait()

            # -------------------------------------- PAUSAR MUSICA DE SPOTIFY -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_pausarmusica):
                    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Config.SPOTI_ID,
                                                                    client_secret=Config.SPOTI_SECRET,
                                                                    redirect_uri=Config.URI,
                                                                    scope=["user-library-read", "user-library-modify", "playlist-read-private", "playlist-read-collaborative", "playlist-modify-public", "playlist-modify-private", "user-read-playback-state", "user-read-currently-playing", "app-remote-control", "user-modify-playback-state"]))

                    sp.pause_playback()

            # -------------------------------------- REANUDAR MUSICA DE SPOTIFY -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_reproducirmusica):
                    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Config.SPOTI_ID,
                                                                    client_secret=Config.SPOTI_SECRET,
                                                                    redirect_uri=Config.URI,
                                                                    scope=["user-library-read", "user-library-modify", "playlist-read-private", "playlist-read-collaborative", "playlist-modify-public", "playlist-modify-private", "user-read-playback-state", "user-read-currently-playing", "app-remote-control", "user-modify-playback-state"]))

                    sp.start_playback()

            # -------------------------------------- BUSCAR EN WEB -------------------------------------- #

                elif any(palabra in comando for palabra in comando_web): #"busca en Google" in comando:
                    # Utilizar el reconocimiento de voz para obtener la palabra o frase a buscar
                    palabra_busqueda = r.recognize_google(audio, language='es-ES')
                    # Utilizar la palabra o frase como argumento para la función de búsqueda de Google
                    webbrowser.open(f"https://www.google.com/search?q={palabra_busqueda}")

            # -------------------------------------- ABRIR TWITCH -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abrirtwitch):
                    webbrowser.open(f"https://www.twitch.tv/")

            # -------------------------------------- ABRIR YOUTUBE -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abriryoutube):
                    webbrowser.open(f"https://www.youtube.com/")

            # -------------------------------------- ABRIR TWITTER -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abrirtwitter):
                    webbrowser.open(f"https://twitter.com/home")

            # -------------------------------------- ABRIR INSTAGRAM -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abririnsta):
                    webbrowser.open(f"https://www.instagram.com")

            # -------------------------------------- SALUDAR ASISTENTE -------------------------------------- #

                elif any(palabra in comando for palabra in comando_saludar):
                    saludos = ["Hola! En que puedo ayudarte?", "Hola como estas?", "Hello! How ar you?"]
                    saludorandom = random.choice(saludos)
                    engine.say(saludorandom)
                    engine.runAndWait()

            # -------------------------------------- BUSCAR EN YT -------------------------------------- #

                elif any(palabra in comando for palabra in comando_webyt):
                    palabra_busqueda = comando.split("busca en youtube")[1].strip()
                    webbrowser.open(f"https://www.youtube.com/results?search_query={palabra_busqueda}")

            # -------------------------------------- BUSCAR EN WIKIPEDIA -------------------------------------- #

                elif any(palabra in comando for palabra in comando_webwikipedia):
                    palabra_busqueda = comando.split("busca en Wikipedia")[1].strip()
                    webbrowser.open(f"https://es.wikipedia.org/wiki/{palabra_busqueda}")

            # -------------------------------------- BUSCAR EN TWITTER -------------------------------------- #

                elif any(palabra in comando for palabra in comando_webtwitter):
                    palabra_busqueda = comando.split("busca en Twitter")[1].strip()
                    webbrowser.open(f"https://twitter.com/search?q={palabra_busqueda}&src=typed_query&f=top")

            # -------------------------------------- BUSCAR EN WIKIPEDIA -------------------------------------- #

                elif any(palabra in comando for palabra in comando_webtwitch):
                    palabra_busqueda = comando.split("busca en twitch")[1].strip()
                    webbrowser.open(f"https://www.twitch.tv/search?term={palabra_busqueda}")

            # -------------------------------------- ABRIR TENDENCIAS TWITTER -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_abrirtendenciastwitter):
                    webbrowser.open(f"https://twitter.com/explore/tabs/trending")

            # -------------------------------------- RESPONDE PREGUNTAS CON OPENAI -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_haz_una_pregunta):
                    subprocess.call("start close_cmdAmino.bat", shell=True)

            # -------------------------------------- DICE LA FECHA ACTUAL -------------------------------------- # 

                elif any(palabra in comando for palabra in comando_fecha):
                    fecha_actual = datetime.datetime.now()

                    fecha_formateada = fecha_actual.strftime("Hoy es %A %d de %B del %Y")

                    engine.say(fecha_formateada)
                    engine.runAndWait()

            # -------------------------------------- ERRORES -------------------------------------- #

                else:
                    engine.say("Lo siento, no entiendo el comando.")
                    engine.runAndWait()
            else:
                engine.say("Lo siento, no te entiendo. ¿Podrías mencionar mi nombre antes de darme una orden?")
        except:
            print("Lo siento, no pude entender lo que dijiste.")
            #engine.say("Lo siento, no pude entender lo que dijiste.")
            engine.runAndWait()

            # -------------------------------------- ##### -------------------------------------- #

# Ejecutar el asistente virtual
asistente_virtual() 

