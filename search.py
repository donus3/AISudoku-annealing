from table import Table
from tree import Tree
import random
import math

class Search:
    
    def __init__(self, filePath='easy1'):
        self.table = Table(filePath+'.csv')

    def getblanknodes(self, table):
        temp = {}
        irow = 0
        for row in table.table:
            icol = 0
            temp[irow] = []
            for col in row:
                if table.table[irow][icol] == 0: #enter when blank
                    temp[irow].append((irow, icol))
                icol += 1
            irow += 1
        return temp

    def init_state(self, blanks, table):
        irow = 0
        for row in table.table:
            icol = 0
            l = {1,2,3,4,5,6,7,8,9} - set(row)
            for col in row:
                if table.table[irow][icol] == 0: #enter when blank
                    table.table[irow][icol] = l.pop()
                icol += 1
            irow += 1

    def randomsuccessor(self, blanks):
        row = random.randrange(9)
        blank_list_row = blanks[row]
        if len(blank_list_row) > 1:
            r = random.sample(range(0,len(blank_list_row)), 2)
            return blank_list_row[r[0]], blank_list_row[r[1]]
        else:
            return blank_list_row[0], blank_list_row[0]
    
    def valueCal(self, table):
        val = 0
        for i in range(0, 9):
            val = val + len(table.checkcol(i)) + len(table.check3x3(i))
        return val

    def simmulate(self, table):
        blank_list  = self.getblanknodes(table)
        self.init_state(blank_list, table)
        T = 1
        val_curr = self.valueCal(table)
        while T > 0.000000001:
            T = T * 0.9999999
            b1, b2 = self.randomsuccessor(blank_list)
            table.table[b1[0]][b1[1]], table.table[b2[0]][b2[1]] = table.table[b2[0]][b2[1]], table.table[b1[0]][b1[1]]
            val_nxt = self.valueCal(table)
            if val_nxt == 0:
                print(" --- value : ", val_nxt)
                return table
            elif val_curr - val_nxt >= 0: val_curr = val_nxt
            elif random.randint(0,100)/10 > math.exp(-abs(val_nxt - val_curr)/T):
                table.table[b1[0]][b1[1]], table.table[b2[0]][b2[1]] = table.table[b2[0]][b2[1]], table.table[b1[0]][b1[1]]
            else: val_curr = val_nxt
        print( " --- value : ", val_curr)
        return table

    def printtable(self, table):
        for row in table.table:
            print(' \n| ',end="")
            for col in row:
                print(col,' | ', end="")
        print("\n------------------------------------------------------------------")

if __name__ == "__main__":
    filename = input("Enter suduku filepath: ")
    s = Search(filename)
    root = Tree()
    print("Pls wait a little. Be claim man.")
    result = s.simmulate(s.table)
    s.printtable(result)
