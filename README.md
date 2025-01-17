# Модуль фитнес-трекера

## Описание:
Модуль фитнес-трекера предназначен для считывания и отображения результатов тренировки.  
Обрабатывает данные 3-х видов тренировок: бега, спортивной ходьбы и плавания.

## Функции:
Этот модуль выполняет следующие функции:
- принимает от блока датчиков информацию о прошедшей тренировке;
- определяут вид тренировки;
- рассчитывает результаты тренировки;
- выводит информационное сообщение о результатах тренировки.

## Информационное сообщение включает следующие данные:
- тип тренировки (бег, ходьба или плавание);
- длительность тренировки;
- дистанцию, которую преодолел пользователь, в километрах;
- среднюю скорость на дистанции, в км/ч;
- расход энергии, в килокалориях.

## Стек технологий:
- Python;
- Git.

## Запуск проекта:
- Клонируйте репозиторий:
```
git clone https://github.com/VeraFaust/hw_python_oop.git
```

- Установите и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```

- Установите зависимости из файла requirements.txt
```
py -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

- Запустите файл homework.py.

## Пример вывода программы:
Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 0.994 км; Ср. скорость: 1.000 км/ч; Потрачено ккал: 336.000.  
Тип тренировки: Running; Длительность: 1.000 ч.; Дистанция: 9.750 км; Ср. скорость: 9.750 км/ч; Потрачено ккал: 699.750.  
Тип тренировки: SportsWalking; Длительность: 1.000 ч.; Дистанция: 5.850 км; Ср. скорость: 5.850 км/ч; Потрачено ккал: 157.500.


## Автор:
Фауст Вера
