from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt


class Ui_openAndBrightness(QWidget):
    img_path = ''

    def setupUi(self, openAndBrightness):
        openAndBrightness.setObjectName("openAndBrightness")
        openAndBrightness.resize(652, 582)
        self.gridLayoutWidget = QtWidgets.QWidget(openAndBrightness)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 489, 661, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.MySlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.MySlider.setMinimum(0)
        self.MySlider.setMaximum(2000)
        self.MySlider.setOrientation(QtCore.Qt.Horizontal)
        self.MySlider.setObjectName("MySlider")
        self.MySlider.valueChanged.connect(self.change_val)
        self.MySlider.setDisabled(True)

        self.gridLayout.addWidget(self.MySlider, 1, 0, 1, 1)
        self.DisVal = QtWidgets.QLabel(self.gridLayoutWidget)
        self.DisVal.setAlignment(QtCore.Qt.AlignCenter)
        self.DisVal.setObjectName("DisVal")
        self.gridLayout.addWidget(self.DisVal, 0, 0, 1, 1)
        self.imageLabel = QtWidgets.QLabel(openAndBrightness)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 651, 451))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.browseBtn = QtWidgets.QPushButton(openAndBrightness)
        self.browseBtn.setGeometry(QtCore.QRect(330, 460, 311, 23))
        self.browseBtn.setObjectName("browseBtn")
        self.browseBtn.clicked.connect(self.browse_img)

        self.saveBtn = QtWidgets.QPushButton(openAndBrightness)
        self.saveBtn.setGeometry(QtCore.QRect(20, 460, 291, 23))
        self.saveBtn.setObjectName("saveBtn")
        self.saveBtn.clicked.connect(self.save_img)
        self.saveBtn.setDisabled(True)

        self.retranslateUi(openAndBrightness)
        QtCore.QMetaObject.connectSlotsByName(openAndBrightness)

    def retranslateUi(self, openAndBrightness):
        _translate = QtCore.QCoreApplication.translate
        openAndBrightness.setWindowTitle(_translate(
            "openAndBrightness", "openAndBrightness"))
        self.DisVal.setText(_translate("openAndBrightness", "0"))
        self.browseBtn.setText(_translate("openAndBrightness", "Browse"))
        self.saveBtn.setText(_translate("openAndBrightness", "Save"))

    # Browse Image
    def browse_img(self):
        filename = QFileDialog.getOpenFileName(
            self, 'Open Image', 'C:\\', 'Image Only (*.jpg)')
        self.img_path = filename[0]
        self.imageLabel.setPixmap(QtGui.QPixmap(self.img_path))

        # Enable slider and save image after importing
        self.MySlider.setDisabled(
            True) if self.img_path == '' else self.MySlider.setDisabled(False)
        self.saveBtn.setDisabled(
            True) if self.img_path == '' else self.saveBtn.setDisabled(False)

    # Birghtness Adjustment and changing label value
    def change_val(self):
        # Changing label value
        brightness_value = (self.MySlider.value()+1000)/1000
        self.DisVal.setText(str(brightness_value))

        # Enhancement
        self.original_img = Image.open(self.img_path)
        enhancer = ImageEnhance.Brightness(self.original_img)
        self.brighted_image = enhancer.enhance(brightness_value)

        # Converting to pixmap
        self.qim = ImageQt(self.brighted_image)
        self.pix = QtGui.QPixmap.fromImage(self.qim)

        # Displaying
        self.imageLabel.setPixmap(QtGui.QPixmap(self.pix))

    # Save image
    def save_img(self):
        filename = QFileDialog.getSaveFileName(
            self, 'Save Image', 'C:\\', 'JPG Only (*.jpg)')

        if filename[0] == '':
            pass
        else:
            self.brighted_image.save(filename[0])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    openAndBrightness = QtWidgets.QWidget()
    ui = Ui_openAndBrightness()
    ui.setupUi(openAndBrightness)
    openAndBrightness.show()
    sys.exit(app.exec_())
