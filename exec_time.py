def display_function_execution_time(exec_start_us, exec_end_us):
    print(f"Execution time: {(exec_end_us - exec_start_us) * 1000000:.2f} microseconds")
