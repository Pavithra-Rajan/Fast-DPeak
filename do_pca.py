import numpy as np

from sklearn.preprocessing import StandardScaler
def featurescaling(df):
	sc=StandardScaler()
	sc.fit(df)
	return sc.transform(df)
def pca(X,reduced_cols_cnt):
    #getting colwise mean for the input data and subtracting it from original input data
    mean_x= np.mean(X , axis = 0)
    x_avg_mod = X - mean_x

    #getting covariance matrix
    cov_mat = np.cov(x_avg_mod , rowvar = False)

    #finding eigen values and eigen vectors
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
    

    #sorting by eigen values in non increasing order
    sorted_index = np.argsort(eigen_values)[::-1]

    sorted_eigenvalue = eigen_values[sorted_index]
    #sorting eigen vectors
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
    
    #considering the first reduced_cols_cnt columns 
    eigenvector_subset = sorted_eigenvectors[:,0:reduced_cols_cnt]
    return np.dot(eigenvector_subset.transpose(),x_avg_mod.transpose()).transpose()