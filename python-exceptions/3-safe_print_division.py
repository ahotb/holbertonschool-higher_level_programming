#!/usr/bin/python3
def safe_print_division(a, b):
    valve = None
    try:
        valve = a / b
        return valve
    except (TypeError, ZeroDivisionError):
        return None
    finally:
        print("{}: {}".format("Inside result", valve))
