a = 1
b = 1
fi = [a, b]
for i in range(20):
    a, b = b, a+b
    fi.append(b)
print(fi)
