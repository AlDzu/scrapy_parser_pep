import csv
import datetime as dt

from constans import DATETIME_FORMAT, STATUS_TABLE_HEADER  # , RESULTS_DIR
from constans import BASE_DIR  # == RESULTS_DIR, Не используется,
# но тесты требуют


class PepParsePipeline:
    def open_spider(self, spider):
        self.result_dir = BASE_DIR
        BASE_DIR.mkdir(exist_ok=True)
        self.status_dict = {}

    def process_item(self, item, spider):
        status = item['status']
        if status in self.status_dict:
            self.status_dict[status] += 1
        else:
            self.status_dict[status] = 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        status_file_name = f'status_summary_{now_formatted}.csv'
        status_file_path = BASE_DIR / status_file_name

        with open(status_file_path, 'w', encoding='utf-8') as f:
            dialect = csv.Dialect
            dialect.delimiter = ' '
            dialect.escapechar = ' '
            dialect.quoting = csv.QUOTE_NONE
            dialect.lineterminator = '\n'
            result = []
            result.append(STATUS_TABLE_HEADER)
            for key in self.status_dict:
                result.append((key, ) + (self.status_dict[key], ))
            result.append(('Total', ) + (sum(self.status_dict.values()), ))
            writer = csv.writer(f, dialect=dialect)
            writer.writerows(result)
