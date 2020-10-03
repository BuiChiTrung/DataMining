import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from random import randint 
import csv 

DATA_POINT = 788
CLUSTER = 7
RANDOM_BOUND = 35

class K_Means():
    X = pd.DataFrame(columns=['x', 'y', 'label'])
    #centers = [[5, 5], [4, 4], [6, 14]]        # manual center
    #centers = [[randint(0, 20), randint(0, 20)], [randint(0, 20), randint(0, 20)], [randint(0, 20), randint(0, 20)]]
    centers = [[randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)], [randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)], [randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)], [randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)], [randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)], [randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)], [randint(0, RANDOM_BOUND), randint(0, RANDOM_BOUND)]]
    is_converged = False

    def init_data_randomly(self):
        # vị trí khởi tạo cụm
        means = [[5, 5], [10, 15], [3, 13]]

        # sử dụng ma trận hiệp phương sai để tạo các cụm dữ liệu hình tròn 
        # https://minhng.info/toan-hoc/ma-tran-hiep-phuong-sai-covariance-matrix.html
        cov   = [[1, 0], [0, 1]]

        for zlabel in range(0, 3, 1):
            cluster = pd.DataFrame(np.random.multivariate_normal(means[zlabel], cov, DATA_POINT // CLUSTER) , columns=['x', 'y'])
            cluster['label'] = -1
            self.X = self.X.append(cluster, ignore_index=True)
        #print(self.X)


    def init_data_from_file(self):
        self.X = pd.read_csv("E:\Data_mining\Clustering\dataset1.csv")
        print(self.X, type(self.X), self.X['x'])


    def display(self):
        plt.scatter(self.X['x'], self.X['y'], c = self.X['label'], alpha = 1)
        for center in self.centers:
            plt.scatter(center[0], center[1], c = 'r', marker='x', alpha = 1)
        plt.show()


    def assign_cluster(self):
        new_label = [0 for i in range (DATA_POINT)]        
        for index, row in self.X.iterrows():
            x = row['x']
            y = row['y']

            min_dist = 1e9
            for i in range(len(self.centers)):
                if float(self.dist([x, y], self.centers[i])) < min_dist:
                    min_dist = float(self.dist([x, y], self.centers[i]))
                    new_label[index] = i

        self.check_converged(new_label)


    def dist(self, point, center):
        return (point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2


    def check_converged(self, new_label):
        self.is_converged = True
        for i in range (DATA_POINT):
            if new_label[i] != self.X.iloc[i, 2]:
                self.X.iloc[i, 2] = new_label[i]
                self.is_converged = False


    def update_center(self):
        group_by_label = self.X.groupby('label')
        for (label, group) in group_by_label:
            self.centers[label] = [group['x'].mean(), group['y'].mean()]



instance = K_Means()


def main():
    
    #instance.init_data_randomly()
    instance.init_data_from_file()
    instance.display()

    k_means()
    instance.display()
    


def k_means():
    while instance.is_converged == False:
        instance.assign_cluster()
        instance.update_center()
        
    
if __name__ == "__main__":
    main()

