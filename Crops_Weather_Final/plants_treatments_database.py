
from email.header import decode_header
from os import curdir
import sqlite3
from sqlite3.dbapi2 import Cursor
import datetime
from datetime import datetime, date
import pandas as pd

### Setting the Database Variables
file = "Planting.db"
connection = sqlite3.connect('planting.db', check_same_thread=False)
###Cursor = connection.cursor()


### Planting Database - This is for the Southeast US, replace as needed
crops_list = [('Asparagus', '2022-03-01', '2022-04-15', '--', '36 x 18', '4 crowns', '2 years'),
('Snap Beans (Spring)', '2022-04-15', '2022-07-01', '3/4 Pound', '36 x 2', '1', '50-60'),
('Snap Beans (Summer)', '2022-07-20', '2022-08-01', '3/4 Pound', '36 x 2', '1', '50-60'),
('Pole Beans (Spring)', '2022-04-15', '2022-07-01', '1/2 Pound', '36 x 4', '1', '60-70'),
('Pole Beans (Summer)', '2022-07-20', '2022-08-01', '1/2 Pound', '36 x 4', '1', '60-70'),
('Half Runner Beans (Spring)', '2022-04-15', '2022-07-01', '1/2 Pound', '36 x 2', '1', '55-65'),
('Half Runner Beans (Summer)', '2022-07-20', '2022-08-01', '1/2 Pound', '36 x 2', '1', '55-65'),
('Pole Lima Beans (Spring)', '2022-05-01', '2022-06-15', '1/2 Pound', '36 x 6', '1 1/2', '70-75'),
('Pole Lima Beans (Summer)', '2022-07-01', '2022-07-15', '1/2 Pound', '36 x 6', '1 1/2', '70-75'),
('Edible Soy Beans (Spring)', '2022-05-01', '2022-06-15', '1/2 Pound', '36 x 3', '1', '60-70'),
('Edible Soy Beans (Summer)', '2022-07-01', '2022-07-15', '1/2 Pound', '36 x 3', '1', '60-70'),
('Beets (Spring)', '2022-03-15', '2022-05-31', '1/2 Ounce', '30 x 2', '3/4', '50-60'),
('Beets (Summer)', '2022-07-15', '2022-08-31', '1/2 Ounce', '30 x 2', '3/4', '50-60'),
('Broccoli (Spring)', '2022-03-20', '2022-04-30', '1/2 Ounce', '36 x 18', '1/2', '60-70'),
('Broccoli (Summer)', '2022-08-15', '2022-09-15', '1/2 Ounce', '36 x 18', '1/2', '60-70'),
('Brussels Sprouts', '2022-08-15', '2022-09-15', '1/2 Ounce', '36 x 18', '1/2', '90-100'),
('Cabbage (Spring)', '2022-03-15', '2022-04-30', '1/2 Ounce', '36 x 12', '3', '60-80'),
('Cabbage (Summer)', '2022-07-15', '2022-08-31', '1/2 Ounce', '36 x 12', '3', '60-80'),
('Cantaloupe', '2022-04-15', '2022-06-05', '1 Ounce', '60 x 24', '1', '75-85'),
('Carrots (Spring)', '2022-02-15', '2022-03-31', '1/4 Ounce', '30 x 1', '1/4', '60-70'),
('Carrots (Summer)', '2022-08-01', '2022-09-15', '1/4 Ounce', '30 x 1', '1/4', '60-70'),
('Cauliflower (Spring)', '2022-03-20', '2022-04-30', '1/4 Ounce', '36 x 18', '1/2', '60-70'),
('Cauliflower (Summer)', '2022-07-15', '2022-08-31', '1/4 Ounce', '36 x 18', '1/2', '60-70'),
('Collards (Spring)', '2022-03-15', '2022-06-30', '1/2 Ounce', '36 x 8', '1/2', '60-70'),
('Collards (Summer)', '2022-08-01', '2022-09-30', '1/2 Ounce', '36 x 8', '1/2', '60-70'),
('Cucumber (Spring)', '2022-04-15', '2022-06-05', '1 Ounce', '60 x 12', '1', '50-60'),
('Cucumber (Summer)', '2022-08-01', '2022-09-30', '1 Ounce', '60 x 12', '1', '50-60'),
('Eggplant', '2022-05-01', '2022-06-30', '--', '36 x 18', '3', '70-80'),
('Garlic', '2022-08-15', '2022-10-15', '--', '--', '--', '--'),
('Kale (Spring)', '2022-03-15', '2022-06-30', '1/2 Ounce', '36 x 1', '1/2', '50-55'),
('Kale (Summer)', '2022-08-01', '2022-09-30', '1/2 Ounce', '36 x 1', '1/2', '50-55'),
('Leeks', '2022-03-15', '2022-06-30', '--', '--', '--', '--'),
('Lettuce', '2022-03-01', '2022-05-15', '--', '--', '--', '--'),
('Mustard (Spring)', '2022-03-15', '2022-07-30', '--', '--', '--', '--'),
('Mustard (Summer', '2022-08-01', '2022-09-15', '--', '--', '--', '--'),
('Onion, sets (Spring)', '2022-02-15', '2022-03-30', '--', '--', '--', '--'),
('Onion, sets (Summer)', '2022-09-15', '2022-10-15', '--', '--', '--', '--'),
('Okra', '2022-05-15', '2022-06-15', '1 Ounce', '36 x 9', '3/4', '60-70'),
('Peanuts', '2022-05-01', '2022-06-30', '1/4 Pound', '30 x 4', '1 1/2', '100-120'),
('Garden Peas (Spring)', '2022-03-01', '2022-04-05', '1 Pound', '36 x 1', '1 1/2', '65-80'),
('Garden Peas (Summer)', '2022-08-15', '2022-10-30', '1 Pound', '36 x 1', '1 1/2', '65-80'),
('Pepper', '2022-05-01', '2022-06-30', '--', '36 x 18', '3', '60-70'),
('Irish Potatoes', '2022-03-15', '2022-04-30', '12 Pounds', '36 x 12', '3', '90-110'),
('Sweet Potatoes', '2022-05-01', '2022-06-15', '--', '36 x 8', '3', '120'),
('Pumpkins', '2022-06-15', '2022-07-15', '--', '--', '--', '--'),
('Radish (Spring)', '2022-03-15', '2022-06-30', '1/2 Ounce', '24 x 1', '1/2', '25-30'),
('Radish (Summer)', '2022-08-01', '2022-09-15', '1/2 Ounce', '24 x 1', '1/2', '25-30'),
('Rutabaga (Spring)', '2022-03-15', '2022-04-30', '1/2 Ounce', '36 x 12', '3/4', '100-110'),
('Rutabaga (Summer)', '2022-07-15', '2022-09-30', '1/2 Ounce', '36 x 12', '3/4', '100-110'),
('Spinach (Spring)', '2022-03-15', '2022-04-15', '1 Ounce', '30 x 2', '1/2', '50-60'),
('Spinach (Summer)', '2022-08-01', '2022-09-30', '1 Ounce', '30 x 2', '1/2', '50-60'),
('Sweet Corn', '2022-03-30', '2022-05-31', '4 Ounces', '36 x 10', '1', '80-95'),
('Summer Squash', '2022-04-15', '2022-08-15', '1 Ounce', '36 x 15', '1', '50-60'),
('Winter Squash', '2022-04-15', '2022-06-15', '1/2 Ounce', '60 x 48', '1 1/2', '90-120'),
('Tomato', '2022-05-01', '2022-06-30', '--', '60 x 24', '4', '70-80'),
('Turnips (Spring)', '2022-03-15', '2022-04-30', '1/4 Ounce', '30 x 2', '1/2', '60-70'),
('Turnips (Summer)', '2022-08-01', '2022-09-15', '1/4 Ounce', '30 x 2', '1/2', '60-70'),
('Watermelon', '2022-04-15', '2022-06-15', '1/2 Ounce', '60 x 60', '1 1/2', '80-100')]


