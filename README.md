# Sudoku Solver

## Latar Belakang

Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.

## Prerequisite

1. [Python 3](https://www.python.org/downloads/)
2. [pip](https://pip.pypa.io/en/stable/installing/)
3. [PIL](https://pypi.org/project/Pillow/)
4. [pytesseract](https://pypi.org/project/pytesseract/)

## How To Run

In `src/` folder, run:
<!---->
`python3 main.py [path image or text]`
<!---->
Alternative (UNIX only):

1. Make sure python3 installed on `/usr/local/bin/python3`, unless change `main.py` to current python3 folder installed
2. `chmod +x main.py`
3. `./main.py [path image or text]`

Example:
<!---->
`./main.py ../test/tc1.txt`
<!---->

## Strategi

Algoritma yang digunakan adalah algoritma backtracking. Algoritma ini  memanfaatkan metode rekursif. Cara kerjanya ialah, salah satu cell di assign untuk satu nomor (1-9), kemudian divalidasi apakah satu kolom, satu baris dan satu box tidak ada yang serupa dengan nomor tersebut. Jika tidak ada maka lanjut ke cell selanjutnya dengan cara yang sama secara rekursif. Jika ada, maka ubah menjadi tetap '0' atau tanda blank cell lainnya dan lanjutkan dengan nomor berikutnya.

## External Library

### pytesseract

Library merupakan library yang dapat menangkap text yang berada pada sebuah gambar. Ini adalah library yang pertama kali ditemukan saat melakukan search di dalam mesin pencarian sekaligus sangat banyak contoh penggunaannya.
Kelebihan dari library ini tentu ia dapat mengambil informasi tertentu pada text yang berada pada suatu gambar. Kekurangannya ialah terkadang akan memakan waktu yang lama jika extract gambar terlalu banyak atau gambar tidak sesuai dengan ekspetasi.

### PIL

PIL merupakan singkatan dari Python Imaging Library. Library ini dapat mengolah gambar (Image) sehingga lebih bisa kita customize seperti cropping, merging, splitting, dan hal lainnya yang berkaitan dengan Image. Library ini merupakan library yang pertama kali terpikir mengingat pernah menggunakannya untuk melakukan Image Proccessing saat extracting feature photo similarity.

## Reference

1. [Geeksforgeeks](https://www.geeksforgeeks.org/sudoku-backtracking-7/)
2. [MicroPyramid](https://medium.com/@MicroPyramid/extract-text-with-ocr-for-all-image-types-in-python-using-pytesseract-ec3c53e5fc3a)
3. [Jaafarbenabderrazak](https://medium.com/@jaafarbenabderrazak.info/ocr-with-tesseract-opencv-and-python-d2c4ec097866)
