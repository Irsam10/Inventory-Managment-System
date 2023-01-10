import sqlite3

class dbHandler:
    def __init__(self):
        self.conn = sqlite3.connect('product.db')

    def __del__(self):
        if self.conn:
            self.conn.close()

    def createTable(self):
        try:
            cur = self.conn.cursor()
            cur.execute("""CREATE TABLE product(
            item_name text UNIQUE,
            size text,
            partNO text,
            quantity integer,
            rate integer
            )""")
            self.conn.commit()
            print("Table Created")
        except Exception as err:
            print(err)
        finally:
            cur.close()

    def dropTable(self):
        try:
            cur = self.conn.cursor()
            cur.execute("""DROP TABLE product
            """)
            self.conn.commit()
            print("Table Dropped")
        except Exception as err:
            print(err)
        finally:
            cur.close()
    def checkIfAlreadyAdded(self, name):
        try:
            cur = self.conn.cursor()
            args = (name,)
            cur.execute("select * from product where item_name = ?", args)
            data = cur.fetchone()
            if data is None:
                cur.close()
                return False
            if len(data) != 0:
                cur.close()
                return True
            else:
                cur.close()
                return False
        except Exception as err:
            print(err)
        finally:
            cur.close()
    def insertData(self, itemName, size, partno,quantity,rate):
        if self.checkIfAlreadyAdded(itemName) == True:
            return False
        try:
            cur = self.conn.cursor()
            args = (itemName,size,partno, quantity,rate)
            cur.execute("INSERT INTO product VALUES (?,?,?,?,?)", args)
            self.conn.commit()
            print("Entry Added")
        except Exception as err:
            print(err)
        finally:
            cur.close()
            return True
    def deleteData(self, name):
        if self.checkIfAlreadyAdded(name) == False:
            return False
        try:
            cur = self.conn.cursor()
            arg =(name,)
            print(arg)
            cur.execute("DELETE from product WHERE item_name = ?", arg)
            self.conn.commit()
            print("Entry Deleted")
        except Exception as err:
            print(err)
        finally:
            cur.close()

    def updateData(self,name):
        try:
            cur = self.conn.cursor()
            arg =(name,)
            cur.execute("DELETE from product WHERE item_name = ?", arg)
            self.conn.commit()
            print("Entry Deleted")
        except Exception as err:
            print(err)
        finally:
            cur.close()
    def displayData(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT rowid, * FROM product")
            data = cur.fetchall()
            for row in data:
                for i in row:
                    print(str(i), end=':')
                print()

        except Exception as err:
            print(err)
        finally:
            cur.close()

    def getData(self, searchedObject):
        data = None
        try:
            cur = self.conn.cursor()
            args = (str(searchedObject),)
            cur.execute("SELECT * FROM product WHERE item_name = ?", args)
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute("SELECT * FROM product WHERE partNO = ?", args)
                data = cur.fetchall()
            if len(data) == 0:
                cur.execute("SELECT * FROM product WHERE size = ?", args)
                data = cur.fetchall()
        except Exception as err:
            print(err)
        finally:
            cur.close()
            return data

    def getDataForReceipt(self,searchedObject):
        data = None
        try:
            cur = self.conn.cursor()
            args = (str(searchedObject),)
            cur.execute("SELECT item_name,size,rate FROM product WHERE item_name = ?", args)
            data = cur.fetchone()
        except Exception as err:
            print(err)
        finally:
            cur.close()
            return data

    def getCurrentAmount(self,name):
        data = None
        try:
            cur = self.conn.cursor()
            args = (name,)
            cur.execute("SELECT quantity FROM product WHERE item_name = ?", args)
            data = cur.fetchone()
            if len(data) == 0:
                print("NO Quantity")
        except Exception as err:
            print(err)
        finally:
            cur.close()
            return data[0]

    def addAmount(self,currentAmount,enteredAmount,name):
        try:
            cur = self.conn.cursor()
            finalAmount = currentAmount + int(enteredAmount)
            args = (finalAmount,name,)
            cur.execute("UPDATE product SET quantity = ? where item_name = ?", args)
            self.conn.commit()
        except Exception as err:
            print(err)
        finally:
            cur.close()

    def subAmount(self,currentAmount,enteredAmount,name):
        try:
            cur = self.conn.cursor()
            finalAmount = currentAmount - int(enteredAmount)
            args = (finalAmount,name,)
            cur.execute("UPDATE product SET quantity = ? where item_name = ?", args)
            self.conn.commit()
        except Exception as err:
            print(err)
        finally:
            cur.close()

    def changeRate(self,name,newRate):
        try:
            cur = self.conn.cursor()
            args = (newRate,name,)
            cur.execute("UPDATE product SET rate = ? where item_name = ?", args)
            self.conn.commit()
        except Exception as err:
            print(err)
        finally:
            cur.close()
"""
handler = dbHandler()
handler.dropTable()
handler.createTable()
handler.insertData("abc","5","13f",50,100)
handler.insertData("abd","5","14f",200,200)
#handler.deleteData("14f")
"""

