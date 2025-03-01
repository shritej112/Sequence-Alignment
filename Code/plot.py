import numpy as np
import matplotlib.pyplot as plt

x_axis_basic = np.array([16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968])

# Time
# y_axis_basic = np.array([
#     1.997232,
#     1.923561,
#     2.999306,
#     6.995201,
#     14.000654,
#     24.979353,
#     50.626040,
#     93.789816,
#     149.602175,
#     203.556061,
#     370.249748,
#     599.232197,
#     818.091154,
#     1150.569439,
#     1453.704119
# ])
# y_axis_eff = np.array([
#     7.908821,
#     16.934633,
#     30.938864,
#     52.126646,
#     85.370064,
#     150.353909,
#     279.664993,
#     421.155930,
#     515.012980,
#     697.171688,
#     1149.024010,
#     1548.779726,
#     2092.076302,
#     2793.968201,
#     3447.983980
# ])

# Memory
y_axis_basic = np.array([
    32352,
    32300,
    32420,
    33032,
    33852,
    33432,
    34548,
    33692,
    34404,
    33680,
    33812,
    34540,
    34172,
    35860,
    33952
])
y_axis_eff = np.array([
    32460,
    32356,
    32612,
    32492,
    32520,
    32328,
    32444,
    32468,
    32624,
    32552,
    32744,
    32868,
    32828,
    33048,
    32908
])

plt.plot(x_axis_basic, y_axis_basic, label='Basic', marker='o', markerfacecolor='blue', markersize=5)
plt.plot(x_axis_basic, y_axis_eff, label='Efficient',  marker='o', markerfacecolor='orange', markersize=5)
plt.xlabel('Problem Size (m+n)')

# plt.ylabel('CPU Time (milliseconds)')
# plt.title('CPU Time vs Problem Size')
# plt.savefig('CPU Time.png')

plt.ylabel('Memory Usage (KB)')
plt.title('Memory Usage vs Problem Size')
plt.savefig('Memory Usage.png')

plt.legend(["Basic", "Efficient"], loc="lower right")
plt.show()