def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def main():
    while True:
        temp = input('Enter a temperature and its unit (e.g., "25 C" or "77 F"): ')

        try:
            value, unit = temp.split()
            value = float(value)
            unit = unit.upper()

            if unit == "C":
                print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(value):.1f} F")
            elif unit == "F":
                print(f"Temperature in Celsius: {fahrenheit_to_celsius(value):.1f} C")
            else:
                raise TypeError(f"'{unit}' is not a valid unit. Use C or F.")

        except ValueError:
            print("Invalid temperature. Enter a number and a unit, like: 25 C")
        except TypeError as error:
            print(error)
        else:
            break


if __name__ == "__main__":
    main()