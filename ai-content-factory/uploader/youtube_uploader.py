"""YouTube uploader scaffold.

To enable upload:
1. Create OAuth credentials in Google Cloud Console.
2. Install `google-auth-oauthlib` if needed.
3. Implement OAuth flow and upload call to YouTube Data API v3.
"""

from pathlib import Path


def list_videos_for_upload() -> list[Path]:
    videos_dir = Path("output/videos")
    return sorted(videos_dir.glob("*.mp4"))


def upload_all_videos() -> None:
    videos = list_videos_for_upload()
    if not videos:
        print("No videos found in output/videos")
        return

    for video in videos:
        print(f"[TODO] Upload: {video}")


if __name__ == "__main__":
    upload_all_videos()
