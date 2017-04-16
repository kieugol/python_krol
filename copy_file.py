import sys

if len(sys.argv) !=3:
    print('copy file to another folder')
else:
    try:
        with open(sys.argv[1], 'r') as inf, open(sys.argv[2], 'w') as outf:
            for line in inf:
               outf.write(line)
    except IOError:
        print('{} File do not exist ...'.format(sys.argv[1]))