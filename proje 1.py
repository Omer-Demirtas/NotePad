from PyQt5.QtWidgets import *
import sys
import sqlite3
from PyQt5.QtGui import QIcon ,QPixmap
import os
from PyQt5.QtCore import Qt, QTimer  , QSize
import time
import requests
from bs4 import BeautifulSoup
import random

class Resim_ekrani(QWidget):
    def __init__(self,image):
        super().__init__()
        self.image = image
        self.init_ui()

    def init_ui(self):
        os.chdir(ilk_mekan + '\ScreenShot')
        self.resim = QLabel("", self)
        pixmap = QPixmap(self.image)
        self.resim.setPixmap(pixmap)
        self.V_BOX = QVBoxLayout()
        self.V_BOX.addWidget(self.resim)
        self.setLayout(self.V_BOX)
        os.chdir(ilk_mekan + '\DataBase')

class ScrollMessageBox(QMessageBox):
    def __init__(self, l, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)
        global ss
        global ilk_mekan
        H_BOXT = QVBoxLayout()
        H_BOXC = QVBoxLayout()
        V_BOX  = QHBoxLayout()
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        self.content = QWidget()
        scroll.setWidget(self.content)
        lay = QVBoxLayout(self.content)

        self.a = 0
        t = 0
        c = 0
        global label_list
        os.chdir(ilk_mekan + '\ScreenShot')
        ss_liste = []
        for x in os.listdir():
            if uzanti_bulma(x) == '.png':
                if x[0:2] == 'ss':
                    ss_liste.append(x)

            else:
                pass
        ss_list_1_9 = []
        ss_list_10_99 = []
        for x in ss_liste:
            if len(str(x)) == 7:
                ss_list_1_9.append(x)
            elif len(str(x)) == 8:
                ss_list_10_99.append(x)
        global ssss
        ssss = []
        for x in ss_list_1_9 :
            ssss.append(x)
        for x in ss_list_10_99 :
            ssss.append(x)

        self.cift = 0
        self.tek = 0
        for x in ss_list_1_9 :
            label = QPushButton(self)
            label.setFixedSize(350, 200)
            label.clicked.connect(self.click)
            label.setIcon(QIcon(ssss[self.a]))
            label.setText(str(self.a + 1))
            label.setIconSize(QSize(350, 350))

            if cift_tek(x[2:3]) == 'tek' :
                H_BOXT.addWidget(label)
                self.tek +=1
            elif cift_tek(x[2:3]) == 'cift':
                H_BOXC.addWidget(label)
                self.cift +=1
            label_list.append(label)
            self.a +=1


        for x in ss_list_10_99 :
            label = QPushButton()
            label.setFixedSize(350, 200)
            label.setIcon(QIcon(ssss[self.a]))
            label.setIconSize(QSize(350, 350))

            label.clicked.connect(self.click)
            label.setText(str(self.a + 1))
            if cift_tek(x[3:4]) == 'tek' :
                H_BOXT.addWidget(label)
                self.tek +=1
            elif cift_tek(x[3:4]) == 'cift' :
                H_BOXC.addWidget(label)
                self.cift +=1
            label_list.append(label)
            self.a +=1

        if self.cift != self.tek :
            if self.tek > self.cift :
                labell = QLabel()
                labell.setFixedSize(350, 200)
                H_BOXC.addWidget(label)
                self.cift+=1
            if self.cift >self.tek :
                labell = QLabel()
                labell.setFixedSize(350, 200)
                H_BOXT.addWidget(label)
                self.tek +=1


        os.chdir(ilk_mekan + '\DataBase')
        #for btn in label_list :
        #H_BOXC.addWidget(btn)

        V_BOX.addLayout(H_BOXC)
        V_BOX.addLayout(H_BOXT)
        lay.addLayout(V_BOX)
        if 0<len(ssss) < 3 :
            self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())

            self.setStyleSheet("QScrollArea{min-width:750 px; min-height: 200}")
        elif 2 <len(ssss) <5 :

            self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())

            self.setStyleSheet("QScrollArea{min-width:750 px; min-height: 400}")

        else:
            self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())

            self.setStyleSheet("QScrollArea{min-width:750 px; min-height: 600}")



    def click(self) :
        global ssss
        sender = self.sender()
        self.hide()
        self.ekran2 = Resim_ekrani(ssss[int(sender.text()) - 1])
        self.ekran2.show()
