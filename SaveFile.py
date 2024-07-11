import json

import xmltodict
import yaml

import validator
import GetFiles


def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def convert_file(file1, file2):
    input_ext = validator.get_extension(file1)
    output_ext = validator.get_extension(file2)

    if not (validator.is_valid_extension(input_ext) and validator.is_valid_extension(output_ext)):
        raise ValueError("Oba formaty muszą być poprawne (.xml, .json, .yml)")

    if input_ext == output_ext:
        print("Formaty są takie same. Nie potrzebna konwersja")
        return

    # Read input file
    input_content = GetFiles.read_file(file1)

    # Parse input content
    if input_ext == '.xml':
        data = xmltodict.parse(input_content)
    elif input_ext == '.json':
        data = json.loads(input_content)
    elif input_ext == '.yml' or input_ext == '.yaml':
        data = yaml.safe_load(input_content)
    else:
        raise ValueError(f"Zły format: {input_ext}")

    # Convert to output format
    if output_ext == '.xml':
        output_content = xmltodict.unparse(data, pretty=True)
    elif output_ext == '.json':
        output_content = json.dumps(data, indent=4)
    elif output_ext == '.yml' or output_ext == '.yaml':
        output_content = yaml.dump(data, sort_keys=False)
    else:
        raise ValueError(f"Zły format: {output_ext}")

    # Write output file
    write_file(file2, output_content)
    print(f"Przekonwertowano {file1} do {file2}")
