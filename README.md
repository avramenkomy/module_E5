1. Клонируем проект
2. Устанавливаем приложения из requirements.txt
3. В проекте есть готовая база данных или фикстура, чтобы загрузить данные из фикстуры нужно выполнить команду:
    python manage.py migrate
    python manage.py loaddata fixtures.xml
4. Запускаем сервер
5. На главнной странице доступны фильтры по:
    model - марка или модель автомобиля
    year from - год выпуска "от"
    year to- год выпуска "до"
    gear - список из возможеных вариантов коробок передач
    
    Все эти фильтры не обязательны к заполнению(можно заполнить как один, так и несколько фильтров
    Если при выборке не окажется подходящих вариантов, в шаблоне будет соответствующее сообщение.
    
6. Так же доступен общий фильтр(поиск), поиск осуществляется по всем полям модели автомобиля, кроме года выпуска.

