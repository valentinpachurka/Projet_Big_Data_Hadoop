import csv
import sys
import time
import happybase
import uuid

def generate_row_key():
    unique_id = str(uuid.uuid4())
    timestamp = str(int(time.time()))
    return '{}_{}'.format(timestamp, unique_id)

def create_hbase_table(connection, table_name, column_names):
    column_families = {column_name: dict() for column_name in column_names}
    connection.create_table(table_name, column_families)

def insert_row_batch(connection, table_name, batch_list, batch_size):
    with connection.table(table_name).batch(batch_size=batch_size) as batch:
        for row_key, column_data in batch_list:
            batch.put(row_key, column_data)

def main():
    connection = happybase.Connection('127.0.0.1', 9090)
    connection.open()

    file_name = 'dataw_fro03.csv'

    total_lines = sum(1 for line in open(file_name, 'r', encoding='utf-8')) - 1

    count = 0
    count_all_lines = 0

    progress_bar_length = 50
    progress_step = None

    start_time = time.time()

    with open(file_name, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        print(header)

        table_name = file_name.replace(".csv", "")
        log_table_name = "Log_" + table_name
        create_hbase_table(connection, table_name, ["cf"])
        create_hbase_table(connection, log_table_name, ['info'])

        batch_size = 1500
        batch_list = []

        for row in csv_reader:
            count_all_lines += 1
            values = [(col_value if col_value != "NULL" else "") for col_value in row]
            row_key = generate_row_key()
            column_data = {}
            for i, column_value in enumerate(values):
                column_name = "cf:" + header[i]
                column_data[column_name] = column_value.encode('utf-8')
            batch_list.append((row_key, column_data))
            count += 1

            if len(batch_list) >= batch_size:
                insert_row_batch(connection, table_name, batch_list, batch_size)
                batch_list = []

            if progress_step is None:
                progress_step = total_lines / progress_bar_length
            if count_all_lines >= progress_step:
                progress_bar_position = int((count_all_lines / total_lines) * progress_bar_length)
                updated_progress_bar = "[" + "#" * progress_bar_position + " " * (progress_bar_length - progress_bar_position) + "]"
                sys.stdout.write("\rProgression : " + updated_progress_bar + " {} / {} lines".format(count_all_lines, total_lines))
                sys.stdout.flush()

        if batch_list:
            insert_row_batch(connection, table_name, batch_list, batch_size)

    sys.stdout.write("\n")
    end_time = time.time()

    print("{} is finished with {} lines inserted".format(table_name, count))

    log = {}

    for key, value in log.items():
        connection.table(log_table_name).put(key, {"info:Error": str(value).encode('utf-8')})

    print("{} is finished".format(log_table_name))

    total_seconds = int(end_time - start_time)
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    print("Total processing : {} minutes and {} seconds with batch size {}".format(minutes, seconds, batch_size))

    connection.close()

if __name__ == "__main__":
    main()
