from function import open_json, get_filtered_data, get_last_values, get_formatted_data


def main():
    FILTER_EMPTY_FROM = True
    COUNT_LAST_VALUES = 2

    data = open_json()

    data = get_filtered_data(data, filter_empty_from=FILTER_EMPTY_FROM)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    print('INFO: Вывод транзакции...')
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