### Function Definitions for Database Maintenance
def TryConnect():
    try:
        conn = sqlite3.connect(file, check_same_thread=False)
        return "Sucessful Connection"
    except:
       return "Failed Connection"


def CreateTableValidation():
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Crops_Fin
                (Crop TEXT, PlantingStart DATE, PlantingEnd DATE, Seed TEXT, Spacing TEXT, PlantingDepth TEXT, DaystoHarvest TEXT )''')
    connection.commit()
    c.close()
    return "Table Validated"

def CreateTableValidation_Neem_Oil():
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Neem_Oil
                (ApplicationDate DATE)''')
    connection.commit()
    c.close()
    return "Table Validated"

def CreateTableValidation_Epsom_Salt():
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Epsom_Salt
                (ApplicationDate DATE)''')
    connection.commit()
    c.close()
    return "Table Validated"

def CreateTableValidation_Fertilizer():
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Fertilizer
                (ApplicationDate DATE)''')
    connection.commit()
    c.close()
    return "Table Validated"

def PopCropTableIfEmpty():
    c = connection.cursor()
    target_actual_search = c.execute('''select Crop from Crops_Fin''')
    target_actual= len(c.fetchall())
    if target_actual < 1:
        c.executemany("insert into Crops_Fin values (?,?,?,?,?,?,?)", crops_list)
        connection.commit()
        c.close()
        return "Table Populated"
    else:
        return "Table Currently Populated"


def convertTuple(tup):
    str = ''.join(tup)
    return str

def add_years(start_date, years):
    try:
        return start_date.replace(year=start_date.year + years)
    except ValueError:
        # preseve calendar day (if Feb 29th doesn't exist, set to 28th)
        return start_date.replace(year=start_date.year + years, day=28)


def planting_date_updates():
    c = connection.cursor()
    update_search = c.execute('''select Crop, PlantingStart, PlantingEnd from Crops_Fin WHERE PlantingEnd < datetime('now', 'localtime')''')
    fetch_update_rows = c.fetchall()
    for row in fetch_update_rows:
        string1 = convertTuple(row)
        plant = row[0]
        plantdate1 = row[1]
        plantdate2 = row[2]
        date_object1 = datetime.strptime(plantdate1, '%Y-%m-%d').date()
        updated_date1 = add_years(date_object1, 1)
        date_object2 = datetime.strptime(plantdate2, '%Y-%m-%d').date()
        updated_date2 = add_years(date_object2, 1)
        c.execute(''' UPDATE Crops_Fin SET PlantingStart = ?, PlantingEnd = ? WHERE Crop = ?''', (updated_date1, updated_date2, plant))
        connection.commit()
        c.close()
    return "Planting Dates Updated"

