def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person("mkv",age=26, height=5.1,number=738)
