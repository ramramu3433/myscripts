import zipfile
import os,sys


def compress():
    zpath1=sys.argv[1]
    zpath=zpath1+'.zip'
    folder=sys.argv[2]

    zf=zipfile.ZipFile(zpath,'w')
    for directories,subdirs,files in os.walk(folder):
        zf.write(directories)
        for filecompress in files:
            zf.write(os.path.join(directories,filecompress))

 
    zf.close()


if __name__=='__main__':
   compress()
