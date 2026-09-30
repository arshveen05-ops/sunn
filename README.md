# Sunn

Lecture notes that never leave your laptop.

Sunn turns a recorded lecture into a searchable transcript, structured notes and revision cards, running locally on a Snapdragon-powered Windows laptop. Built for the Snapdragon AI Lab Build & Present Challenge by Arshveen Kaur Bhasin.

## Status

- Prototype: `sunn/transcribe.py` transcribes an audio file and writes timestamped Markdown. It runs on any machine (CPU).
- Next: move Whisper to the Snapdragon NPU using models from Qualcomm AI Hub and ONNX Runtime QNN, then add on-device note and card generation.

## Run the prototype

```
pip install -r requirements.txt
python -m sunn.transcribe lecture.mp3 --out notes.md
```

## Pipeline

1. Capture audio (mic or file)
2. Transcribe (Whisper)
3. Summarise into notes and cards (small on-device LLM)
4. Search (local embeddings) and store (Markdown)

## Roadmap

Week 1 NPU transcription. Week 2 notes and cards. Week 3 desktop app. Week 4 testing and installer.

## Licences

Models used will be listed here with their licences as they are added.