class doviz_ekran(QWidget):

    def __init__(self):
        super().__init__()
        self.set_ui()
    def set_ui(self):
        self.V_BOX1 = QVBoxLayout()
        self.H_BOX1 = QHBoxLayout()
        self.H_BOX2 = QHBoxLayout()
        self.H_BOX3 = QHBoxLayout()
        self.H_BOX4 = QHBoxLayout()
        self.H_BOX5 = QHBoxLayout()
        self.h_box_list = [self.H_BOX1,self.H_BOX2,self.H_BOX3,self.H_BOX4,self.H_BOX5]
        self.veri_ekleme()
        self.setLayout(self.H_BOX1)
    def veri_ekleme(self):
        url = 'https://www.bloomberght.com/doviz'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')
        find = soup.find_all('tbody')
        find_n = find[5].find_all('tr')
        i = 0
        lay1 = QVBoxLayout()
        lay2 = QVBoxLayout()
        lay3 = QVBoxLayout()
        lay4 = QVBoxLayout()
        lay5 = QVBoxLayout()
        lay6 = QVBoxLayout()
        laylist = [lay1,lay2,lay3,lay4,lay5]
        for a in range(5) :
            for x in find_n[a].text.split() :
                laylist[a].addWidget(QLabel(str(x)))
                self.H_BOX1.addLayout(laylist[a])

class ekran3 (QWidget):
    def __init__(self):
        super().__init__()
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.yuksek = 22
        self.deneme()
        #self.hide()
    def deneme(self):
        self.resim = QLabel('',self)
        self.resim.setPixmap(self.preview_screen.scaled(350, 350,
                                                        Qt.KeepAspectRatio, Qt.SmoothTransformation))

        V_box = QVBoxLayout()
        V_box.addWidget(self.resim)
        self.setLayout(V_box)
        self.setWindowTitle('screenshot')
    def take_ss(self):
        self.resim.setPixmap(self.preview_screen.scaled(350, 350,
                                                              Qt.KeepAspectRatio, Qt.SmoothTransformation))
    def save_it(self):
        """ KONTROL EDİLECEK info.txxt ilk açılışta sıkıntı yapabilir...."""
        with open('info.txt','r')as d:
            self.yazi = d.readline()

        ss_id = 'ss'  + self.yazi + '.png'
        where = os.getcwd()
        os.chdir(where[0:len(where)-9]+'\\ScreenShot')
        self.preview_screen.save(ss_id)
        os.chdir(where)
        with open('info.txt','w') as d:
            d.write(str(int(self.yazi)+1))
class other_windows (QWidget):
    def __init__(self,sender,goal):
        super().__init__()
        self.senderr = sender
        self.goal = goal
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.other_ui()

    def other_ui(self):
        V_BOX1 = QVBoxLayout()
        V_BOX2 = QVBoxLayout()
        V_BOX3 = QVBoxLayout()

        H_BOX1 = QHBoxLayout()
        H_BOX2 = QHBoxLayout()
        H_BOX3 = QHBoxLayout()

        self.yazi_Alani = QLineEdit()
        self.titlee = QTextEdit()
        if self.goal == 'düzenle' :
            self.btn1 = QPushButton('DÜZENLE', self)
            self.btn1.clicked.connect(self.duzenle)
        elif self.goal == 'yeni':

            if self.senderr == 0 :
                self.btn1 = QPushButton('KAYDET', self)
                self.yazi_Alani.setText('ÖNCE İŞLEM YAPACAĞINIZ KÜTÜPHANEYİ SEÇİNİZ')

            else:

                self.btn1 = QPushButton('KAYDET', self)
                self.btn1.clicked.connect(self.yeni)

        btn2 = QPushButton('ÇIK',self)
        btn2.clicked.connect(self.qui)

        H_BOX1.addWidget(self.btn1)
        H_BOX1.addWidget(btn2)

        V_BOX1.addWidget(self.yazi_Alani)
        V_BOX1.addWidget(self.titlee)
        V_BOX1.addLayout(H_BOX1)
        self.setLayout(V_BOX1)
    def verileri_oku(self):
        global sayfa_numarasi
        global anlik_durum
        dbase = anlik_durum
        db = sqlite3.connect(dbase)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM datas")
        datas = cursor.fetchall()
        db.close()
        a = 0
        for x in datas[(sayfa_numarasi * 10 ) : (sayfa_numarasi + 1 )* 10]:
            if str(x[0]) == self.senderr :
                break
            else:
                a +=1
        self.sira = (sayfa_numarasi * 10) + a
        self.yazi_Alani.setText(str(datas[self.sira][0]))
        self.titlee.setText(str(datas[self.sira][1]))
    def duzenle(self):
        self.btn1.setText('ÇOK YAKINDA ANAM')
    def qui(self):
        self.close()
    def yeni(self):
        baslik = self.titlee.toPlainText()
        icerik = self.yazi_Alani.text()
        if self.yazi_Alani.text() == '' :
            pass
        elif self.titlee.toPlainText() == '' :
            pass
        else:
            db = sqlite3.connect(self.senderr)
            cursor = db.cursor()
            cursor.execute("""INSERT INTO datas  VALUES(?,?)""",(str(icerik),str(baslik)))
            db.commit()
            db.close()
            self.close()

