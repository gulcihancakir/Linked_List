import sys

from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QRect, QPropertyAnimation


from queue_convert import Ui_MainWindow
from node import Node
from linkedlist import Linked_List
from queue import Queue


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__queue = Queue()
        self.__linked = Linked_List()
        self.timer = QTimer()
        self.ui.btn_enqueue.clicked.connect(self.enqueue)
        self.ui.btn_dequeue.clicked.connect(self.dequeue)
        
       

        self.__linked.insert_front(Node)
        self.liste = []
        self.ui.label_4.setText('NULL')
        self.ui.label_2.setText('NULL')
        self.x=10
    def enqueue(self):
        data = self.ui.lineEdit.text()
        node = Node(data)
        self.__queue.enqueue(node)
        self.label = QtWidgets.QLabel(self)

        self.label.move(self.x, 90)
        self.label.setText(node.data)
        self.label.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Black))
        # self.label.setFrameStyle(QFrame.Box)
        self.ui.horizontalLayout_2.addWidget(self.label)
        self.label.show()
        self.ui.lineEdit.clear()

      

        self.liste.append(self.label.text())
        print(self.liste)
        self.ui.label_2.setText(self.liste[0])

        for i in range(len(self.liste)):

            self.ui.label_4.setText(self.liste[i])

    

    def dequeue(self):
        y = self.__queue.dequeue()

        self.liste.remove(y)

        for i in reversed(range(self.ui.horizontalLayout_2.count())):

            if i == self.ui.horizontalLayout_2.count()-1:
                widgetToRemove = self.ui.horizontalLayout_2.itemAt(0).widget()
                print(widgetToRemove)
                self.ui.horizontalLayout_2.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)

                break

        if len(self.liste) != 0:
            self.ui.label_2.setText(self.liste[0])

        else:
            self.ui.label_2.setText('NULL')
            self.ui.label_4.setText('NULL')

    

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()
