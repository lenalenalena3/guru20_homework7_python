import pytest
import zipfile
import os.path
from config import PATH_ARCHIVE, PATH_NAME_ZIP, PATH_FILES_DOWNLOAD


@pytest.fixture(scope="function")
def create_archive():  # создание архива
    if not os.path.exists(PATH_ARCHIVE):  # проверяем существует ли папка
        os.mkdir(PATH_ARCHIVE)  # создаем папку если её нет
    with zipfile.ZipFile(PATH_NAME_ZIP, 'w') as zip_archive:
        for file in os.listdir(PATH_FILES_DOWNLOAD):
            file_path = os.path.join(PATH_FILES_DOWNLOAD, file)
            if os.path.isfile(file_path):
                zip_archive.write(file_path, file)  # добавляем файл в архив
