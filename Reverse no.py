num = 1234567
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10           
    reversed_num = reversed_num * 10 + digit  
    num = num // 10             
print(f"Original number: {original_num}")
print(f"Reversed number: {reversed_num}")
