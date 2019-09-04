from PyPDF2 import PdfFileMerger

numPDFs = int(input("Number of PDFs to merge: "))

merger = PdfFileMerger()

for i in range(1, numPDFs + 1):
	path = input("Filepath of PDF #" + str(i) + ": ")
	merger.append(path)

merger.write(input("Filepath of merged PDF: "))
merger.close()

print("Merging successful!")