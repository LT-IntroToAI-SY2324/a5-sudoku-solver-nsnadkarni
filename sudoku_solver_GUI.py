import time
import pygame
import sys

import copy
import os


sys.setrecursionlimit(1000000000)


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
            quit()
        

class board:
    def __init__(self) -> None:
        self.boardvis = [[-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
        self.boardback =[[list(range(1, 10)) for _ in range(9)] for _ in range(9)]
        self.boardsquare = [[1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3], [1, 1, 1, 2, 2, 2, 3, 3, 3], [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6], [4, 4, 4, 5, 5, 5, 6, 6, 6], [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9], [7, 7, 7, 8, 8, 8, 9, 9, 9]]
        self.selected_cell = None
        self.green = 255
        self.red = 0
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
        self.selected_cell = (row, col)
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
            self.green = 255
            self.red = 0
            self.place(ROW, COL, VAL)
        elif LEN == 0:
            self.green = 0
            self.red = 255
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
            self.green = 255
            self.red = 255
            VAL = self.boardback[ROW][COL][0]
            #print(brd)
            sta.add([copy.deepcopy(self.boardback), copy.deepcopy(self.boardvis[:]), ROW, COL, VAL, ID])
            self.place(ROW, COL, VAL)

        os.system("clear")
        screen.fill(WHITE)
        draw_grid()
        draw_selected_cell()
        draw_numbers()
        pygame.display.flip()

        # time.sleep(0.02) # Uncomment for delay in moves

        while not self.is_over():
            self.solve(sta, ID + 1)

        
pygame.init()
brd = board()
sta = stack()

WIDTH, HEIGHT = 450, 450
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

selected = None
solving = False

def draw_grid():
    for i in range(GRID_SIZE + 1):
        line_width = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), line_width)

def draw_selected_cell():
    if selected is not None:
        row, col = selected
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

def draw_numbers():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = brd.boardvis[row][col]
            if num != -1:
                if brd.selected_cell is not None and (row, col) == brd.selected_cell:
                    pygame.draw.rect(screen, (brd.red, brd.green, 0), pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                text = FONT.render(str(num), True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
                screen.blit(text, text_rect)


def solve_sudoku():
    brd.solve(sta, 0)
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not solving:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    selected = (row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    solving = True
                    solve_sudoku()
                elif selected is not None and pygame.key.name(event.key).isnumeric():
                    num = int(pygame.key.name(event.key))
                    brd.place(selected[0], selected[1], num)

    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    draw_selected_cell()
    pygame.display.flip()

pygame.quit()
sys.exit()
