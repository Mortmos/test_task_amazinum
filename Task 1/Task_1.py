import random
import matplotlib.pyplot as plt


def main():
    peaks = [random.randint(0, 26) for _ in range(26)]

    max_depth = 0
    deepest_idx = -1
    target_water_level = 0

    for i in range(len(peaks)):
        l_max = max(peaks[:i + 1])
        r_max = max(peaks[i:])
        water_level = min(l_max, r_max)

        depth = water_level - peaks[i]
        if depth > max_depth:
            max_depth = depth
            deepest_idx = i
            target_water_level = water_level

    if deepest_idx == -1 or max_depth == 0:
        plt.plot(range(26), peaks, marker='o')
        plt.show()
        return

    l_ws_i = deepest_idx
    while l_ws_i > 0 and peaks[l_ws_i] < target_water_level:
        l_ws_i -= 1

    r_ws_i = deepest_idx
    while r_ws_i < len(peaks) - 1 and peaks[r_ws_i] < target_water_level:
        r_ws_i += 1

    bottom = peaks[deepest_idx]
    upper_bound = min(peaks[l_ws_i], peaks[r_ws_i])

    print ('List of peaks:', peaks)
    print('Depth of the deepest lake:', max_depth)

    plt.figure(figsize=(10, 5))
    x = list(range(26))

    plt.plot(x, peaks, marker='o', color='tab:blue')

    plt.plot(x[l_ws_i:r_ws_i + 1], peaks[l_ws_i:r_ws_i + 1], color='red', marker='o')

    plt.axhline(y=upper_bound, linestyle="--", color="green")
    plt.axhline(y=bottom, linestyle="--", color="green")

    plt.xticks(x)
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == '__main__':
    main()