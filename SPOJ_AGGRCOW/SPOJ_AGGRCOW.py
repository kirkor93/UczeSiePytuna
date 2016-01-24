import math

t = int(input("Enter the number of cases: "))

for i in range(t):
    nc = input("""Enter N and C formatted "N C": """).split()
    n = int(nc[0])
    c = int(nc[1])
    locations = []
    for i in range(n):
        locations.append(int(input("Enter location position: ")))

    locations.sort()

    min_distance = locations[len(locations) - 1] - locations[0]
    target_distance = math.ceil(min_distance/c)

    last_left = 1
    last_right = len(locations) - 2

    for i in range(c - 2):
        l_index = last_left
        l = 0
        while l <= target_distance:
            l = locations[l_index] - locations[last_left]
            l_index += 1

        l_index -= 1
        l -= locations[l_index] - locations[l_index - 1]

        r_index = last_right
        r = 0
        while r <= target_distance:
            r = locations[last_right] - locations[r_index]
            r_index -= 1

        r_index += 1
        r -= locations[r_index + 1] - locations[r_index]

        if target_distance - l > target_distance - r:
            min_distance = r
            last_right = r_index + 1
        else:
            min_distance = l
            last_left = l_index - 1

    print(min_distance)