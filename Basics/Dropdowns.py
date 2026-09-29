#Two types of dropdowns
#1. Standard dropdowns     ---------------------> dropdowns developed using select tag
# 2. non standard dropdowns --------------------> dropdowns developed aprt from select tag




# standard dropdowns:-
# two types in standard dropdowns:-
# 1. Single select dropdown

# able to select only one single option
# not be able to select more than one option at once
# not be abe to deselect the option

# 2. Multi select dropdown

# able to select one single option
#able to select more than one option at once
# able to deselect the option








# select class methods:-
# the below are for selecting any option in standard dropdown
# 1. select_by_index(index_value)
# 2. select_by_value("value attri")
# 3. select by_visible_text("text")


# the below are for deselecting any option in standard dropdown
# 1. deselect_by_index(index_value)
# 2. deselect_by_value("value attri")
# 3. deselect by_visible_text("text")
# 4. deselect_all()





# To handle standard dropdowns we have to import select class
# from selenium.webdriver.support.select import Select










# from selenium.webdriver import Chrome,ChromeOptions
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(o)
# from time import sleep
# driver.maximize_window()
# from selenium.webdriver.support.select import Select



# 1. standard dropdowns
# Single select dropdown



# selecting an option in single select dropdown using select_by_index()
'''driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
sleep(3)

# locate dropdown
a=driver.find_element("id","select3")

s=Select(a)
# s.select_by_index(2)
# s.select_by_index(8)

sleep(3)
'''
import pytest

# selecting an option in single select dropdown using select_by_value()
'''driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
sleep(3)
# locate dropdown
a=driver.find_element("id","select3")
# create object for select class
s=Select(a)
# selecting option
s.select_by_value("China")
sleep(4)'''




# selecting an option in single select dropdown using select_by_visible_text()
'''driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
sleep(3)
# locate dropdown
a=driver.find_element("id","select3")
# create object for select class
s=Select(a)
# selecting option
s.select_by_visible_text("China")
sleep(4)
'''




# selecting an option in single select dropdown using select_by_visible_text()
'''driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
sleep(3)
# locate dropdown
a=driver.find_element("id","select7")
# create object for select class
s=Select(a)
# selecting option
s.select_by_index(4)
sleep(4)'''





# delecting the option
'''driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
sleep(3)
# locate dropdown
a=driver.find_element("id","select7")
# create object for select class
s=Select(a)
# selecting option
s.select_by_index(4)

# deselecting option
s.deselect_by_index(4)
sleep(4)'''



# note:- we cannot deselect the option in single select dropdown if we do so we will get NotImplementedError






'''driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
sleep(3)
# locate country dropdown
a=driver.find_element("id","select3")
s1=Select(a)
s1.select_by_index(7)
sleep(4)
# locate state dropdown
b=driver.find_element("id","select5")
s2=Select(b)
s2.select_by_value("Karnataka")
sleep(2)
# locate city dropdown
c=driver.find_element("xpath","(//select[contains(@class,'border')])[5]")
s3=Select(c)
s3.select_by_visible_text("Bangalore Urban")
sleep(5)'''




# Multiselect dropdown:
# selecting one single option in single select dropdown
'''driver.get("https://demoqa.com/select-menu")
sleep(4)
a=driver.find_element("id","cars")
s=Select(a)
s.select_by_index(3)
sleep(4)'''





# selecting more than one option
'''driver.get("https://demoqa.com/select-menu")
sleep(4)
a=driver.find_element("id","cars")
s=Select(a)
s.select_by_index(0)
s.select_by_value("saab")
s.select_by_visible_text("Audi")
sleep(4)'''




# deselecting option in multi select dropdown
'''driver.get("https://demoqa.com/select-menu")
sleep(4)
a=driver.find_element("id","cars")
s=Select(a)
s.select_by_index(0)
s.select_by_value("saab")
s.select_by_visible_text("Audi")
sleep(3)
s.deselect_by_value("volvo")
s.deselect_by_index(1)
s.deselect_by_visible_text("Audi")
sleep(5)'''




# deselecting all options at once
'''driver.get("https://demoqa.com/select-menu")
sleep(4)
a=driver.find_element("id","cars")
s=Select(a)
s.select_by_index(0)
s.select_by_value("saab")
s.select_by_visible_text("Audi")
sleep(3)
s.deselect_all()
sleep(5)'''






