import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, Qt
import random, math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class stock():
    def __init__(self,name="none",first=1000,mob=2.0,num=0):
        self.name = name
        self.price = first
        self.num = num
        self.mob = mob
        self.recordlist = [first]
    
    def gotime(self):
        expo = random.normalvariate(mu=0.0,sigma=1.0)
        if self.mob == 0.0:
            delta = 1.0
        else:
            delta = math.pow(self.mob, expo)
        self.price = int(self.price * delta)
        self.recordlist.append(self.price)
    def record(self):
        return self.recordlist
    def buy(self,num):
        self.num += num
    def sell(self,num):
        self.num -= num
    
    def change_name(self,name="none"):
        self.name = name

class stocksystem():
    def __init__(self):
        a = stock("Aeris",1000)
        b = stock("Bestia",5000)
        c = stock("Crystalli",2000,3.0)
        d = stock("Divus",10000,3.0)
        e = stock("Essentia",5000,5.0)
        f = stock("Floris",50000,5.0)
        g = stock("Glaciei",10000)
        h = stock("Herbae",100000)
        self.stocklist = [a,b,c,d,e,f,g,h]
    
    def gotime(self):
        for stock_ in self.stocklist:
            stock_.gotime()
    def record(self):
        recordlist = {}
        for stock_ in self.stocklist:
            recordlist[stock_.name] = stock_.record()
        return recordlist
    def buy(self,name,num):
        self.stocklist[name].buy(num)
    def sell(self,name,num):
        self.stocklist[name].sell(num)
    
    def return_stock_name(self, n=-1):
        list_ = []
        for i, stock_ in enumerate(self.stocklist):
            if i != n:
                list_.append(stock_.name)
        return list_

    def reset(self,n,name="#",start=0,expo=0.0):
        if name == "#":
            if n <= 7:
                name = ["Aeris","Bestia","Crystalli","Divus","Essentia","Floris","Glaciei","Herbae"][n]
            else:
                name = "Temp"
        try:
            if start <= 0:
                start = [1000,5000,2000,10000,5000,50000,10000,100000][n]
        except:
            if n <= 7:
                start = [1000,5000,2000,10000,5000,50000,10000,100000][n]
            else:
                start = 1000
        try:
            if expo <= 0.0:
                expo = [2.0,2.0,3.0,3.0,5.0,5.0,2.0,2.0][n]
        except:
            if n <= 7:
                expo = [2.0,2.0,3.0,3.0,5.0,5.0,2.0,2.0][n]
            else:
                expo = 2.0
        new = stock(name,start,expo)
        self.stocklist[n] = new
    def add(self,name="#",start=0,expo=0.0):
        if name == "#":
            name = "Temp"
        try:
            if start <= 0:
                start = 10000
        except:
            start = 10000
        try:
            if expo <= 0.0:
                expo = 3.0
        except:
            expo = 3.0
        new = stock(name,start,expo)
        self.stocklist.append(new)
    def change_name(self,n,newName="#"):
        if newName == "#":
            newName = "Temp"
        self.stocklist[n].change_name(newName)
        

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.get_data()

        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.initUI()

        self.show()

    def initUI(self):
        self.itemboxdelete(self.mainlayout)


        self.setWindowTitle('Stock Mini Game')
        self.ScSize(500, 300)
        

        label_title = QLabel('Stock Mini Game')
        label_title.setAlignment(Qt.AlignCenter)
        label_title.setFont(QFont('Arial', 30))

        label_maker = QLabel('made by 172635')
        label_maker.setAlignment(Qt.AlignCenter)
        label_maker.setFont(QFont('Arial', 10))

        btn_start = QPushButton('Start')
        btn_start.clicked.connect(self.gameStart)

        btn_highscore = QPushButton('HoF')
        btn_highscore.clicked.connect(self.gameHallOfFame)

        btn_quit = QPushButton('Quit')
        btn_quit.clicked.connect(QCoreApplication.instance().quit)

        layout_h = QHBoxLayout()
        layout_h.addWidget(btn_start)
        layout_h.addWidget(btn_highscore)
        layout_h.addWidget(btn_quit)

        self.mainlayout.addStretch(3)
        self.mainlayout.addWidget(label_title)
        self.mainlayout.addWidget(label_maker)
        self.mainlayout.addStretch(2)
        self.mainlayout.addLayout(layout_h)
        self.mainlayout.addStretch(1)
        
    def gameStart(self):
        self.nickname = "Guest"
        self.itemboxdelete(self.mainlayout)

        qle = QLineEdit(self)
        qle.setText("Guest")
        qle.textChanged[str].connect(self.gameNickqleAct)

        btn_go = QPushButton("Start")
        btn_go.clicked.connect(self.gameStartGo)

        btn_return = QPushButton("Return")
        btn_return.clicked.connect(self.initUI)

        layoutHbtn = QHBoxLayout()
        layoutHbtn.addStretch(2)
        layoutHbtn.addWidget(btn_go)
        layoutHbtn.addStretch(1)
        layoutHbtn.addWidget(btn_return)
        layoutHbtn.addStretch(2)

        layoutV = QVBoxLayout()
        layoutV.addStretch(2)
        layoutV.addWidget(qle)
        layoutV.addStretch(1)
        layoutV.addLayout(layoutHbtn)
        layoutV.addStretch(2)

        layoutH = QHBoxLayout()
        layoutH.addStretch(1)
        layoutH.addLayout(layoutV)
        layoutH.addStretch(1)

        self.mainlayout.addLayout(layoutH)
    def gameStartGo(self):
        self.stock_class = stocksystem()
        self.Money = 10000
        self.day = 1

        self.gamePage()
    def gameNickqleAct(self, text):
        self.nickname = text

    def gamePage(self):
        self.itemboxdelete(self.mainlayout)


        layoutHE = QHBoxLayout()
        label_player = QLabel("player : "+self.nickname)
        layoutHE.addWidget(label_player)
        layoutHE.addStretch(1)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.gameExit)
        layoutHE.addWidget(btn_exit)


        layoutD = QHBoxLayout()
        
        label_day = QLabel("Day : "+str(self.day))
        label_day.setAlignment(Qt.AlignCenter)
        label_day.setFont(QFont('Arial', 15))
        layoutD.addWidget(label_day)
        layoutD.addStretch(1)


        layoutM = QHBoxLayout()

        label_money = QLabel("Money : "+str(self.Money))
        label_money.setAlignment(Qt.AlignCenter)
        label_money.setFont(QFont('Arial', 15))
        layoutM.addWidget(label_money)
        layoutM.addStretch(1)


        layoutA = QHBoxLayout()

        Asset = self.Money
        for stock in self.stock_class.stocklist:
            Asset += (stock.price * stock.num)
        label_Asset = QLabel("Asset : "+str(Asset))
        label_Asset.setAlignment(Qt.AlignCenter)
        label_Asset.setFont(QFont('Arial', 15))
        layoutA.addWidget(label_Asset)
        layoutA.addStretch(1)


        layoutB = QHBoxLayout()

        btn_chart = QPushButton("Chart")
        btn_chart.clicked.connect(self.drawchart)
        
        btn_bs = QPushButton("Buy / Sell")
        btn_bs.clicked.connect(self.gameStockBS)

        btn_ra = QPushButton("Reset / Add")
        btn_ra.clicked.connect(self.gameStockRA)

        layoutB.addWidget(btn_chart)
        layoutB.addWidget(btn_bs)
        layoutB.addWidget(btn_ra)


        btn_nextday = QPushButton("Next Day")
        btn_nextday.clicked.connect(self.gameNextday)
        
        self.mainlayout.addLayout(layoutHE)
        self.mainlayout.addStretch(3)
        self.mainlayout.addLayout(layoutD)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutM)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutA)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutB)
        self.mainlayout.addWidget(btn_nextday)

    def gameNextday(self):
        self.day += 1
        if self.day == 366:
            self.gameEnd()
        else:
            self.stock_class.gotime()
            self.gamePage()

    def drawchart(self):
        self.itemboxdelete(self.mainlayout)


        layoutHE = QHBoxLayout()
        label_player = QLabel("player : "+self.nickname)
        layoutHE.addWidget(label_player)
        layoutHE.addStretch(1)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.gamePage)
        layoutHE.addWidget(btn_exit)


        label_cb = QLabel("Stock")
        label_cb.setAlignment(Qt.AlignCenter)
        label_cb.setFont(QFont('Arial', 13))


        self.DCcb = self.stock_class.stocklist[0].name
        self.DCcbN = 0
        cb = QComboBox(self)
        for stock in self.stock_class.stocklist:
            cb.addItem(stock.name)
        cb.activated[str].connect(self.DCcbAct)


        ql = QLabel(self.DCcb + " 개당 가격 : " + str(self.stock_class.stocklist[0].price))
        ql.setAlignment(Qt.AlignCenter)


        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)


        self.mainlayout.addLayout(layoutHE)
        self.mainlayout.addStretch(1)
        self.mainlayout.addWidget(label_cb)
        self.mainlayout.addWidget(cb)
        self.mainlayout.addWidget(ql)
        self.mainlayout.addWidget(self.canvas)
        
        ax = self.fig.add_subplot(111)
        ax.plot([i for i in range(1, self.day+1)],self.stock_class.stocklist[0].record(),label = 'Stock Price')
        ax.legend(loc = 'upper left')
        ax.grid()
        self.canvas.draw()
    def DCcbAct(self, text):
        self.DCcb = text
        for i, stock in enumerate(self.stock_class.stocklist):
            if text == stock.name:
                self.DCcbN = i
                self.mainlayout.layout().itemAt(4).widget().setText(self.DCcb + " 개당 가격 : " + str(self.stock_class.stocklist[self.DCcbN].price))
                break
        
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.plot([i for i in range(1, self.day+1)],self.stock_class.stocklist[self.DCcbN].record(),label = 'Stock Price')
        ax.legend(loc = 'upper left')
        ax.grid()
        self.canvas.draw()

    def gameStockBS(self):
        self.itemboxdelete(self.mainlayout)


        layoutHE = QHBoxLayout()
        label_player = QLabel("player : "+self.nickname)
        layoutHE.addWidget(label_player)
        layoutHE.addStretch(1)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.gamePage)
        layoutHE.addWidget(btn_exit)


        label_cb = QLabel("Stock")
        label_cb.setAlignment(Qt.AlignCenter)
        label_cb.setFont(QFont('Arial', 15))


        self.BScb = self.stock_class.stocklist[0].name
        self.BScbN = 0
        cb = QComboBox(self)
        for stock in self.stock_class.stocklist:
            cb.addItem(stock.name)
        cb.activated[str].connect(self.BScbAct)


        label_stock_price = QLabel(self.BScb + " 개당 가격 : " + str(self.stock_class.stocklist[self.BScbN].price))
        label_stock_now = QLabel(self.BScb + " 현재 보유량 : "+ str(self.stock_class.stocklist[self.BScbN].num))


        self.BSqle = 0
        qle = QLineEdit(self)
        qle.setText("0")
        qle.textChanged[str].connect(self.BSqleAct)


        label_total_price = QLabel("total : " + str(self.stock_class.stocklist[self.BScbN].price * self.BSqle))
        label_now_money = QLabel("현재 남은 돈 : " + str(self.Money))


        layoutBS = QHBoxLayout()
        layoutBS.addStretch(1)
        btn_buy = QPushButton("Buy")
        btn_buy.clicked.connect(self.BSbuy)
        layoutBS.addWidget(btn_buy)
        layoutBS.addStretch(1)
        btn_sell = QPushButton("Sell")
        btn_sell.clicked.connect(self.BSsell)
        layoutBS.addWidget(btn_sell)
        layoutBS.addStretch(1)


        self.mainlayout.addLayout(layoutHE)
        self.mainlayout.addStretch(2)
        self.mainlayout.addWidget(label_cb)
        self.mainlayout.addWidget(cb)
        self.mainlayout.addWidget(label_stock_price)
        self.mainlayout.addWidget(label_stock_now)
        self.mainlayout.addWidget(qle)
        self.mainlayout.addWidget(label_total_price)
        self.mainlayout.addWidget(label_now_money)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutBS)
        self.mainlayout.addStretch(4)
    def BSbuy(self):
        if self.stock_class.stocklist[self.BScbN].price * self.BSqle > self.Money:
            QMessageBox.warning(self, "Warning : 경고", "Run out of money. You can't buy these.\n돈이 부족합니다. 이것을 구매하실 수 없습니다.", QMessageBox.Cancel)
        else:
            QMessageBox.about(self, "Done : 구매 완료", "Successful purchase.\n구매에 성공하였습니다.")
            self.Money = self.Money - self.stock_class.stocklist[self.BScbN].price * self.BSqle
            self.stock_class.stocklist[self.BScbN].buy(self.BSqle)
            self.gameStockBS()
    def BSsell(self):
        if self.BSqle > self.stock_class.stocklist[self.BScbN].num:
            QMessageBox.warning(self, "Warning : 경고", "Run out of stock. You can't sell these.\n주식이 부족합니다. 이것을 판매하실 수 없습니다.", QMessageBox.Cancel)
        else:
            QMessageBox.about(self, "Done : 판매 완료", "Successful sales.\n판매에 성공하였습니다.")
            self.Money = self.Money + self.stock_class.stocklist[self.BScbN].price * self.BSqle
            self.stock_class.stocklist[self.BScbN].sell(self.BSqle)
            self.gameStockBS()
    def BSqleAct(self, text):
        try:
            self.BSqle = int(text)
        except:
            self.BSqle = 0
            if text != "":
                self.mainlayout.layout().itemAt(6).widget().setText("0")
        if self.BSqle < 0:
            self.BSqle = 0
            self.mainlayout.layout().itemAt(6).widget().setText("0")
        self.mainlayout.layout().itemAt(7).widget().setText("total : " + str(self.stock_class.stocklist[self.BScbN].price * self.BSqle))
    def BScbAct(self, text):
        self.BScb = text
        for i, stock in enumerate(self.stock_class.stocklist):
            if text == stock.name:
                self.BScbN = i
                self.mainlayout.layout().itemAt(4).widget().setText(self.BScb + " 개당 가격 : " + str(self.stock_class.stocklist[self.BScbN].price))
                self.mainlayout.layout().itemAt(5).widget().setText(self.BScb + " 현재 보유량 : "+ str(self.stock_class.stocklist[self.BScbN].num))
                self.mainlayout.layout().itemAt(6).widget().setText("0")
                self.BSqle = 0
                self.mainlayout.layout().itemAt(7).widget().setText("total : 0")
                break

    def gameStockRA(self):
        self.itemboxdelete(self.mainlayout)


        layoutHE = QHBoxLayout()
        label_player = QLabel("player : "+self.nickname)
        layoutHE.addWidget(label_player)
        layoutHE.addStretch(1)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.gamePage)
        layoutHE.addWidget(btn_exit)


        label_cb = QLabel("Stock")
        label_cb.setAlignment(Qt.AlignCenter)
        label_cb.setFont(QFont('Arial', 15))


        self.RAcb = self.stock_class.stocklist[0].name
        self.RAcbN = 0
        cb = QComboBox(self)
        for stock in self.stock_class.stocklist:
            cb.addItem(stock.name)
        cb.activated[str].connect(self.RAcbAct)


        lblN = QLabel("Name")
        lblN.setAlignment(Qt.AlignCenter)
        self.RAname = "Aeris"
        qleN = QLineEdit(self)
        qleN.setText("Aeris")
        qleN.textChanged[str].connect(self.RAqleNAct)

        lblS = QLabel("Start")
        lblS.setAlignment(Qt.AlignCenter)
        self.RAstart = 1000
        qleS = QLineEdit(self)
        qleS.setText("1000")
        qleS.textChanged[str].connect(self.RAqleSAct)

        lblE = QLabel("Expo")
        lblE.setAlignment(Qt.AlignCenter)
        self.RAexpo = 2.0
        qleE = QLineEdit(self)
        qleE.setText("2.0")
        qleE.textChanged[str].connect(self.RAqleEAct)

        layoutG = QGridLayout()
        layoutG.addWidget(lblN, 0, 0)
        layoutG.addWidget(qleN, 0, 1)
        layoutG.addWidget(lblS, 1, 0)
        layoutG.addWidget(qleS, 1, 1)
        layoutG.addWidget(lblE, 2, 0)
        layoutG.addWidget(qleE, 2, 1)
        layoutG.setColumnStretch(2, 1)


        layoutBS = QHBoxLayout()
        layoutBS.addStretch(1)
        btn_buy = QPushButton("Reset")
        btn_buy.clicked.connect(self.RAreset)
        layoutBS.addWidget(btn_buy)
        layoutBS.addStretch(1)
        btn_sell = QPushButton("Add")
        btn_sell.clicked.connect(self.RAadd)
        layoutBS.addWidget(btn_sell)
        layoutBS.addStretch(1)


        self.mainlayout.addLayout(layoutHE)
        self.mainlayout.addStretch(2)
        self.mainlayout.addWidget(label_cb)
        self.mainlayout.addWidget(cb)
        self.mainlayout.addLayout(layoutG)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutBS)
        self.mainlayout.addStretch(4)
    def RAcbAct(self, text):
        self.RAcb = text
        for i, stock in enumerate(self.stock_class.stocklist):
            if text == stock.name:
                self.RAcbN = i
                
                try:
                    self.mainlayout.layout().itemAt(4).layout().itemAt(1).widget().setText(["Aeris","Bestia","Crystalli","Divus","Essentia","Floris","Glaciei","Herbae"][self.RAcbN])
                    self.RAname = ["Aeris","Bestia","Crystalli","Divus","Essentia","Floris","Glaciei","Herbae"][self.RAcbN]
                    self.mainlayout.layout().itemAt(4).layout().itemAt(3).widget().setText(str([1000,5000,2000,10000,5000,50000,10000,100000][self.RAcbN]))
                    self.RAstart = [1000,5000,2000,10000,5000,50000,10000,100000][self.RAcbN]
                    self.mainlayout.layout().itemAt(4).layout().itemAt(5).widget().setText(str([2.0,2.0,3.0,3.0,5.0,5.0,2.0,2.0][self.RAcbN]))
                    self.RAexpo = [2.0,2.0,3.0,3.0,5.0,5.0,2.0,2.0][self.RAcbN]
                except:
                    self.mainlayout.layout().itemAt(4).layout().itemAt(1).widget().setText("Temp")
                    self.RAname = "Temp"
                    self.mainlayout.layout().itemAt(4).layout().itemAt(3).widget().setText("1000")
                    self.RAstart = 1000
                    self.mainlayout.layout().itemAt(4).layout().itemAt(5).widget().setText("2.0")
                    self.RAexpo = 2.0
                break
    def RAqleNAct(self,text):
        self.RAname = text
        if text == "":
            self.RAname = ["Aeris","Bestia","Crystalli","Divus","Essentia","Floris","Glaciei","Herbae"][self.RAcbN]
    def RAqleSAct(self,text):
        try:
            self.RAstart = int(text)
        except:
            try:
                self.RAstart = [1000,5000,2000,10000,5000,50000,10000,100000][self.RAcbN]
                if text != "":
                    self.mainlayout.layout().itemAt(4).layout().itemAt(3).widget().setText(str([1000,5000,2000,10000,5000,50000,10000,100000][self.RAcbN]))
            except:
                self.RAstart = 1000
                if text != "":
                    self.mainlayout.layout().itemAt(4).layout().itemAt(3).widget().setText("1000")
        if self.RAstart < 0:
            self.RAstart = 0
            self.mainlayout.layout().itemAt(4).layout().itemAt(3).widget().setText("0")
    def RAqleEAct(self,text):
        try:
            self.RAexpo = float(text)
        except:
            try:
                self.RAexpo = [2.0,2.0,3.0,3.0,5.0,5.0,2.0,2.0][self.RAcbN]
                if text != "":
                    self.mainlayout.layout().itemAt(4).layout().itemAt(5).widget().setText(str([2.0,2.0,3.0,3.0,5.0,5.0,2.0,2.0][self.RAcbN]))
            except:
                self.RAexpo = 2.0
                if text != "":
                    self.mainlayout.layout().itemAt(4).layout().itemAt(5).widget().setText("2.0")
        if self.RAexpo < 0.0:
            self.RAexpo = 0.0
            self.mainlayout.layout().itemAt(4).layout().itemAt(5).widget().setText("0.0")
    def RAreset(self):
        if self.stock_class.stocklist[self.RAcbN].num != 0:
            QMessageBox.warning(self, "Warning : 경고", "You have this stock. You can't reset it.\n이 주식을 가지고 있습니다. 이것을 리셋할 수 없습니다.", QMessageBox.Cancel)
        elif self.RAname in self.stock_class.return_stock_name(n = self.RAcbN):
            QMessageBox.warning(self, "Warning : 경고", "The stock named like this already exists. You can't reset it.\n이와 같은 이름의 주식이 존재합니다. 이것을 리셋할 수 없습니다.", QMessageBox.Cancel)
        else:
            QMessageBox.about(self, "Done : 리셋 완료", "Successful reset.\n리셋에 성공하였습니다.")
            self.stock_class.reset(n = self.RAcbN, name = self.RAname, start = self.RAstart, expo = self.RAexpo)
            self.gameStockRA()
    def RAadd(self):
        if self.RAname in self.stock_class.return_stock_name():
            QMessageBox.warning(self, "Warning : 경고", "The stock named like this already exists. You can't add it.\n이와 같은 이름의 주식이 존재합니다. 이것을 추가할 수 없습니다.", QMessageBox.Cancel)
        else:
            QMessageBox.about(self, "Done : 신규 추가 완료", "Successful add.\n추가에 성공하였습니다.")
            self.stock_class.add(name = self.RAname, start = self.RAstart, expo = self.RAexpo)
            self.gameStockRA()

    def gameEnd(self):
        self.itemboxdelete(self.mainlayout)
        
        ql = QLabel("Game End")
        ql.setAlignment(Qt.AlignCenter)
        ql.setFont(QFont('Arial', 25))

        layoutV = QVBoxLayout()

        qlnick = QLabel("NickName : "+self.nickname)
        qlnick.setAlignment(Qt.AlignLeft)
        qlnick.setFont(QFont('Arial', 13))
        layoutV.addWidget(qlnick)

        Asset = self.Money
        for stock in self.stock_class.stocklist:
            Asset += (stock.price * stock.num)
        qlscore = QLabel("End Score(Asset) : "+str(Asset))
        qlscore.setAlignment(Qt.AlignLeft)
        qlscore.setFont(QFont('Arial', 13))
        layoutV.addWidget(qlscore)

        layoutH = QHBoxLayout()
        layoutH.addStretch(1)
        layoutH.addLayout(layoutV)
        layoutH.addStretch(3)

        btn = QPushButton("End")
        btn.clicked.connect(self.gameDataSave)

        layoutH2 = QHBoxLayout()
        layoutH2.addStretch(1)
        layoutH2.addWidget(btn)
        layoutH2.addStretch(1)


        self.mainlayout.addStretch(2)
        self.mainlayout.addWidget(ql)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutH)
        self.mainlayout.addStretch(1)
        self.mainlayout.addLayout(layoutH2)
    def gameExit(self):
        self.itemboxdelete(self.mainlayout)

        self.mainlayout.addStretch(2)

        exitlabel = QLabel("Exit ?")
        exitlabel.setAlignment(Qt.AlignCenter)
        exitlabel.setFont(QFont('Arial', 30))
        self.mainlayout.addWidget(exitlabel)

        self.mainlayout.addStretch(1)

        layoutHE = QHBoxLayout()
        no = QPushButton("Return Game")
        no.clicked.connect(self.gamePage)
        nosaveExit = QPushButton("No Record Exit")
        nosaveExit.clicked.connect(self.initUI)
        exit = QPushButton("Exit")
        exit.clicked.connect(self.gameEnd)
        layoutHE.addStretch(1)
        layoutHE.addWidget(no)
        layoutHE.addStretch(1)
        layoutHE.addWidget(nosaveExit)
        layoutHE.addStretch(1)
        layoutHE.addWidget(exit)
        layoutHE.addStretch(1)
        self.mainlayout.addLayout(layoutHE)

        self.mainlayout.addStretch(1)
    def gameDataSave(self):
        if self.nickname != "Guest":
            Asset = self.Money
            for stock in self.stock_class.stocklist:
                Asset += (stock.price * stock.num)
            self.highscore.append(Asset)
            self.highperson.append(self.nickname)
            self.check_data()
            self.save_data()

        self.initUI()


    def gameHallOfFame(self):
        self.gameHOFP = 1

        self.gameHallOfFamePage()
    def gameHallOfFamePage(self):
        self.itemboxdelete(self.mainlayout)

        layoutG=QGridLayout()
        n = self.gameHOFP - 1
        layoutG.addWidget(QLabel("rank"),0,0)
        layoutG.addWidget(QLabel("nickname"),0,1)
        layoutG.addWidget(QLabel("score"),0,2)
        for i in range(5):
            if i+n*5>=len(self.highscore):
                break
            layoutG.addWidget(QLabel(str(i+n*5+1)),i+1,0)
            layoutG.addWidget(QLabel(str(self.highscore[i+n*5])),i+1,1)
            layoutG.addWidget(QLabel(self.highperson[i+n*5]),i+1,2)

        layoutH = QHBoxLayout()
        btn_left = QPushButton("< Prev")
        btn_left.clicked.connect(self.gameHOFPLeft)
        btn_right = QPushButton("Next >")
        btn_right.clicked.connect(self.gameHOFPRight)
        if self.gameHOFP > 1:
            layoutH.addWidget(btn_left)
        layoutH.addStretch(1)
        if self.gameHOFP < int((len(self.highscore)-1)/5):
            layoutH.addWidget(btn_right)

        layoutHE = QHBoxLayout()
        layoutHE.addStretch(1)
        btn_exit = QPushButton("Exit")
        btn_exit.clicked.connect(self.initUI)
        layoutHE.addWidget(btn_exit)

        self.mainlayout.addLayout(layoutHE)
        self.mainlayout.addLayout(layoutG)
        self.mainlayout.addLayout(layoutH)
        self.mainlayout.addStretch(1)
    def gameHOFPLeft(self):
        if self.gameHOFP == 1:
            return
        self.gameHOFP -= 1
        self.gameHallOfFamePage()
    def gameHOFPRight(self):
        if self.gameHOFP >= int((len(self.highscore)-1)/5):
            return
        self.gameHOFP += 1
        self.gameHallOfFamePage()

    def check_data(self):
        #only one can be greater than others
        for i in range(len(self.highscore)-1):
            j = len(self.highscore) - i - 1
            if self.highscore[j] > self.highscore[j-1]:
                temp = self.highscore[j]
                self.highscore[j] = self.highscore[j-1]
                self.highscore[j-1] = temp
                temp = self.highperson[j]
                self.highperson[j] = self.highscore[j-1]
                self.highscore[j-1] = temp
            else:
                break
    def get_data(self):
        lines = []
        try:
            file = open("highdata.txt","r")
            lines = file.readlines()
            file.close()
        except:
            file = open("highdata.txt","w")
            lines = []
            file.writelines(lines)
            file.close()

        self.highscore = []
        self.highperson = []

        for i in range(int(len(lines)/2)):
            highscore = 0
            try:
                line_1 = lines[i*2]
                highscore = int(line_1[:-1])
            except:
                highscore = 0
            line_2 = lines[i*2+1]

            self.highscore.append(highscore)
            self.highperson.append(line_2[:-1])
    def save_data(self):
        file = open("highdata.txt","w")
        lines = []
        for i in range(len(self.highscore)):
            lines.append(str(self.highscore[i])+"\n")
            lines.append(self.highperson[i]+"\n")
        file.writelines(lines)
        file.close()

    def printItemBoxList(self, box):
        for i in reversed(range(box.layout().count())):
            print(type(box.layout().itemAt(i)))
    def itemboxdelete(self, box):
        for i in reversed(range(box.layout().count())):
            self.boxdelete(box.layout().itemAt(i), box.layout())
    def boxdelete(self, item, box):
        if hasattr(item, "layout"):
            if callable(item.layout):
                layout = item.layout()
        else:
            layout = None

        if hasattr(item, "widget"):
            if callable(item.widget):
                widget = item.widget()
        else:
            widget = None
        
        if hasattr(item, "spacerItem"):
            if callable(item.spacerItem):
                spacer = item.spacerItem()
        else:
            spacer = None

        if widget:
            widget.setParent(None)
        elif layout:
            for i in reversed(range(layout.count())):
                self.boxdelete(layout.itemAt(i), layout)
            box.removeItem(item)
        elif spacer:
            box.removeItem(item)

    def ScSize(self,x,y):
        self.resize(x, y)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())