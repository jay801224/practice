import os
import whisper
import time
from whisper.utils import get_writer
from pytube import YouTube
from googletrans import Translator

# 設定變數
URL = 'https://www.youtube.com/watch?v=BPA_xD4ENMU'
OUTPUT_PATH = 'C:\\ytscript'

def fetch_youtube_title(url):
    yt = YouTube(url)
    return yt.title

def download_youtube_audio(url, OUTPUT_PATH):
    yt = YouTube(url)
    yt.register_on_progress_callback(show_progress)
    audio_stream = yt.streams.filter(only_audio=True).first()
    return audio_stream.download(OUTPUT_PATH)

def show_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size
    print(f"Downloading: {progress * 100:.2f}% complete", end='\r')

def file_exists_in_output_path(filename, OUTPUT_PATH):
    return os.path.exists(os.path.join(OUTPUT_PATH, filename))

def transcribe_audio_to_srt(audio_path, model, title):
    print("Starting transcription...")
    start_time = time.time()
    
    w = get_writer('srt', OUTPUT_PATH)
    result = model.transcribe(audio_path)
    if result:
        valid_title = ''.join(e for e in title if e.isalnum() or e.isspace()).rstrip()
        srt_file_name = os.path.join(OUTPUT_PATH, f'{valid_title}.srt')
        print(f"Writing to {srt_file_name}")
        w(result, srt_file_name)
    else:
        print(f"No transcription for segment: {audio_path}")
    
    end_time = time.time()
    print(f"Transcription completed in {end_time - start_time:.2f} seconds.")
    return srt_file_name

def translate_srt_file(srt_file_name):
    translator = Translator()
    with open(srt_file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        translated_content = translator.translate(content, src='zh-cn', dest='zh-tw').text

    output_filename = srt_file_name.replace(".srt", "_轉繁.srt")
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(translated_content)
    print(f"Translated SRT saved to {output_filename}")

def main_transcribe():
    title = fetch_youtube_title(URL)
    print(f"Title of the video: {title}")
    
    yt = YouTube(URL)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_filename = f"{audio_stream.default_filename}"

    if not file_exists_in_output_path(audio_filename, OUTPUT_PATH):
        print("Audio file not found. Downloading...")
        audio_path = download_youtube_audio(URL, OUTPUT_PATH)
    else:
        print("Audio file found. Skipping download...")
        audio_path = os.path.join(OUTPUT_PATH, audio_filename)
        
    model = whisper.load_model('large')
    return transcribe_audio_to_srt(audio_path, model, title)

def main_translate():
    srt_file_name = main_transcribe()
    translate_srt_file(srt_file_name)

if __name__ == '__main__':
    main_transcribe()  # 只生成SRT in 簡體中文
    main_translate()   # 生成SRT in 簡體中文 and then translate to 繁體中文
