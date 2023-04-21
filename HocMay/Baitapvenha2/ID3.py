from __future__ import print_function
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.tree as tr
import matplotlib.pyplot as pl
from PIL import Image
import csv

# class TreeNode(object):
#     def __init__(self, ids = None, children = [], entropy = 0, depth = 0):
#         self.ids = ids           # chỉ mục dữ liệu trong nút này
#         self.entropy = entropy   # entropy, sẽ điền sau
#         self.depth = depth       # khoảng cách đến nút gốc
#         self.split_attribute = None # thuộc tính nào được chọn, nó không phải là lá
#         self.children = children # danh sách các nút con của nó
#         self.order = None       # thứ tự các giá trị của split_attribute ở con
#         self.label = None       # nhãn của nút nếu nó là một lá

#     # sau khi tính đc entropy của các thuộc tính thì sắp xếp
#     def set_properties(self, split_attribute, order):
#         self.split_attribute = split_attribute# phân tách tại thuộc tính nào
#         self.order = order# thứ tự trong số các nút con của nút này

#     def set_label(self, label):
#         self.label = label# đặt nhãn nếu nút là một lá


# def entropy(freq):#Hàm tính entropy dựa trên tần suất
#     # loại bỏ xác xuất 0 Trong hàm này, chúng ta phải chú ý bỏ các tần suất bằng 0 đi vì logarit tại đây không xác định.
#     freq_0 = freq[np.array(freq).nonzero()[0]]
#     prob_0 = freq_0/float(freq_0.sum())
#     return -np.sum(prob_0*np.log(prob_0))

# class DecisionTreeID3(object):#xây dựng cây
#     def __init__(self, max_depth= 10, min_samples_split = 2, min_gain = 1e-4):
#         self.root = None # nút gốc
#         self.max_depth = max_depth  # độ sâu tối đa
#         self.min_samples_split = min_samples_split # số lượng các mẫu tối thiểu mỗi nốt
#         self.Ntrain = 0 # khởi tạo ban đầu mẫu huấn luyện
#         self.min_gain = min_gain # Hàm đánh giá lợi nhuận tối thiểu
    
#     def fit(self, data, target):
#         self.Ntrain = data.count()[0]
#         self.data = data 
#         self.attributes = list(data)
#         self.target = target 
#         self.labels = target.unique()
        
#         ids = range(self.Ntrain)# từ nút gốc ban đầu gồm tất cả dl trg tập huấn luyện
#         #Treenode tìm và lựa chọn ra tập thuộc tính tốt nhất treenode để làm root 
#         self.root = TreeNode(ids = ids, entropy = self._entropy(ids), depth = 0)# từ nut gốc xây dựng cây con
#         queue = [self.root]# danh sách các giá trị thuộc tính đc chọn
#         while queue:# xây dựng nhánh con từ nút gốc(48-56)
#             node = queue.pop() 
#             if node.depth < self.max_depth or node.entropy < self.min_gain: # xét độ sâu và giá trị entropy có đạt ngưỡng
#                 node.children = self._split(node)# gán nút con 
#                 if not node.children:#cuống lá
#                     self._set_label(node)
#                 queue += node.children
#             else:
#                 self._set_label(node)
                
#     def _entropy(self, ids):
#         # tính toán entropy của một nút với id chỉ mục
#         if len(ids) == 0: return 0
#         ids = [i+1 for i in ids] # chỉ mục chuỗi gấu trúc bắt đầu từ 1
#         freq = np.array(self.target[ids].value_counts())
#         return entropy(freq)

#     def _set_label(self, node):
#         # tìm nhãn cho một nút nếu nó là một lá
#         # chỉ được chọn bằng cách bỏ phiếu chính
#         target_ids = [i + 1 for i in node.ids]  # target là một biến chuỗi
#         node.set_label(self.target[target_ids].mode()[0]) # nhãn thường gặp nhất
    
#     def _split(self, node):#tách
#         ids = node.ids 
#         best_gain = 0
#         best_splits = []
#         best_attribute = None
#         order = None
#         sub_data = self.data.iloc[ids, :]
#         for i, att in enumerate(self.attributes):#;iệt kê
#             values = self.data.iloc[ids, i].unique().tolist()
#             if len(values) == 1: continue # entropy = 0
#             splits = []
#             for val in values: 
#                 sub_ids = sub_data.index[sub_data[att] == val].tolist()
#                 splits.append([sub_id-1 for sub_id in sub_ids])
#             # không tách nếu một nút có số điểm quá nhỏ
#             if min(map(len, splits)) < self.min_samples_split: continue
#             # information gain
#             HxS= 0
#             for split in splits:
#                 HxS += len(split)*self._entropy(split)/len(ids)
#             gain = node.entropy - HxS 
#             if gain < self.min_gain: continue # dừng lại nếu lợi nhuận nhỏ
#             if gain > best_gain:
#                 best_gain = gain 
#                 best_splits = splits
#                 best_attribute = att
#                 order = values
#         node.set_properties(best_attribute, order)# tính chất
#         child_nodes = [TreeNode(ids = split,
#                      entropy = self._entropy(split), depth = node.depth + 1) for split in best_splits]
#         return child_nodes

#     def predict(self, new_data):
#         #param new_data: khung dữ liệu mới, mỗi hàng là một điểm dữ liệu
#         npoints = new_data.count()[0]
#         labels = [None]*npoints
#         for n in range(npoints):
#             x = new_data.iloc[n, :] # 1 điểm
#             # tuốt từ gốc và du hành đệ quy nếu không gặp lá 
#             node = self.root
#             while node.children: 
#                 node = node.children[node.order.index(x[node.split_attribute])]
#             labels[n] = node.label
            
#         return labels #return: các nhãn được dự đoán cho mỗi hàng



# lb = DecisionTreeID3()

df = pd.read_excel('test.xlsx')
# X = df.iloc[:, :-1]#cung cấp vectơ hàng của các giá trị của cột cuối cùng
# y = df.iloc[:, -1]

# xtrain, xtest, ytrain, ytest = train_test_split(X,y,train_size=0.7, shuffle = False)
# print(xtest)
# tree = lb(max_depth = 4, min_samples_split = 2)
# tree.fit(xtrain,ytrain)
# data = tree.predict(xtest)
# y_test = np.array(ytest)
# dem = 0
# for i in range(len(data)):
# 	if(data[i] == y_test[i]):
# 		dem = dem + 1
# 	print('Dự đoán [', data[i], '] Thực tế là [', y_test[i], ']\n')
# print("Thuật toán ID3 dự đoán đúng được ",dem,' giá trị trên tổng số ',len(data))
