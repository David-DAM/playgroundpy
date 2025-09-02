import os


def srt_to_vtt(input_srt, output_vtt):
    with open(input_srt, "r", encoding="utf-8") as srt_file:
        lines = srt_file.readlines()

    master_output = os.path.join(output_vtt, "subtitles.vtt")

    with open(master_output, "w", encoding="utf-8") as vtt_file:
        vtt_file.write("WEBVTT\n\n")  # cabecera obligatoria VTT

        for line in lines:
            # Convertir línea de tiempo
            if "-->" in line:
                line = line.replace(",", ".")
            # Ignorar los índices de SRT (números de línea)
            if line.strip().isdigit():
                continue
            vtt_file.write(line)

    print(f"Archivo VTT generado en: {master_output}")


if __name__ == "__main__":
    input_srt = r""
    output_vtt = r""

    srt_to_vtt(input_srt, output_vtt)
