import matplotlib
import matplotlib.pyplot as plt
import math

plt.figure()

# 単位はMKS系
m = 0.15
R = 0.075
rho = 1.293
g = 9.80665
v = 33 / 3.6
a = 9.5
b = 0.6
th = math.atan(v * v / (g * a))
# 1秒に1回転
om = 2 * math.pi
# om = 0.000013
dt = 0.0001
def calc_diff(vx, vy, eta) :
    return vx, vy, (-eta * vy), (eta * vx - g)
for i in range(6) :
    eta = 4 * math.pi * rho * (R ** 3) * om / m
    print(eta)
    A = math.sqrt(v * v - 2 * g * math.cos(th) / eta + g * g / (eta * eta))
    phi = math.atan((v * math.sin(th)) / (v * math.cos(th) - g / eta))
    if math.sin(phi) < 0 :
        phi += math.pi
    X = []
    Y = []
    x, y = 0, 0
    vx, vy = v * math.cos(th), v * math.sin(th)
    tim = 0
    cnt = 0
    # 4次ルンゲクッタ法で軌道を計算する。
    while y >= 0 and x < a + 0.1 and tim < 5.0 :
        X.append(x)
        Y.append(y)
        k1x, k1y, k1vx, k1vy = calc_diff(vx, vy, eta)
        k2x, k2y, k2vx, k2vy = calc_diff(vx + k1vx * dt / 2, vy + k1vy * dt / 2, eta)
        k3x, k3y, k3vx, k3vy = calc_diff(vx + k2vx * dt / 2, vy + k2vy * dt / 2, eta)
        k4x, k4y, k4vx, k4vy = calc_diff(vx + k3vx * dt, vy + k3vy * dt, eta)
        x += (k1x + k2x * 2 + k3x * 2 + k4x) / 6 * dt
        y += (k1y + k2y * 2 + k3y * 2 + k4y) / 6 * dt
        vx += (k1vx + k2vx * 2 + k3vx * 2 + k4vx) / 6 * dt
        vy += (k1vy + k2vy * 2 + k3vy * 2 + k4vy) / 6 * dt
        # x = (A / eta) * math.sin(eta * tim + phi) + (g * tim / eta) - (A / eta) * math.sin(phi)
        # y = -(A / eta) * math.cos(eta * tim + phi) + (A / eta) * math.cos(phi)
        # print(x, y)
    plt.plot(X, Y)
    om *= 2
plt.show()
