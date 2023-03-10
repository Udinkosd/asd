# Search Algoritma Pada Struktur Data
Abdul Rahman (2209116045)

#### Dokumentasi Algoritma Fibonacci Search
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


#### Dokumentasi Binary Search

## Def binary_search
Dalam binary search, metode yang digunakan adalah slice, dimana program akan mengambil nilai tengah, setelah membaginya, yaitu index awal / index 0 dan index akhir / index, untuk mengetahui index akhir, maka nanti kita menggunakan len
![image](https://user-images.githubusercontent.com/126738691/224394875-31b6b282-7765-43e7-9073-b440b66a65c0.png)

Jika index awal lebih besar dari index akhir maka akan return -1 atau tidak ada / error

![image](https://user-images.githubusercontent.com/126738691/224395782-93d38a25-9b65-4e69-8714-03fdf0760e03.png)

Selanjutnya adalah isinstance() yaitu sebuah fungsi bawaan Python yang digunakan untuk memeriksa apakah sebuah objek merupakan sebuah instance atau turunan dari sebuah kelas tertentu. Fungsi ini mengembalikan nilai True jika objek yang diberikan adalah sebuah instance atau turunan dari kelas yang diberikan, dan mengembalikan nilai False jika bukan.

Pada kode yang diberikan, isinstance(arr[i], list) digunakan untuk memeriksa apakah elemen arr[i] adalah sebuah list atau bukan. Jika iya, maka kode akan melakukan pencarian nilai x pada list tersebut dengan menggunakan algoritma Fibonacci Search.

![image](https://user-images.githubusercontent.com/126738691/224396648-34a858e2-3cbe-4e48-96a6-059280700e96.png)

Jika kondisi pada baris 2 terpenuhi (index awal lebih besar dari index akhir), maka akan dikembalikan nilai None karena elemen yang dicari tidak ditemukan dalam array. Kemudian jika kondisi pada baris 4 terpenuhi (indeks elemen tengah sama dengan elemen yang dicari), maka indeks elemen tersebut akan dikembalikan sebagai output.

![image](https://user-images.githubusercontent.com/126738691/224397900-82a5e4de-1ae4-40ba-9be4-2b7f835cd1ae.png)

("Nama {cari} terdapat pada indeks:") adalah string yang berisi pesan untuk menampilkan bahwa elemen yang dicari ditemukan pada indeks tertentu. ({metode}) adalah variabel yang berisi nilai dari indeks elemen yang dicari. Kemudian ("dikolom {kolom}") adalah string yang berisi pesan untuk menampilkan pada kolom mana elemen tersebut ditemukan.








