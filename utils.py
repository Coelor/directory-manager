import time


def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Time taken: {(end_time - start_time)*1000:.4f} ms")
    return result


def print_results(title, result):
    print(f"\n{title}")
    if isinstance(result, list):
        for item in result:
            print(f"  - {item}")
    else:
        print(result)
