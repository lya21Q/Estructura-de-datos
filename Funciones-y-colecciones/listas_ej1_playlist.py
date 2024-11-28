"""
Rosalinda Aquino pérez
"""
op=None
def menu():
    print("*** Este programa es una playlist de videos de Youtube ***")
    print("[1].- Ver playlist por videos añadidos.")
    print("[2].-Ver playlist por orden ascendente (A-Z).")
    print("[3].-Ver playlist por orden descendente (Z-A).")
    print("[4].-Añadir video de YouTube a la playlist.")
    print("[5].-Añadir varios videos de YouTube a la playlist.")
    print("[6].-Eliminar video de la playlist.")
    print("[7].-: Eliminar video")
    print("[0].-: Salir del programa")
    op = int(input("ingrese una opción:"))
    return op

playlist=[]
def videos(op,playlist):
    while op!=0:
        if(op==1):
            for video in playlist:
                print(f"videos añadido:{video}")
        elif(op==2):
            for video in playlist:
                playlist.sort()
                print(video)
        elif(op==3):
            for video in playlist:
                playlist.sort(reverse = True )
                print(video)
        elif(op==4):
            video=input("Ingrese una lista de videos a la playlist:")
            playlist.append(video)
            print(f"Video '{video}' añadido a la playlist.")
        elif(op==5):
            num_videos = int(input("¿Cuántos videos desea añadir? "))
            for video in range(num_videos):
                video=input("ingrese un video: ")
                playlist.append(video)
                print(f"Video añadido: {video}")
        elif(op==6):
            print(f"Ingrese el nombre del video")
            playlist.remove(video)
            print(f"El video eliminado Video {video}")
        else:
            print("Opcion no vàlida")
    return playlist
op=menu()
playlist=videos(op,playlist)