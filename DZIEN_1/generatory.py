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


