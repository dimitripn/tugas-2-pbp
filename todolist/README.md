# Tugas 4

### [Link Deployment](https://tutu-2.herokuapp.com/todolist/)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
CSRF Token (Cross Site Request Forgery Token) merupakan sebuah random string yang di-generate setiap kali halaman form muncul. Token tersebut memiliki variasi yang unik, acak, serta memiliki nilai yang besar sehingga menjadikannya rumit untuk diretas oleh _hacker_ atau peretas. Jika tidak terdapat potongan kode tersebut pada elemen `<form>`, maka peretas dapat melakukan hal-hal yang tidak diinginkan melalui link atau HTTP _request_.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Ya, kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`). Contohnya semisal kita ingin menerima input password, maka kita dapat membuat elemen `<form>` dan men-declare secara eksplisit parameter atau input yang dinginkan seperti menuliskan `{{ form.password }}`.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada _database_, hingga munculnya data yang telah disimpan pada template HTML.
1. Ketika form telah diisi dan tombol submit diklik oleh _user_, data akan dibawa oleh _request_ yang nantinya akan disimpan ke dalam suatu variabel oleh fungsi `views.py`.

2. Kemudian diinisiasikan objek baru sesuai dengan _request_ dari _user_. Lalu objek tersebut akan disimpan ke dalam _database_ menggunakan perintah `<objek>.save()`. Contohnya seperti:
   ```
   if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
   ```

3. Pengambilan objek dilakukan oleh `views.py` melalui `models.py` yang akan mengambil data yang sesuai dengan data _user_ dari _database_.

4. Setelah itu data yang tersimpan akan di-_render_ ke HTML untuk ditampilkan kepada _user_.

## Implementasi Tugas 4
1. Membuat folder todolist di dalam clone repository dengan menjalankan command `python manage.py startapp todolist` di terminal.

2. Melakukan routing path ke app `todolist` dengan `path('todolist/', include('todolist.urls'))` pada `project_django/urls.py`:
   ```
   urlpatterns = [
        ...
        path('todolist/', include('todolist.urls')),
    ]
   ```

3. Membuat model `MyToDoList` pada file `models.py` di dalam folder `todolist`:
   ```
   class MyToDoList(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(null = False, blank = False, auto_now_add = True)
        title = models.CharField(max_length = 255)
        description = models.TextField()
        is_finished = models.BooleanField(default = False)
   ```

4. Membuat fungsi untuk `register`, `login`, dan `logout` pada `views.py` kemudian membuat bentuk html nya:
   ```
   def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Akun telah berhasil dibuat!')
                return redirect('todolist:login_user')
        
        context = {'form':form}
        return render(request, 'register.html', context)
    ```
    ```
    def login_user(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse('todolist:show_todolist'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Username atau Password salah!')
        context = {}
        return render(request, 'login.html', context)
    ```
    ```
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('todolist:login_user'))
        response.delete_cookie('last_login')
        return response
    ```

5. Membuat fungsi `show_todolist`, `add_task`, `delete_task`, dan `update_task` pada `views.py` kemudian membuat bentuk html nya:
   ```
   @login_required(login_url='/todolist/login/')
    def show_todolist(request):
        data_tasks = MyToDoList.objects.filter(user=request.user)
        context = {'data_tasks':data_tasks,
                'user' : request.user,
                'last_login': request.COOKIES['last_login'],}
        return render(request, 'todolist.html', context)
    ```
    ```
    @login_required(login_url='/todolist/login/')
    def add_task(request):
        form = TaskForm()
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('todolist:show_todolist')
            
        context = {'form':form}
        return render(request, 'add_task.html', context)
    ```
    ```
    @login_required(login_url='/todolist/login/')
    def delete_task(request, task_id):
        task = MyToDoList.objects.get(id=task_id)
        if task:
            task.delete()
            return redirect('todolist:show_todolist')
        messages.error(request, 'Tidak dapat menghapus task!')
        return redirect('todolist:show_todolist')
    ```
    ```
    @login_required(login_url='/todolist/login/')
    def update_task(request, task_id):
        task = MyToDoList.objects.get(id=task_id)
        if task.is_finished:
            task.is_finished = False
        else:
            task.is_finished = True
        task.save()
        return redirect('todolist:show_todolist')
    ```

6. Membuat routing path pada file `urls.py` di folder `todolist`:
   ```
   urlpatterns = [    
        path('', show_todolist, name='show_todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login_user'),
        path('logout/', logout_user, name='logout_user'),
        path('create-task/', add_task, name='add_task'),
        path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
        path('update-task/<int:task_id>/', update_task, name='update_task'),
    ]
    ```

7. Melakukan _push_ ke repositori dan _deployment_ ke Heroku. Lalu membuat 2 _user_ dan 3 data _task_ pada masing-masing _user_