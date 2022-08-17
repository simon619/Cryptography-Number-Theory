class PreRanNum:

    def __init__(self, modulus, multiplier, increament, first_number):
        self.m = modulus
        self.a = multiplier
        self.c = increament
        self.x = first_number

    def __rules__(self):
        bool = True
        if not 2 <= self.a < self.m:
            bool = False
        if not 0 <= self.c < self.m:
            bool = False
        if not 0 <= self.x < self.m:
            bool = False
        return bool

    def __generate__(self, x, list, counter):
        if counter == self.m:
            return list
        else:
            next_number = (self.a * x + self.c) % self.m 
            list.append(next_number)
            return self.__generate__(next_number, list, counter + 1)

if __name__ == "__main__":
    modulus, multiplier, increament, first_number = 9, 7, 4, 3
    inst = PreRanNum(modulus, multiplier, increament, first_number)
    purity = inst.__rules__()
    if purity:
        result = inst.__generate__(first_number, [], 0)
        print(f'Generated Number: {result}')
    else:
        print("Rule are not maintained")