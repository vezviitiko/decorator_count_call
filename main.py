def f():
    return 1


def counted(limit):
    print(counted.call_count)
    if counted.call_count > limit:
        raise ValueError("exceeding the allowed function limit")
    else:
        counted.call_count += 1
        return f()
    

counted.call_count = 0

print(counted(4))
print(counted(4))
print(counted(4))
print(counted(4))
print(counted(4))
print(counted(4))
