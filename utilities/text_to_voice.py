import re

import pyttsx3


def show_voices_available():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for i, voice in enumerate(voices):
        print(f"Voice {i}: {voice.name}, {voice.id}, {voice.languages}")


def read_srt_file_in_blocks(subtitles, block_size=500):
    subtitles_split = subtitles.split(". ")
    for i in range(0, len(subtitles_split), block_size):
        yield " ".join(subtitles_split[i:i + block_size])


def process_in_blocks(engine, subtitles):
    for i, text_block in enumerate(read_srt_file_in_blocks(subtitles)):
        audio_file = f"audio_part_{i + 1}.mp3"
        engine.save_to_file(text_block, audio_file)
        print(f"Generating: {audio_file}")
        engine.runAndWait()


def process_all(engine, subtitles):
    engine.save_to_file(subtitles, "audio.mp3")
    engine.runAndWait()


def generate_voice(text_path):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)

    engine.setProperty('volume', 0.9)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    with open(text_path, "r") as file:
        content = file.read()

        text = re.findall(
            r"(?<=\n\n)(?:\d+\n)?\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n(.+?)(?=\n\n|\Z)", content,
            re.DOTALL)
        
        subtitles = " ".join(text)

        # process_in_blocks(engine, subtitles)
        process_all(engine, subtitles)
        print("Audio generated successfully!")


if __name__ == "__main__":
    generate_voice("subtitles.srt")
