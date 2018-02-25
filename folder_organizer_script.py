from os import listdir, mkdir, rename
from os.path import join, isfile, exists

source_folder = '/Users/alaminsarker/Downloads'
items_list = listdir(source_folder)

print items_list

extension_to_folder_mapper = {

    'app dmg pkg': 'applications',
    'zip tar gz bz2': 'compressed_files',
    'txt xlsx xls doc docx pdf PDF pptx': 'text_files',
    'py pyc whl sh': 'programming_files',
    'mp3': 'audio_files',
    'mp4': 'video_files'
}


def get_file_extension(file_name):
    split_name = file_name.split('.')
    return split_name[-1]


def create_folder(name):
    if not exists(join(source_folder, name)):
        mkdir(join(source_folder, name))


def move_file_to_folder(file_name, folder_name):
    old_path = join(source_folder, file_name)
    new_path = join(source_folder, folder_name, file_name)
    rename(old_path, new_path)


def map_extension_to_folder(extension, name):
    folder_name = 'others'
    for extension_list, destination_folder in extension_to_folder_mapper.iteritems():
        if extension in extension_list.split(' '):
            folder_name = destination_folder
            break

    create_folder(folder_name)
    move_file_to_folder(name, folder_name)


def main():
    for item_name in items_list:
        if isfile(join(source_folder, item_name)):

            # split_name = item_name.split('.')
            extension = get_file_extension(item_name)
            map_extension_to_folder(extension, item_name)

if __name__ == '__main':
    main()
