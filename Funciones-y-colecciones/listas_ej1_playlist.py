"""
Rosalinda Aquino pérez
Descripción del programa:Este programa es una playlist de videos de Youtube.
"""
op=None#Variable que controla las opciones.
playlist = []
while op!=0:
    print("*** Este programa es una playlist de videos de Youtube ***")
    print("[1].- Ver playlist por videos añadidos.")
    print("[2].-Ver playlist por orden ascendente (A-Z).")
    print("[3].-Ver playlist por orden descendente (Z-A).")
    print("[4].-Añadir video de YouTube a la playlist.")
    print("[5].-Añadir varios videos de YouTube a la playlist.")
    print("[6].-Eliminar video de la playlist.")
    print("[0].-: Salir del programa")
    #Solicita al usuario que ingrese una opción.
    op = int(input("ingrese una opción:"))
#Csaso para salir del programa.
    if op==0:
        print("Saliendo del programa.")
    #caso para ver la playlist de videos añadidos.
    elif op==1:
        numero=1
        for playlist in playlist:
            print(f"videos añadidos:{numero}.-{playlist}")
            numero+=1
    #Caso para ver playlist por orden ascendente(A-Z).
    elif op==2:
        playlist.sort()
        for video in playlist:
            print(video,end=",")
    # Caso para ver playlist por orden descendente(Z-A).
    elif op==3:
        playlist.sort(reverse=True)
        for video in playlist:
            print(video,end=",")
    #Caso para añadir video de yotube a la playlist.
    elif op==4:
        video=input("Agregue el nombre del video a ala playlist:")
        playlist.append(video)
        print(f"Video {video} añadido a la playlist.")
    #Caso para añadir a varios videos a la playlis.
    elif op==5:
        num_videos = int(input("¿Cuántos videos desea añadir? "))
        contador=1
        while contador <=num_videos:
            video=input("ingrese un video: ")
            playlist.append(video)
            contador+=1
            print(f"Video añadido: {video}")
    #Caso para eliminar un video de la playlist.
    elif op==6:
        video_eliminar=input(f"Ingrese el nombre del video:")
        playlist.remove(video_eliminar)
    else:
        print("Opcion no vàlida")