class widgett(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_ui()
    def widget_ui(self):
        """SAYFA SAYISI"""
        global sayfa_numarasi
        sayfa_numarasi = 0

        global databases
        V_BOX  = QVBoxLayout()
        V_BOX2 = QVBoxLayout()
        V_BOX3 = QVBoxLayout()
        V_BOXANA=QVBoxLayout()

        H_BOX  = QHBoxLayout()
        H_BOX2 = QHBoxLayout()
        H_BOX3 = QHBoxLayout()




        btn1 = QPushButton("",self)
        btn2 = QPushButton("",self)
        btn3 = QPushButton("",self)
        btn4 = QPushButton("",self)
        btn5 = QPushButton("",self)
        btn6 = QPushButton("",self)
        btn7 = QPushButton("",self)
        btn8 = QPushButton("",self)
        btn9 = QPushButton("",self)
        btn10= QPushButton('',self)
        global btnlist
        btnlist = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10]



        for x in btnlist :
            x.setFixedSize(100,20)

            x.clicked.connect(self.note_menu)

        V_BOX.addWidget(btn1)
        V_BOX.addWidget(btn2)
        V_BOX.addWidget(btn3)
        V_BOX.addWidget(btn4)
        V_BOX.addWidget(btn5)
        V_BOX.addWidget(btn6)
        V_BOX.addWidget(btn7)
        V_BOX.addWidget(btn8)
        V_BOX.addWidget(btn9)
        V_BOX.addWidget(btn10)


        label1 = QLabel("KÜTÜPHANE SEKMESİNDEN",self)
        label2 = QLabel("İŞLEM YAPMAK ŞSTEDİĞİNİZ",self)
        label3 = QLabel("DOSYAYI SEÇİNİZ...",self)
        label4 = QLabel("",self)
        label5 = QLabel("",self)
        label6 = QLabel("",self)
        label7 = QLabel("",self)
        label8 = QLabel("",self)
        label9 = QLabel("",self)
        Label10= QLabel('',self)
        global Labelist
        Labelist = [label1, label2, label3, label4, label5, label6, label7, label8, label9,Label10]
        for L in Labelist:
            V_BOX2.addWidget(L)

        H_BOX.addLayout(V_BOX)
        H_BOX.addLayout(V_BOX2)
        H_BOX.addLayout(V_BOX3)

        V_BOXANA.addLayout(H_BOX)
        """ BOŞLUK """
        global bosluk
        bosluk =  "              "

        self.btngeri = QPushButton("<",self)
        self.btngeri.clicked.connect(self.sayfa_numarsi)
        self.sayfa = QLabel(bosluk + str(sayfa_numarasi + 1))
        self.btnileri= QPushButton(">",self)
        self.btnileri.clicked.connect(self.sayfa_numarsi)

        H_BOX2.addWidget(self.btngeri)
        H_BOX2.addWidget(self.sayfa)
        H_BOX2.addWidget(self.btnileri)


        V_BOXANA.addLayout(H_BOX2)
        self.setLayout(V_BOXANA)
    def sayfa_numarsi(self):
        global max_sayfa
        global sayfa_numarasi
        global bosluk
        sender = self.sender()
        global s
        s = 0
        global anlik_durum
        if sender.text() == ">" :
            if anlik_durum == 0 :
                pass
            else:
                if sayfa_numarasi == max_sayfa :
                    self.deneme2()

                else:
                    sayfa_numarasi = int(sayfa_numarasi) + 1
                    self.sayfa.setText(str(sayfa_numarasi))
                    self.deneme2()
            if sender.text() == "<" :

                if sayfa_numarasi == 0 :
                    pass
                else:
                    sayfa_numarasi = int(sayfa_numarasi) - 1
                    self.sayfa.setText(str(bosluk + str(sayfa_numarasi + 1)))

                    self.deneme()

    def note_menu(self):
        sender = self.sender()
        if sender.text() == '':
            pass
        else:
            self.ekran2 = other_windows(sender.text(),'düzenle')
            self.ekran2.verileri_oku()
            self.ekran2.show()

    def deneme(self):
        global datas
        global anlik_durum
        global sayfa_numarasi
        global max_sayfa


        dbase = anlik_durum
        db = sqlite3.connect(dbase)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM datas")
        datas = cursor.fetchall()
        db.close()
        if int(len(datas[(sayfa_numarasi * 10) :  (sayfa_numarasi * 10) + 10])/10 ) == len(datas[(sayfa_numarasi * 10) :  (sayfa_numarasi * 10) + 10])/10 :
            a = 0
            for x in btnlist:

                x.setText(str(datas[sayfa_numarasi * 10 + a][0]))
                a += 1

            a = 0
            for x in Labelist:
                x.setText(ilk_n_satiri_Goster(str(datas[sayfa_numarasi * 10 + a][1])))
                a+=1
        else:
            for x in Labelist:
                x.setText("")
    def arayuz_guncelle(self):
        global anlik_durum
        global sayfa_numarasi
        global max_sayfa
        for x in btnlist :
            x.setText('')
        for x in Labelist :
            x.setText('')
    def deneme2(self):
        global datas
        global anlik_durum
        global sayfa_numarasi
        global max_sayfa
        global bosluk
        self.sayfa.setText(bosluk + str(sayfa_numarasi + 1 ))


        dbase = anlik_durum
        db = sqlite3.connect(dbase)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM datas")
        datas = cursor.fetchall()
        db.close()
        for x in btnlist :
            x.setText('')
        for x in Labelist :
            x.setText('')
        c = 0
        for x in datas[((sayfa_numarasi * 10)): (((sayfa_numarasi * 10) + 10))]:
            if c == 10:
                break
            btnlist[c].setText(str(x[0]))
            Labelist[c].setText(ilk_n_satiri_Goster(str(x[1])))
            c += 1

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_Ui()
        self.widget_ui = widgett()

        self.setGeometry(300, 300, 300, 100)

        self.setCentralWidget(self.widget_ui)
    def set_Ui(self):
        """      MENUBAR          """
        self.menu = self.menuBar()
        """      DATALAR           """
        global datalar

        dosya = self.menu.addMenu("dosya")
        dosya.triggered.connect(self.response)

        yenidoys = QAction("YENİ +", self)
        dosya.addAction(yenidoys)

        screenshot = QAction('screenshot' , self)
        dosya.addAction(screenshot)
        screenshot.setShortcut('Ctrl+Q')

        doviz = QAction('DÖVİZ DURUMU',self)
        dosya.addAction(doviz)
        exitAct = QAction('&Exit', self)
        #exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')

        fileMenu = self.menu.addMenu("file")
        fileMenu.addAction(exitAct)
        fileMenu.triggered.connect(self.response)

        self.kutuphane = self.menu.addMenu("Kütüphane")
        """   FONKSİYON ÇİFTLEME  """
        #self.kutuphane.triggered.connect(self.showng_screen)
        self.kutuphane.triggered.connect(self.veri_Degistir)    
        global databases
        databases = []
        for x in os.listdir() :
            if uzanti_bulma(x) == ".db" :
                self.kutuphane.addAction(str(x))
                databases.append(str(x))
            else:
                pass



        """      TOOLBAR          """
        toolbar = self.addToolBar("")
        NewFile = QAction((QIcon('1.png')),"YENİ", self)
        toolbar.addAction(NewFile)
        #toolbar.actionTriggered[QAction].connect(self.note_menu)

        ssshow = QAction((QIcon('2.png')),"ScreenShot", self)
        toolbar.addAction(ssshow)
        toolbar.actionTriggered[QAction].connect(self.note_menu)

        self.setWindowTitle("Notpad part2")
        self.show()
        if len(datalar) == 0 :

            self.verileri_ekleme()
    def screenshow(self):
        pass

    def note_menu(self,action):
        if action.text() == 'YENİ' :
            global anlik_durum
            self.ekran2 = other_windows(anlik_durum, 'yeni')
            self.ekran2.show()
        if action.text() == 'ScreenShot' :
            global label_list
            label_list = []
            self.lst = [str(i) for i in range(2000)]

            self.result = ScrollMessageBox(self.lst, None)
            self.result.exec_()
    def verileri_ekleme(self):
        text, ok = QInputDialog.getText(self, 'yeni not oluştur', "Not'un başlığı Yaz:")
        if ok:
            database_creating(text)
            self.kutuphaneye_ekleme(str(text) + '.db')
    def veri_Degistir(self,action):
        global anlik_durum
        global sayfa_numarasi
        global max_sayfa
        max_sayfa = max_sayfaa(action.text())

        sayfa_numarasi = 0

        anlik_durum = action.text()

        self.widget_ui.deneme2()

    def response(self,action):
        if action.text() == "YENİ +" :
            text, ok = QInputDialog.getText(self, 'yeni not oluştur', "Not'un başlığı Yaz:")
            if ok:
                database_creating(text)
                self.kutuphaneye_ekleme(text + '.db')

        if action.text() == 'screenshot' :
            self.hide()
            time.sleep(1)
            self.ekran4 = ekran3()
            self.ekran4.save_it()
            self.ekran4.show()
            self.show()
        if action.text() == 'DÖVİZ DURUMU' :
            self.ekran5 = doviz_ekran()
            self.ekran5.show()
    def kutuphaneye_ekleme(self,action):
        self.kutuphane.addAction(str(action))



