import csv


def list_of_years():
    with open('csvs/API_SP.POP.TOTL_DS2_en_csv_v2_1120881.csv') as csv_year_list:
        csv_reader = csv.reader(csv_year_list, delimiter=',')
        row_count = 0
        column_count = 0
        year_list = []
        for i in csv_reader:
            if row_count == 2:
                for j in i:
                    if 3 < column_count < 64:
                        year_list.append(j)
                    column_count += 1
            row_count += 1
        return year_list


def list_of_countries():
    with open('csvs/API_SP.POP.TOTL_DS2_en_csv_v2_1120881.csv') as csv_country_list:
        csv_reader = csv.reader(csv_country_list, delimiter=',')
        line_count = 0
        country_list = []
        for i in csv_reader:
            if 2 < line_count < 267:
                country_list.append(i[0])
            line_count += 1
        return country_list

def world_population(country_year):
    country = country_year[0]
    year = country_year[1]
    with open('csvs/API_SP.POP.TOTL_DS2_en_csv_v2_1120881.csv') as csv_world_population:
        csv_reader = csv.reader(csv_world_population, delimiter=',')
        line_count = 0
        for i in csv_reader:
            if line_count == 2:
                column = int(i.index(year))
            if i[0] == country:
                row = i
            line_count += 1
        return int(row[column-1])


def total_people():
    with open('csvs/Bevolking__geslacht__leeftijd_en_burgerlijke_staat__1_januari_12062020_114527.csv') as csv_bevolking:
        csv_reader = csv.reader(csv_bevolking, delimiter=';')
        line_count = 0
        totalpeople = []
        for i in csv_reader:
            try:
                if 8 < line_count < 29:
                    totalpeople.append(i[1])
            except:
                continue
            line_count += 1
    return totalpeople


def dead_people():
    with open('csvs/leeftijd-en-geslacht-overledenen.csv') as csv_dead:
        csv_reader = csv.reader(csv_dead, delimiter=';')
        line_count = 0
        deadpeople = []
        for i in csv_reader:
            try:
                if line_count > 0:
                    deadpeople.append(i[3])
            except:
                continue
            line_count += 1
    return deadpeople
