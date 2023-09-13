Nama    : Rakha Davin Bani Alamsyah

NPM     : 2206082650

Kelas   : PBP F

Jurusan : Sistem Informasi-Fasilkom UI

Link : 
https://github.com/rakhadavin/Tugas2-ManageVent/tree/mainBranch (Github)
https://managevent01.adaptable.app/main (Addaptable)




Selamat Datang di Repository saya. Repository ini berisi file-file untuk Tugas 2 PBP, yaitu penerapan Model-View-Template (MVT). Hasil Deployment website ini, akan saya namakan ManageVent. Makna dari ManageVent sendiri adalah sesuai panduan dan arahan tugas 2, kami diminta membuat penerapan MVT untuk melakukan pengelolaan inventris. Dengan demikian ManageVent memiliki arti web yang berfungsi untuk anda dapat melakukan management inventoris dan segala keperluan Anda lainnya.

Sekian dan Terimakasih



# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

step 1 (Inisiasi Ide):
Dengan Memanfaatkan ChatGpt saya mendapatkan insgiht mengenai conoh penerapan pengelolaan inventori. Salah satunya adalah di Apotek. salah satu permasalahan apoteker yaitu, mereka harus menghapal jumlah, harga, jenis, nama, kegunaan dari masing-masing obat yang ada di apotek, sekalipun ada pencatatan itu hanya di buku saja, rentan hilang dan tidak ada "Backup". Dengan demikian saya memanfaatkan Tugas 2 ini untuk mebantu apoteker, dengan membuat form yang nantinya akan ditampilkan dalam bentuk tabel-tabel data mengenai metadata masing-masing obat yang ada di apotek

step 2 (Membuat Project dan App 'main'):
Saya memberi nama ManageVent untuk nama project saya, dan terdapat app bernama 'main', dimana dalam app tersebut ada class Item beserta atribute sesuai dengan ketentuan yang ada di tugas 2.

step 3 (Routing):
Kemudian saya melakukan konfigurasi url (routing) agar lebih mudah dicari menggunakan search engine. Konfigurasi ini saya lakukan berserta dengan pengaturan views yang berkesinambungan dengan url dan juga template yang berisi file html dan css, untuk ditampilkan dalam web.

step 4 (Pengaturan Models):
Saya membuat form untuk diisi dan disimpan dalam database, yang nantinya bisa ditampilkan sebagai metadata dari masing-masing obat.

disini saya menggunakan saya hanya menggunakan modul dari django.db.models, untuk melakukan pemodelan dalam database. Validasi dan batasan input dalam form tersebut juga saya lakukan, sebagai best practice.  

kemudian selain atribute yang diwajibkan saya juga membuat artribute yang menurut saya dibutuhkan untuk kasus permaslahan apotek ini dengan spesifikasi  sebagai berikut :

    nama_obat --> CharField #nama obat
    amount --> IntegerField() #stok obat tersedia
    harga --> PositiveIntegerField() #harga per apa

    satuan_harga --> CharField, berupa dropdown dengan  menu yang terdapat dibawah ini :
                        pilihan_jenis_satuan_harga = {
                            ("s","1 Strip"),
                            ("b","Botol/Sirup"),
                            ("k","Kotak/Kemasan"),
                            ("c","1 Butir Kapsul"),
                        }

    jenis_obat --> CharField, dropdown dengan daftar sebagai berikut :
                        pilihan_jenis_obat ={
                            ("h","Herbal/Suplemen"),
                            ("a", "Alergi"),
                            ("g","Generic"),
                            ('r', "Racik"),
                            ("An","Khusus Anak (0-17 tahun)"),
                            ("pd","Penyakit dalam"),
                            ("ot","Penyakit Orang Tua"),
                            
                        }
    
    


    deskripsi --> TextField(), akan berisi kegunaan obat, dosis, ukuran, komposisi, dan sebagainya.
    expired --> CharField( max_length=8,default=dateNow.strftime("%d-%m-%Y")) --> tanggal expired obat dengan format (dd-mm-yyyy)
    



step 5 (Membuat fungsi pada views.py):
fungsi yang saya buat pada views.py yang ada di app main bernama home, yang akan mengembalikan file html yang saya buat di folder templates, untuk ditampilkan pada laman web.

isi file home.html --> menampilkan, nama Program-nama app, nama mahasiswa, kelas. 



# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


![alt text](/Images/BaganDjango.png)

