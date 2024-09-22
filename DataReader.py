import re

class DataReader(object):

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        data = []

        with open(self.filename, 'r') as f:
            headers = [header.strip().lower() for header in f.readline().split(',')]

            for line in f:
                tokens = [token.strip() for token in line.split(',')]
                record = {}
                for i in range(len(tokens)):
                    value = tokens[i]
                    if headers[i] != 'zip' and re.match('\d+(\.\d*)?', value):
                        value = float(value)
                    if value == '':
                        value = 0
                    record[headers[i]] = value
                data.append(record)

        return data