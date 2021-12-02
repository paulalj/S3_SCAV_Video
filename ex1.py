import subprocess

def converter():
    # Comanda per convertir a vp8, canviem el códec de vídeo però també d'àudio
    # perquè els arxius .webm tenen códec d'àudio vorbis
    subprocess.call(['ffmpeg', '-i', 'BBB_720.mp4', '-c:v', 'libvpx', '-c:a',
                     'libvorbis', 'BBB_720_vp8.webm'])
    subprocess.call(['ffmpeg', '-i', 'BBB_480.mp4', '-c:v', 'libvpx', '-c:a',
                     'libvorbis', 'BBB_480_vp8.webm'])
    subprocess.call(['ffmpeg', '-i', 'BBB_360x240.mp4', '-c:v', 'libvpx', '-c:a',
                     'libvorbis', 'BBB_360x240_vp8.webm'])
    subprocess.call(['ffmpeg', '-i', 'BBB_160x120.mp4', '-c:v', 'libvpx', '-c:a',
                     'libvorbis', 'BBB_160x120_vp8.webm'])

    # Comanda per convertir a vp9, canviant també l'àudio códec
    subprocess.call(['ffmpeg', '-i', 'BBB_720.mp4', '-c:v', 'libvpx-vp9',
                     '-c:a', 'libvorbis', 'BBB_720_vp9.webm'])
    subprocess.call(['ffmpeg', '-i', 'BBB_480.mp4', '-c:v', 'libvpx-vp9',
                     '-c:a', 'libvorbis', 'BBB_480_vp9.webm'])
    subprocess.call(['ffmpeg', '-i', 'BBB_360x240.mp4', '-c:v', 'libvpx-vp9',
                     '-c:a', 'libvorbis', 'BBB_360x240_vp9.webm'])
    subprocess.call(['ffmpeg', '-i', 'BBB_160x120.mp4', '-c:v', 'libvpx-vp9',
                     '-c:a', 'libvorbis', 'BBB_160x120_vp9.webm'])

    # Comanda per convertir a h265, no canviem el códec d'àudio perquè
    # és el mateix que l'h264
    subprocess.call(['ffmpeg', '-i', 'BBB_720.mp4', '-c:v', 'libx265',
                     'BBB_720_h265.mp4'])
    subprocess.call(['ffmpeg', '-i', 'BBB_480.mp4', '-c:v', 'libx265',
                     'BBB_480_h265.mp4'])
    subprocess.call(['ffmpeg', '-i', 'BBB_360x240.mp4', '-c:v', 'libx265',
                     'BBB_360x240_h265.mp4'])
    subprocess.call(['ffmpeg', '-i', 'BBB_160x120.mp4', '-c:v', 'libx265',
                     'BBB_160x120_h265.mp4'])

    # Comanda per convertir a av1, no canviem el códec d'àudio
    # Utilitzem "-cpu-used 3" perquè d'aquesta manera va més
    # ràpida la conversió.
    subprocess.call(['ffmpeg', '-i', 'BBB_720.mp4', '-c:v', 'libaom-av1',
                     '-cpu-used', '3', 'BBB_720_av1.mp4'])
    subprocess.call(['ffmpeg', '-i', 'BBB_480.mp4', '-c:v', 'libaom-av1',
                     '-cpu-used', '3', 'BBB_480_av1.mp4'])
    subprocess.call(['ffmpeg', '-i', 'BBB_360x240.mp4', '-c:v', 'libaom-av1',
                     '-cpu-used', '3', 'BBB_360x240_av1.mp4'])
    subprocess.call(['ffmpeg', '-i', 'BBB_160x120.mp4', '-c:v', 'libaom-av1',
                     '-cpu-used', '3', 'BBB_160x120_av1.mp4'])

def main():
    converter()

if __name__ == "__main__":
    main()