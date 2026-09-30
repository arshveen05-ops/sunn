"""Sunn prototype: transcribe a lecture and write timestamped Markdown (CPU path)."""
import argparse
from faster_whisper import WhisperModel


def stamp(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--out", default="notes.md")
    ap.add_argument("--model", default="base")
    args = ap.parse_args()

    model = WhisperModel(args.model, compute_type="int8")
    segments, info = model.transcribe(args.audio, vad_filter=True)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(f"# Transcript ({info.language})\n\n")
        for seg in segments:
            f.write(f"- [{stamp(seg.start)}] {seg.text.strip()}\n")
    print(f"Saved {args.out}")


if __name__ == "__main__":
    main()
