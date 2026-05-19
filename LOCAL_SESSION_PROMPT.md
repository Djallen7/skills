# GSR Field Segments Transcription Task

## Task Description

Find all roll-in segments in `/Volumes/media1/GSR/06_FIELD_SEGMENTS` (20 videos total), create audio-only versions, transcribe them, and output transcripts to a new folder in Downloads. Keep original file names for each .txt file. Organize into 4 subfolders based on segment groups.

## Video File Paths (20 total)

### KIDS_CORNER (3 videos)
```
/Volumes/media1/GSR/06_FIELD_SEGMENTS/KIDS_CORNER/KC_S02_Ep024_Copper/01_MASTERS/KC_S02_Ep024_Copper_MASTER_000240_4K_2997_50Mbps.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/KIDS_CORNER/KC_S02_Ep025_RobertAitkenBible/01_MASTERS/KC_S02_Ep025_RobertAitkenBible_MASTER_000240_4K_2997_45Mbps.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/KIDS_CORNER/KC_S02_Ep021_Bobcats/01_MASTERS/KC_S02_Ep021_Bobcats_MASTER_000230_4K_2997_45Mbps.mp4
```

### VIEWER_VOICES (5 videos)
```
/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_01_Liz_Gabe_000034_1080p_2997_40Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_02_Kimmie_Gabe_000037_1080p_2997_40Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_03_Carla_Daniel_000032_1080p_2997_40Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_04_Diane_Daniel_000032_1080p_2997_40Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/VIEWER_VOICES/2026_05_06_5x_Viewer_Voices/01_MASTERS/VV_05_Wanda_Gabe_000031_1080p_2997_40Mbps_H264.mp4
```

### GSR_Q&A (5 videos)
```
/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E21/01_MASTERS/QA_S1_E21_YOUTUBE_000212_1080p_2997_25Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E22/01_MASTERS/QA_S1_E22_YOUTUBE_000228_1080p_2997_30Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E23/01_MASTERS/QA_S1_E23_YOUTUBE_000228_1080p_2997_30Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E24/01_MASTERS/QA_S1_E24_YOUTUBE_000135_1080p_2997_30Mbps_H264.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/GSR_Q&A/QA_S1_E25/01_MASTERS/QA_S1_E25_YOUTUBE_000303_1080p_2997_30Mbps_H264.mp4
```

### FEATURED_RESOURCE (5 videos)
```
/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_01_CarvedInStone_Morgan_000051_4k_2997_40Mbps.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_02_GeneticEntropy_Ben_000054_4k_2997_40Mbps.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_03_TheCreatedCosmos_Morgan_000053_4k_2997_40Mbps.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_04_TheDarwinEffect_Ben_000046_4k_2997_40Mbps.mp4
/Volumes/media1/GSR/06_FIELD_SEGMENTS/FEATURED_RESOURCE/GSR_2026_05_06_5x_FeaturedResources/01_MASTERS/FR_05_TheGeniusOfEarlyMan_Morgan_000106_4k_2997_40Mbps.mp4
```

## Required Output Structure

```
~/Downloads/GSR_Transcripts/
├── KIDS_CORNER/
│   ├── KC_S02_Ep024_Copper_MASTER_000240_4K_2997_50Mbps.txt
│   ├── KC_S02_Ep025_RobertAitkenBible_MASTER_000240_4K_2997_45Mbps.txt
│   └── KC_S02_Ep021_Bobcats_MASTER_000230_4K_2997_45Mbps.txt
├── VIEWER_VOICES/
│   ├── VV_01_Liz_Gabe_000034_1080p_2997_40Mbps_H264.txt
│   ├── VV_02_Kimmie_Gabe_000037_1080p_2997_40Mbps_H264.txt
│   ├── VV_03_Carla_Daniel_000032_1080p_2997_40Mbps_H264.txt
│   ├── VV_04_Diane_Daniel_000032_1080p_2997_40Mbps_H264.txt
│   └── VV_05_Wanda_Gabe_000031_1080p_2997_40Mbps_H264.txt
├── GSR_Q&A/
│   ├── QA_S1_E21_YOUTUBE_000212_1080p_2997_25Mbps_H264.txt
│   ├── QA_S1_E22_YOUTUBE_000228_1080p_2997_30Mbps_H264.txt
│   ├── QA_S1_E23_YOUTUBE_000228_1080p_2997_30Mbps_H264.txt
│   ├── QA_S1_E24_YOUTUBE_000135_1080p_2997_30Mbps_H264.txt
│   └── QA_S1_E25_YOUTUBE_000303_1080p_2997_30Mbps_H264.txt
└── FEATURED_RESOURCE/
    ├── FR_01_CarvedInStone_Morgan_000051_4k_2997_40Mbps.txt
    ├── FR_02_GeneticEntropy_Ben_000054_4k_2997_40Mbps.txt
    ├── FR_03_TheCreatedCosmos_Morgan_000053_4k_2997_40Mbps.txt
    ├── FR_04_TheDarwinEffect_Ben_000046_4k_2997_40Mbps.txt
    └── FR_05_TheGeniusOfEarlyMan_Morgan_000106_4k_2997_40Mbps.txt
```

## Instructions for Local Claude Code Session

Please complete the following:

1. **Verify all 20 video files exist** at the paths listed above
2. **Create output directory structure** at `~/Downloads/GSR_Transcripts/` with the 4 subfolders
3. **For each video:**
   - Extract audio using ffmpeg
   - Transcribe the audio using a transcription tool (Whisper local, Whisper API, or similar)
   - Save transcript as `.txt` with the same base filename as the original video
   - Place in the correct subfolder based on segment group
4. **Clean up** any temporary audio files after transcription
5. **Verify** all 20 transcripts exist in the correct locations before completing
6. **Report** completion status with a summary of any failed files

## Tools Available

- `ffmpeg` for audio extraction (install with `brew install ffmpeg` if needed)
- OpenAI Whisper API (requires `OPENAI_API_KEY` env var) OR local Whisper (`pip install openai-whisper`)
- Standard Python libraries

## Reference Script

A starter Python script is available at `transcribe_field_segments.py` in the `claude/transcribe-field-segments-MTwKY` branch of the `Djallen7/skills` repository. You can use it as a reference or run it directly after setting up the API key.

## Success Criteria

- [ ] All 20 transcript .txt files exist in correct subfolders
- [ ] Filenames match the original video filenames (just with .txt extension)
- [ ] No temporary audio files left behind
- [ ] Transcripts contain readable text content
