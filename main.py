import requests
import json
import datetime

class Menu:
    def __init__(self, menuType="lunch"):
        self.link = f'https://novi.api.nutrislice.com/menu/api/weeks/school/novi-high-school/menu-type/{menuType}/' #?format=json
        
    def changeMenu(self, menuType="lunch"):
        self.link = f'https://novi.api.nutrislice.com/menu/api/weeks/school/novi-high-school/menu-type/{menuType}/'

    def _getData(self, date):
        response = requests.get(self.link + date.replace("-", "/"))
        data = json.loads(response.text)    
        return data
        
    def getDate(self, date: str):
        data = self._getData(date)
        for dayNum in range(1,6):
            if data["days"][dayNum]["date"] == date:
                day = data["days"][dayNum]["menu_items"]
                return(self._getFoodList(day))
        #date formatted like "2023/9/12"
        #print(data["start_date"]) #start of week 2023-09-11
        #print(data["days"][1].keys()) #dict_keys(['date', 'has_unpublished_menus', 'menu_info', 'menu_items'])
        #print(data["days"][1]["menu_items"][1].keys()) #dict_keys(['id', 'date', 'position', 'is_section_title', 'bold', 'featured', 'text', 'no_line_break', 'blank_line', 'food', 'is_holiday', 'food_list', 'station_id', 'is_station_header', 'station_is_collapsible', 'image', 'image_description', 'image_alt', 'image_thumbnail', 'category', 'price', 'serving_size', 'serving_size_amount', 'serving_size_unit', 'smart_recipe_id', 'menu_id'])
        #print(data["days"][1]["menu_items"][1]["food"].keys()) dict_keys(['id', 'name', 'description', 'subtext', 'image_url', 'hoverpic_url', 'price', 'ingredients', 'food_category', 'food_highlight_message', 'file_url', 'download_label', 'rounded_nutrition_info', 'serving_size_info', 'has_nutrition_info', 'icons', 'icons_approved', 'nested_foods', 'aggregated_data', 'food_sizes', 'ds_calories_override', 'synced_id', 'sync_placeholder', 'has_options_or_sides', 'digest', 'pos_item_id', 'smart_recipe_id', 'has_subfoods', 'meal_plan_price', 'use_custom_sizes', 'synced_ordering_enabled', 'ordering_enabled', 'ordering_enabled_unlocked'])
        
    def _getFoodList(self, day):
        info = dict()
        foodList = []
        for food in day:
            if food["food"] is None:
                if len(foodList) > 0:
                    info[category] = foodList
                    foodList = []
                category = food["text"]
                continue
            foodList.append(food["food"]["name"])
        return info
    
    def getToday(self): #, imageLink=False, nutrtion=False, description=False, ingredients=False
        today = str(datetime.date.today())
        return(self.getDate(today))
    
    def getTmmrw(self):
        day = str(datetime.date.today() + datetime.timedelta(days=1))
        return(self.getDate(day))
    
    def getWeek(self, weeks=None): #YYYY/MM/DD fomrat
        #if today is None: #make it weeks
        today = datetime.date.today() + datetime.timedelta(days = (7*weeks))
        monday = today - datetime.timedelta(days = today.weekday())
        info = dict()
        for i in range(5):
            date = str(monday + datetime.timedelta(days=i))
            info[date] = self.getDate(date)
        return info
                              
if __name__ == "__main__": 
    school = Menu()
    myFile = open("food.txt", "w")
    for i in range(1,5):
        data = school.getWeek(i)
        try:
            for date in data:
                myFile.write(f"-----------------{date}-----------------\n")
                myFile.write(f"Create\n")
                myFile.write(str(data[date]["Create"]) + "\n")
                myFile.write(f"Global Eats\n")
                myFile.write(str(data[date]["Global Eats"]) + "\n")
                print(date, "lunch menu wrote")
        except:
            print(date, "error")
            myFile.write("Error occured")
    myFile.close()
