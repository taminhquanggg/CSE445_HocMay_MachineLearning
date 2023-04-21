import numpy as np
def predict(w, X):
#dự đoán nhãn của mỗi hàng X, cho trước w
# X: mảng hình dạng numpy 2-d (N, d), mỗi hàng là một điểm dữ liệu
# w_init: mảng 1-d có hình dạng (d))
    return np.sign(X.dot(w))
# hàm predict(w, X) dự đoán nhãn của mỗi hàng của X dựa trên công thức,cho trước w (13.2).
# Hàm perceptron(X, y, w_init) thực hiện thuật toán PLA với tập dữ liệu X, nhãn y và nghiệm
# ban đầu w_init.

def perceptron(X, y, w_init):
#thực hiện thuật toán học perceptron
# X: mảng hình dạng numpy 2-d (N, d), mỗi hàng là một điểm dữ liệu
# y: mảng 1-d có hình dạng (N), nhãn của mỗi hàng X. y [i] = 1 / -1
# w_init: mảng 1-d có hình dạng (d)
    w = w_init
    while True:
        
        pred = predict(w, X) # hàm nhận kq dấu dự đoán theo w
        print('y dư đoán',pred)
        print('y thực tế',y)
        # tìm chỉ mục của các điểm bị phân loại sai
        mis_idxs = np.where(np.equal(pred, y) == False)[0]#pred:dấu dự đoán,y dấu thực tế
        # số điểm phân loại sai
        num_mis = mis_idxs.shape[0]#xét có điểm nào gắn nhãn sai k thì hàm mis_idxs=0
        if num_mis == 0:# không còn điểm phân loại sai
            return w
        # chọn ngẫu nhiên một điểm bị phân loại sai
        random_id = np.random.choice(mis_idxs, 1)[0]
        # cập nhật w
        w = w + y[random_id]*X[random_id] 
    
means = [[-1, 0], [1, 0]] #vector kỳ vọng được lưu trong means.
cov = [[.3, .2], [.2, .3]] #ma trận hiệp phương sai cov  
N = 10
X0 = np.random.multivariate_normal(means[0], cov, N)#Vẽ mẫu ngẫu nhiên từ phân phối chuẩn đa biến.
X1 = np.random.multivariate_normal(means[1], cov, N)
X = np.concatenate((X0, X1), axis = 0)#Nối một chuỗi các mảng dọc theo một trục hiện có.
y = np.concatenate((np.ones(N), -1*np.ones(N)))
Xbar = np.concatenate((np.ones((2*N, 1)), X), axis = 1)
w_init = np.random.randn(Xbar.shape[1])#Trả lại một mẫu (hoặc các mẫu) từ phân phối "chuẩn thông thường".

w = perceptron(Xbar, y, w_init)
print('w=',w)
