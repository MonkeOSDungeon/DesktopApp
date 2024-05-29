import os
from datetime import datetime


class Cleaner:
    def __init__(self, video_life_time: int) -> None:
        self.life_time = video_life_time
        # Получаем текущую дату и время
        self.current_datetime = datetime.now()

    # get lifetime from file
    def get_file_lifetime(self, file_path):

        # Получаем время создания файла в секундах с начала эпохи
        creation_time = os.path.getctime(file_path)

        # Преобразуем время создания в объект datetime
        creation_datetime = datetime.fromtimestamp(creation_time)

        # Вычисляем время жизни файла в часах
        hours_difference = (self.current_datetime - creation_datetime).total_seconds() / 3600

        # Выводим результат
        return int(hours_difference)
    
    def clean_directory(self, directory):
                # Укажите желаемое расширение файла
        file_extension = ".avi"

        # Получите список файлов и папок в указанной папке
        files_and_folders = os.listdir(directory)

        # Перебираем файлы в папке
        for item in files_and_folders:

            # Проверяем, является ли элемент файлом с указанным расширением
            if item.endswith(file_extension):

                # Получаем полный путь к файлу
                file_path = os.path.join(directory, item)
                
                if (self.get_file_lifetime(file_path) >= self.life_time):

                        # Проверка существования файла

                    if os.path.exists(file_path):
                        # Удаление файла
                        os.remove(file_path)
                        print(f"Файл {file_path} успешно удален.")
                    else:
                        print(f"Файл {file_path} не найден.")
