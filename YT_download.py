from pytube import YouTube
import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("python " + sys.argv[0] + " {url file} {output directory path}")
    
    url_file = sys.argv[1]
    output_directory = sys.argv[-1]

    with open(url_file) as f:
        for url in f.readlines():
            yt = YouTube(url.strip())
            music = yt.streams.filter(only_audio=True).first().download(output_path=output_directory)

            base, ext = os.path.splitext(music)
            new_file = base + '.mp3'
            os.rename(music, new_file)
  
            print(yt.title + " has been successfully downloaded.")

    print("Have a good mix !")
