# REVIEW — Tips Jogging Untuk Overweight (v2, ikut Format Edit Video)

## Keputusan
- Ikut **Format Edit Video, Format B (tanpa VO)**. Pengguna minta **warna tulisan dikekalkan** (merah Steapex #E8322B, putih, gelap, beige). Jadi warna format (pink/hijau) **hanya** digunakan pada bar progres pink→hijau. Blok tulisan kekal merah/putih.
- **10 klip**, 45.8 s, intro satu shot (B-roll sakit lutut, laju asal).
- **Saiz:** headline hook 100px (paling besar). Hook sub-headline & pelekat save 47px. Sub-headline penerangan 35px tidak bold (permintaan pengguna). Nombor heart rate "ZONE 2" 64px. Tajuk babak 76–92px. Nombor 15–20 96px. Kad CTA 72–96px. Pill ✓/⚠ 40px. Label kecil (Zone 1–5, KELEBIHAN #, nama warna) 19px.
- **Font:** Anton (fail dalam `assets/fonts`) untuk headline, tajuk dan nombor. Montserrat 800/900 untuk pill, label dan sub-headline.
- **Setiap klip:** zoom masuk 1.18→1.04 dalam 0.35 s, kemudian push perlahan ke 1.10, dengan kilatan putih pada setiap potongan. Vignette 0.35 melalui `media-treatment`.
- **Gegar skrin:** pada hook (impact) dan cop RESTOCK.
- **Bunyi:** tiada muzik latar. Bunyi asal setiap klip −57 LUFS, diukur pada segmen yang dipakai. SFX disintesis sendiri.

## Diukur vs dilihat
- `check`: 0 error. 3 amaran `text_below_floor` **disimpan dengan sengaja**, kerana format menetapkan 19px untuk label kecil (Zone 1–5, KELEBIHAN #1/#2, label "BEIGE").
- Snapshot setiap babak dilihat. Dibetulkan:
  - Ilustrasi kasut Edu ③ jatuh atas kepala orang, jadi dibuang.
  - Sub-headline USP wrap tak kemas, jadi baris dipecah sendiri.
  - "Plate keras" bertindih dengan sub-headline, jadi dipisah ke dua baris.
- Render akhir: 1080×1920, 60 fps, 45.8 s, 64.5 MB. Audio -22.5 LUFS (tiada muzik; SFX + bunyi asal), true peak -5.1 dBTP, tiada clipping — **diukur, tidak didengar**.

## Shot paling lemah
- Edu ② guna kasut putih/pink (tiada footage squat dengan kasut beige).
