from scipy import constants
import math

h = constants.value(u'reduced Planck constant')
pi2 = math.pow(math.pi, 2)
mass = 1
a = 1
omega = (pi2 * h) / (2 * mass * math.pow(a, 2))

Final = ((2 * pi2 + 3)/(2 * pi2 - 3)) * h * omega

c1 = .5 * math.sqrt((6 * pi2)/(2*pi2-3))


def cn(nput):
    t1 = -(1/pi2)
    t2 = math.sqrt((24 * pi2) / (2*pi2-3))
    t3 = ((1/math.pow(nput-1, 2)) - (1/math.pow(nput+1, 2)))
    temp = t1 * t2 * t3
    return temp


print("Final answer should be: " + str(Final))

ans = c1
for i in range(2, 10000, 2):
    ans += cn(i)

print("Approximation is: " + str(ans))

