# web_django_in_5_minutes
Tạo một website django trong 5 phút hỗ trợ Window, Linux, MacOs.<br>

<h1>Yêu cầu:</h1>
<ul>
     <li>python 3.6.9</li>
     <li>git</li>
</ul>
<br>
<h1>Window</h1>
<h2>Cài đặt:</h2>
<h3>Bước 1:  Mở Command Prompt và đến tư mục cần lưu Project</h3>
<pre>
cd parentProjectDir\projectDir
</pre>
<h3>Bước 2: Dán vào đoạn mã bên dưới</h3>
<pre>
git clone https://github.com/quangkhoi1228/web_django_in_5_minutes.git
cd web_django_in_5_minutes
python helpers\get-pip.py
pip install virtualenv
virtualenv projectenv
.\projectenv\Scripts\activate
pip install Django
start cmd.exe /c python manage.py runserver
explorer "http://localhost:8000/"
echo done
</pre>
<h1>MacOs</h1>
<h2>Cài đặt:</h2>
<h3>Bước 1: Mở Teminal và đến tư mục cần lưu Project</h3>
<pre>
cd parentProjectDir/projectDir
</pre>
<h3>Bước 2: Dán vào đoạn mã bên dưới</h3>
<pre>
git clone https://github.com/quangkhoi1228/web_django_in_5_minutes.git
cd web_django_in_5_minutes
python helpers/get-pip.py
pip install virtualenv
virtualenv projectenv
source projectenv/bin/activate
pip install Django
osascript -e 'tell app "Terminal"
    do script "open http://localhost:8000/"    
    do script "exit"       
end tell'
python manage.py runserver
echo done
</pre>
<h1>Linux</h1>
<h2>Cài đặt:</h2>
<h3>Bước 1: Mở Teminal và đến tư mục cần lưu Project</h3>
<pre>
cd parentProjectDir/projectDir
</pre>
<h3>Bước 2: Dán vào đoạn mã bên dưới</h3>
<pre>
git clone https://github.com/quangkhoi1228/web_django_in_5_minutes.git
cd web_django_in_5_minutes
python helpers/get-pip.py
pip install virtualenv
virtualenv projectenv
source projectenv/bin/activate
pip install Django
osascript -e 'tell app "Terminal"
    do script "open http://localhost:8000/"    
    do script "exit"       
end tell'
python manage.py migrate
python manage.py runserver
echo done
</pre>
