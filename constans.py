from pathlib import Path

RESULTS_DIR = Path(__file__).parent / 'results'
BASE_DIR = RESULTS_DIR
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PEP_TABLE_HEADER = ('Номер', 'Название', 'Статус')
STATUS_TABLE_HEADER = (('Статус'), ('Количество'))
