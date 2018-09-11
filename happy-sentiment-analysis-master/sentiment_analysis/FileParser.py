import csv

class FileParser:
    def parse(self, file_path):
        result = []
        with open(file_path, newline='') as csvfile:
            dict_reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')

            for row in dict_reader:
                result.append(row)
        return result

    def write(self, file_path, file_content):
        file_content_keys = file_content[0].keys()

        with open(file_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, file_content_keys, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            writer.writerows(file_content)
