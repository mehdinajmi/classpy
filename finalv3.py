### Mehdi Najmi- sematec Python class - Thursday 2:00 pm to 6:00 pm
#To Desgin a phonebook 
def add():
    first_name_add=input('enter your first name:\n').lower()
    second_name_add=input('enter your second name:\n').lower()
    number_add=int(input( 'enter your number:\n'))
    counyty_add=input('enter counry name:\n').lower()
    city_add=input('enter city name:\n').lower()
    dbs_firstname_add=[]
    dbs_secondname_add=[]
    dbs_number_add=[]
    dbs_country_add=[]
    dbs_city_add=[]
    dbs_firstname_add.append(first_name_add.lower())
    dbs_secondname_add.append(second_name_add.lower())
    dbs_number_add.append(number_add)
    dbs_country_add.append(counyty_add.lower())
    dbs_city_add.append(city_add.lower())
    import sqlite3
    connect_add=sqlite3.connect('phonebook.db')
    cursor=connect_add.cursor()
    add_query=f'insert into phonebook values ("{dbs_firstname_add[0]}","{dbs_secondname_add[0]}",{dbs_number_add[0]},"{dbs_country_add[0]}","{dbs_city_add[0]}")'
    cursor.execute(add_query)
    connect_add.commit()
    connect_add.close()
    print (f' contact details of "{dbs_firstname_add[0]}" "{dbs_secondname_add[0]}" from "{dbs_country_add[0]}" "{dbs_city_add[0]}" has been added to the phonebook')
#######################################################################################
def search():
    first_name_search=input('enter first name:\n')
    second_name_search=input('enter  second name:\n')
    country_search=input( 'enter  country name:\n')
    city_search=input('enter city name:\n')
    import sqlite3
    connect_search=sqlite3.connect('phonebook.db')
    cursor=connect_search.cursor()
    search_query=f'select * from phonebook where firstname="{first_name_search}"and secondname="{second_name_search}"and country="{country_search}"and city="{city_search}"'
    # search_query='select * from phonebook '
    cursor.execute(search_query)
    result_search=cursor.fetchall()
    connect_search.close()
    #print ( 'search result :', result_search)
    for raw in result_search:
        print(raw)
##################################################################################################
def remove():
    first_name_remove=input('enter first name:\n').lower()
    second_name_remove=input('enter  second name:\n').lower()
    country_remove=input('enter country name:\n').lower()
    city_remove=input('enter city name:\n').lower()
    import sqlite3
    connect_remove=sqlite3.connect('phonebook.db')
    cursor=connect_remove.cursor()
    remove_query=f'delete from phonebook where firstname="{first_name_remove}" and secondname= "{second_name_remove}" and country="{country_remove}" and city="{city_remove}"'
    cursor.execute(remove_query)
    connect_remove.commit()
    connect_remove.close()
    print (f' contact deatils for {first_name_remove} {second_name_remove} from {country_remove} {city_remove} has been sucessfuly deleted')
##########################################################################################################
while True:

        intro='''this is a Telephone book . to find a  number enter "search",
        to add a number enter" add" , to delete a number enter "remove" and
        if you do not have furthur request enter " no request"'''
        print(intro)
        request=input(' What you want to do :\n' )
        if request =='add':
            add()
        elif request =='search':
            search()
        elif  request =='remove':
            remove()
        elif request=='no request':
            print(' thank you for using our phonebook and see you later')
            break
        else:
            print(' your request can not be processed')
