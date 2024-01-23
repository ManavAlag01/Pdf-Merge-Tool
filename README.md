# PDF Merger Tool

This Python script utilizes the PyPDF library to merge multiple PDF files into a single PDF file.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required library using the following command:

   ```bash
   pip install PyPDF2

Place the PDF files you want to merge in the same directory as the script.
<br>
Run the script using the following command: python PDF_Merger.py
<br>
The merged PDF file will be created in the same directory with the name "new merger.pdf".

## Script Explanation
The script uses the PyPDF library to:

Create a PdfWriter instance for merging PDFs.
<br>
Retrieve a list of PDF files in the current directory.
<br>
Iterate through each PDF file, appending it to the PdfWriter.
<br>
Write the merged content to a new PDF file named "new merger.pdf".

   

