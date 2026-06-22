from pathlib import Path

import torch
from diffusers import StableDiffusionPipeline

_pipe = None


def _get_pipeline() -> StableDiffusionPipeline:
    global _pipe
    if _pipe is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5"
        ).to(device)
    return _pipe


def generate_images(prompts: list[str], prefix: str = "img") -> list[str]:
    output_dir = Path("output/images")
    output_dir.mkdir(parents=True, exist_ok=True)

    pipe = _get_pipeline()
    paths = []

    for i, prompt in enumerate(prompts):
        image = pipe(prompt).images[0]
        path = output_dir / f"{prefix}_{i}.png"
        image.save(path)
        paths.append(str(path))

    return paths
