# There are a total of n courses you have to take, labeled from 0 to n-1
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1
# which is expressed as a pair: [0,1]. Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses ?
# Example:
# Imput: 2, [[1,0]]
# output: true
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is. possible.
# Example 2: 
# Input: 2, [[1,0],[0,1]]
# output: false
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should 1
# also have finished course 1. So it is impossible.
# Note:
# 1. The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# Read more about how a graph is represented.
# 2. You may assume that there are no duplicate edges in the input prerequisites.

def dfs(numCourses, arr):
    if len(arr) == 0:
        return False
    inDegrees = numCourses * [0]
    for item in arr:
        inDegrees[item[0]] += 1
    # contain prerequisites course
    stack = []
    for i in range(0 , len(inDegrees)):
        if inDegrees[i] == 0:
            stack.append(i)
    count = 0
    while len(stack) != 0:
        count += 1
        current = stack.pop()
        for i in range(0, len(arr)):
            if arr[i][1] == current:
                arr[i][0] -= 1
                if arr[i][0] == 0:
                    stack.append(arr[i][0])
    return count == numCourses



prerequisites = [[1,0]]
print(dfs(2, prerequisites))