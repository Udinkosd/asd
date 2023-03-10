# Search Algoritma Pada Struktur Data
Abdul Rahman (2209116045)

### Dokumentasi Algoritma Fibonacci Search
Fibonacci Search adalah suatu algoritma yang mana menerapkan prinsip bilangan Fibonacci. Dalam ilmu komputer, algoritma ini menggunakan konsep divide  dan conquer. Fibonacci search hanya memeriksa lokasi yang yang memiliki tingkat penyebaran data yang rendah. Fibbonaci search dalam prakteknya memiliki keuntungan yakni cepatnya mengakses data pada suatu storage.

#### Def fibonacciSearch
![image](https://user-images.githubusercontent.com/126738691/224379761-b1fdefd0-9a24-472c-bf99-0e5f0635624e.png)

Berdasarkan gambar diatas, variable fib2 = 0 adalah fibonacci(n-2) atau dalam perhitungan fibonacci adalah 0, lalu fib1 = 1 adalah fibonacci(n-1) dan fib = fib2 + fib1 adalah fibonacci(n) dalam hal ini fib2 + fib1 = 0, 1, 1, 2

![image](https://user-images.githubusercontent.com/126738691/224381622-c4558795-0d46-49ae-b23d-6e0e398a53cc.png)

Variabel while digunakan untuk mencari nilai dari fibonacci(n) yang terbesar, lebih kecil atau sama dengan n

![image](https://user-images.githubusercontent.com/126738691/224381763-ceb56265-f9a2-44a5-89f1-3df3d3a93436.png)

Diatas, jika elemen merupakan list [Wahyu, Wibi], lakukan pencarian di dalamnya...Sehingga python membaca Wahyu = 0 dan Wibi = 1

![image](https://user-images.githubusercontent.com/126738691/224382017-65193150-c0f1-4a70-b387-5a981d44f14a.png)

Kemudian, pada gambar diatas, jika x lebih besar daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kanan dan jika x lebih kecil daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kiri

![image](https://user-images.githubusercontent.com/126738691/224382320-8f8af730-f3c1-4f49-8a3b-bd233d6420bd.png)

Lalu jika x ditemukan, kembalikan indeks i namun apabila elemen tidak ditemukan, kembalikan -1, dan jika elemen tidak ditemukan, kembalikan -1

![image](https://user-images.githubusercontent.com/126738691/224387002-ff0202e2-f079-416d-b66b-059f02e66247.png)

Saat user melakukan input pada variabel cari, maka akan melakukan pencarian dimana jika metode sama dengan -1 atau false, atau flag bahwa itu tidak ada, maka program akan print out "Nama tidak ada"
