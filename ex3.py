import subprocess

def broadcast(ip):
    # Afegim la IP donada per l'usuari a la comanda que
    # necessitarem per l'FFMPEG
    IP="udp://"+ip+":5000"

    #Amb aquesta comanda fem el broadcast a la IP desitjada en el port 5000
    subprocess.call(["ffmpeg", "-re", "-i", "BBB.mp4",
                     "-vcodec", "copy", "-acodec", "copy", "-f", "mpegts", IP])

def main():
    ip=input("Digues l'adreça IP: ")
    if ip=="":
        ip="127.0.0.1"
    broadcast(ip)

if __name__ == "__main__":
    main()