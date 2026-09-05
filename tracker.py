import json
import os
import time
import csv
class Tracker:
    def __init__(self):
        self.entries =[]
    def add_entry(self,title, category, due_date):
        self.entries.append({"title": title, "category": category, "due_date": due_date, "done": False, "duration": None})
    def save_entries(self): 
        with open("tracker_data.json","w") as f:
            json.dump(self.entries,f)
    def export_csv(self):
        entries_header=["title","category","due_date","done","duration"]
        with open("tracker_data.csv","w", newline="") as f:
            writer=csv.DictWriter(f,fieldnames=entries_header)
            writer.writeheader()
            writer.writerows(self.entries)
    def load_entries(self):
        if os.path.exists("tracker_data.json"):
            with open("tracker_data.json") as f:
                self.entries = json.load(f)
        else:
            with open("tracker_data.json","x") as f:
                json.dump([],f)
    def show_entry(self):
        for x, item in enumerate(self.entries):
            print(f"{x+1},{item["title"]} [{item["category"]}] {item["due_date"]} {"not done -" if item["done"] == False else "done -"}{item["duration"]}")
    def counter(self,t):
        while t:
            mins,sec = divmod(t,60)
            timer='{:02d}:{:02d}'.format(mins,sec)
            print(timer,end='\r')
            time.sleep(1)
            t-=1
        print("task complete")
    def select_entry(self):
        self.show_entry()
        try:
            num = int(input("which entry number"))
        except ValueError:
            print("enter the correct number!")
            return None
        index = num-1
        if 0<= index<len(self.entries):
            return index
        else:
            print("no entry with that number")
            return None
    def mark_done(self,index):
        self.entries[index]["done"]=True
        self.save_entries()

    def delete_entry(self,index):
        self.entries.pop(index)
        self.save_entries()

    def edit_entry(self):
        while True:
        
            print("1.set duration 2.mark done 3.delete entry 4.remove all entries 5.back to menu")
            try:
                user_input=int(input())
            except ValueError:
                print("enter a number")
                continue
            if user_input==1:
                current_index=self.select_entry()
                if current_index == None:
                    continue
                try:
                    t=int(input("enter time in seconds"))
                except ValueError:
                    print("enter the time in seconds")
                    continue
             
                self.entries[current_index]["duration"]=t
                self.save_entries()
                self.counter(t)
            if user_input== 2:
                current_index=self.select_entry()
                if current_index == None:
                    continue
                self.mark_done(current_index)
            if user_input==3:
                current_index=self.select_entry()
                if current_index == None:
                    continue
                self.delete_entry(current_index)
            if user_input==4:
                self.entries.clear()
                self.save_entries()
            if user_input==5:
                break
def main():
    tracker=Tracker()
    tracker.load_entries()
    while True:
     print("1.add entry 2.show entry 3.start 4.export csv 5.quit")
     try:
      user_input=int(input())
     except ValueError:
         print("Enter a number")
         continue
     if user_input ==5:
          break
     elif user_input==1:
          title=input("Assign a title:")
          category=input("Assign a category:")
          date=input("Enter the date:")
          tracker.add_entry(title,category,date)
          tracker.save_entries()
     elif user_input ==2:
          tracker.show_entry()
     elif user_input==3:
         tracker.edit_entry()
     elif user_input==4:
          tracker.export_csv()
     else:
          print("invalid choice, try again")
     
main()

