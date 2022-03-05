line = ""
with open('countres_list.txt') as f:
    line = f.readline()

countres_list = [country.strip().lower() for country in line.split()]

