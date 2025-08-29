# logging levels
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# By default, the logging module logs the messages with a logging level of WARNING or above.

import logging

# Set logger for employee module
logger=logging.getLogger(__name__)

logger.setLevel(logging.INFO)

file_handler=logging.FileHandler('employee.log')
# file_handler.setLevel(logging.ERROR) # You can set specific level for handler too
logger.addHandler(file_handler)

formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

# logging.basicConfig(filename='employee.log', level=logging.INFO,
#                     format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        # logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')