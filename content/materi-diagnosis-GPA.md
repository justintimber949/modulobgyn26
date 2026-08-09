---
title: "Cara Menulis Diagnosis Kehamilan Format G-P-Ab"
description: "Panduan lengkap menulis status obstetri G_P____Ab___ (Gravida, Para 4 digit sistem TPAL, Abortus 3 digit), lengkap dengan contoh kasus dan verifikasi."
date: 2026-07-19
tags:
  - obgyn
  - obstetri
  - koas
  - diagnosis
  - status-obstetri
aliases:
  - GPA
  - G-P-Ab
  - TPAL
  - Status Obstetri GPA
draft: false
---

# Cara Menulis Diagnosis Kehamilan Format G-P(4 digit)-Ab(3 digit)

> [!info] Ringkasan
> Materi ini membahas cara menulis status obstetri dengan format `G_P____Ab___` — mencakup arti tiap digit, hubungan matematis antara digit ke-3 P dan bagian Ab, contoh kasus, serta kesalahan umum yang perlu dihindari.

## Daftar Isi

- [[#1. Pendahuluan]]
- [[#2. Gravida (G) — 1 Digit]]
- [[#3. Para (P) — 4 Digit, Sistem TPAL]]
- [[#4. Abortus (Ab) — 3 Digit]]
- [[#5. Contoh Kasus Lengkap]]
- [[#6. Kesalahan Umum yang Perlu Dihindari]]
- [[#7. Ringkasan / Cheat Sheet]]

## 1. Pendahuluan

Status obstetri (GPA) adalah ringkasan riwayat kehamilan seorang pasien yang ditulis dalam kode singkat pada diagnosis. Format lengkap yang sering dipakai di rumah sakit pendidikan:

```
G_ P____ Ab___
```

- **G (Gravida)** — total jumlah kehamilan, termasuk kehamilan yang sedang berlangsung sekarang
- **P (Para)** — 4 digit, merinci hasil persalinan menurut sistem **TPAL**
- **Ab (Abortus)** — 3 digit, merinci jenis-jenis keguguran/abortus

Format ini adalah gabungan dari sistem GPA klasik dengan sistem TPAL yang lebih rinci, sehingga satu baris diagnosis sudah memuat gambaran obstetri yang cukup lengkap.

---

## 2. Gravida (G) — 1 Digit

**G = jumlah seluruh kehamilan**, dihitung dari:

- Semua kehamilan yang pernah dialami (berapapun hasilnya: lahir hidup, lahir mati, abortus, kehamilan ektopik, mola)
- **Kehamilan saat ini ikut dihitung**

Contoh: pasien datang ANC, ini kehamilan ketiganya (2 kehamilan sebelumnya + yang sekarang) → **G3**

> [!warning] Kesalahan umum
> Lupa memasukkan kehamilan saat ini ke dalam hitungan G.

---

## 3. Para (P) — 4 Digit, Sistem TPAL

Empat digit setelah P masing-masing mewakili satu huruf dari **T-P-A-L**:

| Digit ke- | Kode            | Kepanjangan             | Definisi                                                      |
| --------- | --------------- | ----------------------- | ------------------------------------------------------------- |
| 1         | **T** (Term)    | Persalinan cukup bulan  | Bayi lahir pada usia kehamilan **≥ 37 minggu**                |
| 2         | **P** (Preterm) | Persalinan kurang bulan | Bayi lahir pada usia kehamilan **20–36 minggu 6 hari**        |
| 3         | **A** (Abortus) | Keguguran               | Kehamilan berakhir **< 20 minggu** (spontan maupun disengaja) |
| 4         | **L** (Living)  | Anak hidup              | Jumlah anak yang **saat ini masih hidup**                     |

Jadi kalau ditulis P2011, artinya:

- Digit 1 = 2 → 2 kali melahirkan cukup bulan
- Digit 2 = 0 → tidak ada persalinan preterm
- Digit 3 = 1 → 1 kali abortus
- Digit 4 = 1 → 1 anak hidup saat ini

### Digit ke-3 P dan hubungannya dengan bagian Ab — penjelasan mendalam

Ini bagian yang paling sering membingungkan, jadi perlu dibahas tuntas.

**Definisi digit ke-3 dalam sistem TPAL itu baku dan tidak bersyarat**: digit ini menghitung **setiap kehamilan yang berakhir sebelum usia 20 minggu**, apapun penyebabnya — baik itu abortus spontan, abortus provokatus (medisinalis maupun kriminalis), maupun kehamilan ektopik yang berakhir. Definisi ini konsisten di seluruh literatur GTPAL/TPAL, tanpa pengecualian untuk "jenis abortus tertentu". Artinya: **begitu ada riwayat kehamilan yang berakhir <20 minggu — apapun bentuknya — digit ke-3 P wajib bertambah**.

**Lalu, kenapa ada bagian Ab yang seolah mengulang informasi ini di akhir diagnosis?**

Karena fungsinya bukan mengulang, melainkan **merinci**. Bandingkan dengan digit ke-4 (L / Living) yang juga sebetulnya bisa "diturunkan" dari digit T dan P (jumlah anak hidup biasanya berkorelasi dengan jumlah persalinan), tapi tetap dicantumkan terpisah karena tidak semua bayi yang lahir (term atau preterm) otomatis masih hidup sekarang — bisa saja meninggal setelah lahir. L memberi informasi tambahan yang tidak bisa disimpulkan hanya dari T dan P.

Prinsip yang sama berlaku untuk pasangan **digit ke-3 P** dan **Ab**:

- **Digit ke-3 P** menjawab pertanyaan: _"berapa total kali pasien mengalami kehamilan yang berakhir <20 minggu?"_
- **Bagian Ab** menjawab pertanyaan lanjutan: _"dari total itu, apa saja jenisnya — spontan, provokatus, atau ektopik?"_

Kedua angka ini **saling melengkapi, bukan saling menggantikan**. Sama seperti T dan P (term dan preterm) yang keduanya digit terpisah tapi sama-sama bagian dari "jumlah total persalinan", digit ke-3 P dan tiga digit Ab juga membentuk hubungan total-dan-rincian:

```
digit ke-3 P  =  digit1 Ab + digit2 Ab + digit3 Ab
   (total)         (spontan) (provokatus) (ektopik)
```

**Kenapa versi "digit ke-3 P dibiarkan 0 karena sudah ada Ab" itu bermasalah?**

1. **Bertentangan dengan definisi baku TPAL.** Kalau digit ke-3 P dipaksa 0 padahal pasien punya riwayat abortus, maka digit tersebut menjadi salah secara definisi — bukan lagi merepresentasikan "jumlah kehamilan <20 minggu", melainkan sesuatu yang lain yang tidak didefinisikan di textbook manapun.
2. **Berisiko secara klinis.** Dalam praktik sehari-hari, banyak tenaga medis yang membaca status pasien secara cepat hanya dari rangkaian G-P saja (misalnya saat serah terima jaga, atau membaca ringkasan singkat), tanpa sempat membaca rincian Ab di baris/bagian berikutnya. Kalau digit ke-3 P selalu 0, maka pembaca cepat akan menyimpulkan pasien **tidak pernah** abortus — padahal riwayat abortus (apalagi berulang) sangat relevan secara klinis: berkaitan dengan risiko inkompetensi serviks, risiko abortus berulang (recurrent pregnancy loss), kebutuhan skrining tambahan, dsb. Sistem pencatatan medis semestinya tidak pernah menyembunyikan informasi klinis penting demi alasan "menghindari duplikasi".
3. **Duplikasi bukan masalah nyata dalam rekam medis.** Banyak sistem dokumentasi klinis memang sengaja mengulang informasi penting di beberapa tempat sekaligus (misalnya alergi obat dicatat di gelang pasien, status rekam medis, dan resep sekaligus) justru demi keamanan pasien, bukan dianggap cacat desain. Pola P dan Ab yang "redundan" ini serupa: P memberi angka ringkas untuk pembacaan cepat, Ab memberi detail untuk pembacaan menyeluruh.

**Kesimpulan yang dipakai di materi ini:** digit ke-3 P **selalu mencerminkan total keseluruhan riwayat abortus** (dijumlah dari tiga digit Ab), dan bagian Ab merinci jenisnya. Ini pendekatan yang lebih defensible secara logika sistem TPAL dan lebih aman secara klinis, walau bentuk format gabungan G*P\_\*\*\_Ab*\*\* ini sendiri bukan berasal dari satu textbook tunggal yang baku secara internasional — jadi tetap ada kemungkinan variasi antar institusi.

> [!note] Catatan penting soal variasi konvensi
> Meskipun penjelasan di atas adalah pendekatan yang paling logis dan konsisten dengan definisi asli TPAL, **format gabungan `G_P____Ab___` ini sendiri adalah adaptasi lokal** (tidak ditemukan sebagai satu sistem baku tunggal di textbook internasional). Karena itu, sangat mungkin ada rumah sakit atau pembimbing yang mengajarkan versi berbeda (termasuk versi yang membiarkan digit ke-3 P tetap 0). **Selalu konfirmasikan ke pembimbing/DPJP** format resmi yang dipakai di institusi kamu, dan gunakan penjelasan di atas sebagai dasar pemahaman logika sistemnya — bukan sebagai satu-satunya jawaban yang mutlak benar di semua tempat.

### Poin penting lain terkait P

- Kehamilan kembar (gemelli) yang lahir hidup **tetap dihitung sebagai 1 persalinan** (1 digit T atau P), tapi anaknya dihitung 2 di digit L.
- Kehamilan saat ini (yang belum lahir) **tidak** dimasukkan ke dalam digit manapun di P — P hanya menghitung kehamilan yang **sudah selesai/lahir**.

---

## 4. Abortus (Ab) — 3 Digit

Bagian **Ab** ditulis terpisah di akhir, merinci **jenis-jenis abortus** yang pernah dialami pasien. Contoh format:

```
Ab010
```

Susunan 3 digit ini umumnya membagi abortus berdasarkan **penyebab/cara terjadinya**, bukan berdasarkan usia kehamilan lagi (karena usia <20 minggu sudah pasti abortus, itu sudah tercermin di digit ke-3 P). Pembagian yang lazim dipakai:

| Digit ke- | Kategori               | Definisi                                                                                                                                                  |
| --------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1         | **Abortus spontan**    | Keguguran yang terjadi dengan sendirinya, tanpa tindakan/intervensi (misalnya abortus imminens yang berlanjut jadi abortus komplit, missed abortion, dsb) |
| 2         | **Abortus provokatus** | Keguguran akibat tindakan yang disengaja — bisa **provokatus medisinalis** (atas indikasi medis) atau **provokatus kriminalis** (di luar indikasi medis)  |
| 3         | **Kehamilan ektopik**  | Kehamilan di luar rahim (misalnya di tuba fallopi) yang berakhir sebelum viable, termasuk KET (Kehamilan Ektopik Terganggu)                               |

### Hubungan matematis antara Ab dan digit ke-3 P

Karena Ab adalah **rincian**, bukan pencatatan baru, maka berlaku aturan:

```
digit ke-3 P = jumlah seluruh digit pada Ab
```

Contoh: kalau Ab = 211 (2 spontan, 1 provokatus, 1 ektopik), maka total = 2+1+1 = 4, sehingga digit ke-3 P **harus** bernilai 4. Kalau angka ini tidak cocok, berarti ada kesalahan pencatatan di salah satu bagian — entah digit ke-3 P kurang, atau ada jenis abortus yang lupa dimasukkan ke Ab.

Aturan ini bisa dipakai sebagai **alat verifikasi**: setiap kali menulis diagnosis dengan format G*P\_\*\*\_Ab*\*\*, selalu cek ulang apakah total tiga digit Ab sudah sama dengan digit ke-3 P. Kalau berbeda, salah satu bagian pasti keliru.

### Contoh interpretasi **Ab010**

- Digit 1 = **0** → tidak pernah abortus spontan
- Digit 2 = **1** → pernah **1 kali abortus provokatus**
- Digit 3 = **0** → tidak pernah kehamilan ektopik

Jadi **Ab010** berarti: pasien memiliki riwayat **1 kali abortus provokatus**, dan tidak ada riwayat abortus spontan maupun kehamilan ektopik. Karena totalnya 1, maka digit ke-3 P pada diagnosis pasien ini **harus bernilai 1** juga.

### Kemungkinan lain untuk digit tengah (posisi ke-2)

Karena posisi tengah ini yang paling sering bervariasi antar sumber, berikut kemungkinan makna lain yang bisa ditemui tergantung konvensi institusi:

1. **Abortus provokatus** (medisinalis + kriminalis digabung) — konvensi paling umum
2. **Abortus provokatus medisinalis** saja (jika ada digit ke-4 terpisah untuk kriminalis di beberapa format yang lebih rinci)
3. **Missed abortion** sebagai kategori sendiri (di sebagian format lain, missed abortion dipisah dari abortus spontan biasa)

> Karena variasi ini, **selalu konfirmasikan ke DPJP/pembimbing** urutan digit yang dipakai di tempat rotasi, supaya penulisan diagnosis konsisten dengan yang diajarkan.

---

## 5. Contoh Kasus Lengkap

### Kasus 1

Ny. A, kehamilan ke-4 (termasuk yang sekarang). Riwayat: 2x melahirkan cukup bulan dengan anak hidup, 1x keguguran spontan usia 8 minggu.

> [!example] Diagnosis: G4P2011Ab100
>
> - G4 → kehamilan keempat (2 persalinan sebelumnya + 1 abortus sebelumnya + kehamilan saat ini)
> - P2011 → 2 term, 0 preterm, **1 abortus** (mencerminkan riwayat abortus spontannya), 1 anak hidup
> - Ab100 → rincian jenis abortus: 1x spontan, 0x provokatus, 0x ektopik

> [!success] Verifikasi
> Total digit Ab = 1+0+0 = 1, dan digit ke-3 P = 1. Cocok — konsisten.

### Kasus 2

Ny. B, kehamilan ke-3 (termasuk sekarang). Riwayat: 1x melahirkan preterm anak hidup, 1x abortus provokatus medisinalis (indikasi medis karena kelainan janin berat).

> [!example] Diagnosis: G3P0111Ab010
>
> - G3 → kehamilan ketiga
> - P0111 → 0 term, 1 preterm, 1 abortus (mencerminkan riwayat abortus provokatusnya), 1 anak hidup
> - Ab010 → rincian jenis abortus: 0x spontan, 1x provokatus, 0x ektopik

> [!success] Verifikasi
> Total digit Ab = 0+1+0 = 1, dan digit ke-3 P = 1. Cocok — konsisten.

### Kasus 3

Ny. C, kehamilan ke-5 (termasuk sekarang). Riwayat: 2x melahirkan cukup bulan hidup, 1x kehamilan ektopik terganggu (tuba pecah), 1x abortus spontan.

> [!example] Diagnosis: G5P2021Ab101
>
> - G5 → kehamilan kelima
> - P2021 → 2 term, 0 preterm, **2 abortus** (mencerminkan total 2 kejadian: 1x spontan + 1x ektopik), 1 anak hidup
> - Ab101 → rincian jenis abortus: 1x spontan, 0x provokatus, 1x kehamilan ektopik

> [!success] Verifikasi
> Total digit Ab = 1+0+1 = 2, dan digit ke-3 P = 2. Cocok — konsisten.

> [!question] Kenapa digit ke-3 P berisi 2, bukan 1?
> Karena ada **dua kejadian terpisah** yang sama-sama masuk kategori "kehamilan berakhir <20 minggu": satu abortus spontan dan satu kehamilan ektopik. Meskipun jenisnya berbeda, keduanya tetap dihitung dalam definisi digit ke-3 P karena definisinya adalah jumlah kejadian, bukan jumlah jenis.

### Kasus 4 — Riwayat abortus berulang (untuk melihat pola digit ke-3 P lebih jelas)

Ny. D, kehamilan ke-6 (termasuk sekarang). Riwayat: 1x melahirkan cukup bulan anak hidup, 2x abortus spontan (usia 6 minggu dan 10 minggu), 2x abortus provokatus medisinalis, 1x kehamilan ektopik terganggu.

> [!example] Diagnosis: G6P1051Ab221
>
> - G6 → kehamilan keenam
> - P1051 → 1 term, 0 preterm, **5 abortus** (total dari semua jenis: 2 spontan + 2 provokatus + 1 ektopik), 1 anak hidup
> - Ab221 → rincian jenis abortus: 2x spontan, 2x provokatus, 1x kehamilan ektopik (total 5 kejadian abortus)

> [!success] Verifikasi
> Total digit Ab = 2+2+1 = 5, dan digit ke-3 P = 5. Cocok — konsisten.

> [!question] Kenapa digit ke-3 P berisi 5, bukan 0?
> Ini kasus yang paling jelas menunjukkan pentingnya konsistensi. Kalau digit ke-3 P dipaksa 0 di sini, seseorang yang membaca cepat "G6P1051" tanpa sempat membaca Ab221 akan mengira pasien ini **tidak pernah** mengalami abortus sama sekali — padahal riwayatnya berat: 5 kali kehilangan kehamilan, termasuk kehamilan ektopik yang mengancam nyawa. Riwayat abortus berulang seperti ini juga punya arti klinis tersendiri (curiga _recurrent pregnancy loss_, perlu evaluasi lebih lanjut), sehingga wajib terlihat jelas di ringkasan P, bukan hanya tersembunyi di bagian Ab.

> [!tip] Catatan penulisan
> Karena digit ke-3 P bisa lebih dari 1 digit angka pada kasus dengan riwayat abortus banyak (seperti nilai 5 di atas), penulisan P tetap mengikuti apa adanya jumlahnya (P1051), bukan dipotong jadi 1 digit saja.

### Kasus 5 — Latihan menulis dari nol, langkah demi langkah

Ny. E datang untuk ANC. Ini kehamilan ke-2. Riwayat kehamilan pertama: pada usia kehamilan 9 minggu mengalami perdarahan, dilakukan kuretase, didiagnosis abortus inkomplit (abortus spontan). Tidak ada riwayat persalinan sama sekali.

**Langkah 1 — Tentukan G:**
Total kehamilan = 1 (dulu) + 1 (sekarang) = **G2**

**Langkah 2 — Tentukan digit 1 dan 2 pada P (Term dan Preterm):**
Belum pernah melahirkan sama sekali (baik cukup bulan maupun kurang bulan) → digit 1 = **0**, digit 2 = **0**

**Langkah 3 — Tentukan digit 3 pada P (Abortus):**
Ada 1 kejadian kehamilan berakhir <20 minggu (abortus spontan usia 9 minggu) → digit 3 = **1**

**Langkah 4 — Tentukan digit 4 pada P (Living):**
Belum ada anak yang lahir hidup → digit 4 = **0**

Sehingga P = **0010**

**Langkah 5 — Tentukan Ab (rincian jenis abortus):**
Jenisnya adalah abortus spontan (bukan disengaja/provokatus, bukan ektopik) → Ab = **100**

**Langkah 6 — Verifikasi:**
Total digit Ab (1+0+0=1) harus sama dengan digit ke-3 P (1). ✓ Cocok.

> [!example] Diagnosis akhir
> **G2P0010Ab100**

Ini adalah pola paling dasar yang sebaiknya dikuasai duluan sebelum masuk ke kasus yang lebih kompleks (kombinasi banyak jenis abortus seperti Kasus 4).

---

## 6. Kesalahan Umum yang Perlu Dihindari

1. **Lupa memasukkan kehamilan saat ini** ke dalam hitungan G
2. **Memasukkan kehamilan saat ini** ke dalam hitungan P (padahal P hanya untuk kehamilan yang sudah selesai/lahir)
3. **Salah urutan digit** dalam P (tertukar antara Term dan Preterm)
4. **Membiarkan digit ke-3 P bernilai 0 padahal ada riwayat abortus** — ini melanggar definisi baku sistem TPAL dan berisiko menyembunyikan informasi klinis penting dari pembaca yang hanya sempat membaca P tanpa membaca Ab
5. **Tidak melakukan verifikasi total** — setiap selesai menulis diagnosis, selalu jumlahkan tiga digit Ab dan cocokkan dengan digit ke-3 P; kalau tidak sama, salah satu bagian pasti keliru
6. **Menganggap kehamilan kembar sebagai 2 persalinan** — seharusnya tetap 1 di digit P, hanya anaknya yang dihitung 2 di digit L

---

## 7. Ringkasan / Cheat Sheet

```
G _ P _ _ _ _ Ab _ _ _
    │ │ │ │ │    │ │ └─ Kehamilan ektopik
    │ │ │ │ │    │ └─── Abortus provokatus
    │ │ │ │ │    └───── Abortus spontan
    │ │ │ │ └────────── L: Jumlah anak hidup
    │ │ │ └──────────── A: Jumlah abortus (dalam TPAL) — HARUS = jumlah 3 digit Ab
    │ │ └────────────── P: Jumlah persalinan preterm
    │ └──────────────── T: Jumlah persalinan aterm/cukup bulan
    └────────────────── Jumlah seluruh kehamilan (termasuk saat ini)
```

**Rumus verifikasi cepat:**

```
digit ke-3 pada P  =  digit1 Ab + digit2 Ab + digit3 Ab
      (total)           (spontan)  (provokatus)  (ektopik)
```

> [!important] Poin kunci
> Digit ke-3 P (kolom Abortus dalam TPAL) **selalu diisi sesuai definisi bakunya** — yaitu jumlah total seluruh kejadian kehamilan yang berakhir <20 minggu, apapun jenisnya. Bagian Ab di akhir diagnosis bukan pengganti angka ini, melainkan **rincian** dari angka tersebut. Keduanya harus selalu konsisten secara matematis (total Ab = digit ke-3 P). Pendekatan ini dipilih karena paling sesuai dengan definisi asli sistem TPAL dan paling aman secara klinis, karena tidak menyembunyikan riwayat abortus dari pembaca yang hanya membaca ringkasan P saja.

> [!warning] Tetap konfirmasi ke pembimbing
> Karena format gabungan `G_P____Ab___` ini adalah adaptasi lokal (bukan satu sistem baku tunggal internasional), **tetap disarankan untuk mengonfirmasi ulang** ke dr. Benny Marcel Pandango, Sp.OG atau format resmi yang berlaku di RSUD Karsa Husada Batu, agar penulisan status pasien konsisten dengan yang diajarkan dan dipakai di tempat rotasi.

---

_Catatan: file ini kompatibel dengan [Obsidian](https://obsidian.md) (mendukung callout, wikilink internal, dan frontmatter YAML) serta [Quartz](https://quartz.jzhao.xyz) untuk publikasi sebagai digital garden._
