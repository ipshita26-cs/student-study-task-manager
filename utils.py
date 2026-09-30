def get_non_empty_input(message):
    """Get input that cannot be empty."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_number(message):
    """Get a positive number from the user."""

    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(message):
    """Get a positive integer from the user."""

    while True:
        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Please enter a positive whole number.")

        except ValueError:
            print("Please enter a valid whole number.")


def get_mark(message):
    """Get a mark between 0 and 100."""

    while True:
        try:
            mark = float(input(message))

            if 0 <= mark <= 100:
                return mark

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")