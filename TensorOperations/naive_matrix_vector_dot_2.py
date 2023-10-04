def naive_matrix_vector_dot(x, y):
    z = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
            z[i] = naive_matrix_vector_dot(x[i,:], y)
    return z






#                                                                              .