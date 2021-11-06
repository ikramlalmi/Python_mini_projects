test_cases = int(input("please enter the number of test cases: "))

def max_border(tc):

    for _ in range(tc):
        # get the number of rows and columns
        m, n = map(int, input("Please enter the number of rows and columns: "). strip().split())
        # need to get the shape input
        array = [list(input("enter your shape: ")) for i in range(m)]


        border_list = []

        for i in range(0,m):
            top, bottom = 0, 0
            topMax , BottomMax = top, bottom
            # if there is only one row in the matrix
            if m==1 :
                border_list.append(str(array[i].count("#")))
                break

            for j in range(0,n):
                # first row top border
                if i == 0 and array[i][j]== '#' and m!=1:
                    top+=1
                    if array[i+1][j] == ".":
                        bottom+=1
                    elif bottom>BottomMax: 
                        BottomMax = bottom
                        bottom = 0
                elif i == 0 and j==n-1:
                    if bottom>BottomMax: BottomMax = bottom
                    border_list.append(max([BottomMax, top]))

                # last row bottom border
                if i== m-1 and array[i][j]== '#' and m!=1:
                    bottom+=1
                    if array[i-1][j] == ".":
                        top+=1
                    elif top>topMax: 
                        topMax = top
                        top = 0
                elif i == m-1  and j==n-1:
                    if top>topMax: topMax = top
                    border_list.append(max([topMax, bottom]))

                # remaining rows: third case
                if i!= m-1 and i!=0 and array[i][j]== '#' and m!=1:
                    if array[i+1][j] == ".":
                        bottom+=1
                    elif bottom>BottomMax: 
                        BottomMax = bottom
                        bottom = 0
                    if array[i-1][j] == ".":
                        top+=1
                    elif top>topMax: 
                        topMax = top
                        top = 0
                elif i != m-1 and i!=0 and j==n-1:
                    if top>topMax: topMax = top
                    if bottom>BottomMax: BottomMax = bottom
                    border_list.append(max([topMax, BottomMax]))

        print(max(border_list))


max_border(test_cases)






  