class PositiveNumberTuple(tuple):
    def __new__(cls, *numbers):
        skipped_val = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped_val += 1
        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_val = skipped_val
        return instance

postp = PositiveNumberTuple(9,12,3,0,6,0,-9,12,-3,99,-99,0,123,-56,-23,-111,345,6,7,9)
print(postp)
print(type(postp))
print(postp.skipped_val)
