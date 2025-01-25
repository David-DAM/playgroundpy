import torch
import whisper


def cuda_works():
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0))


def format_time(seconds):
    ms = int((seconds - int(seconds)) * 1000)
    s = int(seconds) % 60
    m = (int(seconds) // 60) % 60
    h = int(seconds) // 3600
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def generate_subtitles(video_path):
    model_name = "medium"
    model = whisper.load_model(model_name)

    result = model.transcribe(video_path, task="translate", language="es")

    srt_path = "subtitles.srt"
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            srt_file.write(f"{segment['id'] + 1}\n")
            srt_file.write(f"{format_time(start)} --> {format_time(end)}\n")
            srt_file.write(f"{text}\n\n")

    print(f"Subtítle generated in path: {srt_path}")


if __name__ == "__main__":
    # cuda_works()
    generate_subtitles(r"your_file_path")
