# Novi-High-School-Nutrslice-scrape
### Scrapes info off of nutrislice, spefically from Novi High School, will prolly update to scrape off of any highschool soon.

Uses all default libraries, so anyone should be able to use with python, has menu class and then you have use a date, getToday, getTmmrw, or getWeek
### getWeek()
takes in one parameter, how many weeks from this week, so putting in nothing or 0 will be current week, 1 will be next week, etc.

return a dictionary with date corresponding to the days lunch menu {date : {station name : foods from station}}

### getTody(), getTmmrw(), getDate(YYYY-MM-DD or YYYY/MM/DD format: in string)
These are all pretty self explanatory, however note that all of these functions return a dictionary {station name : foods from station} 
for every station

# Example Code


<img width="468" alt="image" src="https://github.com/AkaHeez/Novi-High-School-Nutrslice-scrape/assets/118094954/63152473-75b0-4f14-a65a-9f8761dc2731">



### This code stores information of the date and then the foods, for the next 5 weeks