# 1                         2                         3                  4                5
[Request Client]   -->   [urls.py]           -->      [views.py]                 -->   [models.py]
contoh (..../main)      ("home/", "views.home")      (def home(){ 
                                                return....  home.html, context}) 

                                                        |
                                                        v   
                                                [HTML Templates] (get home.html)
                                                        |
                                                        v
                                                    [Response]
                                                        |
                                                        v
                                                [Client Browser] (menampilkan file homt.html)

PENJELASAN :
1. client request halaman web, dengan url pattern tertentu, misal (ManageVent/main). (routing)
2. url menerima request, dan mencari jenis pattern url yang sesuai(ManageVent/main) dan ternyata pattern tersebut berkaitan dengan fungsi yang ada di views, misal url nya : ("home/", "views.home")  maka fungsi yang akan dicari : "views.home" --> mencari fungsi 'home' di dalam file views.py
3. kemudian urls.py memberi respon berupa mengirimkan request / sinyal ke views.py dan mencari function 'home'
4. Pada views.py terdapat function 'home' yang mengeembalikan file 'home.html, kembali mengirim permintaan untuk mencari file bernama 'home.html' pada folder templates untuk dirender ke tampilan web
5. models.py akan berfungsi sebagai blueprint untuk struktur data atau model-data yang akan digunakan oleh aplikasi kita, dilengkapi denga pendefinisian model, dan skema database/ Bahasa mudahnya ialah berguna untuk melakukan pemodelan data yang berisi attribute tertentu, yang juga dapat ditampilkan ke halaman web dengan mengintegrasikannya melalui file html.


# 3. Jelaskan mengapa kita menggunakan virtual environment? 
Virtual Environment dibuat agar mempermudah developer dalam melakukan developing web berbasis python. Hal tersebut dapat berupa :

a. Isolasi Proyek : hal ini diperlukan agar proyek tidak bentrok dengan proyek lain dan tetap memiliki path/jalur nya sendiri

b. Kemudahan Tracing : tracing yang dimaksud ialah mulai dari debugging, tracing error, mencari solusi error, bahkan kita dengan mudah dapat mencari file model,url, views, dll untuk masing-masing app. dapat dibayangkan jika terdapat banyak app dan semua file untuk masing-masing app yang berbeda  disatukan hanya berdasarkan jenis file saja ( views.py, urls.py, models.py) tanpa ada foldering yang rapi, sungguh sangat berantakan, sulit untuk dimengerti terlebih jika kita bekerja dengan team, hal ini sungguh memberatkan team, bahkan hal yang tidak diinginkan seperti error yang tidak terduga dapat terjadi saat mengubah satu bagian dari file tersebut padahal line yang terdapaat error tersebut tidak pernah diubah. Hal ini dikarenakan kesinmbungan diantaranya.

c. Keamanan : virtusl environment dapat membantu mengurangi resiko yang mungkin timbul akibat menginstall package yang tidak terverifikasi. Sehingga jika1 file terkena virus atau semacamnya, file file yang terpisah dari file terindikasi virus tersebut dapat diselamatkan dan diamankan lebih awal, dan langkah preventif menjadi efektif sebelum langkah recovery dijalankan.

d. Efisiensi dan Produktifitas : dengan melakukan foldering, kita dapat bekerjasama dengan team di wakt yang bersamaan tanpa mengganggu kinerja progrrammer lain di file lain. Dengan demikian proses developing akan semakin cepat selesai.

e.Untuk dapat dijalankan di versi python yang berbeda-beda, dan tidak terjadi masalah dengan versi package yang tidak sesuai, atau versi python nya.


# 4. Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Ya bisa, hanya saja kita akan lebih sulit melakukan tracing file, lebih sulit dalam mengelola dan pengaturan file. Dari segi resiko, ketika 1 file di ubah oleh lebih dari 1 programmer, dan sifatnya tidak update on realtime, maka akan terjadi ambiguitas dan file terancam banyak terdapat error bahkan rusak. Dengan demikian untuk memperbaikinya perklu waktu lagi, dan hal ini menyebabkan ketidakefisiensian kinerja.


# 5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.


DEFINISI SECARA GARIS BESAR :

Models : komponen ini berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Kompnen ini bertugas untuk mendapatkan dan memanipulasi data (CRUD), berkomunikasi dengan urls, controller, database. 

Views : menangani interface atau tampilan untuk user, sebagai implementasi dari controller dan berkomunmikasi dengan model untuk ditampilkan kepada user di halaman web. Views akan berisi file-file html, css, javascript, dan sebagainya sebagai pengatur dalam melakukan interaksi yang dinamis kepada user (penampil komponen UI)

