# 100KG Nak Start Briskwalk? (VO 2) — Steapex Surge (HyperFrames, Format A dengan VO)

- `index.html` — root: 11 klip (footage penuh, tanpa zoom), 7 scene grafik, caption, overlay (bar progres + kilatan putih), VO, SFX
- `compositions/` — `hook`, `padat`, `empuk`, `bounce`, `flex`, `restock`, `cta`, `captions`, `overlay`
- `assets/vo/new-vo.wav` — VO asal (dari `New VO`, tidak diubah)
- `transcript.json` — transkrip dibetulkan (asal Whisper: `transcript.whisper-raw.json`)
- `TRANSKRIP.md` — transkrip, susunan klip, teks tambahan
- `renders/100kg-briskwalk-2.mp4` — video akhir

Footage proxy (60 fps + audio) dikongsi dengan projek `../video` (lihat `../video/README.md`), tidak di-commit.

```bash
npx hyperframes check
npx hyperframes media-treatment --selector video --grading '{"details":{"vignette":0.35}}' --apply
npx hyperframes render -o renders/100kg-briskwalk-2.mp4 -q standard -f 60 --video-bitrate 14M
```
