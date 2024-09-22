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
                limit = len(headers)
                if len(headers) > len(tokens):
                    limit = len(tokens)
                for i in range(limit):
                    value = tokens[i]
                    try:
                        value = float(value)
                    except:
                        value = tokens[i]
                    if value == '':
                        value = 0
                    record[headers[i]] = value
                data.append(record)

        return data