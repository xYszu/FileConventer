import os


def get_extension(file_name):
    return os.path.splitext(file_name)[1].lower()


def is_valid_extension(extension):
    return extension in ['.xml', '.json', '.yml', '.yaml']
