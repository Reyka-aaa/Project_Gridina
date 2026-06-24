#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения
class Counter:
    def __init__(self, v=0):
        self.v = v

    def inc(self):
        self.v += 1
        return self.v

    def dec(self):
        self.v -= 1
        return self.v

    def show(self):
        print(f"Значение: {self.v}")


c1 = Counter()
c2 = Counter(10)

print("Счетчик 1:")
c1.show()
c1.inc()
c1.show()
c1.inc()
c1.show()
c1.dec()
c1.show()

print("\nСчетчик 2:")
c2.show()
c2.dec()
c2.show()
c2.dec()
c2.show()
c2.inc()
c2.show()
