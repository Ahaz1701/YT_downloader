from pytube import YouTube
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("python " + sys.argv[0] + " {url file} {output directory path}")
    
    url_file = sys.argv[1]
    output_directory = sys.argv[-1]
    url_error = []

    with open(url_file) as f:
        for url in list(set(f.read().splitlines())):
            yt = YouTube(url)
            try:
                music = yt.streams.get_audio_only().download(output_path=output_directory)
            except:
                url_error.append(url)
                continue

            base, ext = os.path.splitext(music)
            cpt = 1
            while True:
                new_file = base + '.mp3' if cpt == 1 else base + str(cpt) + '.mp3'
                if not os.path.exists(new_file):
                    os.rename(music, new_file)
                    break
                cpt += 1
  
            print("[+] " + yt.title)

    print("\nHave a good mix !\n")
    [print("[ERROR] " + url) for url in url_error]
