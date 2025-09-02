import os.path

import torch
import whisper


def cuda_works():
    print(torch.cuda.is_available())
    if torch.cuda.is_available():
        print(torch.cuda.get_device_name(0))


def format_time_vtt(seconds):
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02}:{m:02}:{s:02}.{ms:03}"  # VTT usa punto para los milisegundos


def generate_subtitles_vtt(input_path, output_path):
    model_name = "medium"
    model = whisper.load_model(model_name)

    result = model.transcribe(input_path, language="es")

    master_output = os.path.join(output_path, "subtitles.vtt")

    with open(master_output, "w", encoding="utf-8") as vtt_file:
        vtt_file.write("WEBVTT\n\n")  # cabecera obligatoria VTT
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            vtt_file.write(f"{format_time_vtt(start)} --> {format_time_vtt(end)}\n")
            vtt_file.write(f"{text}\n\n")

    print(f"Subtítulo VTT generado en: {master_output}")


if __name__ == "__main__":
    input_video = r""
    output_vtt = r""

    # cuda_works()
    generate_subtitles_vtt(input_video, output_vtt)
