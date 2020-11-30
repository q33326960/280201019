books = ["DAS KAPITAL","COMMUNIST MANIFESTO","KADINSIZ ERKEKLER"]
book_dict = dict()
charl = list()
for i in books:
    charl = []
    for char in i:
        if char not in charl:
            charl.append(char)       
    book_dict[i] = (len(i),len(charl))
print(book_dict)