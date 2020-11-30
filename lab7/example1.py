inp1 = [("Sıla",21), ("Elif",20), ("Buse" ,17), ("Çıtır", 16)]
inp1d = dict(inp1)
for i in inp1d:
    if inp1d.get(i) > 18:
        print(i)