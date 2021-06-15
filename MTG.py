from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import regex as re

options = Options()
options.headless = True

driver = webdriver.Chrome(options=options)
driver.get("https://www.mtgprice.com/magic-the-gathering-prices.jsp")

cardnames = driver.find_elements_by_class_name("ng-scope")
list = []
set = driver.find_elements_by_xpath("/html/body/div[1]/div[10]/div/div/table/tbody")

for sets in set:
    names = sets.text.strip()  # removes selectors from web info
    expr = re.compile('\d{2}/\d{2}/\d{4}')  # removes dates from end of each string
    line = re.sub(expr, '', names)  # replace all dates with ''
    line = line.replace(" ", "_")  # replace all spaces with underscores for web link usage
    list.append(line.split('_\n'))  # splits elements by each new line
    #  print(line)  # prints the list, for testing

cardset = list[-1]  # prints the new list
i = 0  # starts iteration for looping through each card set to pull data

masterlist = []  # creates the empty list we'll put all the data into
user_prompt = input("what MTG set?")  # we can input a single set or "All" to determine which sets we look through
prompt = '_'.join(user_prompt.split(' '))  # replace spaces with underscores to place into url
if prompt == "All":  # if we put in all we will go through all sets
    for cardsets in cardset:  # begins loop over every card set

        driver.get(f"https://www.mtgprice.com/spoiler_lists/{cardset[i]}")  # lets us directly link to
        # each card set to iterate over
        i = i + 1  # moves to the next card set
        cardnames = driver.find_elements_by_class_name("ng-scope")  # pulls card information from website
        count = 0
        for cardname in cardnames:  # begins loop within every card set
            mastercard = cardname.text.strip()  # turns card set data into plaintext (removes selectors)
            count += 1
            if count > 10:
                masterlist.append(mastercard.split(" $"))  # adds data to the empty list we'll put all the data into,
            # splitting each

elif prompt == "None":
    pass

# else:  # if we put in a single set we will only go through that one
driver.get(f"https://www.mtgprice.com/spoiler_lists/{prompt}")  # lets us directly link to specific card set listed
i = i + 1  # moves to the next card set
cardnames = driver.find_elements_by_class_name("ng-scope")  # pulls card information from website
count = 0
for cardname in cardnames:  # begins loop within every card set
    mastercard = cardname.text.strip() # turns card set data into plaintext (removes selectors)
    count += 1
    if count > 10:
        masterlist.append(mastercard.split(" $")) # adds data to the empty list we'll put all the data into,
    # splitting each
    # this is where I pickle

print(masterlist) # prints all of the data being stored in masterlist, for testing purposes

driver.quit()


#  Test converting to json


