import time
from decorator import Decorator


def findElapsedTime(func):
    def wrapper(data):
        print("\n")
        start = time.time()
        func(data)
        end = time.time()
        print(f"Function-decorator elapsed time = {end-start:01f} sec")

    return wrapper


@findElapsedTime
@Decorator
def sorted(data):
    data.sort(key=lambda a: len(a))
    print(f"Sorted = {rawData}")


@findElapsedTime
@Decorator
def unique(data):
    """
    set - множество
    """
    print(f"Unique = {list(set(data))}")


@findElapsedTime
@Decorator
def myEnumerate(data=None):
    if data is None:
        data = []
    i = range(len(data))
    s = zip(i, data)
    print(list(s))


@findElapsedTime
@Decorator
def frequencyOfWords(filename):
    f = open("test.txt")
    data = f.read()
    f.close()
    data = data.split(" ")
    res = {}
    for i in data:
        res[i] = data.count(i)
    print(res)


@findElapsedTime
@Decorator
def pow2For(data):
    buf = list(range(len(data)))
    for i in range(len(data)):
        buf[i] = pow(data[i], 2)
    print(buf)


@findElapsedTime
@Decorator
def pow2ListComprehension(data):
    i = [pow(i, 2) for i in data]
    print(i)


@findElapsedTime
@Decorator
def pow2Map(data):
    print(list(map(lambda x: x**2, data)))


rawData = ["python", "perl", "c", "haskell", "cpp", "haskell", "cpp", "ruby", "ruby"]


print(f"Raw data = {rawData}")

print("\nTask 1")
findElapsedTime(unique(rawData))

print("\nTask 2")
findElapsedTime(sorted(rawData))

print("\nTask 3")
findElapsedTime(myEnumerate(rawData))

print("\nTask 4")
findElapsedTime(frequencyOfWords("test.txt"))


print("\nTask 5")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f"Initial array = {arr}")
print("For")
findElapsedTime(pow2For(arr))
print("\n\nList Comprehension")
findElapsedTime(pow2ListComprehension(arr))
print("\n\nMap")
findElapsedTime(pow2Map(arr))
