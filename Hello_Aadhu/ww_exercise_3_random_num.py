
import random

class smallestNum:
    def __init__(self, random_num, numLow, numHigh):
        self.random_num = random_num
        self.numLow = numLow
        self.numHigh = numHigh

    def genrate_rand_n(self):
        listOfNumbers = []
        for x in range(0, self.random_num):
            listOfNumbers.append(random.randint(self.numLow, self.numHigh))
        print(f"The {self.random_num} random numbers are below - ")
        print(listOfNumbers, '\n')
        ordered_list = set(listOfNumbers)
        print(f"You got the following {len(ordered_list)} uniqe numbers from random generated numbers -\n",
              list(ordered_list), '\n')
        nth_pos = int(
            input(f"Enter the nth smallest number you want to print from {len(ordered_list)} uniqe numbers: "))

        try:
            if nth_pos > len(ordered_list) or nth_pos < 1 - len(ordered_list):
                nth_pos = int(input(f"Index out of range, Please enter a valid positive nth position in range from {len(ordered_list)} uniqe numbers: "))
        except IndexError:
            print("Unexpected Error...!!")
        else:
            temp = list(ordered_list)[nth_pos - 1]
            print(f"Smallest value in position '{nth_pos}' is {temp} from {len(ordered_list)} uniqe numbers, range({self.numLow},{self.numHigh})")


input_randum = int(input("Enter positive count value to generate random numbers greater than zero: "))
num_Low = int(input("Enter lower range: "))
num_High = int(input("Enter higher range: "))
p1 = smallestNum(input_randum, num_Low, num_High)
p1.genrate_rand_n()


