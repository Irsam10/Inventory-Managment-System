from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Menu import Ui_MenuWindow
from MakeReceiptWin import Ui_MakeReceiptWindow
from AddProduct import Ui_addProductWindow
from DeleteProduct import Ui_deleteProductWindow
from AddAmount import Ui_addAmountWindow
from SubtractAmount import Ui_subtractAmountWindow
from Search import Ui_SearchProductWindow
from ChangeRate import Ui_ChangeRateWindow
from ReceiptMaker import makeReceipt
from dbHandler import dbHandler

from qt_material import apply_stylesheet
from qt_material import list_themes

class MenuWindow(QtWidgets.QMainWindow,QtWidgets.QLabel,Ui_MenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.searchProductBtn.clicked.connect(self.openSearchWindow)
        self.secondWindow = SearchWindow()
        self.secondWindow.closed.connect(self.show)

        self.addProductWin = AddProduct()
        self.addProductBtn.clicked.connect(self.openAddProductWindow)
        self.addProductWin.closed.connect(self.show)

        self.deleteProductWin = DeleteProduct()
        self.deleteProductBtn.clicked.connect(self.openDeleteProductWindow)
        self.deleteProductWin.closed.connect(self.show)
        apply_stylesheet(app, theme='dark_teal.xml')
    def openSearchWindow(self):
        self.secondWindow.show()
        self.hide()

    def openAddProductWindow(self):
        self.addProductWin.show()
        self.hide()

    def openDeleteProductWindow(self):
        self.deleteProductWin.show()
        self.hide()



class MakeReceipt(QtWidgets.QMainWindow,Ui_MakeReceiptWindow):
    closed = QtCore.pyqtSignal()

    def __init__(self,data):
        super().__init__()
        self.setupUi(self)
        self.makeRecpBtn.clicked.connect(self.printReceipt)
        self.billno = None
        self.name = None
        self.dataList = data



    def printReceipt(self):
        self.billno = self.billNoTextBox.text()
        self.name = self.recpNameTextBox.text()
        self.biltyno = self.biltyNoTextBox.text()

        if self.billno == '' or self.name == '' or self.biltyno == '':
            self.showEmptyFieldMessageBox()
        else:
            arg = (self.billno,self.name,self.biltyno,self.dataList)
            print(self.dataList)
            makeReceipt(arg)
            self.close()


    def showEmptyFieldMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("One or more Field is empty, Please fill all fields")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
    def showNotDigitsMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid Amount,Please enter digits only")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showAmountUpdatedSuccesfullyBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Succes")
        msg.setText("Amount Updated Succesfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showNegativeQuantityBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Amount entered more than the remaining product quantity")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def closeEvent(self, event):
        self.closed.emit()





#Search Functionality

class SearchWindow(QtWidgets.QMainWindow,Ui_SearchProductWindow):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clickSearchBtn.clicked.connect(self.getLineInput)

        self.addWin = AddAmount()
        self.subWin = SubtractAmount()
        self.rateWin = ChangeRate()

        self.addWin.closed.connect(self.clearSelectedRow)
        self.addAmountBtn.clicked.connect(self.showAddAmountWindow)

        self.subWin.closed.connect(self.clearSelectedRow)
        self.subtractAmountBtn.clicked.connect(self.showSubtractAmountWindow)

        self.rateWin.closed.connect(self.clearSelectedRow)
        self.changeRateBtn.clicked.connect(self.showChangeRateWindow)
    def getLineInput(self):
        searchedObject= self.searchTextBox.text()
        self.search(searchedObject)

    def search(self, searchedObject):
        handler = dbHandler()
        data = handler.getData(searchedObject)
        i = 0
        self.tableShowWidget.setRowCount(len(data))
        for row in data:
            self.tableShowWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableShowWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableShowWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableShowWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableShowWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            i = i + 1

    def showAddAmountWindow(self):
        tableSelectedData = self.getSelectedRowData()
        if tableSelectedData is not None:
            self.addWin.show()
            self.addWin.getTableData(tableSelectedData)
        else:
            self.showNoSelectionMessageBox()

    def showSubtractAmountWindow(self):
        tableSelectedData = self.getSelectedRowData()
        if tableSelectedData is not None:
            self.subWin.show()
            self.subWin.getTableData(tableSelectedData)
        else:
            self.showNoSelectionMessageBox()

    def showChangeRateWindow(self):
        tableSelectedData = self.getSelectedRowData()
        if tableSelectedData is not None:
            self.rateWin.show()
            self.rateWin.getTableData(tableSelectedData)
        else:
            self.showNoSelectionMessageBox()

    def getSelectedRowData(self):
        row = self.tableShowWidget.currentRow()
        firstColInRow = self.tableShowWidget.item(row, 0)
        #thirdColInRow = self.tableShowWidget.item(row,3)
        if firstColInRow is None or firstColInRow.text() is None:
            return None
        return firstColInRow.text()

    def clearSelectedRow(self):
        self.getLineInput()
        self.tableShowWidget.clearSelection()
        self.tableShowWidget.selectionModel().clearCurrentIndex()

    def showNoSelectionMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("No Product Selected,Please Select a product to make changes")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
    def closeEvent(self, event):
        self.closed.emit()






#Delete and Subtract Functionality

