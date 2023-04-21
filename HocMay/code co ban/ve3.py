import matplotlib.pyplot as plt
D = { 'CTTT': 60, 'Kế toán': 310, 'Kinh tế': 360, 'CNTT': 580, 'Cơ khí': 340, 'Thủy văn': 290 }
plt.pie(D.values(), labels=D.keys(), autopct='%1.1f%%') 
plt.axis('equal') # trục x = trục y
plt.show()
