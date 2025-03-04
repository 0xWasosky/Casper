import os 
import shutil
import secrets
import sys 


def shred(file_name: str, file_size: int):
    data = secrets.token_bytes(file_size)

    with open(file_name, 'wb') as f:
        f.write(data)

    os.remove(file_name)

def main():
    dir_ = sys.argv[1]
    n_shredding = int(sys.argv[2])

    for root, dirs, files in os.walk(dir_, topdown=False):
        for file in files:
            f = root + '/' + file
            size =  os.path.getsize(f)
            for _ in range(n_shredding):
                f = root + '/' + file
                shred(f,size)
    shutil.rmtree(dir_)
                
                
    
if __name__ == "__main__":
    main()

