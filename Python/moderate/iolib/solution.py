import psutil
# you can convert that object to a dictionary
before = dict(psutil.virtual_memory()._asdict())['percent']
print("Start Memory Usage:")
print(before)

with open ("myins.sql", "r") as fin:
    with open ("myinsR.sql", "w") as fout:
        data="S"
        while(data!=''):
            data=fin.readline()

            data=data.replace("`",'')
            data=data.replace("0)",'FALSE)')
            data=data.replace("1)",'TRUE)')
            data=data.replace("'????'",'NULL')
            fout.write(data)

print("Memory usage after load in lines:")
after = dict(psutil.virtual_memory()._asdict())['percent']
print(after)
print("Diffference:")
print(after-before)
print(" \n")
print("Start Memory Usage:")
print(before)


with open ("myins.sql", "r") as fin:
    with open ("myinsR.sql", "w") as fout:
        data= fin.read()
        data=data.replace("`",'')
        data=data.replace("0)",'FALSE)')
        data=data.replace("1)",'TRUE)')
        data=data.replace("'????'",'NULL')
        fout.write(data)

print("Memory usage after full load:")
after = dict(psutil.virtual_memory()._asdict())['percent']
print(after)
print("Difference:")
print(after-before)
