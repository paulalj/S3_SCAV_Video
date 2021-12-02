import subprocess

def video_vs_video():
    # Comanda per posar els vídeos un al costat de l'altre
    # (primer el de l'esquerra i després el de la dreta)
    subprocess.call(['ffmpeg', '-i', 'BBB_720_vp8.webm', '-i',
                     'BBB_720_vp9.webm', '-filter_complex', 'hstack',
                     'vp8_vs_vp9.mp4'])
    # El vídeo amb códec vp9 es veu molt millor que el de vp8,
    # el de vp8 ha patit una pèrdua de qualitat bastant gran
    # mentre que el vp9 segueix igual.

    subprocess.call(['ffmpeg', '-i', 'BBB_720_h265.mp4', '-i',
                     'BBB_720_av1.mp4', '-filter_complex', 'hstack',
                     'h265_vs_av1.mp4'])
    # Els dos vídeos es veuen igual, no hi ha cap diferència ni de qualitat,
    # ni de color ni de res.

def main():
    video_vs_video()

if __name__ == "__main__":
    main()

