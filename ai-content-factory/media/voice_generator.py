from pathlib import Path

from gtts import gTTS


def generate_voice(script: str, filename: str) -> str:
    tts = gTTS(script)

    output_dir = Path("output/audio")
    output_dir.mkdir(parents=True, exist_ok=True)

    path = output_dir / f"{filename}.mp3"
    tts.save(str(path))

    return str(path)
