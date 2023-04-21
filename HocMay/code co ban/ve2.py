import matplotlib.pyplot as plt
D = { 'CTTT': 60, 'Kế toán': 310, 'Kinh tế': 360, 'CNTT': 580, 'Cơ khí': 340, 'Thủy văn': 290 }
plt.bar(range(len(D)), D.values(), align='center') 
plt.xticks(range(len(D)), D.keys()) 
plt.title('Các ngành tuyển sinh của Đại học Thủy Lợi') 
plt.show()
