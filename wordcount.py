import re

chr = {"!","\"","{","}",",","|",".","-","(",")","&","%","^",":",";","#","$","@","~","*","/","-","+","\\","?"}

fin = open("rawdata.txt",'r')
fout = open("finaldata.txt",'w')
for lines in fin:
    for i in chr:
        lines=lines.replace(i,"")
    " ".join(lines.split())
    lines=lines.replace(" ", ",")
    fout.write(lines)
fin.close()
fout.close()



'''
some_string = "This will remove@$#^@!* the double \"quotes as\" well, which is not "
for i in chr:
    some_string=some_string.replace(i,"")
    " ".join(some_string.split())
    some_string=some_string.replace(" ", ",")
chr = {"!","\"","{","}",",","|",".","-","(",")","&","%","^",":",";","#","$","@","~","*","/","-","+","\\","?"}
#','.join(re.findall('', some_string))
print(some_string)
#print(s)
'''
