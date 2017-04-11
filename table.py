import csv

class Table:

    def __init__(self, filepath):
        self.table = []
        self.createTable(filepath)

    def createTable(self, filepath):
        with open(filepath, newline='') as csvfile:
            suReader = csv.reader(csvfile)
            for row in suReader:
                self.table.append(list(map(int, row)))
    
    def add(self, i, j, number):
        self.table[i][j] = number
        return self.table

    def delete(self, i, j):
        self.table[i][j] = 0
        return self.table

    def checkrow(self, row_num):
        return {1,2,3,4,5,6,7,8,9} - set(self.table[row_num])

    def checkcol(self, col_num):
        s = set()
        for i in range(0,9):
            s.add(self.table[i][col_num])
        return {1,2,3,4,5,6,7,8,9} - s       
    
    def check3x3(self, group_num):
        r_row = 0
        r_col = 0
        s = set()
        if group_num%3 == 1 : r_row = (0,3)
        elif group_num%3 == 2 : r_row = (3,6)
        else: r_row = (6,9)
        if group_num < 3: r_col = (0,3)
        elif group_num < 6: r_col = (3,6)
        else: r_col = (6,9)
        for i in range(r_row[0], r_row[1]):
            for j in range(r_col[0], r_col[1]):
                s.add(self.table[i][j])
        return {1,2,3,4,5,6,7,8,9} - s

    def checkall(self, row_num, col_num, group_num):
        return self.checkrow(row_num) & self.checkcol(col_num) & self.check3x3(group_num)

    def checkConstein(self):
        flagcheck = 1
        while flagcheck:
            flagcheck = 0
            irow = 0
            for row in self.table:
                icol = 0
                for col in row:
                    if self.table[irow][icol] == 0:
                        val_set = self.checkall(irow, icol, int(irow/3)*3+int(icol/3))
                        if len(val_set) < 2 and len(val_set) > 0:
                            val = val_set.pop()
                            self.add(irow, icol, val)
                            flagcheck = 1
                    icol += 1
                irow +=1

if __name__ == "__main__":
    t = Table('hard1.csv')
    t.checkConstein()
    for row in t.table:
        print(row)
