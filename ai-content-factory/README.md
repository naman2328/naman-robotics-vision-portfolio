# AI Content Factory (v2)

This project generates short-form vertical videos in batches using:

- AI-generated ideas and scripts
- Stable Diffusion images (GPU accelerated)
- TTS voiceovers
- Automated video assembly
- Optional YouTube upload integration

## Project structure

```text
ai-content-factory
├── README.md
├── requirements.txt
├── config.yaml
├── generator
│   ├── idea_generator.py
│   ├── script_generator.py
│   └── prompt_builder.py
├── media
│   ├── image_generator.py
│   ├── voice_generator.py
│   └── video_creator.py
├── automation
│   ├── pipeline.py
│   └── scheduler.py
├── uploader
│   └── youtube_uploader.py
├── assets
│   └── background_music.mp3
└── output
    ├── images
    ├── audio
    └── videos
```

## Setup

1. Install prerequisites:
   - Python 3.10+
   - Git
   - FFmpeg (`ffmpeg -version`)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the `ai-content-factory` directory:

```bash
python automation/pipeline.py
```

## Notes

- Stable Diffusion uses `runwayml/stable-diffusion-v1-5` and prefers CUDA.
- Generated media is stored under `output/`.
- YouTube upload is scaffolded in `uploader/youtube_uploader.py`.
