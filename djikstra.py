import heapq



def dijkstra(start, end):
    graph = {
                'Gate' : {'Logik' : 1.5, 'FCSE' : 3.3, 'Admin' : 1.2},
                'Logik' : {'Gate' : 1.5, 'GuestHouse' : 1.8},
                'Admin' : {'Gate' : 1.2, 'SportsGround' : 2.4},
                'GuestHouse' : {'Logik' : 1.8, 'Tuc' : 5.2},
                'SportsGround' : {'SportsComplex' : 2.2, 'Admin' : 2.4, 'H9' : 1.4},
                'Tuc' : {'GuestHouse' : 5.2, 'TransportOffice' : 0.9, 'MedicalCentre' : 4.4},
                'SportsComplex' : {'SportsGround' : 2.2, 'H10' : 1.7},
                'MedicalCentre' : {'Tuc' : 4.4, 'GirlsHostel' : 2.5, 'FMCE' : 7.04},
                'H10' : {'SportsComplex' : 1.7, 'H9' : 1.49, 'H2' : 0.2},
                'H9' : {'SportsGround' : 1.4, 'H10' : 1.49, 'H1' : 0.3},
                'H1' : {'H9' : 0.3, 'H2': 1.5, 'H3' : 4, 'Mosque' : 2.3}, 
                'H2' : {'H10' : 0.2, 'H4' : 5.7, 'H1' : 1.5}, 
                'H3' : {'H4' : 1.59, 'H1' : 4, 'H5' : 0.4, 'Mosque' : 2.8},
                'H4' : {'H2' : 5.7, 'H3' : 1.59, 'H6' : 0.5},
                'H5' : {'H6' : 1.6, 'H3' : 0.4, 'H8' : 1.82},
                'H6' : {'H5' : 1.6, 'H4' : 0.5},
                'H11' : {'H8' : 1.68, 'H12' : 0.8},
                'H8' : {'H11' : 1.68, 'AcademicBlock' : 2.7, 'H5' : 1.82},
                'H12' : {'H11' : 0.8, 'AcademicBlock' : 2.9},
                'AcademicBlock' : {'H12' : 2.9, 'H8' : 2.7, 'FES' : 1.72, 'Auditorium' : 0.58, 'Library' : 2.18},
                'Mosque' : {'H3' : 2.8, 'H1' : 2.3, 'FES' : 3.6},
                'FES' : {'Mosque' :  3.6, 'AcademicBlock' : 1.72, "FCSE" : 1.3, 'Auditorium' : 1.76},
                'FCSE' : {'FES' :  1.3,'FME' : 1, 'Gate' : 3.3},
                'FME' : {'FMCE' : 1.94, 'FCSE' : 1},
                'FMCE' : {'MedicalCentre' : 7.04, 'FME' : 1.94, 'BrabersBuilding' : 3.86, 'Auditorium' : 2.06},
                'BrabersBuilding' : {'FMCE' : 3.86, 'Library' : 2.75, 'GirlsHostel' : 2, 'FacultyClub' : 5},
                'Library' : {'AcademicBlock' :  2.18, 'Auditorium' : 1.81, 'BrabersBuilding' : 2.75},
                'Auditorium' : {'AcademicBlock' : 0.58, 'FES' : 1.76, 'Library' : 1.81, 'FMCE' : 2.06}, #31 lOCATIONS
                'TransportOffice' : {'Tuc' : 0.9},
                'GirlsHostel' : {'BrabersBuilding' : 2, 'MedicalCentre' : 2.5},
                'FacultyClub' : {'BrabersBuilding' : 5}
                }

    # Set up a priority queue with (distance, node) as the elements
    pq = [(0, start)]
    # Set up a dictionary to store the distance from the start node to each node
    distances = {}
    # Set up a dictionary to store the previous node in the shortest path to each node
    prev = {}
    # Initialize the distances and previous nodes
    for node in graph:
        distances[node] = float('inf')
        prev[node] = None
    # The distance from the start node to itself is 0
    distances[start] = 0
    # While there are nodes in the priority queue
    while pq:
        # Pop the node with the smallest distance from the queue
        distance, node = heapq.heappop(pq)
        # If we have reached the end node, return the distance and the path
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = prev[node]
            return distance, list(reversed(path))
        # If we have not reached the end node, check the neighbors
        for neighbor in graph[node]:
            # Calculate the distance to the neighbor through the current node
            alt = distance + graph[node][neighbor]
            # If the distance to the neighbor through the current node is shorter than the current distance, update the distance and the previous node
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                prev[neighbor] = node
                # Push the neighbor onto the priority queue
                heapq.heappush(pq, (alt, neighbor))
    # If we have exhausted the priority queue and have not reached the end node, there is no path
    return float('inf'), []



