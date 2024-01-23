# Importing the PdfWriter class from the PyPDF library
from pypdf import PdfWriter

# Importing the os module for file-related operations
import os   

# Creating an instance of PdfWriter to merge PDF files
merger = PdfWriter()

# Listing all files in the current directory with a '.pdf' extension
files = [file for file in os.listdir() if file.endswith('.pdf')]

# Iterating through each PDF file and appending it to the merger
for pdf in files:
    merger.append(pdf)

# Writing the merged content to a new PDF file named "new merger.pdf"
merger.write("new merger.pdf")

# Closing the PdfWriter instance
merger.close()
