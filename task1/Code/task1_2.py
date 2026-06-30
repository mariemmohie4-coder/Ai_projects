
x = [50, 60, 80, 100, 120]                 ##(house size)
y = [150, 180, 240, 300, 330]              ##(price in thousands)

##Convert the data into a NumPy array.
import numpy as np
x_arr = np.array(x)
y_arr = np.array(y)

##Reshape X into a column vector.
x_col = x_arr.reshape(-1,1)

##Add a bias column of ones to X.
x_new = np.hstack([np.ones((x_col.shape[0],1)),x_col])
 

##Compute the parameter vector θ= (Xᵀ X)⁻¹ Xᵀ y 
multiply = x_new.T @ x_new
inverse = np.linalg.inv(multiply)
θ = inverse @ x_new.T @ y_arr

##Use the computed θ to predict the price of a 90 m² house 
##result ​=θ0​+90*θ1
price = θ[0] + (90 * θ[1])
print("the predicted price = ",np.round(price,3))



