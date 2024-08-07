import sys

def main(n, m):
    result = [1]

    for i in range(1, n):
        index = (m - 1) * i
        element = (index + 1) % n
        element = n if element == 0 else element

        if element == 1:
            break

        result.append(element)

    print(''.join(map(str, result)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Пример использования: python your_script.py <n> <m>")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        main(n, m)