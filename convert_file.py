import win32com.client as win32
import os


def  convert_to_doc_pdf(input_path: str):
    try:
        # Creating an object Word
        word = win32.gencache.EnsureDispatch('Word.Application')
        # word = win32.Dispatch('Word.Application')  # The same
        word.Visible = False

        # Openint the document DOCX
        print(f"Opening document: {input_path}")
        doc = word.Documents.Open(input_path)
        print("Opened!")
        print("doc", doc)

        out_dir, out_file = os.path.split(input_path)
        out_path = os.path.join(out_dir, "output", out_file)
        # Saving as DOC
        doc_path = out_path.replace('.docx', '.doc')
        print(f"Saving as DOC: {doc_path}")
        doc.SaveAs(doc_path, FileFormat=0) # 0 == doc
        # Saving as pdf
        pdf_path = out_path.replace('.docx', '.pdf')
        print(f"Saving as DOC: {pdf_path}")
        doc.SaveAs(pdf_path, FileFormat=17) # 17 == pdf

        # Closing the document and the Word
        print("Closing document...")
        doc.Close(SaveChanges=False)
        print("Quitting Word application...")
        word.Quit()

        # Setting the resources free
        del doc
        del word
        print("Conversion successful.")
    except Exception as e:
        print('Error!', e)

if __name__ == '__main__':
    input_path = 'E:\\Py_Projects\\word_to_pdf\\bspl\\CV_Jakutow.docx' 
    convert_to_doc_pdf(input_path)
