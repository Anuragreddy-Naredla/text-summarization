
import os
import zipfile
from textsummarization.logging import logger
from textsummarization.utils.common import get_size
from urllib.request import urlretrieve
from textsummarization.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # def download_file(self, ):
    #     if not os.path.exists(self.config.local_data_file):
    #         print("SOURCE_URL:::", self.config.source_URL, self.config.local_data_file)
    #         filename, headers = urlretrieve(
    #             url = self.config.source_URL,
    #             filename = self.config.local_data_file
    #         )
    #         logger.info(f"{filename} download! with following info: \n{headers}")
    #     else:
    #         logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
