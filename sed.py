def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f1 = open(source)
    f2 = open(dest, 'w')

    for line in f1:
        new_line = line.replace(pattern, replace)
        f2.write(new_line) 

    f1.close()
    f2.close()



pattern = 'Hey Jude'
replace = 'Hi Donald'
source = 'sed_tester.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)