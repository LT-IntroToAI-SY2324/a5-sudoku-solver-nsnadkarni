import copy
import os
import sys

sys.setrecursionlimit(10000)

class stack:
    def __init__(self) -> None:
        self.stack = []
        pass

    def add(self, boarde) -> None:
        self.stack.append(boarde)
        print()
    
    def get_del(self):
        try:
            return self.stack.pop(0)
        except:
            return "Impossible to solve!"

        

class board:
    def __init__(self) -> None:
        self.boardvis = [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
        self.boardback =[[list(range(1, 10)) for _ in range(9)] for _ in range(9)]
        self.boardsquare = [[1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3], [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6], [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9]]
        pass

    def __str__(self) -> str:
        strBuild = ""
        count1 = 0
        count2 = 0
        countR = 0

        strBuild += "    0 1 2   3 4 5   6 7 8\n"
        strBuild += "  -------------------------\n"
        for i in self.boardvis:
            strBuild += str(countR) + " | "
            countR += 1
            for x in i:
                if(x == -1):
                    strBuild += "* "
                    count1 += 1
                    count2 += 1
                else:
                    strBuild += str(x) + " "
                    count1 += 1
                    count2 += 1
                if(count2 == 3):
                    strBuild += "| "
                    count2 = 0
                if(count1 == 27):
                    strBuild += "\n  -------------------------"
                    count1 = 0
                
            strBuild += "\n"

        return(strBuild)
    
    def place(self, row, col, num):
        self.fixrow(row, num)
        self.fixcol(col, num)
        self.fixsquare(row, col, num)
        self.boardback[row][col] = num
        self.boardvis[row][col] = num


    def fixrow(self, row, num):
        try:
            for i in self.boardback[row]:
                try:
                    i.pop(i.index(num))
                except:
                    pass
        except:
            pass
    
    def fixcol(self, col, num):
        for i in range(9):
            try:
                self.boardback[i][col].pop(self.boardback[i][col].index(num))
            except:
                pass
    
    def fixsquare(self, row, col, num):
        try:
            numtosq = self.boardsquare[row][col]
            countR = -1
            countC = -1
            for i in self.boardback:
                countR += 1
                for x in i:
                    countC += 1
                    if self.boardsquare[countR][countC] == numtosq:
                        try:
                            x.pop(x.index(num))
                        except:
                            continue
                countC = -1
        except:
            pass

    def most_constrained_cell(self):
        lowest = 10
        row = 0
        col = 0
        try:
            countR = -1
            countC = -1
            for i in self.boardback:
                countR += 1
                for x in i:
                    countC += 1
                    if isinstance(x, list): 
                        if(len(x) < lowest):
                            lowest = len(x)
                            row = countR
                            col = countC
                countC = -1

            return [row, col]
        except:
            pass

    def is_over(self) -> bool:
        for i in self.boardvis:
            for x in i:
                if x == -1:
                    return False

        return True

    def solve(self, sta, ID):
        ROW = self.most_constrained_cell()[0]
        COL = self.most_constrained_cell()[1]
        print(self.most_constrained_cell())
        print(self.boardback[ROW][COL])
        try:
            VAL = self.boardback[ROW][COL][0]
        except:
            pass
        LEN = len(self.boardback[ROW][COL])
        if LEN == 1:
            self.place(ROW, COL, VAL)
        elif LEN == 0:
            e = sta.get_del()
            if isinstance(e, list):
                print(e[0])
                ROW = e[2]
                COL = e[3]
                VALDEL = e[4]
                #print(self.boardback[ROW])
                print(e)
                self.boardback = e[0]
                self.boardvis = e[1]
                #print(self.boardback[ROW])
                try:
                    self.boardback[ROW][COL].pop(self.boardback[ROW][COL].index(VALDEL))
                except:
                    print("Impossible to solve!")
            else:
                print("Impossible to solve!")
                quit()
        else:
            VAL = self.boardback[ROW][COL][0]
            #print(brd)
            sta.add([copy.deepcopy(self.boardback), copy.deepcopy(self.boardvis[:]), ROW, COL, VAL, ID])
            self.place(ROW, COL, VAL)

        os.system("clear")
        print(brd)
        while not self.is_over():
            self.solve(sta, ID + 1)

        



brd = board()
# brd.place(0, 5, 2)
# brd.place(0, 6, 1)
# brd.place(0, 8, 4)
# brd.place(1, 2, 8)
# brd.place(1, 5, 1)
# brd.place(1, 8, 3)
# brd.place(2, 0, 5)
# brd.place(2, 4, 6)
# brd.place(2, 7, 9)
# brd.place(3, 1, 9)
# brd.place(3, 4, 8)
# brd.place(3, 7, 4)
# brd.place(3, 8, 6)
# brd.place(4, 0, 6)
# brd.place(4, 3, 7)
# brd.place(5, 0, 1)
# brd.place(5, 7, 8)
# brd.place(6, 1, 3)
# brd.place(6, 2, 7)
# brd.place(6, 3, 2)
# brd.place(6, 7, 1)
# brd.place(6, 8, 9)
# brd.place(7, 7, 3)
# brd.place(8, 4, 9)
sta = stack()

def loop() -> None:
    while True:
        solve = input("Solve? (y/n):\n").lower()
        if(solve == "y"):
            print(brd.boardback)
            brd.solve(sta, 0)
            break
        row = int(input("Row?:\n"))
        col = int(input("Col?:\n"))
        num = int(input("Num?:\n"))
        brd.place(row, col, num)
        os.system("clear")
        print(brd)

        print(brd.most_constrained_cell())



loop()


