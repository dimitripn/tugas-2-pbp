# README

### [Link Heroku](https://tutu-2.herokuapp.com/katalog/)

## Bagan _Request Client_

![Bagan]

Penjelasan:
1. _Request client_ diproses dengan mencari informasi yang diinginkan oleh client pada file `urls.py`
2. Setelah ditemukan, `urls.py` akan memanggil fungsi view yang terletak pada `views.py`
3. `views.py` akan mengambil data-data yang akan ditampilkan melalui file `models.py`
4. Kemudian diakhiri dengan mengembalikan response yang kemudian akan dirender dan ditampilkan kepada _client_.

## _Virtual Environment_
### Alasan menggunakan virtual environment
_Virtual environment_ merupakan sebuah tools yang berfungsi untuk membuat lingkungan yang terisolasi untuk sebuah _project_. Dengan menggunakan virtual _environment_, maka _project_ yang sedang dikerjakan akan terisolasi dari project lain, artinya _packages_ serta _dependencies_ yang digunakan tidak akan tercampur antar-_project_. Dengan begitu, perubahan yang dilakukan pada satu _project_ tidak akan mempengaruhi proyek lain.

### Apakah tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virutal environment_?
Ya, tetap bisa dilakukan, namun sangat tidak dianjurkan. Hal tersebut karena aplikasi web merupakan suatu hal yang kemungkinan akan digunakan oleh banyak pengguna, sehingga dapat menimbulkan berbagai masalah dan juga akan lebih rumit untuk me-_maintain_-nya.

## Implementasi Pengerjaan Tugas 2
### 1. Membuat sebuah fungsi pada `views.py` yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
```
...
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_katalog,
        'name': 'Dimitri Prima Nugraha',
        'id': '2106750396',
    }
    return render(request, "katalog.html", context)
```
Pada file ini saya membuat fungsi bernama `show_katalog` yang menerima parameter berupa _request_ dan mengembalikan fungsi render. Fungsi render tersebut berfungsi untuk menampilkan html berisi data yang telah diambil pada fungsi dan disimpan di variabel `data_katalog`

### 2. Membuat sebuah routing untuk memetakan fungsi yang telah dibuat pada `views.py`
```
...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('katalog/', include('katalog.urls')),
]
```
```
...
urlpatterns = [
    path('', show_katalog, name='show_katalog')
]
```
Pada file `urls.py` yang terletak di dalam folder `project_django` ditambahkan sebuah elemen pada variabel `urlpatterns` agar program dapat mengambil data yang sesuai dengan _request client_ (kode pertama). KKemudian pada file `urls.py` yang terletak di folder `katalog` ditambahkan sebuah elemen pada variabel urlpatterns juga yang berfungsi untuk memanggil fungsi show_katalog untuk menampilkan data yang telah dikumpulkan dan disimpan pada variabel di dalam fungsi tersebut (kode kedua).

### 3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
```
...
{% for katalog in list_katalog %}
        <tr>
            <th>{{katalog.item_name}}</th>
            <th>{{katalog.item_price}}</th>
            <th>{{katalog.item_stock}}</th>
            <th>{{katalog.rating}}</th>
            <th>{{katalog.description}}</th>
            <th>{{katalog.item_url}}</th>
        </tr>
...
```

### 4. Melakukan `deployment` ke Heroku terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman melalui Internet. 

Pada tahap ini dibuat aplikasi baru pada heroku. Kemudian dihubungkan dengan github melalui secrets yang ditambahkan `HEROKU_APP_NAME` dan `HEROKU_API_KEY`.
