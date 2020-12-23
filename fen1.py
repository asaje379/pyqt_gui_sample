from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from fen2 import Fen2
import matplotlib.pyplot as plt

btnCss = ''' 
    background-color: midnightblue;
    color: #fff;
    border: none;
    padding: 10px;
    border-radius: 5px
'''

# La classe Fen est un Widget donc elle 
# hérite de QWidget
class Fen(QWidget):
    
    # Constructeur
    def __init__(self):
        
        # On appelle le constructeur de la classe mère
        QWidget.__init__(self)
        
        self.lay = QVBoxLayout()
        
        self.button = QPushButton('Tracer la courbe')
        self.button.setStyleSheet(btnCss)
        
        self.ouvrir = QPushButton('Suivant')
        self.ouvrir.setStyleSheet(btnCss)
        
        self.courbe = QLabel()
        
        self.lay.addWidget(self.courbe)
        self.lay.addWidget(self.button)
        self.lay.addWidget(self.ouvrir)
        self.setLayout(self.lay)
        
        self.fen2 = None
        
        # On connecte le clicked des boutons aux méthodes correspondantes
        # Attention c'est uniquement le nom de la fonction qui est passée
        # en paramètre de connect
        self.button.clicked.connect(self.drawCurve)
        self.ouvrir.clicked.connect(self.openFen2)
        
    def drawCurve(self):
        x = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
        y = [4, 5, 2, 0, 1, 9, 7]
        
        # On dessine la courbe
        plt.plot(x, y)
        
        # On enregistre l'image de la courbe dans le dossier courant
        plt.savefig('courbe.png')
        
        # On recharge l'image dans l'interface
        imageFile = QImage('courbe.png')
        pixmap = QPixmap.fromImage(imageFile)
        self.courbe.setPixmap(pixmap)
        
        # Vous pouvez décommenter cette ligne pour voir le comportement
        plt.clf()
        
    def openFen2(self):
        self.fen2 = Fen2()
        
        # On cache la fenetre actuelle
        self.hide()
        
        # On ouvre la fenetre 2
        self.fen2.show()
        
        
        
    
        
