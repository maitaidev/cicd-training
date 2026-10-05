def greet(name):
    return f"Привет, {name}!"


def is_even(n):
    return n % 2 == 0


def main():
    name = input("Как тебя зовут? ")
    print(greet(name))

    numbers = [1, 2, 3, 4, 5]
    for n in numbers:
        kind = "чётное" if is_even(n) else "нечётное"
        print(f"{n} — {kind}")

    total = sum(numbers)
    print(f"Сумма: {total}")


if __name__ == "__main__":
    main()
    
