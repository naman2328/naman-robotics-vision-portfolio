import os
from pathlib import Path

import yaml

from generator.idea_generator import generate_idea
from generator.prompt_builder import build_prompts
from generator.script_generator import generate_script
from media.image_generator import generate_images
from media.video_creator import create_video
from media.voice_generator import generate_voice


BASE_DIR = Path(__file__).resolve().parents[1]


def main() -> None:
    os.chdir(BASE_DIR)

    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    videos = config["videos_per_run"]
    img_count = config["image_per_video"]

    os.makedirs("output/images", exist_ok=True)
    os.makedirs("output/audio", exist_ok=True)
    os.makedirs("output/videos", exist_ok=True)

    for i in range(videos):
        idea = generate_idea()
        script = generate_script(idea)
        prompts = build_prompts(script, img_count)

        images = generate_images(prompts, prefix=f"video_{i}_img")
        audio = generate_voice(script, f"voice_{i}")
        video = create_video(images, audio, f"video_{i}")

        print("Video created:", video)


if __name__ == "__main__":
    main()
