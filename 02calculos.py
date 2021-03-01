import math

a = 4
b = 5
c = 1

r1 = (a+b)/2
r2 = (-b+math.isqrt(b**2-4*a*c))/(2*a)
r3 = (3*a + 2*b)/(a+b)

print(f"Resposta 01: {r1:.2f}, Resposta 02: {r2:.2f}, Resposta 03: {r3:.2f}")