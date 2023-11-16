import zipfile
import os

def extract_zip(zip_file_path, extract_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def analysys_of_a_folder(folder_path):
    sizes = []
    mtimes = []
    tableoflists = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            infos = os.stat(file_path)
            size1 = infos.st_size
            sizes.append(size1)
            mt = infos.st_mtime
            mtimes.append(mt)
            tableoflists.append(filename)
            if(sizes):
                maximum = max(sizes)
                minimum = min(sizes)
                m_timemax = tableoflists[mtimes.index(max(mtimes))]

    return f'Maximal filesize: {maximum}\nMinimal filesize: {minimum}\nMost recently modified file is: {m_timemax}'



if __name__ == '__main__':
    zip_file_path = r'C:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2\bitwy.zip'
    extract_path = r'C:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2'
    extracted_path = r'C:\Users\Ania\Documents\Bioinformatyka\2023-2024_3_rok\python\python-programs\konwersatoria2\bitwy'
    extract_zip(zip_file_path, extract_path)
    print(analysys_of_a_folder(extracted_path))
