"""
Utils to manipulate file access.
"""
import os

def get_absolute_path_file(file_name: str) -> str:

    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    return os.path.join(parent_dir, file_name)
