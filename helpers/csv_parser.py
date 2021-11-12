
def csv_headers(headers):
    processed = []
    i = 0
    for header in headers:
        if header == 'Event':
            header = header + ' {}'.format(i)
            i = i + 1

        processed.append(header)
    
    return processed


def combine_record(headers, row):
    zip_it = zip(headers, row)
    record = dict(zip_it)

    return record