def plant_now():
    c = connection.cursor()
    for row in c.execute("select * from Crops_Fin where datetime('now', 'localtime') BETWEEN PlantingStart and PlantingEnd"):
        print(row)
    c.close()

def full_crop_table():
    c = connection.cursor()
    for row in Cursor.execute("select * from Crops_fin"):
        print(row)
    c.close()


### Main Function to call the above subfunctions to validate the database and Update the plating dates
def plant_db_spin_up():
    TryConnect()
    CreateTableValidation()
    CreateTableValidation_Neem_Oil()
    CreateTableValidation_Epsom_Salt()
    CreateTableValidation_Fertilizer()
    PopCropTableIfEmpty()
    planting_date_updates()

### Define Function for update_planting_db.py to be scheduled in CHRON/Task Scheduler
def plant_Update_process():
    print(TryConnect())
    print(planting_date_updates())

### Define Functons for Streamlit Calls
def Neem_Oil_Insert():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Neem_Oil()
    c.execute('''INSERT INTO Neem_Oil VALUES (date(datetime('now', 'localtime')))''')
    connection.commit()
    c.close()

def Neem_Oil_Update():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Neem_Oil()
    neem_oil_all = c.execute('''Select * from Neem_Oil''')
    count_neem_oil_all = len(c.fetchall())
    if count_neem_oil_all > 1:
        c.execute("DELETE from Neem_Oil where ApplicationDate = (select min(ApplicationDate) from Neem_Oil)")
        connection.commit()
        c.close()

def Neem_Oil_Update_button():
    Neem_Oil_Insert()
    Neem_Oil_Update()

def Neem_Oil_result():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Neem_Oil()
    neem_oil_query = c.execute("Select max(ApplicationDate) from Neem_Oil")
    neem_data = c.fetchall()
    c.close()
    return neem_data

def Epsom_Insert():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Epsom_Salt()
    c.execute('''INSERT INTO Epsom_Salt VALUES (date(datetime('now', 'localtime')))''')
    connection.commit()
    c.close()

def Epsom_Update():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Epsom_Salt()
    epsom_salt_all = c.execute('''Select * from Epsom_Salt''')
    count_epsom_salt_all = len(c.fetchall())
    if count_epsom_salt_all > 1:
        c.execute("DELETE from Epsom_Salt where ApplicationDate = (select min(ApplicationDate) from Epsom_salt)")
        connection.commit()
        c.close()

def Epsom_Update_button():
    Epsom_Insert()
    Epsom_Update()

def Epsom_Salt_result():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Epsom_Salt()
    epsom_salt_query = c.execute("Select max(ApplicationDate) from Epsom_Salt")
    epsom_data = c.fetchall()
    c.close()
    return epsom_data
        
def Fertilizer_Insert():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Fertilizer()
    c.execute('''INSERT INTO Fertilizer VALUES (date(datetime('now', 'localtime')))''')
    connection.commit()
    c.close()

def Fertilizer_Update():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Fertilizer()
    fertilizer_all = c.execute('''Select * from Fertilizer''')
    count_fertilizer_all = len(c.fetchall())
    if count_fertilizer_all > 1:
        c.execute("DELETE from Fertilizer where ApplicationDate = (select min(ApplicationDate) from Fertilizer)")
        connection.commit()
        c.close()

def Fertilizer_Update_button():
    Fertilizer_Insert()
    Fertilizer_Update()

def Fertilizer_result():
    c = connection.cursor()
    TryConnect()
    CreateTableValidation_Fertilizer()
    fertilizer_query = c.execute("Select max(ApplicationDate) from Fertilizer")
    fertilizer_data = c.fetchall()
    c.close()
    return fertilizer_data

def crops_stream_SQL_Output():
    c = connection.cursor()
    TryConnect()
    plant_db_spin_up()
    c.execute("select Crop, PlantingStart, PlantingEnd  from Crops_Fin where datetime('now', 'localtime') BETWEEN PlantingStart and PlantingEnd")
    data = c.fetchall()
    c.close()
    return data

"""
### DEBUG Functions ####
print(TryConnect())
print(CreateTableValidation())
target_actual_search = Cursor.execute('''select Crop from Crops_Fin''')
target_actual= len(Cursor.fetchall())
print(PopCropTableIfEmpty())
update_search = Cursor.execute('''select Crop, PlantingStart, PlantingEnd from Crops_Fin WHERE PlantingEnd < datetime('now', 'localtime')''')
fetch_update_rows = Cursor.fetchall()
print(planting_date_updates())
print("***********************************************")
print("What to plant now \n\n")
print(plant_now())
print("***********************************************")
print(full_crop_table())


print(plant_now())
"""