def stock_purchase_maximization(n, stocks_and_values, amount):
    def max_stocks(index, remaining_amount):
        if index == 0 or remaining_amount == 0:
            return 0
        if stocks_and_values[index - 1][1] > remaining_amount:
            result = max_stocks(index - 1, remaining_amount)
        else:
            include_current = stocks_and_values[index - 1][0] + max_stocks(
                index - 1, remaining_amount - stocks_and_values[index - 1][1]
            )
            exclude_current = max_stocks(index - 1, remaining_amount)
            result = max(include_current, exclude_current)
        return result
    return max_stocks(n, amount)


def read_test_cases(filename="input.txt"):
    # Initialize empty
    test_cases = []
    with open(filename, "r") as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            n = int(lines[i].strip())
            i += 1  # Next Parsed Line
            data = (
                lines[i].strip().strip("]").replace("[", "").split("], ")
            )  # String manipulation shannanigans, don't even bother
            stocks_and_values = [list(map(int, item.split(", "))) for item in data]
            i += 1  # Next Parsed Line
            amount = int(lines[i].strip())

            # Skip newLine
            i += 2

            # Finally add the data
            test_cases.append((n, stocks_and_values, amount))
    return test_cases


def main():
    # Import from input.txt
    test_cases = read_test_cases()

    # Open output.txt with w perms
    output_file = open("output.txt", "w")

    for i, (N, stocks_and_values, amount) in enumerate(test_cases, start=1):
        # Run calculation algorithm
        output = stock_purchase_maximization(N, stocks_and_values, amount)
        print(f"Test Case {i}: {output}")

        # Write to the file
        output_file.write(f"Test Case {i}: {output}\n")


if __name__ == "__main__":
    main()