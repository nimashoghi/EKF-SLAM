import csv
import multiprocessing as mp
import time

def write_results(name, end_time, start_time, duration):
    with open(name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([name, end_time, start_time, duration])

def time_execution(name):
    def decorator(f):
        def inner(*args, **kwargs):
            start_time = time.time_ns()
            return_value = f(*args, **kwargs)
            end_time = time.time_ns()
            duration = end_time - start_time

            process = mp.Process(target=write_results, args=(name, end_time, start_time, duration))
            process.start()

            return *args, **kwargs
        return inner
    return decorator
