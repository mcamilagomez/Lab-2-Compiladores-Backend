def export_to_file(json_data, filename):
    with open(filename, 'w') as json_file:
        json_file.write(json_data)