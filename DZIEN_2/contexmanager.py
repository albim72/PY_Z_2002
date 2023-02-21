class ContextManager:
    def __init__(self):
        print('wywołanie metody init')

    def __enter__(self):
        print('wywołanie metody enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('wywołanie metody exit')


with ContextManager() as manager:
    print('to jest blok instrukcji with')
    
