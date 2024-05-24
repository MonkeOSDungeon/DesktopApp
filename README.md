# DesktopApp

Desktop application for Operating System subject in SSAU \

convert .ui to .py

```shell
pyside6-uic change_zone.ui -o ui_change_zone.py
pyside6-uic main_window.ui -o ui_main_window.py
```

# Добавить бд где будут храниться адреса ip камер

# Добавить сохранение видео
```shell
https://www.google.com/search?q=python+%D0%BA%D0%B0%D0%BA+%D1%81%D0%BE%D0%B7%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE+%D0%B8%D0%B7+%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9&rlz=1C1CHZN_ruRU1020RU1021&oq=python+%D0%BA%D0%B0%D0%BA+%D1%81%D0%BE%D0%B7%D1%85%D1%80%D0%B0%D0%BD%D0%B8%D1%82%D1%8C+%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE+%D0%B8%D0%B7+%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRifBdIBCTEzODE3ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
https://ru.stackoverflow.com/questions/1426240/%D0%A1%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-%D0%B8%D0%B7-%D1%84%D0%BE%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B9-python-open-cv
https://ru.stackoverflow.com/questions/805599/%D0%A1%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D1%8C-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-%D0%B8%D0%B7-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B0%D0%BC%D0%B8-opencv
https://stackoverflow.com/questions/43048725/python-creating-video-from-images-using-opencv
```

Todo list: \
    Написать нормальный README \
    поддержка нескольких камер (хотя бы 2) \
    Бд, куда будут сохраняться видео \
    Каждое видео хранящееся в бд длиной в час \
    На видео должны быть пометки, в какой промежуток времени был обнаружен человек (как в кадре так и в зоне) \
    Переработка интерфейса \
    Возможность задавать зону через прямоугольник \
    Добавление нескольких зон \
    Добавление зоны, в которой не нужно распознавать \

Настройки: \
    Указание почты куда будет приходить уведомления \
    Изменение качества видео \

Идеи (по реализации, какой либо фичи или сама фича): \
    combobox в котором выбираешь камеру (один из вариантов поддержки нескольких камер) \
    сохранение изображения в зоне в более высоком качестве (сохранять отдельно фоновое(изображение вне зоны сохраяется в 360р) и зона отдельно (в 480р) например) \
