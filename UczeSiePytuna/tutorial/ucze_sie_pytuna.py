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
    def min(n1, n2):
        if(n1 < n2):
            return n1
        else:
            return n2

    @staticmethod
    def max(n1, n2):
        if(n1 > n2):
            return n1
        else:
            return n2

    @staticmethod
    def clamp(value, min = 0, max = 1):
        if(min > max):
            tmp = max
            max = min
            min = tmp

        return min(max(value, min), max)