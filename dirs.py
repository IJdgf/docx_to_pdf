import os
from convert_file import convert_to_doc_pdf 

def create_out_dir(input_path: str):
    out_path =  input_path + '/output'
    try:
        if os.path.isdir(input_path):
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            else: 
                print("Already exists")
        else:
            print("It's not a directory or not exists!")
    except IOError as ioe:
        print(f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {ioe}")
        return
    except Exception as e:
        print(f"Kann nicht den Output-Folder erstellen: {e}")
        return
    try:
        for file in os.listdir(input_path):
            full_path = os.path.join(input_path, file)
            if os.path.isfile(full_path):
                print(f"File: {full_path}") 
                convert_to_doc_pdf(full_path)
            else:
                print(f"Not a file: {full_path}") 
    except Exception as e:
        print(e)

input_path = 'E:\\Py_Projects\\word_to_pdf\\bspl' 

if __name__ == '__main__':
     create_out_dir(input_path)