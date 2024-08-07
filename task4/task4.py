import sys
import statistics

def main(filename):
    with open(filename) as file:
        nums = [int(line.strip()) for line in file]
    median = int(statistics.median(nums))
    moves = sum(abs(num - median) for num in nums)
    print(moves)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите файл с данными по примеру: python your_script.py <filename>.txt")
    else:
        main(sys.argv[1])