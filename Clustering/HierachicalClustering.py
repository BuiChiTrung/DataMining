from math import sqrt

INPUT_FILE =  "E:\Data_mining\Clustering\dataset2.txt"
TARGET_CLUSTER = 10

class HierachicalClustering():
    total_clusters = 0
    clusters = []
    points = []
    euclide_dist_matrix = []
    

    def init_from_data_file(self):
        with open(INPUT_FILE, "r") as inp_file:
            data = inp_file.readlines()
            point_id = 0
            
            for line in data:
                line = list(map(int, line.split()))
                if line == []: break

                self.total_clusters += 1
                self.clusters.append([point_id])
                self.points.append(line)

                point_id += 1

            self.calculate_dist_matrix()


    def calculate_dist_matrix(self):
        total_point =  len(self.points)
        self.euclide_dist_matrix = [[0 for i in range(total_point)] for i in range (total_point)]

        for i in range(0, len(self.points), 1):
            for j in range(0, len(self.points), 1):
                self.euclide_dist_matrix[i][j] = self.euclide_dist(i, j)


    def euclide_dist(self, id1, id2):
        ans = float(0)
        for i in range (len(self.points[id1])):
            ans += (self.points[id1][i] - self.points[id2][i]) ** 2
        return ans


    def iteration(self):
        while self.total_clusters > TARGET_CLUSTER:
            join_clusters = []
            min_dist = 1e9

            for i in range (0, len(self.clusters), 1):
                if len(self.clusters[i]) == 0: continue

                for j in range (i + 1, len(self.clusters), 1):
                    if len(self.clusters[j]) == 0: continue

                    distance = self.cluster_dist(i, j)
                    if distance < min_dist:
                        min_dist = distance
                        join_clusters = [i, j]

            print(join_clusters)
            self.join(join_clusters[0], join_clusters[1])



    def cluster_dist(self, id1, id2):
        distance = 0
        for i in self.clusters[id1]:
            for j in self.clusters[id2]:
                distance += self.euclide_dist_matrix[i][j]
        distance = distance // (len(self.clusters[id1]) + len(self.clusters[id2]))

        return distance


    def join(self, id1, id2):
        self.clusters[id1] += self.clusters[id2]
        self.clusters[id2] = []
        self.total_clusters -= 1


    def test(self):
        for cluster in self.clusters:
            if len(cluster) != 0:
                print(cluster, len(cluster))

def main():
    instance = HierachicalClustering()
    instance.init_from_data_file()
    instance.iteration()
    instance.test()


if __name__ == "__main__":
    main()