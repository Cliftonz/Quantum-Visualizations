from scipy import constants
import math

h = constants.value(u'reduced Planck constant')
pi2 = math.pow(math.pi, 2)

Final = ((2 * pi2 + 3)/(2 * pi2 - 3))

c1 = .5 * math.sqrt((6 * pi2)/(2*pi2-3))


def cn(nput):
    t1 = (1/pi2)
    t2 = math.sqrt((24 * pi2) / (2*pi2-3))
    t3 = ((1/math.pow(nput-1, 2)) - (1/math.pow(nput+1, 2)))
    temp = math.pow(t1 * t2 * t3, 2) * math.pow(nput, 2)
    return temp


print("Final answer should be: " + str(Final))

ans = c1
for i in range(2, 20, 2):
    ans += cn(i)

print("Approximation is: " + str(ans))

print("The difference is " + str(ans-Final))

print("The percent difference is " + str(math.fabs((Final - ans)/((Final+ans)/2))*100))

