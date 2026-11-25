# Tips Jogging Untuk Overweight — Steapex (HyperFrames)

Video menegak 9:16, 45.8 s, 60 fps, dibina dengan [HyperFrames](https://hyperframes.heygen.com) ikut *Format Edit Video* (Format B — tanpa voiceover).

- `index.html` — komposisi root: 10 klip (bunyi asal −57 LUFS), 6 scene grafik + overlay, SFX
- `compositions/` — `hook`, `edu1`, `edu2`, `edu3`, `usp`, `cta`, `overlay` (bar progres + kilatan putih)
- `tools/synth_sfx.py` — jana semua SFX (`python3 tools/synth_sfx.py assets/sfx`)
- `assets/fonts/Anton-Regular.ttf` — Anton (SIL OFL)
- `TRANSKRIP.md` — transkrip teks on-screen, susunan shot, apa yang dibuang, kredit
- `REVIEW.md` — nota review
- `renders/tips-jogging-overweight.mp4` — video akhir

## Footage (tidak di-commit — ~470 MB)

Proxy H.264 60 fps (dengan audio asal) dalam `assets/footage/` dibuat daripada fail Drive asal:

| Proxy | Fail asal |
| --- | --- |
| `knee-pain.mp4` | B-roll `video_20251226_091215.mp4` |
| `foot-pain.mp4` | B-roll `video_20260429_114700.mp4` |
| `workout.mp4` | `video_20260726_134425.mp4` |
| `beige-indoor.mp4` | `lv_0_20260810105559.mp4` |
| `beige-track.mp4` | `lv_0_20260719163435.mp4` |
| `beige-unbox.mp4` | `lv_0_20260719154019.mp4` |

```bash
ffmpeg -i <asal>.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=60,format=yuv420p" \
  -c:v libx264 -preset veryfast -crf 20 -g 60 -keyint_min 60 -sc_threshold 0 -c:a aac -b:a 160k -ar 48000 -movflags +faststart assets/footage/<proxy>.mp4
```

## Render

```bash
npx hyperframes check
npx hyperframes media-treatment --selector video --grading '{"details":{"vignette":0.35}}' --apply   # vignette
npx hyperframes render -o renders/tips-jogging-overweight.mp4 -q standard -f 60 --video-bitrate 11M   # ≤70MB
```
