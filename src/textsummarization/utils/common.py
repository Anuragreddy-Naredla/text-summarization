import os
from box.exceptions import BoxValueError
import yaml
from textsummarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations # for brief description refer to trials.ipynb notebook.
def read_yaml(path_to_yaml: Path):
    """
    reads yaml file.
    Args:
        path_to_yaml (str): path of the yaml file
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)# i will call with the key names only for this we will use ConfigBox Refer trials.ipynb file.
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    creates list of directories.
    Args:
        path_to_directories (list) : list of path of the directories.
        verbose(bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def get_size(path:Path):
    """
    get size in KB.

    Args:
        path(Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

