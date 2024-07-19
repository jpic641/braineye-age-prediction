import os
import glob

def get_image_paths(data_dir, extensions=('JPG', 'jpeg', 'JPEG', 'png')):
    """Retrieve image paths from a given path

    Args:
        data_dir (str): directory of images
        extensions (tuple[str]): image extensions to retrieve. Defaults to ('JPG', 'jpeg').

    Returns:
        file_paths: list of image file paths
    """
    file_paths = []

    for extension in extensions:
        path = os.path.join(data_dir, f'**/*.{extension}')
        file_path = glob.glob(path, recursive=True)
        file_paths.extend(file_path)

    return file_paths