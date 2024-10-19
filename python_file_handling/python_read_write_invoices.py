# Random access is the term used to access data from any part of a file. RAM (Random access memory) means the
# computer can read (write) to any location in its memory. Random access in files means the file pointer can be
# changed to any location in the file, for reading and writing.

# File pointer keeps track of where you are in the file. When you write data to the file, data is written at the
# current position of the file pointer. File pointer moves forward as data is written. Similarly, when reading from
# text file, reading takes place from file pointer's position, and it moves forward as data is read.

# Random access in Python is very limited with text files. It is only possible to position the file pointer either
# at the start of the file or at the end. For true random access to your text data, you have to either open the file
# in binary mode or read entire file into a string.

# With text files, we have 2 options when seeking: 1) seek relative to the start of the file 2) seek to the end of the
# file. It is possible to seek further on from start of the file.

import datetime
from os import SEEK_SET
from typing import TextIO

invoice_input_filename = '../files/invoices.csv'

def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, invoice_number = invoice_number.split('-')
    return int(year), int(invoice_number)


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_year, invoice_number = parse_invoice_number(invoice_number)
    year = get_year()
    if invoice_year == year:
        invoice_number += 1
    else:
        invoice_year = year
        invoice_number = 1
    new_invoice_number = f'{invoice_year}-{invoice_number:04d}'
    return new_invoice_number


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr: int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk .

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_ptr: The position of the start of the last line in the file. This will be obtained
        from the previous call to the `record_invoice`.
    :return The position of the start of the last line in the file. This will be used in the subsequent
        calls to the `record_invoice`.
    """
    invoice_file.seek(last_line_ptr, SEEK_SET)
    last_row = ""
    for line in invoice_file:
        last_row = line
    if last_row:
        # Below line, we have used _,_ as those variables are not used, it is also a convention in Python
        # invoice_num, _, _ = last_row.split('\t')
        invoice_num = last_row.split('\t')[0]
        new_invoice_num = next_invoice_number(invoice_num)
    else:
        # File is empty
        year = get_year()
        new_invoice_num = f'{year}-{1:04d}'

    last_line_ptr = invoice_file.tell()
    print(f'{new_invoice_num}\t{company}\t{amount}', file=invoice_file)

    return last_line_ptr

data_file = '../files/invoices.csv'

# r+ is used to open the file in read mode and also lets you write to the file
# w+ also lets you read and write in the file, but 'w' will truncate the file if it already exists (content deleted).
with open(data_file, 'r+') as invoices:
    last_line = record_invoice(invoices, 'ACME Roadrunner', 18.40, 0)
    last_line = record_invoice(invoices, 'Squirrel Storage', 320.40, last_line)

# With text files, you can seek to the start or end of the file. You can seek to a position within the file, but the
# position must be a position obtained by calling tell. We cant provide any random integer value here.

print("================================================================================")

# Test code:
current_year = get_year()
test_data = [
    ('2019-0005', (2019, 5), f'{current_year}-0001'),
    (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
    (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
    (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
]

for test_string, result, next_number in test_data:
    parts = parse_invoice_number(test_string)
    if parts == result:
        print(f'{test_string} parsed successfully')
    else:
        print(f'{test_string} failed to parse. Expected {result} got {parts}')

    new_number = next_invoice_number(test_string)
    if next_number == new_number:
        print(f'New number {new_number} generated correctly for {test_string}')
    else:
        print(f'New number {new_number} is not correct for {test_string}')

    print("================================================================================")

