

def demo():
    a = 1
    try:
        return a.ccc
    except Exception as e:
        return a


b = demo
print(b)

