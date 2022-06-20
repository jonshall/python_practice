class Solution(object):
    def MinDistance(self, word1, word2):
        n = len(word1)+1
        m = len(word2)+1
        dist = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(0,n):
            dist[i][0] = i
        
        for j in range(0,m):
            dist[0][j] = j
        
        for i in range(1,n):
            for j in range(1,m):
                if word1[i-1] == word2[j-1]:
                    dist[i][j] = dist[i-1][j-1]
                else:
                    dist[i][j] = 1 + min(dist[i-1][j-1], dist[i-1][j], dist[i][j-1])
        
        return dist[n-1][m-1]
