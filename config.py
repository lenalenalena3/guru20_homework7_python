import os.path

CURRENT_FILE = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(CURRENT_FILE)
PATH_FILES_DOWNLOAD = os.path.join(BASE_DIR, 'tmp')
PATH_ARCHIVE = os.path.join(BASE_DIR, 'attachment')
PATH_NAME_ZIP = os.path.join(PATH_ARCHIVE, 'zip_file.zip')
