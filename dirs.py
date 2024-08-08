import os, re
from convert_file import convert_to_doc_pdf 

def create_out_dir(input_path: str):
    out_path =  input_path + '/000_output'
    try:
        if os.path.isdir(input_path):
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            else: 
                print("Already exists")
        else:
            print("It's not a directory or not exists!")
            return "It's not a directory or not exists!"
    except IOError as ioe:
        print(f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {ioe}")
        return f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {ioe}"
    except Exception as e:
        print(f"Kann nicht den Output-Folder erstellen: {e}")
        return f"Kann nicht den Output-Folder erstellen: {e}"
    try:
        docx_pattern = re.compile(r'.+\.docx$')
        for file in os.listdir(input_path):
            print(f"File: {file}") 
            if docx_pattern.match(file):
                full_path = os.path.join(input_path, file)
                if os.path.isfile(full_path):
                    result = convert_to_doc_pdf(full_path)
                    print(result)
                else:
                    print(f"Not a file: {full_path}") 
        return "Fertig!"
    except Exception as e:
        print(e)
        return e

# input_path = 'E:\\Py_Projects\\word_to_pdf\\bspl' 

# if __name__ == '__main__':
#      create_out_dir(input_path)