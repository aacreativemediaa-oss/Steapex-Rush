# Plus Size Nak Start Jogging? — Steapex (HyperFrames, Format A dengan VO)

- `index.html` — root: 10 klip (footage penuh, tanpa zoom), 9 scene grafik, caption, overlay (bar progres + kilatan putih), VO, SFX
- `compositions/` — `hook`, `pain`, `tips`, `absorb`, `steady`, `vent`, `use`, `restock`, `cta`, `captions`, `overlay`
- `assets/vo/new-vo.wav` — VO asal (dari `New VO`, tidak diubah)
- `transcript.json` — transkrip dibetulkan (asal Whisper: `transcript.whisper-raw.json`)
- `TRANSKRIP.md` — transkrip, susunan klip, teks tambahan
- `renders/plus-size-jogging.mp4` — video akhir

Footage proxy (60 fps + audio) dikongsi dengan projek `../video` (lihat `../video/README.md`), tidak di-commit.

```bash
npx hyperframes check
npx hyperframes media-treatment --selector video --grading '{"details":{"vignette":0.35}}' --apply
npx hyperframes render -o renders/plus-size-jogging.mp4 -q standard -f 60 --video-bitrate 14M
```
