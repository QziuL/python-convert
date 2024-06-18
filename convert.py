import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

def check_ffmpeg_installed():
    try:
        subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def convert_video_to_mp3():
    if not check_ffmpeg_installed():
        messagebox.showerror("Erro", "FFmpeg não está instalado. Por favor, instale o FFmpeg para continuar.")
        return

    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'downloaded_audio.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        new_file = 'downloaded_audio.mp3'
        messagebox.showinfo("Sucesso", f"Download concluído: {new_file}")

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao converter o vídeo: {e}")


# Configuração da interface gráfica
root = tk.Tk()
root.title("YouTube to MP3 Converter")

tk.Label(root, text="URL do YouTube:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

convert_button = tk.Button(root, text="Converter", command=convert_video_to_mp3)
convert_button.pack(pady=20)

root.mainloop()