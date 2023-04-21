import pandas as pd
import numpy as np
 
A = pd.read_csv("test.csv")
A.head
print(A)

# Phan tich hoi quy
from sklearn import linear_model
clf = linear_model.LinearRegression()
 
# Tạo dataframe chỉ chứa data làm biến giải thích
X1 =A.drop("d", axis=1)
X=X1
 
# Sử dụng quality làm biến mục tiêu
Y = A['d']
 
# Tạo model
clf.fit(X, Y)
 
# Hệ số hồi quy
print(pd.DataFrame({"Name":X1.columns,
                    "Coefficients":clf.coef_}).sort_values(by='Coefficients') )
 
# Sai số
print(clf.intercept_)

