import pytest
import zipfile
from config import PATH_ARCHIVE, PATH_NAME_ZIP, PATH_FILES_DOWNLOAD


@pytest.fixture(scope="function")
def create_archive():  # создание архива
    if not PATH_ARCHIVE.exists():  # проверяем существует ли папка
        PATH_ARCHIVE.mkdir()  # создаем папку если её нет
    with zipfile.ZipFile(PATH_NAME_ZIP, 'w') as zip_archive:
        for file in PATH_FILES_DOWNLOAD.iterdir():
            if file.is_file():
                zip_archive.write(file, file.name)  # добавляем файл в архив
