
def findSimilar(query, database):
    points = []
    for each in database:
        point = calculatePoint(query, each)
        print point
        points.append(point)
    i = points.index(max(points))

# cool visualization
# sort the points list then visualize how good a match is by 
# caluculating points/len(query) and color green/yellow/red

    return database[i]

def calculatePoint(query, each):
    point = 0
    for i in range(len(query)):
        char = query[i]
        if char in each:
            point += 1
    return point

database = ['naruto', 'bleach', 'claymore', 'shingeki-no-kyojin']

findSimilar('shingeki no kyojin', database)




