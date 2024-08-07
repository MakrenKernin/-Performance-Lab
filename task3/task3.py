import json
import sys

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def build_value_map(values):
    return {entry['id']: entry['value'] for entry in values}

def fill_values(tests, value_map):
    for test in tests:
        test_id = test.get('id')
        if test_id in value_map:
            test['value'] = value_map[test_id]
        if 'values' in test:
            fill_values(test['values'], value_map)

def main():
    if len(sys.argv) != 4:
        print("Укажите три пути к файлам: python script.py <values.json> <tests.json> <report.json>")
        return

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = read_json_file(values_file)
    tests_data = read_json_file(tests_file)

    value_map = build_value_map(values_data['values'])

    fill_values(tests_data['tests'], value_map)

    write_json_file(report_file, tests_data)

if __name__ == "__main__":
    main()