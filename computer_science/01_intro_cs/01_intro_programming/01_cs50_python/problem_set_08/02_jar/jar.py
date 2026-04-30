class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if not int(n) or self.size + int(n) > self.capacity:
            raise ValueError("Adding this many would exceed the cookie jar's capacity")
        self.size += int(n)

    def withdraw(self, n):
        if not int(n) or self.size - int(n) < 0:
            raise ValueError("There are not that many cookies in the cookie jar")
        self.size -= int(n)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not int(capacity) or int(capacity) < 0:
            raise ValueError("Capacity is not a non-negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = int(n)

def main():
    jar = get_jar()
    jar.deposit(1)
    print(jar)
    jar.withdraw(1)
    print(jar)

def get_jar():
    capacity = int(input("What is the jar's capacity: "))
    return Jar(capacity)

if __name__ == "__main__":
    main()
