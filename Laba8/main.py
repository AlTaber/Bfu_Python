import os
import random
import csv

class Laba8:
    def __init__(self, file_path=""):
        self.file_path = file_path
        if file_path == "":
            self.file_path = os.path.join(os.getcwd(), "data.csv")
            with open(self.file_path, "w+", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Age", "City", "Age_Squired", "Bool"])
                for _ in range(100):
                    name = random.choice(["Абоба", "Абобус", "Амогус", "Влад", "Андрей", None])
                    age = random.randint(2, 42)
                    city = random.choice(["Москва", "Калининград", "Санкт-Петербург", "Отсо City", "Город Влада", None])
                    age_squired = age * age
                    bool_value = random.choice([True, False])
                    writer.writerow([name, age, city, age_squired, bool_value]) 
        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.data = [row for row in reader]
    
    def show(self, output_style="top", amount=5, separator=" "): 
        if len(self.data) < amount:
            print(f"Данных недостаточно чтобы вывести {amount} строк")
            amount = len(self.data)
        
        match output_style:
            case "top":
                for i in range(amount):
                    print(separator.join([str(self.data[i][key]) for key in self.data[i]]))
            case "bottom":
                for i in range(len(self.data) - amount, len(self.data)):
                    print(separator.join([str(self.data[i][key]) for key in self.data[i]]))
            case "random":
                for i in random.sample(range(len(self.data)), amount):
                    print(separator.join([str(self.data[i][key]) for key in self.data[i]]))
    
    def info(self):
        print(f"{len(self.data)}x{len(self.data[0])}")
        for key in self.data[0]:
            count = 0
            type_value = "str"
            type_found = False
            for row in self.data:
                if row[key]:
                    count += 1
                    if type_found:
                        continue
                    if row[key] in ["True", "False"]:
                        type_value = "bool"
                        type_found = True
                    elif row[key].isdigit():
                        type_value = "int"
                        type_found = True
            print(f"{key} {count} {type_value}")
    
    def DelNaN(self):
        self.data = [row for row in self.data if all(row.values())]
        print("Убраны строки с неполными данными")
    
    def MakeDS(self):
        workdata_path = os.path.join(os.getcwd(), "workdata")
        os.makedirs(workdata_path, exist_ok=True)
        os.makedirs(os.path.join(workdata_path, "Learning"), exist_ok=True)
        os.makedirs(os.path.join(workdata_path, "Testing"), exist_ok=True)
        train_amount = round(len(self.data) * 0.7)
        test_amount = len(self.data) - train_amount
        data_copy = self.data.copy()
        random.shuffle(data_copy)
        with open(os.path.join(workdata_path, "Learning", "train.csv"), "w+", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            for row in self.data[:train_amount]:
                writer.writerow(row)
        with open(os.path.join(workdata_path, "Testing", "test.csv"), "w+", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            for row in self.data[train_amount:]:
                writer.writerow(row)
    

A = Laba8()
A.info()
A.DelNaN()
A.info()
A.MakeDS()
A.show("random", 10, ",")

        