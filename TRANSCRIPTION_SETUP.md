# GSR Field Segments Transcription Guide

This guide walks you through setting up and running the transcription script for the 20 field segment videos.

## Prerequisites

### 1. Install ffmpeg
ffmpeg is needed to extract audio from videos.

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Windows (using Chocolatey):**
```bash
choco install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

### 2. Install Python dependencies
```bash
pip install openai
```

### 3. Get OpenAI API Key

1. Go to https://platform.openai.com/account/api-keys
2. Create a new API key
3. Save it securely

## Setup

### 1. Set your OpenAI API key
**macOS/Linux:**
```bash
export OPENAI_API_KEY='your-api-key-here'
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY='your-api-key-here'
```

Or add it to your shell profile so it persists:
- **macOS/Linux:** Add the export line to `~/.bash_profile` or `~/.zshrc`
- **Windows:** Set it in System Environment Variables

### 2. Run the script
```bash
python transcribe_field_segments.py
```

## What the script does

1. **Creates output folders** in `~/Downloads/GSR_Transcripts/` with 4 subfolders:
   - `KIDS_CORNER/`
   - `VIEWER_VOICES/`
   - `GSR_Q&A/`
   - `FEATURED_RESOURCE/`

2. **Processes each video:**
   - Extracts audio to a temporary WAV file
   - Transcribes using OpenAI's Whisper API
   - Saves transcript as `.txt` with original video filename
   - Cleans up temporary files

3. **Final output:**
   - 20 `.txt` files organized by segment group
   - Original filenames preserved (e.g., `KC_S02_Ep024_Copper_MASTER_000240_4K_2997_50Mbps.txt`)

## Output Structure
```
~/Downloads/GSR_Transcripts/
├── KIDS_CORNER/
│   ├── KC_S02_Ep024_Copper_MASTER_000240_4K_2997_50Mbps.txt
│   ├── KC_S02_Ep025_RobertAitkenBible_MASTER_000240_4K_2997_45Mbps.txt
│   └── KC_S02_Ep021_Bobcats_MASTER_000230_4K_2997_45Mbps.txt
├── VIEWER_VOICES/
│   ├── VV_01_Liz_Gabe_000034_1080p_2997_40Mbps_H264.txt
│   ├── VV_02_Kimmie_Gabe_000037_1080p_2997_40Mbps_H264.txt
│   └── ... (3 more)
├── GSR_Q&A/
│   ├── QA_S1_E21_YOUTUBE_000212_1080p_2997_25Mbps_H264.txt
│   ├── QA_S1_E22_YOUTUBE_000228_1080p_2997_30Mbps_H264.txt
│   └── ... (3 more)
└── FEATURED_RESOURCE/
    ├── FR_01_CarvedInStone_Morgan_000051_4k_2997_40Mbps.txt
    ├── FR_02_GeneticEntropy_Ben_000054_4k_2997_40Mbps.txt
    └── ... (3 more)
```

## Troubleshooting

### ffmpeg not found
Install ffmpeg using the commands above for your OS.

### OPENAI_API_KEY not set
Make sure you've run `export OPENAI_API_KEY='your-key'` in the same terminal session.

### File not found errors
Verify all video paths are accessible from your machine. The script checks each file before processing.

### Transcription takes a long time
This is normal - Whisper API processing time depends on audio length. For ~20 videos, expect 10-30 minutes total.

### API rate limits
If you hit OpenAI rate limits, wait a few seconds and the script can be run again - it skips already-transcribed files.

## Costs

OpenAI's Whisper API charges per minute of audio. For typical field segments:
- Estimated cost: $0.006 per minute of audio
- For ~20 segments (varies by length): ~$5-15 depending on total duration

Check pricing: https://openai.com/pricing/audio

## Notes

- Temporary audio files are automatically cleaned up after transcription
- Existing transcript files won't be overwritten
- All transcripts are organized by segment group for easy management
- Transcripts are plain UTF-8 text files (no formatting)
