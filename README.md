# 🦉 Owo Language — Teknik Kompilasi

**Owo Language** adalah bahasa pemrograman edukatif yang dikembangkan sebagai proyek akhir untuk mata kuliah **Teknik Kompilasi**. Bahasa ini menggunakan sintaks berbasis **bahasa Jawa sehari-hari** 
---

## 🎯 Tujuan Proyek
- Mempelajari proses pembuatan bahasa pemrograman dari awal
- Menerapkan materi: lexer, parser, interpreter, semantic analysis, dan error handling
- Menciptakan bahasa yang dekat dengan kultur lokal (bahasa Jawa)
- Memudahkan pemula dalam memahami konsep pemrograman

---

## 🧱 Komponen Bahasa

### 🔤 Token (Kata Kunci)

| Python | Owo Language | Arti dalam Bahasa Jawa |
|--------|--------------|------------------------|
| `print`| `dudohno`    | tampilkan/tunjukkan    |
| `if`   | `yen`        | jika                   |
| `else` | `liyane`     | selainnya              |
| `for`  | `kanggo`     | untuk                  |
| `fun`  | `gunane`     | fungsi                 |
| `then` | `dadine`     | maka                   |
| `to`   | `moro`       | ke                     |

Token lainnya:
- `STRING`, `EQEQ (==)`, `ARROW (=>)`, `NAME (variabel)`, dsb.

---

## 🧠 Penjelasan Komponen

### 1. Lexer
Lexer bertugas memecah input (kode program) menjadi token-token yang dikenali, seperti `yen`, `dudohno`, dll.

### 2. Parser
Parser membaca token dan menyusunnya menjadi **pohon sintaks** agar bisa dianalisis dan dieksekusi.

### 3. Interpreter
Interpreter menjalankan logika program berdasarkan hasil parsing — bekerja baris demi baris, seperti bahasa interpretatif lainnya.

### 4. Analisis Semantik
Melakukan pengecekan:
- Tipe data
- Nama variabel
- Struktur kode yang valid

### 5. Penanganan Kesalahan
Jika terjadi error (contoh: variabel tak dikenal), interpreter akan memberikan pesan error tanpa menghentikan seluruh sistem.

---

## 📦 3.File-File Proyek

Kamu bisa membuat file secara manual sesuai struktur di bawah ini, atau langsung clone dari GitHub:

```text
Owo_Language/
├── LexerOwo.py           # Komponen lexer: mengubah kode sumber menjadi token
├── ParserOwo.py          # Komponen parser: membentuk pohon sintaks dari token
├── InterpreterOwo.py     # Komponen interpreter: mengeksekusi logika kode
├── Main.py               # Entry point: menjalankan perintah Owo langsung
├── Index.py              # Menjalankan file eksternal .owo via terminal
├── contoh_program.owo    # Contoh kode dalam bahasa Owo
└── README.md             # Dokumentasi proyek
```

---

## ▶️ 4. Menjalankan Program

### 🔹 Jalankan langsung dengan `Main.py`

```bash
python Main.py
```

Kamu bisa langsung mengetikkan perintah Owo di terminal, contoh:

```owo
dudohno "halo iki Owo Language!"
```

---

### 🔹 Jalankan file `.owo` dengan `Index.py`

1. Buat file eksternal dengan ekstensi `.owo`, misalnya:

```text
contoh_program.owo
```

2. Isi file tersebut dengan kode Owo:

```owo
gunane salam()
  dudohno "halo, iki program Owo!"
```

3. Jalankan melalui terminal:

```bash
python Index.py contoh_program.owo
```
