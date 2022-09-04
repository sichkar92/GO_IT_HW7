import os
import shutil
from normalize import normalize_filename
from typing import Dict, List, Optional

ARCHIVES = 'archives'
UNKNOWN = 'unknown'

CATEGORIES: Dict[str, list] = {
    'images': ['jpeg', 'png', 'jpg', 'svg'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audios': ['mp3', 'ogg', 'wav', 'amr'],
    'videos': ['avi', 'mp4', 'mov', 'mkv'],
    'archives': ['zip', 'gz', 'tar'],
    'unknown': []
}


def define_category(file_path: str):
    global CATEGORIES
    extention = file_path.split('.')[-1]
    for category, category_extentions in CATEGORIES.items():
        if extention in category_extentions:
            return category
    CATEGORIES[UNKNOWN].append(extention)
    return UNKNOWN


def unpack_archive(archive_src: str, destination_folder: str):
    shutil.unpack_archive(archive_src, destination_folder)


def move_to_category_folder(src: str, destination: str):
    category = define_category(src)
    destination_folder: str = os.path.join(destination, category)
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)
    if category == ARCHIVES:
        unpack_archive(src, destination_folder)
        return
    filename: str = os.path.split(src)[-1]
    filename_without_ext = os.path.splitext(filename)[0]
    extention_filename = os.path.splitext(filename)[1]
    new_filename = ''.join([normalize_filename(filename_without_ext), extention_filename])
    destination_filepath = os.path.join(destination_folder, new_filename)
    shutil.move(src, destination_filepath)


def arrange_folder(target_path: str, destination_folder: str = None):
    if destination_folder is None:
        destination_folder = target_path
    inner_files = os.listdir(target_path)
    for filename in inner_files:
        file_path: str = os.path.join(target_path, filename)
        if os.path.isdir(file_path):
            arrange_folder(file_path, destination_folder)
        elif os.path.isfile(file_path):
            move_to_category_folder(file_path, destination_folder)
        else:
            raise OSError
    try:
        os.rmdir(target_path)  # delete empty folder
    except OSError:
        return


def folder_handler(target_folder: str):
    storage_of_filenames = {}
    handler_category = os.listdir(target_folder)
    for category in handler_category:
        target_category = os.path.join(target_folder, category)
        if os.path.isdir(target_category):
            storage_of_filenames.update({category: os.listdir(target_category)})
    return storage_of_filenames


def extentions_handler(storage_of_filenames: Dict):
    known_ext = []
    unknown_ext = []
    for categories, files in storage_of_filenames.items():
        for file in files:
            extent = file.split('.')[-1]
            if categories == 'archives':
                continue
            elif categories == 'unknown':
                unknown_ext.append(extent)
            else:
                known_ext.append(extent)

    return f'KNOWN EXTENTIONS: {set(known_ext)}', f' UNKNOWN EXTENTIONS:{set(unknown_ext)}'