class SubtractAmount(QtWidgets.QMainWindow, Ui_subtractAmountWindow):
    closed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.subBtn.clicked.connect(self.getLineInput)
        self.subAndReceiptBtn.clicked.connect(self.showMakeReceiptWindow)

        self.dataList = []

    def getTableData(self, getItem):
        self.selectedItem = getItem

    def getLineInput(self):
        self.enteredAmountNum = self.enteredAmount.text()
        self.subAmount(self.enteredAmountNum)

    def subAmount(self, enteredAmount):
        data = []
        if enteredAmount.isdigit() == False:
            self.showNotDigitsMessageBox()
            return False
        else:
            handler = dbHandler()
            currentAmount = handler.getCurrentAmount(self.selectedItem)

            if int(enteredAmount) > currentAmount:
                self.showNegativeQuantityBox()
                return False

            handler.subAmount(currentAmount, enteredAmount, self.selectedItem)
            try:
                temp = handler.getDataForReceipt(self.selectedItem)
                for i in temp:
                    data.append(i)
                data.append(enteredAmount)
                self.dataList.append(data)
            except Exception as e:
                print(e)

            self.enteredAmount.clear()
            self.showAmountUpdatedSuccesfullyBox()
            self.close()
            return False


    def showMakeReceiptWindow(self):
        self.hide()

        self.enteredAmountNum = self.enteredAmount.text()
        self.subAmount(self.enteredAmountNum)

        self.makeReceiptWin = MakeReceipt(self.dataList)
        self.makeReceiptWin.closed.connect(self.closeAndClear)

        self.makeReceiptWin.show()

    def closeAndClear(self):
        print("Called Clear")
        self.dataList.clear()
        self.close()

    def showNotDigitsMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid Amount,Please enter digits only")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showAmountUpdatedSuccesfullyBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Succes")
        msg.setText("Amount Updated Succesfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showNegativeQuantityBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Amount entered more than the remaining product quantity")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showDataListExceededBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Limit of Items that can be entered in one receipt exceeded, Make new Receipt for new items")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def closeEvent(self, event):
        self.closed.emit()


class DeleteProduct(QtWidgets.QMainWindow,Ui_deleteProductWindow):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.deleteProductBtn.clicked.connect(self.deleteProduct)

    def deleteProduct(self):
        itemName = self.itemNameTextBox.text()
        handler = dbHandler()
        response = handler.deleteData(itemName)

        if response == False:
            self.showProductDoesntExistBox()
        else:
            self.showProductDeletedSuccesfullyBox()
        self.itemNameTextBox.clear()

    def showProductDoesntExistBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Product you are trying to delete doesn't exist")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showProductDeletedSuccesfullyBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Succes")
        msg.setText("Product Deleted Succesfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
    def closeEvent(self, event):
        self.closed.emit()





#Add Functionality

class AddProduct(QtWidgets.QMainWindow,Ui_addProductWindow):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addProductBtn.clicked.connect(self.addProduct)

    def addProduct(self):
        name = self.nameTextBox.text()
        size = self.sizeTextBox.text()
        #partNo = self.partNoTextBox.text()
        quantity =int(self.quantityTextBox.text())
        rate = int(self.lineEdit.text())
        handler = dbHandler()
        response = handler.insertData(name, size, quantity, 123 ,rate)
        if response == False:
            self.showProductAlreadyAddedBox()
        else:
            self.showProductAddedSuccesfullyBox()

        self.nameTextBox.clear()
        self.sizeTextBox.clear()
        self.partNoTextBox.clear()
        self.quantityTextBox.clear()
        self.lineEdit.clear()

    def showProductAlreadyAddedBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Product with this Part No. already exists")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showProductAddedSuccesfullyBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Succes")
        msg.setText("Product Added Succesfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
    def closeEvent(self, event):
        self.closed.emit()


class AddAmount(QtWidgets.QMainWindow,Ui_addAmountWindow):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addBtn.clicked.connect(self.getLineInput)

    def getTableData(self, getItem):
        self.selectedItem = getItem

    def getLineInput(self):
        enteredAmount = self.enteredAmount.text()
        self.addAmount(enteredAmount)

    def addAmount(self,enteredAmount):
        if enteredAmount.isdigit() == False:
            self.showNotDigitsMessageBox()
        else:
            handler = dbHandler()
            currentAmount = handler.getCurrentAmount(self.selectedItem)
            handler.addAmount(currentAmount,enteredAmount,self.selectedItem)
            self.enteredAmount.clear()
            self.showAmountUpdatedSuccesfullyBox()
            self.close()

    def showNotDigitsMessageBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid Amount,Please Enter Digits only")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showAmountUpdatedSuccesfullyBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Succes")
        msg.setText("Amount Updated Succesfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def closeWindow(self):
        self.close()

    def closeEvent(self, event):
        self.closed.emit()













#Change Rate Functionality


class ChangeRate(QtWidgets.QMainWindow,Ui_ChangeRateWindow):
    closed = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.changeBtn.clicked.connect(self.changeRate)

    def getTableData(self, getItem):
        self.selectedItem = getItem

    def changeRate(self):
        newRate = self.rateTextBox.text()
        if newRate.isdigit() is False:
            self.showErrorChangingRateBox()
            self.rateTextBox.clear()
            return

        handler = dbHandler()
        try:
            handler.changeRate(self.selectedItem, newRate)
            self.showRateChangedSuccesfullyBox()
        except Exception as err:
            print(err)
            self.showErrorChangingRateBox()

        self.rateTextBox.clear()

    def showRateChangedSuccesfullyBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Succes")
        msg.setText("Rate Changed Succesfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def showErrorChangingRateBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Error changing the rate of product")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()
    def closeEvent(self, event):
        self.closed.emit()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MenuWindow()
    mainWindow.show()
    sys.exit(app.exec_())