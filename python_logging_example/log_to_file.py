import os
import logging
import iolite as io

logger = logging.getLogger(__name__)


def run():
    logger.info('BEGIN')

    logger.setLevel('DEBUG')

    fd = io.folder(os.path.expandvars('$PYTHON_LOGGING_EXAMPLE_DATA/log_to_file'), reset=True)
    for idx in range(3):
        file_handler = logging.FileHandler(fd / f'{idx}.txt')
        formatter = logging.Formatter('%(asctime)s: [%(levelname)s] %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.debug(f'{idx}: debug')
        logger.info(f'{idx}: info')
        logger.warning(f'{idx}: warning')

        logger.removeHandler(file_handler)
