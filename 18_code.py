#шебанг
if __name__ == "__main__":
    main_list = []
    size = 10
    maximum = [[0] * size for i in range(size)]
    minimum = [[0] * size for j in range(size)]
#--------------------------------------------------------------------------

    for i in range(size):
        main_list.append(list(map(int, input().split()))) #введем все в одну строку
    maximum[0][0] = main_list[0][0]
    minimum[0][0] = main_list[0][0]
    for i in range(1, size, 1):
        maximum[0][i] = maximum[0][i - 1] + main_list[0][i]
        minimum[0][i] = minimum[0][i - 1] + main_list[0][i]
    for i in range(1, size, 1):
        maximum[i][0] = maximum[i - 1][0] + main_list[i][0]
        minimum[i][0] = minimum[i - 1][0] + main_list[i][0]
    for i in range(1, size):
        for j in range(1, size, 1):
            maximum[i][j] = max(maximum[i - 1][j], maximum[i][j - 1]) + main_list[i][j]
            minimum[i][j] = min(minimum[i - 1][j], minimum[i][j - 1]) + main_list[i][j]

#----------------------------------------------------------------------------
    print(maximum[-1][-1], minimum[-1][-1])