def devisible_by_08(num):
    if num % 8 == 0:
        print(num)
        
# Use for the questions below:
nums = [i for i in range(1,1001)]
print("Divisible by 08: ")
for num in nums:
    devisible_by_08(num)
