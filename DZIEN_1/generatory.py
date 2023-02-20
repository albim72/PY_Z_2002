#przykład 1
def liczby():
    for i in range(17):
        yield i*2

print(liczby())
print(list(liczby()))

for p in liczby():
    print(p)


#przykład 2
def wznowienie(n,k):
    print("wstrzymanie działania...")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania...")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania")

    print("ekstra struktura")
    def wz(k):
        return (k-1)**3
    yield wz(n)

for i in wznowienie(6,8):
    print(f"zwróconono wartość i = {i}")


def complexgen():
    x=0
    while True:
        print("x-print1")
        y = yield x
        print("x-print2")
        if y is None:
            x = x+1
        else:
            x=y

g= complexgen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(115))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


