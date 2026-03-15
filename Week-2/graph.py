class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dic = {}
        for start, end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start] = [end]
        print("Graph dict:", self.graph_dic)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        # Base Case: We found the destination
        if start == end:
            return [path]

        # If the city has no outgoing flights
        if start not in self.graph_dic:
            return []

        paths = []
        for node in self.graph_dic[start]:
            if node not in path: # Avoid infinite loops (cycles)
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
       

    def shortest_path(self, start, end, path=[]):
     path = path + [start]

    # Base case: We found it!
     if start == end:
        return path

    # If the city isn't in our map, we can't go anywhere from here
     if start not in self.graph_dic:
        return None

     shortest = None
     for node in self.graph_dic[start]:
        if node not in path:
            # We call shortest_path (this function), NOT get_paths
            sp = self.shortest_path(node, end, path)
            if sp:
                # If we haven't found a path yet, OR this new one is shorter
                if shortest is None or len(sp) < len(shortest):
                    shortest = sp
                    
     return shortest



      
if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"
    print(f"Shortest Paths between {start} and {end}:", route_graph.shortest_path(start, end))