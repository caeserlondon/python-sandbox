"""Module providing a function printing high score without the MAX()"""

INP = "78 65 89 86 55 91 64 89"

n_list = INP.split()
# MAX_NUM = 0
print(n_list)


# for NUMB in num_list:

#     if int(NUMB) > MAX_NUM:
#         MAX_NUM = int(NUMB)

num_list = [int(n) for n in n_list]
MAX_NUM = num_list[0]

for n in num_list:
    if n > MAX_NUM:
        MAX_NUM = n

print(f"The highest score in the list is: {MAX_NUM}")