# open demoapp qspiders
# select only option that is white gold plated PR
# thn deselect the same option




# open demoapp qspiders
# select two options that is Silicon and Acer
# thn deselect the silicon option






# properties of select class:-
# 1. is_multiple:-
#
# checks whthr dropdpwn is single select or multi select
# if multi select---->True
# if not ------> none or false


'''driver.get("https://demoqa.com/select-menu")
sleep(3)
a=driver.find_element("id","oldSelectMenu")
s=Select(a)
print(s.is_multiple)'''



'''driver.get("https://demoqa.com/select-menu")
sleep(3)
a=driver.find_element("id","cars")
s=Select(a)
print(s.is_multiple)'''




# options:-
# it is used to extract ALLL THE OPTONS FROM DROPDOWN,we can print options from
# single select as well as multi select


'''driver.get("https://demoqa.com/select-menu")
sleep(3)
a=driver.find_element("id","oldSelectMenu")
s=Select(a)
b=s.options
print(b)                               #b=[<selenium session......,> <selenium session......,> <selenium session......,>]
for i in b:
    print(i.text)'''




'''driver.get("https://demoqa.com/select-menu")
sleep(3)
a=driver.find_element("id","cars")
s=Select(a)
b=s.options
print(b)                               #b=[<selenium session......,> <selenium session......,> <selenium session......,>]
for i in b:
    print(i.text)'''






'''driver.get("https://demoapps.qspiders.com/ui/dropdown/multiSelect?sublist=1")
sleep(3)
a=driver.find_element("id","select-multiple-native")
s=Select(a)
b=s.options
print(b)                               #b=[<selenium session......,> <selenium session......,> <selenium session......,>]
for i in b:
    print(i.text)

'''







# all_selected_option:-
# used to print all the selected options from multiselect dropdown
# have to use for loop

# syntax:- ob.all_selected_options


'''
driver.get("https://demoqa.com/select-menu")
sleep(3)

z=driver.find_element("id","cars")
s=Select(z)

s.select_by_index(0)
s.select_by_index(1)
sleep(3)
b=s.all_selected_options
for i in b:
    print(i.text)'''




# first selected option:-
# it will return the first selected option as an output among all the selected options
# syntax:- ob.first_selected_option


'''driver.get("https://demoqa.com/select-menu")
sleep(3)

z=driver.find_element("id","cars")
s=Select(z)

s.select_by_index(0)
s.select_by_index(1)
sleep(3)


b=s.first_selected_option
print(b.text)'''







# NON STANDARD DROPDOWNS:-
# The dropdowns which are not developed using select tag
# we should not use select class for handling non standard dropdowns,if we use it wont work


'''driver.get("https://demoqa.com/select-menu")
sleep(4)

# locate dropdown and click
driver.find_element("xpath","//div[@class='css-19bb58m']").click()

# locate option click on option
driver.find_element("xpath","//div[text()='A root option']").click()'''





'''driver.get("https://demoqa.com/select-menu")
sleep(4)

# locate dropdown and click
driver.find_element("xpath","(//div[@class='css-19bb58m'])[2]").click()
sleep(2)



# locate option click on option
driver.find_element("xpath","//div[text()='Dr.']").click()
sleep(3)
'''



'''
driver.get("https://demoqa.com/select-menu")
sleep(4)


driver.find_element("xpath","(//div[@class='css-19bb58m'])[3]").click()
sleep(2)


driver.find_element("xpath","//div[text()='Green']").click()
sleep(1)
driver.find_element("xpath","//div[text()='Black']").click()
sleep(4)
'''















# driver.quit()

















'''class A:
    def disp(self):
        pass


obj=A()
obj.disp()'''











'''
class Select:
    def select_by_index(self):
        pass
    

s=Select()
s.select_by_index()'''












#
# append()---->list
#
#
# a=(1,2,3)
# a.append('s')








'''a='python'
for i in a:
    print(i)
    

i='p'
1. for 'p' in 'python':
    print('p')
    

i='y'
2. for 'y' in 'python':
    print('y')
    
    

i='t'
for 't' in 'python':
    print('t')
'''





# a=[10,20,30]
# for i in a:
#     print(i)


# i=10
# 1. for 10 in a:
#     print(10)


# i=20
# 2. for 20 in a:
#     print(20)



# i=30
# 3. for 30 in a:
#   print(30)















