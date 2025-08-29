import logging
import employee

# Set logger
logger= logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler('test.log')
logger.addHandler(file_handler)

formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

# logging.basicConfig(filename='test.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
# logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
# logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
# logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
# logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))