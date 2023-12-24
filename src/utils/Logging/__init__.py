import logging

all_handler = logging.FileHandler('logi_all.log')
info_handler = logging.FileHandler('logi_info.log')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

all_handler.setFormatter(formatter)
info_handler.setFormatter(formatter)

all_handler.setLevel(logging.DEBUG)
info_handler.setLevel(logging.INFO)

logger1 = logging.getLogger('../ReferenceBook/ReferenceBook')


