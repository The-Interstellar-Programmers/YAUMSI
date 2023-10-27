import sys
import subprocess  
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QComboBox
from PyQt6.QtGui import QFont, QFontDatabase, QPixmap  
from PyQt6.QtCore import Qt
import requests
from bs4 import BeautifulSoup



def is_macos_dark_mode():
    #Detects if macOS is in dark mode.
    try:
        mode = subprocess.check_output(['defaults', 'read', '-g', 'AppleInterfaceStyle']).decode().strip()
        return mode == "Dark"
    except subprocess.CalledProcessError:
        return False

class NewPage(QMainWindow):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(800, 300)
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        if parent:
            parent_pos = parent.pos()
            self.move(parent_pos.x() + 40, parent_pos.y() - 40)

"""
 __  __       _         _____                 
|  \/  |     (_)       |  __ \                
| \  / | __ _ _ _ __   | |__) |_ _  __ _  ___ 
| |\/| |/ _` | | '_ \  |  ___/ _` |/ _` |/ _ \
| |  | | (_| | | | | | | |  | (_| | (_| |  __/
|_|  |_|\__,_|_|_| |_| |_|   \__,_|\__, |\___|
                                    __/ |     
                                   |___/      
"""

class MinecraftServerHomePage(QMainWindow):
    
    
    
    def __init__(self):
        id = QFontDatabase.addApplicationFont("/Users/qingchen.deng/GitHub/YAUMSI/assets/fonts/MinecraftRegular-Bmg3.otf")
        if id < 0: print("Error")

        families = QFontDatabase.applicationFontFamilies(id)
        
        titlefz = QFont(families[0], 35)
        subtitlefz = QFont(families[0], 20)
        paragraphfz = QFont(families[0], 14)
        
        super().__init__()
        
        self.setStyleSheet("""  
            QMainWindow {  
                background-image: url('/Users/qingchen.deng/GitHub/YAUMSI/assets/img/menubg.png');  
                background-repeat: no-repeat;  
                
                background-position: center;  
            }  
        """)  
        #self.setGeometry(100, 100, 800, 600)  # 设置窗口的位置和大小  
        #self.setWindowTitle('Custom Background')  # 设置窗口标题  
        #self.show()

        self.setWindowTitle("Yet Another Universal Minecraft Server Installer - Home")
        #self.resize(800, 300)
        self.setFixedSize(1000, 450)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        title_layout = QHBoxLayout()
        
        
        font_color = "white" if is_macos_dark_mode() else "black"
        title = QLabel("Yet Another Universal Minecraft Server Installer\n(Version 0.0.1a)", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setBold(True)
        title_font.setItalic(True)
        title.setFont(titlefz)
        title.setStyleSheet(f"color: {font_color}; margin-bottom: 20px; background-color: transparent;")
        title_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addLayout(title_layout)

        self.install_btn = QPushButton("Install Minecraft Server", self)
        self.install_btn.setFont(subtitlefz) #self.get_button_font())
        self.install_btn.clicked.connect(self.install_clicked)
        main_layout.addWidget(self.install_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(20)

        self.settings_btn1 = QPushButton("Settings", self)
        self.settings_btn1.setFont(subtitlefz)
        self.settings_btn1.clicked.connect(self.settings_clicked)
        #self.settings_btn1.clicked.connect(self.settings_clicked)
        main_layout.addWidget(self.settings_btn1, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(20)

        self.help_btn = QPushButton("Help", self)
        self.help_btn.setFont(subtitlefz)
        self.help_btn.clicked.connect(self.help_clicked)
        main_layout.addWidget(self.help_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(20)

        self.credits_btn = QPushButton("Credits", self)
        self.credits_btn.setFont(subtitlefz)
        self.credits_btn.clicked.connect(self.credits_clicked)
        main_layout.addWidget(self.credits_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        central_widget.setLayout(main_layout)

        self.opened_windows = []

    def get_button_font(self):
        btn_font = QFont()
        btn_font.setBold(True)
        return btn_font



    def install_clicked(self):
        title = "Yet Another Universal Minecraft Server Installer - Installation"
        layout = QVBoxLayout()
        servertype_label = QLabel("Please Choose Your Server Type:",  alignment=Qt.AlignmentFlag.AlignCenter)
        # Add more widgets and configurations specific to Spigot here.
        layout.addWidget(servertype_label)
        # Combo Box
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Vanilla", "Spigot", "PaperMC", "Forge", "Bukkit"])
        layout.addWidget(self.combo_box, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Confirmation Button
        confirm_button = QPushButton("Ok, Let's Move On!", self)
        confirm_button.clicked.connect(self.confirm_server_type)
        layout.addWidget(confirm_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        new_page = NewPage(title, self)
        new_page.setCentralWidget(central_widget)
        new_page.show()
        self.opened_windows.append(new_page)

    def confirm_server_type(self):
        self.chosenServerType = self.combo_box.currentText()
        title = f"Yet Another Universal Minecraft Server Installer - {self.chosenServerType} Server Installation"
        server_page = NewPage(title, self)
        if self.chosenServerType == "Spigot":
            self.setup_spigot_page(server_page)
        elif self.chosenServerType == "PaperMC":
            self.setup_papermc_page(server_page)
        elif self.chosenServerType == "Forge":
            self.setup_forge_page(server_page)
        else:  # Vanilla
            self.setup_vanilla_page(server_page)
        server_page.show()
        self.opened_windows.append(server_page)



    
    def setup_spigot_page(self, page):
        try:
            spigot_versions_link = 'https://getbukkit.org/download/spigot'
            request = requests.get(spigot_versions_link)
            soup = BeautifulSoup(request.text, 'lxml')
            
            heading_tags = ["h2"]
            spigot_versions_list =  []
            for tags in soup.find_all(heading_tags):
                #(Test CODE)(Test CODE)(Test CODE)(Test CODE): print(tags.name + ' -> ' + tags.text.strip()) 
                spigot_versions_list.append(tags.text.strip())
            print(spigot_versions_list)
        except:
            print("Error Retriving Spigot Versions List.")
        
        layout = QVBoxLayout()
        setuplabel = QLabel("Spigot Setup Page")
        # Add more widgets and configurations specific to Spigot here.
        layout.addWidget(setuplabel)
        
        versionlabel = QLabel("Versions List:",  alignment=Qt.AlignmentFlag.AlignHCenter)
        # Add more widgets and configurations specific to Spigot here.
        layout.addWidget(versionlabel)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(spigot_versions_list)
        layout.addWidget(self.combo_box, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Confirmation Button
        confirm_button = QPushButton("Ok", self)
        confirm_button.clicked.connect(self.confirm_spigot_server_version)
        layout.addWidget(confirm_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        page.setCentralWidget(central_widget)
        


    def setup_papermc_page(self, page):
        layout = QVBoxLayout()
        label = QLabel("This is the PaperMC setup page!")
        # Add more widgets and configurations specific to PaperMC here.
        layout.addWidget(label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        page.setCentralWidget(central_widget)

    def setup_forge_page(self, page):
        layout = QVBoxLayout()
        label = QLabel("This is the Forge setup page!")
        # Add more widgets and configurations specific to Forge here.
        layout.addWidget(label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        page.setCentralWidget(central_widget)

    def setup_vanilla_page(self, page):
        layout = QVBoxLayout()
        label = QLabel("This is the Vanilla setup page!")
        # Add more widgets and configurations specific to Vanilla here.
        layout.addWidget(label)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        page.setCentralWidget(central_widget)
        

    def settings_clicked(self):
        title = "Yet Another Universal Minecraft Server Installer - Settings"
        new_page = NewPage(title, self)
        new_page.show()
        self.opened_windows.append(new_page)

    def help_clicked(self):
        title = "Yet Another Universal Minecraft Server Installer - Help"
        new_page = NewPage(title, self)
        new_page.show()
        self.opened_windows.append(new_page)

    def credits_clicked(self):
        title = "Yet Another Universal Minecraft Server Installer - Credits"
        new_page = NewPage(title, self)
        new_page.show()
        self.opened_windows.append(new_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MinecraftServerHomePage()
    window.show()
    sys.exit(app.exec())
