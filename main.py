import matplotlib.pyplot as plt
import numpy as np


v_taxi = 45
v_0 = v_taxi

km_into_meters = 1000./3600.


S_max = 460
t_max = S_max / (v_taxi * km_into_meters)

print( 'Maximum time = ', t_max)

l_taxi = 4.38
distance = 10

l = l_taxi + distance

t = np.linspace(0, t_max + 10, 1000)
delta_t = t[1]-t[0]
v = np.ones(len(t)) * v_taxi

a = 2 * (l + S_max - v_0 * km_into_meters * t_max) / (t_max**2)
print("Acceleration = ", a)

V_find  =  v_0 + (a * t)/km_into_meters
plt.plot(t, v)
plt.plot(t, V_find)
plt.xlabel("t, s")
plt.ylabel("velocity, km/h")
plt.ylim(v_0 - 5, v_0 + 50)
plt.xlim(0, t_max + 10)
plt.axvline(x=t_max)
plt.show()

print("Max speed = ", V_find[int(t_max / delta_t)])

S_taxi = np.zeros(len(t))
S_taxi = km_into_meters * v_taxi * t


plt.plot(t,S_taxi)
plt.plot(t,v_0 * km_into_meters * t + a * t**2/2)
plt.xlabel("t, s")
plt.ylabel("L, m")
plt.ylim(0, S_max + 100)
plt.xlim(0, t_max + 10)
plt.axvline(x=t_max)
plt.show()
