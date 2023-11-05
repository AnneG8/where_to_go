# Куда пойти — Москва 

Сайта о самых интересных местах в Москве. 

![Куда поити](static/.gitbook/assets/site.png)

## Демо-версия сайта

Демо-версию сайта можно посмотреть на [AnneG8.pythonanywhere.com](https://AnneG8.pythonanywhere.com/).

## Как установить

Python3.11 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```shell
pip install -r requirements.txt
```
Создайте файл **.env** в корне репозитория, добавьте в него **переменные окружения**:
- SECRET_KEY — секретный ключ приложения. Используется для криптографической подписи, должен быть установлен в уникальное, непредсказуемое значение.
- ALLOWED_HOSTS — список допустимых хостов/доменных имен, которые могут обслуживаться приложением. Это важная мера безопасности, которая помогает предотвратить атаки на заголовок HTTP Host.
- DEBUG — булевое значение, включающее режим отладки. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. По умолчанию - `False`.

Создайте базу данных:
```shell
python manage.py makemigrations
python manage.py migrate
```
Создайте суперпользователя:
```sh
python manage.py createsuperuser
```

### Как запустить

Запустите разработческий сервер:
```shell
python manage.py runserver
```

### Как заполнить базу данных

Вы можете заполнить базу данных, используя команду **load_place**:
```shell
python manage.py load_place https://адрес/первого/json/файла.json https://адрес/второго/json/файла.json
```
При этом структура json-файла должна быть [такой](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json).
Количество ссылок на файлы, которых можно указать за раз, не ограничено.


### Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

![debug mode](static/.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

### Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
