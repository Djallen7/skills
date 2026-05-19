#!/usr/bin/env python3
"""
Transcribe field segment videos from GSR.
Extracts audio and creates transcripts organized by segment group.
"""

import os
import subprocess
import json
from pathlib import Path
from openai import OpenAI

# Initialize OpenAI client (uses OPENAI_API_KEY environment variable)
client = OpenAI()

# Define video files organized by segment group
SEGMENT_FILES = {
    "KIDS_CORNER": [
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/KIDS_CORNER/KC_S02_Ep024_Copper/01_MASTERS/KC_S02_Ep024_Copper_MASTER_000240_4K_2997_50Mbps.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/KIDS_CORNER/KC_S02_Ep025_RobertAitkenBible/01_MASTERS/KC_S02_Ep025_RobertAitkenBible_MASTER_000240_4K_2997_45Mbps.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/KIDS_CORNER/KC_S02_Ep021_Bobcats/01_MASTERS/KC_S02_Ep021_Bobcats_MASTER_000230_4K_2997_45Mbps.mp4",
    ],
    "VIEWER_VOICES": [
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_01_Liz_Gabe_000034_1080p_2997_40Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_02_Kimmie_Gabe_000037_1080p_2997_40Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_03_Carla_Daniel_000032_1080p_2997_40Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_04_Diane_Daniel_000032_1080p_2997_40Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_05_Wanda_Gabe_000031_1080p_2997_40Mbps_H264.mp4",
    ],
    "GSR_Q&A": [
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E21/01_MASTERS/QA_S1_E21_YOUTUBE_000212_1080p_2997_25Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E22/01_MASTERS/QA_S1_E22_YOUTUBE_000228_1080p_2997_30Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E23/01_MASTERS/QA_S1_E23_YOUTUBE_000228_1080p_2997_30Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E24/01_MASTERS/QA_S1_E24_YOUTUBE_000135_1080p_2997_30Mbps_H264.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E25/01_MASTERS/QA_S1_E25_YOUTUBE_000303_1080p_2997_30Mbps_H264.mp4",
    ],
    "FEATURED_RESOURCE": [
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_01_CarvedInStone_Morgan_000051_4k_2997_40Mbps.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_02_GeneticEntropy_Ben_000054_4k_2997_40Mbps.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_03_TheCreatedCosmos_Morgan_000053_4k_2997_40Mbps.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_04_TheDarwinEffect_Ben_000046_4k_2997_40Mbps.mp4",
        "/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_05_TheGeniusOfEarlyMan_Morgan_000106_4k_2997_40Mbps.mp4",
    ],
}


def setup_output_directories():
    """Create output directories in Downloads for each segment group."""
    base_dir = Path.home() / "Downloads" / "GSR_Transcripts"
    base_dir.mkdir(exist_ok=True)

    dirs = {}
    for group in SEGMENT_FILES.keys():
        group_dir = base_dir / group
        group_dir.mkdir(exist_ok=True)
        dirs[group] = group_dir

    return base_dir, dirs


def extract_audio(video_path, output_audio_path):
    """Extract audio from video using ffmpeg."""
    print(f"Extracting audio from: {Path(video_path).name}")
    try:
        subprocess.run(
            ["ffmpeg", "-i", video_path, "-q:a", "9", "-n", output_audio_path],
            capture_output=True,
            check=True,
        )
        print(f"  ✓ Audio extracted to: {output_audio_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Error extracting audio: {e}")
        return False


def transcribe_audio(audio_path):
    """Transcribe audio using OpenAI Whisper API."""
    print(f"Transcribing: {Path(audio_path).name}")
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
            )
        print(f"  ✓ Transcription complete")
        return transcript.text
    except Exception as e:
        print(f"  ✗ Error transcribing: {e}")
        return None


def process_segment_group(group_name, video_paths, output_dir):
    """Process all videos in a segment group."""
    print(f"\n{'='*60}")
    print(f"Processing: {group_name}")
    print(f"{'='*60}")

    success_count = 0

    for video_path in video_paths:
        if not os.path.exists(video_path):
            print(f"✗ File not found: {video_path}")
            continue

        # Get base filename without extension
        filename_base = Path(video_path).stem

        # Create temporary audio file path
        audio_path = output_dir / f"{filename_base}.wav"

        # Extract audio
        if not extract_audio(video_path, str(audio_path)):
            continue

        # Transcribe audio
        transcript = transcribe_audio(str(audio_path))
        if not transcript:
            continue

        # Save transcript
        transcript_path = output_dir / f"{filename_base}.txt"
        transcript_path.write_text(transcript)
        print(f"  ✓ Transcript saved to: {transcript_path.name}")

        # Clean up audio file
        audio_path.unlink()
        print(f"  ✓ Audio file removed")

        success_count += 1

    print(f"\n{group_name}: {success_count}/{len(video_paths)} processed successfully")
    return success_count


def main():
    """Main execution function."""
    print("GSR Field Segments Transcription Tool")
    print("="*60)

    # Check dependencies
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: ffmpeg not found. Install it with: brew install ffmpeg")
        return

    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        return

    # Setup output directories
    base_dir, output_dirs = setup_output_directories()
    print(f"Output directory: {base_dir}\n")

    # Process each segment group
    total_success = 0
    for group_name, video_paths in SEGMENT_FILES.items():
        success = process_segment_group(group_name, video_paths, output_dirs[group_name])
        total_success += success

    # Summary
    total_files = sum(len(paths) for paths in SEGMENT_FILES.values())
    print(f"\n{'='*60}")
    print(f"SUMMARY: {total_success}/{total_files} transcripts created")
    print(f"Output saved to: {base_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
