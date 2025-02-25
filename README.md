Penjelasan Kode 1
Fungsi Utama:

Kode ini digunakan untuk membaca data dari beberapa sensor (PIR, LDR, DHT22) dan mengirimkan data tersebut ke platform Ubidots.
Detail Fungsi:

Inisialisasi Pin:

Mengatur pin untuk sensor PIR, LED, LDR, dan DHT.
Koneksi WiFi:

Menghubungkan perangkat ke jaringan WiFi yang ditentukan sehingga bisa mengakses internet.
Pengukuran Sensor:

Membaca nilai dari sensor PIR untuk mendeteksi gerakan.
Membaca nilai dari LDR untuk mengukur intensitas cahaya.
Membaca data suhu dan kelembapan dari sensor DHT22.
Kontrol LED:

Menghidupkan atau mematikan LED berdasarkan status deteksi gerakan.
Kirim Data ke Ubidots:

Mengirim data ke server Ubidots setiap 5 detik setelah pengukuran.

Penjelasan Kode 2
Fungsi Utama:

Kode ini berfungsi sebagai API menggunakan Flask untuk mengambil dan menampilkan data sensor dari MongoDB.
Detail Fungsi:

Inisialisasi Flask:

Membuat aplikasi Flask untuk membangun API.
Koneksi MongoDB:

Menghubungkan ke basis data MongoDB dan menentukan koleksi untuk menyimpan data sensor.
Route API:

Route utama (/) memberikan pesan status.
Route /api/sensor_data untuk mengambil data sensor terbaru dari MongoDB dan mengembalikannya dalam format JSON.

Penjelasan Kode 3
Fungsi Utama:

Kode ini mengambil data dari platform Ubidots dan menyimpannya ke dalam MongoDB.
Detail Fungsi:

Koneksi MongoDB:

Menghubungkan ke MongoDB dan menentukan koleksi untuk menyimpan data yang diambil.
Mengambil Data dari Ubidots:

Mengambil data dari API Ubidots secara berkala (setiap 60 detik).
Simpan Data ke MongoDB:

Menyimpan nilai sensor ke basis data MongoDB termasuk timestamp untuk setiap entri.