#                                                   MVC: (Popular)
Models : komponen ini berisi tentang logika bisnis dan status data yang ada di dalam aplikasi. Kompnen ini bertugas untuk mendapatkan dan memanipulasi data (CRUD), berkomunikasi dengan urls, controller, database.

Views : menangani interface atau tampilan untuk user, sebagai implementasi dari controller dan berkomunmikasi dengan model untuk ditampilkan kepada user di halaman web. Views akan berisi file-file html, css, javascript, dan sebagainya sebagai pengatur dalam melakukan interaksi yang dinamis kepada user (penampil komponen UI)

Controller : jembatan antara views dan models, dimana berperan sebagai controller yang akan melangsungkan interaksi agar kesinambungan antara views dengan models dapat berjalan dengan baik dan web dapat dinikmati secara interaktif dan dinamis untuk user. Hal ini juga berisi logic-logic interaktif, seperti contoh dalam penggunaan validasi pengguna, yg berkatidan pada kemanan data ang terdapat di dalamnya.

perbedaan signifikan ::
# 1. bussines logic (logika aplikas) terpisah dari model (layer UI, lapisan interface)
# 2. karena file file saling terpisah, maka perubahan yang terjadi dalam file file yang ada secara bersamaan, tidak akan mengganggu satu sama lain
# 3. Kompleksitas yang semakin tinggi, karena kurangnya konektivitas dari komponen yang ada.
# 4. file-file terkait dengan tampilan, disimpan terpisah semua berdasarkan masing-masing halaman web, atau fungsionalitas

#                                                       MVVM (Best): 
Models : secara konsep models tetaplah menjadi komponen logika dalam code kita, perbedannya dalam MVVM ini, ia menerima dan mengirim request ke repository, dan penyimpanan juga

Views : secara konsep sama sama untuk menampilkan komponen UI kepada user, dan Views dalam MVVMN akan menerima response dari Views-Model

View-Models : secara mayoritas apa yang terjadi di UI, dilakukan di Views-Models ini, tanpa mengetahui views mana (app) yang memnaggilnya. Seacar konsep VM ini sama dengan controller, hanya saja cara kerjanya yang sedikit berbeda, yaitu ia melakukan pengaturan value via observable. Obsevable adalah sejenis kelas unutk objek yang dapat diamati lewat interface.

VM dapat berisi logic code untuk melakukan request ke Model, dan Models akan merespon dengan mengembalikan apa yang dibutuhkan oleh VM tadi, yang diambil melaui repository, local data source, remote data source.

perbedaan signifikan ::
# 1. bekerja dengan konsep observable (clas Obsevable) sebagai penghubung dengan model dan views
# 2. views tidak akan pernah berkomunikasi langsung dengan models, Views-Models sebagai jembatannya fasilitasnya
# 3. Observable function harus dibuat pada setiap komponen UI
# 4. Mudah untuk unit test
# 5. Tidak ideal untuk projek kecil

#                                                    MVT: 

Model : Sekumpulan data set yang sengaja disimpan untuk di proses dalam app kita. set -set data tersebut disimpan dala bentuk connected table, tabel yang saling terkoineksi satu sama lain. Kita bisa melakukan CRUD (Create, Read, Update, Delete) data melalui command-command tertentu, yang nantinya data dari tabel tersebut dapat ditampilkan di halaman web, dan ini berkesinambungan dengan Templates.

Views : sebuah fungsi dalam python yang menerima request serta mengirim response ke halamnan web. reponse yang diberikan dapat berupa html file, redirect, error trigger ( 404 error ) 

Templates : mudahnya dapat kita katakan sebagai Dynamic HTML. Karena pada templates ini, kita dapat melakukan assign value dalam file html yang nilainya dapat berubah ubah. File html dapat diubah dan disisipkan logic code seperti looping, conditional, dan sebagainya karena dalam MVT Django ini terdapat Django Template Language  (DTL), yang memiliki syntax nya sendiri untuk melakukan perubahan nilai secara mandiri sesuai dengan data data yang diminta dan tersedia.

Ada dua jenis templat:

{{ variabel }} Digunakan untuk variabel yang berbeda.
{% logics %} Digunakan untuk meletakkan logika, loop dan link.

Pembeda :

# 1. Dapat dilakukan dynamic html
# 2. Dapat digunakan sebagai penerima request sekaligus pemberi Responses
# 3. lebih muda dimodifikasi, file lebih terstruktur, dan mudah dimengerti jalur file nya
# 4. terdapat url's paterns mapping, memudahkan routing

Link Adaptable : 


