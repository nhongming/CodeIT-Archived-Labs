from sys import argv
import csv


def reconstructPath(edgeTo, end, start):
    cur = edgeTo[end]
    path = []
    while True:
        if cur == start:
            break
        path.append(cur)
        cur = edgeTo[cur]

    path.reverse()
    return path


def shortestPaths(start, adjList):

    visited = {}
    edgeTo = {}

    for user in adjList:
        visited[user] = False

    queue = []
    queue.append(start)
    visited[start] = True

    while len(queue) != 0:
        v = queue.pop(0)
        adjList[v].sort()

        for dest in adjList[v]:
            if not visited[dest]:

                # TRAVERSE BY SORTED ORDER
                edgeTo[dest] = v
                queue.append(dest)
                visited[dest] = True

    result = {}
    for friend2 in edgeTo:
        if edgeTo[friend2] != -1 and edgeTo[friend2] != start:
            path = reconstructPath(edgeTo, friend2, start)
            if len(path) == 0:
                continue
            result[friend2] = path

    return result


def betweennessCentrality(adjList):

    keys = {}
    for j in adjList:
        keys[j] = shortestPaths(j, adjList)

    count = {}
    for person in adjList:
        count[person] = 0

    for user in keys:
        for names in keys[user].values():
            for name in names:
                count[name] += 1

    return count


def main():

    if len(argv) < 2:
        print("Require network file to load edges")
        return

    adjList = {}

    with open('networks/' + argv[1], "r") as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            u, v = row[0], row[1]
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            adjList[u].append(v)

    print(betweennessCentrality(adjList))


if __name__ == "__main__":
    main()
