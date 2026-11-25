# Tips Jogging Untuk Overweight — Steapex (HyperFrames)

Video menegak 9:16, 55 s, dibina dengan [HyperFrames](https://hyperframes.heygen.com).

- `index.html` — komposisi root: 19 shot footage, 6 scene grafik, muzik, SFX
- `compositions/` — `hook`, `tip1`, `tip2`, `tip3`, `usp`, `cta`
- `TRANSKRIP.md` — transkrip teks on-screen, susunan shot, apa yang dibuang, kredit
- `REVIEW.md` — nota review
- `renders/tips-jogging-overweight.mp4` — video akhir

## Footage (tidak di-commit — ~470 MB)

Proxy H.264 30 fps dalam `assets/footage/` dibuat daripada fail Drive asal:

| Proxy | Fail asal |
| --- | --- |
| `knee-pain.mp4` | B-roll `video_20251226_091215.mp4` |
| `foot-pain.mp4` | B-roll `video_20260429_114700.mp4` |
| `toe-pain.mp4` | B-roll `video_20250529_093604.mp4` |
| `workout.mp4` | `video_20260726_134425.mp4` |
| `beige-indoor.mp4` | `lv_0_20260810105559.mp4` |
| `beige-track.mp4` | `lv_0_20260719163435.mp4` |
| `beige-unbox.mp4` | `lv_0_20260719154019.mp4` |

```bash
ffmpeg -i <asal>.mp4 -an -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p" \
  -c:v libx264 -preset veryfast -crf 19 -g 30 -keyint_min 30 -sc_threshold 0 -movflags +faststart assets/footage/<proxy>.mp4
```

## Render

```bash
npx hyperframes check
npx hyperframes render -o renders/tips-jogging-overweight.mp4 -q standard --crf 20
```
