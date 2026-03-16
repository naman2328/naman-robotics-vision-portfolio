from pathlib import Path

from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips


def create_video(images: list[str], audio: str, filename: str) -> str:
    clips = []

    for img in images:
        clips.append(ImageClip(img).set_duration(3))

    video = concatenate_videoclips(clips)
    audio_clip = AudioFileClip(audio)
    video = video.set_audio(audio_clip)

    output_dir = Path("output/videos")
    output_dir.mkdir(parents=True, exist_ok=True)

    output = output_dir / f"{filename}.mp4"
    video.write_videofile(str(output), fps=24)

    return str(output)
