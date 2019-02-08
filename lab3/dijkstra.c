#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int* Dijkstra(int n, int st, int** w)
{
    int index, u, inf;
    int *visited = (int*)calloc(n,sizeof(int));//(1)
    int *D = (int*)calloc(n,sizeof(int));//(2)

    for(unsigned int i = 0; i < n; i++)
    {
        D[i] = w[st][i];//(3)
        visited[i] = 0;//(4)
    }

    D[st] = 0;//(5)
    index = 0;//(6)
    u = 0;//(7)

    for (unsigned int i = 0; i < n; i++)
    {
        inf = INT_MAX;//(8)
        for (unsigned int j = 0; j < n; j++)
        {
            if (!visited[j] && (D[j] < inf))//(9)
            {
                inf= D[j];//(10) 
                index = j;//(11)
            }
        }
        u = index;//(12)
        visited[u] = 1;//(13)
        for(unsigned int j = 0; j < n; j++)
        {   
            if (!visited[j] && (w[u][j] != INT_MAX) && (D[u] != INT_MAX) && (D[u] + w[u][j] < D[j]))//(14)
            {
                D[j] = D[u] + w[u][j];//(15)
            }
        }
    }
    return D;
}

int main(void)
{
    int **w = (int**)calloc(4,sizeof(int*));
    for(int i = 0; i <4; i++)
        w[i] = (int*)calloc(4,sizeof(int));
    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
            w[i][j] = INT_MAX;
    }
    w[0][1] = 2;
    w[0][2] = 11;
    w[2][3] = 6;
    w[3][1] = 9;
    
    int* result = Dijkstra(4, 0, w);

}
