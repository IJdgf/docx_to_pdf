import os, re
from convert_file import convert_to_doc_pdf 


def write_logs(logs: list, out_path: str):
    if os.path.exists(out_path):
        logs_path = os.path.join(out_path, '00_logs.txt')
        with open(logs_path, 'w') as logfile:
            logfile.write("\n".join(logs))

def create_out_dir(input_path: str) -> str:
    out_path =  input_path + '/000_output'
    logs = []
    try:
        if os.path.isdir(input_path):
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            else: 
                print("Already exists")
        else:
            print("It's not a directory or not exists!")
            logs.append("It's not a directory or not exists!")
            write_logs(logs, out_path)
            return "It's not a directory or not exists!"
    except IOError as ioe:
        print(f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {ioe}")
        logs.append(f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {ioe}")
        write_logs(logs, out_path)
        return f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {ioe}"
    except Exception as e:
        print(f"Kann nicht den Output-Folder erstellen: {e}")
        logs.append(f"IO-Fehler. Kann nicht den Output-Folder erstellen:\n {e}")
        write_logs(logs, out_path)
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
                    logs.append(": ".join((file, result)))
                else:
                    logs.append(": ".join((file, "Not a file")))
                    print(f"Not a file: {full_path}") 
            else:
                logs.append(": ".join((file, "Not a docx-file or bad naming")))
        write_logs(logs, out_path)
        return "Fertig!"
    except Exception as e:
        print(e)
        logs.append(f'Error: {e}')
        write_logs(logs, out_path)
        return e