def print_hello(value):
    if isinstance(value, str):
        return f'Hello, {value}'
    else:
        return 'This is not str'
    

if __name__ == '__main__':
    result = print_hello('John')
    print(result)
