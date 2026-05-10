def main():
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    widget = QOpusWidget()
    widget.show()
    sys.exit(app.exec_())