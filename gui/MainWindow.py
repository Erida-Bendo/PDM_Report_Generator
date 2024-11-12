from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel, QLineEdit, QMessageBox, QComboBox, QDateEdit
from PyQt5.QtCore import QDate
from PyQt5 import QtGui
import pandas as pd
from main import create_report, extract_excel_data


def clear_layout(layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()

class MainWindow(QWidget):
    def __init__(self):
        # Initialize the UI
        super().__init__()
        self.initUI()
        # Resize the window
        self.resize(500, 100)
        # Initialize the folder path
        self.folder_path = None
        

    def initUI(self):
        # Create and set up the UI elements
        self.setWindowTitle("PDM Report Generator")
        self.setWindowIcon(QtGui.QIcon('resources/logo.png'))
        loadExcelBtn = QPushButton('Select Excel File', self)
        loadExcelBtn.clicked.connect(self.load_excel)
        loadExcelBtn.setMinimumWidth(500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(loadExcelBtn)
    
    def load_excel(self):
        # Open a dialog to select a folder
        self.file_path = QFileDialog.getOpenFileName(self, 'Select Excel File', '', 'Excel Files (*.xlsx *.xls)')[0]
        self.excel_data = pd.ExcelFile(self.file_path)
        if self.excel_data is not None:
        # Clear the dialog box
            clear_layout(self.layout)

            projectName = QLabel('Type Project Name', self)
            self.projectNameValue = QLineEdit(self)
            projectCode = QLabel('Type Project Code', self)
            self.projectCodeValue = QLineEdit(self)

            generate = QPushButton('Generate', self)
            generate.clicked.connect(self.generate_report)

            self.sheet_dropdown = QComboBox(self)
            self.sheet_dropdown.addItems(self.excel_data.sheet_names)
            self.sheet_dropdown.currentIndexChanged.connect(self.update_columns)
            
            self.doc_title = QComboBox(self)
            self.page_type = QComboBox(self)
            self.drawing_no = QComboBox(self)
            self.author = QComboBox(self)
            self.checker = QComboBox(self)
            self.revision = QComboBox(self)
            
            self.date = QLineEdit(self)

            loadFolderBtn = QPushButton('Select Output Folder', self)
            loadFolderBtn.clicked.connect(self.load_output)

            self.layout.addWidget(projectName)
            self.layout.addWidget(self.projectNameValue)
            self.layout.addWidget(projectCode)
            self.layout.addWidget(self.projectCodeValue)
            
            self.layout.addWidget(QLabel('Select Worksheet:', self))
            self.layout.addWidget(self.sheet_dropdown)

            self.layout.addWidget(QLabel('Select Column of Document Title:', self))
            self.layout.addWidget(self.doc_title)
            self.layout.addWidget(QLabel('Select Column of Page Type:', self))
            self.layout.addWidget(self.page_type)
            self.layout.addWidget(QLabel('Select Column of Drawing Number:', self))
            self.layout.addWidget(self.drawing_no)
            self.layout.addWidget(QLabel('Select Column of Author:', self))
            self.layout.addWidget(self.author)
            self.layout.addWidget(QLabel('Select Column of Checker:', self))
            self.layout.addWidget(self.checker)
            self.layout.addWidget(QLabel('Select Column of Revision number:', self))
            self.layout.addWidget(self.revision)
            self.date_edit = QDateEdit(self)
            self.date_edit.setCalendarPopup(True)
            self.date_edit.setDate(QDate(2024, 1, 1))
            self.layout.addWidget(QLabel('Select a Date:', self))
            self.layout.addWidget(self.date_edit)

            
            self.layout.addWidget(loadFolderBtn)
            self.layout.addWidget(generate)

    def load_output(self):
        # Open a dialog to select a folder
        self.output_path = QFileDialog.getExistingDirectory(self, 'Select Output Folder')


    def generate_excel_column_titles(self, num_columns):
        titles = []
        for i in range(num_columns):
            title = ''
            while i >= 0:
                title = chr(i % 26 + 65) + title
                i = i // 26 - 1
            titles.append(title)
        return titles

    def update_columns(self):
        # Get the selected sheet name
        sheet_name = self.sheet_dropdown.currentText()

        # Load the sheet into a DataFrame
        df = pd.read_excel(self.file_path, sheet_name=sheet_name)

        column_titles = self.generate_excel_column_titles(len(df.columns))

        # Clear the column dropdown and add new items
        self.doc_title.clear()
        self.doc_title.addItems(column_titles)
        self.page_type.clear()
        self.page_type.addItems(column_titles)
        self.drawing_no.clear()
        self.drawing_no.addItems(column_titles)
        self.author.clear()
        self.author.addItems(column_titles)
        self.checker.clear()
        self.checker.addItems(column_titles)
        self.revision.clear()
        self.revision.addItems(column_titles)

    def generate_report(self):
        # Generate a report based on the files in the selected folder
        
        try:
            data = extract_excel_data(self.file_path, self.sheet_dropdown.currentText(), self.revision.currentIndex(),
                                      self.doc_title.currentIndex(), self.page_type.currentIndex(),
                                      self.drawing_no.currentIndex(), self.author.currentIndex(),
                                      self.checker.currentIndex())
            
            selected_date=self.date_edit.date()
            date_number=selected_date.toString('dd.MM.yyyy')
            date_month=selected_date.toString('dd MMMM yyyy')

            for item in data:
                auth_name = item['author']
                check_name = item['checker']
                words = auth_name.split()
                auth_init = ''.join([word[0] for word in words]) 
                words = check_name.split()
                check_init = ''.join([word[0] for word in words]) 
                email_id = auth_name.lower().replace(' ', '.') + "@burohappold.com"
                output_path=str(self.output_path)
                # Create a sensible file name
                file_name = f"{output_path}//{item['proj_name'].replace(' ', '_')}_{item['proj_code']}.tex"
                folder_name = f"{output_path}//{item['proj_name'].replace(' ', '_')}_{item['proj_code']}"
                
                create_report(date_number, date_month, str(self.projectNameValue.text()), str(self.projectCodeValue.text()), folder_name, file_name, item['proj_name'], item['proj_code'].replace('_','\\_'), item['rev_num'].replace('_','\\_'), auth_name, item['proj_name'], check_name, auth_init, check_init, email_id, item['page_type'])
            
            if not data:
                print("No data was extracted! Please check the debug output above.")
                
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        QMessageBox.information(self, "Success", "Report successfully generated!🥳\nPlease check the folder.")
    