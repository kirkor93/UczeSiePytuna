class Math:
    "Test documentation for math class"

    @staticmethod
    def pow(n):
        if n < 0:
            return None
        else:
            i = 1
            for a in range(1, n + 1, 1):
                i *= a
            return i

    @staticmethod
    def min(n1, n2, *numbers):
        selected_number = n1 if n1 < n2 else n2
        for n in numbers:
            if n < selected_number:
                selected_number = n

        return selected_number

    @staticmethod
    def min(iterable):
        selected_number = iterable[0]
        for n in iterable:
            if n < selected_number:
                selected_number = n

        return selected_number

    @staticmethod
    def max(*numbers):
        if numbers is None:
            return None

        selected_number = numbers[0]
        for n in numbers:
            if n > selected_number:
                selected_number = n

        return selected_number

    @staticmethod
    def clamp(value, min = 0, max = 1):
        if(min > max):
            tmp = max
            max = min
            min = tmp

        return min(max(value, min), max)