import os
import subprocess


def convert_to_hls_multires(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    renditions = [
        {"name": "1080p", "scale": "1920:1080", "bitrate": "3500k", "maxrate": "3850k", "bufsize": "5250k",
         "hls_time": 10},
        {"name": "720p", "scale": "1280:720", "bitrate": "2800k", "maxrate": "2996k", "bufsize": "4200k",
         "hls_time": 10},
        {"name": "480p", "scale": "854:480", "bitrate": "1400k", "maxrate": "1498k", "bufsize": "2100k", "hls_time": 4},
        {"name": "360p", "scale": "640:360", "bitrate": "800k", "maxrate": "856k", "bufsize": "1200k", "hls_time": 4},
    ]

    variant_playlist_lines = []

    for r in renditions:
        print(f"Procesando {r['name']}...")

        out_path = os.path.join(output_dir, r["name"])
        os.makedirs(out_path, exist_ok=True)
        playlist_name = f"{r['name']}.m3u8"

        command = [
            "ffmpeg", "-y",
            "-hwaccel", "cuda",
            "-i", input_file,
            "-vf", f"hwupload_cuda,scale_cuda={r['scale']}:format=yuv420p",
            "-c:a", "aac", "-ar", "48000",
            "-c:v", "h264_nvenc",
            "-preset", "p4",
            "-b:v", r["bitrate"],
            "-maxrate", r["maxrate"],
            "-bufsize", r["bufsize"],
            "-g", "60",
            "-sc_threshold", "0",
            "-hls_time", str(r["hls_time"]),
            "-hls_playlist_type", "vod",
            "-hls_segment_filename", os.path.join(out_path, f"{r['name']}_%03d.ts"),
            os.path.join(out_path, playlist_name)
        ]

        subprocess.run(command, check=True)

        resolution = r["scale"]
        bandwidth = r["bitrate"].replace("k", "000")
        variant_playlist_lines.append(
            f'#EXT-X-STREAM-INF:BANDWIDTH={bandwidth},RESOLUTION={resolution}\n{r["name"]}/{playlist_name}'
        )

    master_playlist_path = os.path.join(output_dir, "master.m3u8")
    with open(master_playlist_path, "w") as f:
        f.write("#EXTM3U\n")
        for line in variant_playlist_lines:
            f.write(line + "\n")

    print(f"\n✅ HLS generado con éxito. Playlist maestro: {master_playlist_path}")


if __name__ == "__main__":
    convert_to_hls_multires(
        r"C:\Users\david\Videos\Social media\Cursos\Java Moderno de Cero a Experto\Introduccion\Introducción Curso Java Moderno de Cero a Experto.mp4",
        r"C:\Users\david\Videos\Social media\Cursos\Java Moderno de Cero a Experto\Introduccion"
    )
