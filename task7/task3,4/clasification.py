import numpy as np

class LogisticRegression :
    def __init__(self,iterations,lr):
        self.iterations = iterations
        self.lr = lr
    

    def fit (self , x_train , y_train ) :
         
         self.m ,n = x_train.shape
         self.w = np.zeros(n + 1)
         
         x_train_new = np.hstack((np.ones(shape=(self.m , 1)),x_train))

         for i in range(self.iterations) :
             z = x_train_new @ self.w
             h = 1 / (1 + np.exp(-z))
             self.w = self.w - (self.lr/self.m)*(x_train_new.T @ (h-y_train))
 
    
    def predict (self , x_test) :
        m_test = x_test.shape[0]
        x_test_new = np.hstack((np.ones(shape=(m_test , 1)),x_test))
        z = x_test_new @ self.w
        h = 1 / (1 + np.exp(-z)) 
        
        return np.where(h >= 0.5 , 1 , 0)



             
    
