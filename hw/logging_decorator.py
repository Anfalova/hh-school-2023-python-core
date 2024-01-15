import time
import logging


logging.basicConfig(level=logging.INFO, filename="logging.log",
                    format="%(asctime)s %(levelname)s %(message)s")


def logging_decorator(function):

    def inner_func(*args, **kwargs):
        start_time = time.time()
        logging.info(f'Start time for {function.__name__}: {start_time}')
        result = function(*args, **kwargs)
        end_time = time.time()
        logging.info(f'End time for {function.__name__}: {end_time}')
        logging.info(f'Execution time for {function.__name__}: {end_time - start_time}')
        return result

    return inner_func
