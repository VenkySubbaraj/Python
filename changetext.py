search_txt = "occupation" 
replace_txt = "age"

with open(r'./classname.py','r') as file:
    data = file.read()
    print(data)

    data = data.replace(search_txt, replace_txt)
    print(data, "data after replace")

with open(r'./classname.py','w') as file:
    file.write(data)
