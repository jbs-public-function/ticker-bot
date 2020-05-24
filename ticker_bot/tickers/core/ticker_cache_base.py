import os
import shutil
import pickle
import datetime
import logging

logging.basicConfig(level=logging.INFO)

class TickerCacheEpochBase(object):
    LABEL = 'TickerCacheEpochBase'
    def __init__(self, seconds_threshold: int):
        self.seconds_threshold = seconds_threshold
        if self.seconds_threshold is None:
            self.seconds_threshold = 900
        self.logger = logging.getLogger(self.LABEL)

    @property
    def current_timestamp(self):
        return round(datetime.datetime.now().timestamp())

    def timestamp_within_cache_window(self, new_timestamp: int, old_timestamp: int):
        return (new_timestamp - old_timestamp) < self.seconds_threshold
    

class TickerCacheBase(TickerCacheEpochBase):
    LABEL = 'TickerCacheBase'
    CACHE_DIR = os.path.dirname(__file__)
    CACHE_DATA_DIR = '.ticker-cache'

    def __init__(self, sub_directory: str, seconds_threshold: int):
        super().__init__(seconds_threshold)
        self.sub_directory = sub_directory
        if sub_directory is None:
            self.sub_directory = 'default'

    @property
    def latest_timestamp(self):
        timestamp = self.get_latest_cached_timestamp
        current_timestamp = self.current_timestamp
        if self.timestamp_within_cache_window(current_timestamp, timestamp):
            return timestamp
        self._remove_tree(os.path.join(self.cache_dir_base, f'{timestamp}'))
        return current_timestamp

    @property
    def cache_dir_base(self):
        cache_dir_base = os.path.join(self.CACHE_DIR, self.CACHE_DATA_DIR)
        if not os.path.exists(cache_dir_base):
            os.makedirs(cache_dir_base)
        return cache_dir_base

    @property
    def cache_dir(self):
        cache_dir = os.path.join(self.cache_dir_base, f'{self.latest_timestamp}', self.sub_directory)
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        return cache_dir

    @property
    def get_latest_cached_timestamp(self):
        dirs = os.listdir(self.cache_dir_base)        
        dirs = sorted([int(_dir) for _dir in dirs if self.valid_cached_timestamp(_dir)], reverse=True)
        if len(dirs) == 0:
            return 0
        return dirs[0]

    def valid_cached_timestamp(self, timestamp):
        try:
            return isinstance(int(timestamp), int)
        except ValueError:
            self._remove_tree(os.path.join(self.cache_dir_base, f'{timestamp}'))
        return False

    def _write_file_to_cache(self, descriptors, data):
        filename = os.path.join(self.cache_dir, self.hash_filename(descriptors))
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        return os.path.isfile(filename)

    def _read_file_from_cache(self, descriptors):
        filename = os.path.join(self.cache_dir, self.hash_filename(descriptors))
        with open(filename, 'rb') as file:
            return pickle.load(file)
    
    def _remove_tree(self, path):
        self.logger.info(f'Removing tree at path - {path} - if it exists')
        if self.cache_dir_base not in path:
            self.logger.error(OSError('Attempting to remove a file or directory outside the scope of this project. Bad path {path}'))
            return
        if not os.path.exists(path):
            return
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.exists(path):
            shutil.rmtree(path)
        return 

    @classmethod
    def hash_filename(cls, descriptors):
        return str(hash(cls.stringify_descriptors(descriptors)))

    @classmethod
    def stringify_descriptors(cls, descriptors):
        if isinstance(descriptors, str):
            return descriptors
        if isinstance(descriptors, (tuple, list)):
            return ''.join(descriptors)
        return str(descriptors)


class TickerCache(TickerCacheBase):
    CACHE_DIR = os.path.join(os.path.dirname(__file__), '..')
    LABEL = 'TickerCache'
    def __init__(self, sub_directory: str, seconds_threshold: int):
        super().__init__(sub_directory=sub_directory, seconds_threshold=seconds_threshold)

    def write_file_to_cache(self, descriptors, data):
        try:
            return self._write_file_to_cache(descriptors, data)
        except FileNotFoundError as fnfe:
            self.logger.error(fnfe)
        return False

    def read_file_from_cache(self, descriptors):
        try:
            return (True, self._read_file_from_cache(descriptors))
        except FileNotFoundError as fnfe:
            self.logger.error(fnfe)
        return (False, '')