def max_sayfaa(kutuphane):
    dbase =  kutuphane
    db = sqlite3.connect(dbase)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM datas")
    datass = cursor.fetchall()

    db.close()
    if int(len(datass)/10) == int(int(len(datass)/10)) :
        return int(len(datass)/10)
    else:
        return int(len(datass)/10) + 1
def database_creating(isim):
    db = sqlite3.connect(str(isim) + '.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS datas
                                                (title , content)""")
    db.close()
def begining():

    global ilk_mekan
    ilk_mekan = os.getcwd()
    ilk_liste = os.listdir()
    global anlik_durum
    anlik_durum = 0
    i = 0
    for x in os.listdir():
        if x == "DataBase":
            i = 1
            break

        else:
            pass
    if i == 0:
        os.mkdir("DataBase")

    g = 0
    for x in os.listdir():
        if x == "ScreenShot":
            g = 1
            break
        else:
            pass
    if g == 0:
        os.mkdir("ScreenShot")
    os.chdir(os.getcwd() + "\\DataBase")
    k = 0
    for x in os.listdir() :
        if x == 'info.txt' :
            k = 1
    if k == 0 :
        with open('info.txt',"w")as d:
            d.write('1')
    """   ANLIK DURUM  """
    global datalar
    datalar = []
    for x in os.listdir() :
        if  uzanti_bulma(x) == '.db' :
            datalar.append(x)
        else :
            pass
    """   GLOBAL SS  """
    global ss
    os.chdir(ilk_mekan + '\ScreenShot')
    ss = []
    for x in os.listdir():
        if uzanti_bulma(x) == '.png':
            ss.append(x)
        else:
            pass
    os.chdir(ilk_mekan + "\\DataBase")
def ilk_n_satiri_Goster(isim):
    kelime = isim
    other_vord = ""
    sayi = len(isim)
    if sayi < 30 :
        fark = 30 - sayi
        while sayi < 30 :
            sayi+=1
            kelime =kelime + ' '
        return kelime
    elif sayi > 30 :
        a = 0
        for x in isim :
            if a == 20 :
                break
            if x == " " :
                pass
            other_vord = other_vord + str(x)
            a +=1
        return other_vord + '...'
def uzanti_bulma(dosya):

    d = dosya
    i = 0
    harfler = []
    for x in d :
        harfler.append(str(x))

        i +=1

    z = 0
    uzanti = []
    for x in harfler :
        if x == "." :
            uzanti.append(harfler[z])
            uzanti.append(harfler[z+1])
            uzanti.append(harfler[z+2])
            try:
                global uzantii
                uzanti.append(harfler[z+3])
                uzantii = (str(uzanti[0]) + str(uzanti[1]) + str(uzanti[2]) + str(uzanti[3]) )
            except:
                uzantii = (str(uzanti[0]) + str(uzanti[1]) + str(uzanti[2]))

        z +=1

    return uzantii
def cift_tek(rakam):
    tek = [1,3,5,7,9]
    cift = [0,2,4,6,8]

    basamak_sayisi =len(str(rakam))
    son_basamak = str(rakam)[basamak_sayisi - 1:basamak_sayisi]
    for x in tek :
        if int(x) == int(son_basamak) :
            return 'tek'
        else:
            pass
    return 'cift'

def uzanti_silme(isim):
    a = 0
    liste = []
    for x in isim :
        if x == '.' :
            break
        else:
            a +=1
            liste.append(str(x))
    kelime = ''
    for x in isim[0:a] :
        kelime +=str(x)

    return kelime


begining()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindows()
    sys.exit(app.exec_())

