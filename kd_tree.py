import heapq

class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

class KDTree:

    def __init__(self, points):
        self.root = self.build_kdtree(points, depth=0)

    def build_kdtree(self, points, depth):
        if not points:
            return None

        k = len(points[0])
        axis = depth % k

        points.sort(key=lambda x: x[axis])
        median = len(points) // 2

        return Node(
            points[median],
            self.build_kdtree(points[:median], depth + 1),
            self.build_kdtree(points[median + 1:], depth + 1)
        )

    def find_nearest_neighbor(self, query_point):
        best_node, best_dist = self.find_nearest_neighbor_recursive(self.root, query_point, depth=0, best=None)
        return best_node

    def find_nearest_neighbor_recursive(self, current_node, query_point, depth, best):
        if current_node is None:
            return best, float('inf')

        k = len(query_point)
        axis = depth % k

        next_best = None
        next_branch = None

        if best is None or self.distance(query_point, best.point) > self.distance(query_point, current_node.point):
            next_best = current_node
        else:
            next_best = best

        if query_point[axis] < current_node.point[axis]:
            next_branch = current_node.left
        else:
            next_branch = current_node.right

        next_best, next_dist = self.find_nearest_neighbor_recursive(next_branch, query_point, depth + 1, next_best)

        if next_dist < self.distance(query_point, next_best.point):
            next_best = current_node
            next_dist = self.distance(query_point, next_best.point)

        return next_best, next_dist

    def distance(self, point1, point2):
        return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5

# Pontos de exemplo
points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (20, 10)]

# Construir a KD-tree
kdtree = KDTree(points)

# Ponto de consulta
query_point = (6, 3)

# Encontrar o ponto mais próximo
nearest_neighbor = kdtree.find_nearest_neighbor(query_point)

print("Ponto mais próximo de {}: {}".format(query_point, nearest_neighbor.point))
