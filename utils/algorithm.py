def modify_segments_list(sections: list) -> list:
    sections = [[item[0]] * item[1] for item in sections]
    return [item for sublist in sections for item in sublist]


def max_sum_sequence(arr, l) -> tuple:
    n = len(arr)
    dp = [0] * (l + 1)
    choices = [[] for _ in range(l + 1)]

    for i in range(n):
        for j in range(l, arr[i] - 1, -1):
            if dp[j] < dp[j - arr[i]] + arr[i]:
                dp[j] = dp[j - arr[i]] + arr[i]
                choices[j] = choices[j - arr[i]] + [arr[i]]

    return tuple(choices[l])


def update_segments(arr: list, l: int) -> list[list[tuple[int], int]]:
    result: list[list[tuple[int], int]] = []
    while True:
        optimal_sequence: tuple[int] = max_sum_sequence(arr, l)
        remainder: int = l - sum(optimal_sequence)
        result.append([optimal_sequence, remainder])
        for item in optimal_sequence:
            arr.remove(item)
        if len(arr) == 0:
            return result


def get_optimal(length: int, segments: list[list[int,int]]) -> list[list[tuple[int], int]]:
    length: int = length
    segments: list[int] = modify_segments_list(segments)
    optimal_values: list[list[tuple[int], int]] = update_segments(segments, length)
    return optimal_values
