def display_function_execution_time(exec_start_us, exec_end_us, function_name=''):
    result = exec_end_us - exec_start_us
    if result > 1:
        print(f"{function_name} execution time: {result:.2f} s")
    elif result > .001:
        print(f"{function_name} execution time: {result * 1_000:.2f} ms")
    else:
        print(f"{function_name} execution time: {result * 1_000_000:.2f} microseconds (\u03BCs)")
