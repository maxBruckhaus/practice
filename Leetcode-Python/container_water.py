def max_area_cubic(height):
    max_area = 0

    for i in range(len(height)):
        for j in range(1, height[i] + 1):
            # find longest height to the right of i
            for z in range(len(height)-1, i, -1):
                if height[z] >= j:
                    area = j * (z - i)
                    if area > max_area:
                        max_area = area
                    break
    return max_area


def max_area_linear(height):
    max_area = 0
    l = 0
    r = len(height) - 1

    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == '__main__':
    h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area_cubic(h1))

    h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area_linear(h1))
