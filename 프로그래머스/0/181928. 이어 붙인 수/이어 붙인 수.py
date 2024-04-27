def solution(num_list):
    odd_sum = "".join(str(num) for num in num_list if num % 2 != 0)
    even_sum = "".join(str(num) for num in num_list if num % 2 == 0)
    return int(odd_sum) + int(even_sum)