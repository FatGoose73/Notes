import os
import argparse


def genPath(dirStr):
    """
    dirStr: 文件存储目录
    """
    filePath = [path for path in os.listdir(dirStr)]
    for p in filePath:
        curretnGenPath = '- [{}]({}/{})'.format(os.path.basename(p).split('.')[0], dirStr, p)
        print(curretnGenPath) 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fast generate markdown used path for docsify')
    parser.add_argument('-d', '--dirStr', default='./')
    args = parser.parse_args()
    genPath(args.dirStr)    