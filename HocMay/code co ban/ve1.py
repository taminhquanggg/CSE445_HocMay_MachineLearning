import numpy as np                 # thư viện numpy 
import matplotlib.pyplot as plt    # thư viện pyplot
# chia đoạn từ 0 đến 3 thành các đoạn con 0.1 
x = np.arange(0, 3 * np.pi, 0.1) # tính sin tương ứng với từng phần tử của x 
y = np.sin(x)
# vẽ biểu đồ tương quan giữa x và y 
plt.plot(x, y) # hiển thị biểu đồ 
plt.show()
