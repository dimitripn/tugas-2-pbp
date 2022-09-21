# Tugas 3

### [Link Deployment](https://tutu-2.herokuapp.com/mywatchlist/html/)

## Perbedaan antara JSON, XML, dan HTML
JSON (_JavaScript Object Notation_) ialah format data, sedangkan XML (_Extensible Markup Language_) adalah bahasa _markup_. XML biasanya digunakan untuk mengangkut dan menyimpan data dari satu aplikasi ke aplikasi lainnya melalui internet. Di sisi lain, JSON adalah format pertukaran data ringan yang jauh lebih mudah bagi komputer untuk mengurai data yang sedang dikirim. HTML (_Hypertext Markup Language_) pun sama seperti XML, yaitu merupakan bahasa _markup_. Dalam membuat file HTML, terdapat standar atau format khusus yang harus diikuti. Format tersebut dapat ditemukan dalam standar kode internasional atau ASCII.

## Mengapa Memerlukan _Data Delivery_ dalam Mengimplementasi Sebuah Platform
Kita memerlukan _data delivery_ dalam mengimplementasi sebuah platform karena dalam mengembangkan sebuah platform kita perlu melakukan pengiriman data. Dengan adanya _data delivery_, pengiriman data tersebut akan berjalan dengan lebih mudah karena data dapat dengan mudah di-_transfer_ dari satu pihak ke pihak lainnya.

## Implementasi Tugas 3
1. Membuat folder mywatchlist di dalam clone repository dengan menjalankan command `python manage.py startapp mywatchlist` di terminal.

2. Melakukan routing pada file `urls.py` di dalam folder `project_django` dengan menambahkan path ke dalam `urlpatterns` seperti pada di bawah ini.
```
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```

3. Melakukan routing pada `urls.py` di dalam folder `mywatchlist` juga.

4. Membuat modelnya pada file `models.py` di folder `mywatchlist` sesuai dengan ketentuan tugas yang diminta seperti di bawah ini.
```
class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.DateField()
    review = models.TextField()
```

5. Membuat fungsi untuk menampilkan html, xml, dan json pada file `views.py` di dalam folder `mywatchlist` seperti di bawah ini.
```
def show_watchlist(request):
    watchlist = MyWatchList.objects.all()
    context = {
        'watchlist': watchlist,
        'nama' : 'Dimitri Prima Nugraha',
        'id' : '2106750396'
    }
    return render(request, 'watchlist.html', context)
```
```
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
```
```
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')
```

6. Kemudian, melakukan migrasi model yang telah dibuat dengan menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` di cmd.

## Postman
### HTML
### JSON
### XML