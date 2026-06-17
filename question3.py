def analyze_numbers(lst):
    even_count = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_sum += num

    return even_count, odd_sum

numbers = [1, 2, 3, 4, 5, 6]
even, odd = analyze_numbers(numbers)

print("Even Count =", even)
print("Odd Sum =", odd)
