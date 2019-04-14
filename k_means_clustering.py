import numpy as np

#Function to take in some d dimensional data set and an integer k and return classifications of points and the cluster means
def k_means(data,num_clusters,showIter):

    #Initialize means
    means = init_means(data,num_clusters)
    old_means = np.zeros((num_clusters,len(data[0])))

    r = np.zeros((len(data),num_clusters))
    iterations = 0
    #repeat
    while(not converged(means,old_means)):
        iterations+=1
        #E Step
        r = np.zeros((len(data),num_clusters))
        for n in range(len(data)):
            dist = np.zeros((num_clusters))
            for k in range(num_clusters):
                dist[k] = (np.linalg.norm(data[n] - means[k]))**2
            r[n][np.argmin(dist)] = 1

        #M Step
        old_means = np.copy(means)
        for k in range(num_clusters):
            sum = 0
            for n in range(len(data)):
                sum += r[n][k]*data[n]
            #means[k] = np.sum(r[:,k]*data)/np.sum(r[:,k])
            means[k] = sum/np.sum(r[:,k])

        if(showIter):print("Iteration: " + str(iterations))

    print("Iterations: " + str(iterations) + " --- Objective Function Value: " + str(objective_function(data,means,r)))
    return means, r

#check equality of means - equal once data ceases being classified differently
def converged(means,old_means):
    return(np.array_equal(means,old_means))

#Function measuring effectiveness of cluster placement - Sum of square distances to assigned means
def objective_function(data,means,indicators):
    J = 0.0
    for n in range(len(data)):
        for k in range(len(means)):
            J += indicators[n][k]*(np.linalg.norm(data[n] - means[k]))**2
    return J

#Initialize the k means to k unique points in the data set
def init_means(data,num_clusters):
    means = np.zeros((num_clusters,len(data[0])))
    for k in range(num_clusters):
        val = np.random.randint(0,len(data))
        point = data[val]
        while point in means:
            val = np.random.randint(0,len(data))
            point = data[val]
        means[k] = point

    return means

#Generate a dataset of points sampled from a variety of normal Distributions
def generate_dataset(means):
    #import matplotlib.pyplot as plt
    cov = [[1, 0], [0, 1]]

    data = np.zeros((200*len(means),2))
    for i in range(0,len(data),len(means)):
        for k in range(len(means)):
            data[i+k] = np.random.multivariate_normal(means[k], cov)

    return data

#Plot objective function wrt different choices of K clusters
def graph_obj_func(plt):
    plt.subplot(1,2,2)
    plt.title("Distortion Measure vs. Cluster Choice")
    plt.ylabel("Distortion Measure")
    plt.xlabel("Number of Clusters")
    J = []
    for i in range(1,8):
        means, indicators = k_means(data,i,False)
        J.append(objective_function(data,means,indicators))
    plt.plot(np.arange(1,8),J,color = 'black')
    plt.show()

#Plot dataset and means, color coding for classification
def graph_data(plt,distr_means, data, means):
    plt.subplot(1,2,1)
    plt.title("K = " + str(k) + " with " +str(len(distr_means)) + " Distributions")
    colors = ['red','blue','green','yellow','orange','purple','pink','brown']
    for n in range(len(data)):
        plt.plot(data[n][0],data[n][1],'x',color = colors[int(np.argmax(indicators[n]))])

    for i in range(0,k):
        plt.plot(means[i][0],means[i][1],'X',color = 'black')
    plt.axis("equal")


#MAIN
if __name__ == "__main__":
    k = 6
    distr_means = [[4, 4],[-4,-4],[4,-4],[-4,4]]
    data = generate_dataset(distr_means)
    means, indicators = k_means(data,k,False)

    #plotting
    import matplotlib.pyplot as plt
    graph_data(plt, distr_means, data, means)
    graph_obj_func(plt)
