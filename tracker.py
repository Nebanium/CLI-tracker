import json
import os
import time
import csv
entries=[]
def add_entry(title, category, due_date):
    entry = {"title": title, "category": category, "due_date": due_date, "done": False, "duration": None}
    entries.append(entry)

def save_entries():
 
    with open("tracker_data.json","w") as f:
        json.dump(entries,f)

def export_csv():
    entries_header=["title","category","due_date","done","duration"]
    with open("tracker_data.csv","w", newline="") as f:
         writer=csv.DictWriter(f,fieldnames=entries_header)
         writer.writeheader()
         writer.writerows(entries)
def load_entries():
    global entries
    if os.path.exists("tracker_data.json"):
            with open("tracker_data.json") as f:
                entries = json.load(f)
    else:
            with open("tracker_data.json","x") as f:
                json.dump([],f)
              
def show_entry():
    for x, item in enumerate(entries):
         print(f"{x+1},{item["title"]} [{item["category"]}] {item["due_date"]} {"not done -" if item["done"] == False else "done -"}{item["duration"]}")

def counter(t):
    while t:
        mins,sec = divmod(t,60)
        timer='{:02d}:{:02d}'.format(mins,sec)
        print(timer,end='\r')
        time.sleep(1)
        t-=1
    print("task complete")

def select_entry():
    show_entry()
    try:
        num = int(input("which entry number"))
    except ValueError:
        print("enter the correct number!")
        return None
    index = num-1
    
    if 0<= index<len(entries):
        return index
    else:
        print("no entry with that number")
        return None

def mark_done(index):
    entries[index]["done"]=True
    save_entries()

def delete_entry(index):
    entries.pop(index)
    save_entries()
            
def edit_entry():
    while True:
        
        print("1.set duration 2.mark done 3.delete entry 4.remove all entries 5.back to menu")
        try:
           user_input=int(input())
        except ValueError:
           print("enter a number")
           continue
        if user_input==1:
             current_index=select_entry()
             if current_index == None:
                         continue
             try:
                t=int(input("enter time in seconds"))
             except ValueError:
                print("enter the time in seconds")
                continue
             
             entries[current_index]["duration"]=t
             save_entries()
             counter(t)
        if user_input== 2:
            current_index=select_entry()
            if current_index == None:
                        continue
            mark_done(current_index)
        if user_input==3:
            current_index=select_entry()
            if current_index == None:
                        continue
            delete_entry(current_index)
        if user_input==4:
            entries.clear()
            save_entries()
        if user_input==5:
            break

def main():

    load_entries()
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
          add_entry(title,category,date)
          save_entries()
     elif user_input ==2:
          show_entry()
     elif user_input==3:
         edit_entry()
     elif user_input==4:
          export_csv()
     else:
          print("invalid choice, try again")
     

        
#load_entries()
#add_entry("studio deadline", "architecture", "2026-08-01")
#save_entries()
#show_entry()
main()