def calculate_removed_value(bin_str, char_values):
    length = len(bin_str)
    total_removed = 0
    prev_char = None
    highest_value_idx = -1
    for idx in range(length):
        if bin_str[idx] == prev_char:
            if char_values[idx] > char_values[highest_value_idx]:
                total_removed += char_values[highest_value_idx]
                highest_value_idx = idx
            else:
                total_removed += char_values[idx]
        else:
            prev_char = bin_str[idx]
            highest_value_idx = idx
    return total_removed

bin_str = input().strip()
char_values = list(map(int, input().strip().split()))
print(calculate_removed_value(bin_str, char_values), end='')
