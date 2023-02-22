from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

values = [2,4,9,11]
nval = [324324,325346,8967867876,234534667557,35456547657]
def square(n):
    return n**2

def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square,nval)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
