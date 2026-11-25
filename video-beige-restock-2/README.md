# Warna Beige Bila Nak Restock? — Steapex (HyperFrames, Format A dengan VO)

- `index.html` — root: 10 klip, 8 scene grafik, caption, overlay (bar progres + kilatan putih), VO, SFX
- `compositions/` — `hook`, `news`, `size`, `stock`, `colour`, `foam`, `comfort`, `cta`, `captions`, `overlay`
- `assets/vo/new-vo.wav` — VO asal (dari `New VO`, tidak diubah)
- `transcript.json` — transkrip Whisper large-v3 dengan masa perkataan
- `TRANSKRIP.md` — transkrip, susunan klip, teks tambahan
- `renders/beige-restock-vo2.mp4` — video akhir

Footage proxy (60 fps + audio) dikongsi dengan projek `../video` (lihat `../video/README.md`), tidak di-commit.

```bash
npx hyperframes check
npx hyperframes media-treatment --selector video --grading '{"details":{"vignette":0.35}}' --apply
npx hyperframes render -o renders/beige-restock-vo2.mp4 -q standard -f 60 --video-bitrate 14M
```
