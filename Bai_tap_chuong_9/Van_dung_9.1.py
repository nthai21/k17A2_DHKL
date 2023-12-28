def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
print(sign(8))  # 1
print(sign(-8))  # -1
print(sign(0))   # 0