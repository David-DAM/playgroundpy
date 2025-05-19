import os
import subprocess


def convert_to_hls_multires(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    renditions = [
        {"name": "1080p", "scale": "1920:1080", "bitrate": "5000k", "maxrate": "5350k", "bufsize": "7500k"},
        {"name": "720p", "scale": "1280:720", "bitrate": "2800k", "maxrate": "2996k", "bufsize": "4200k"},
    ]

    # Comando ffmpeg básico con mapas de video para cada resolución
    command = ["ffmpeg", "-i", input_file]

    variant_playlist_lines = []

    for i, r in enumerate(renditions):
        out_path = os.path.join(output_dir, r["name"])
        os.makedirs(out_path, exist_ok=True)
        playlist_name = f"{r['name']}.m3u8"

        command += [
            "-vf", f"scale=w={r['scale'].split(':')[0]}:h={r['scale'].split(':')[1]}",
            "-c:a", "aac", "-ar", "48000", "-c:v", "h264", "-profile:v", "main",
            "-crf", "20", "-sc_threshold", "0",
            "-g", "48", "-keyint_min", "48",
            "-b:v", r["bitrate"],
            "-maxrate", r["maxrate"],
            "-bufsize", r["bufsize"],
            "-hls_time", "4",
            "-hls_segment_filename", os.path.join(out_path, f"{r['name']}_%03d.ts"),
            os.path.join(out_path, playlist_name)
        ]

        # Línea para master playlist
        variant_playlist_lines.append(
            f'#EXT-X-STREAM-INF:BANDWIDTH={r["bitrate"].replace("k", "000")},RESOLUTION={r["scale"]}\n{r["name"]}/{playlist_name}'
        )

    # Ejecutar ffmpeg
    subprocess.run(command, check=True)

    # Crear playlist maestro
    master_playlist_path = os.path.join(output_dir, "master.m3u8")
    with open(master_playlist_path, "w") as f:
        f.write("#EXTM3U\n")
        for line in variant_playlist_lines:
            f.write(line + "\n")

    print(f"HLS generado en múltiples calidades. Playlist maestro: {master_playlist_path}")


if __name__ == "__main__":
    convert_to_hls_multires(
        r"C:\Users\david\Videos\Social media\Products\Web template\Presentacion\Trailer Spring Boot Web Template EN.mp4",
        "output_hls")
