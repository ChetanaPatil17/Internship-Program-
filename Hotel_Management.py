print("  **** SHINE PARADISE **** ")
user_name=input("plzz Enter your name: ")
print(f"Heyy!! {user_name} Welcome to Shine Paradise..")

print("_______________________________________________________________________________")
a = "Wedding"
b = "Birthday Party"
choice=input("Enter your choice: a.wedding and b.birthday party: ")
if choice =='a':
    print("____ Wedding ____")
elif choice == 'b':
    print("_____ Birthday Party ____")
else:
    print("Invalid Choice!")

if choice == 'a' or choice == 'b':
    age=int(input("Enter your age: "))
    if age<=30:
        print("Ok! plzz go to the hall no 3 at second floor!")
    elif age<18:
        print("Ok! plzz go to the hall no 5 at second floor!")
    elif age>30 and age<120:
        print("Ok! plzz go to the hall no 4 at second floor!")
    else:
        print("Invalid age! Plzz enter valid age..")

print("__________________________________________________________________________________")
if choice == 'a' or choice == 'b':
    meal=int(input("Plzz select your meal.. 1.veg or 2.non-veg : "))
    if meal==1:
        print("<<< Veg Menu >>>")
        list = ['1.Indian', '2.South Indian', '3.Chinese',]
        for i in list:
            print("---", i ,"---")
        mt=int(input("Enter choice..What kind of food you want.:- "))
        if mt == 1:
            print("<<<  List of Indian Food  >>>")
            l1= ['Masala Dosa', 'Dal-Makhani', 'Aloo-Puri', 'Rajma', 'Paneer tikka']
            for i in l1:
                print("---", i ,"---")
            veg_food1=input("____Enter the name of dish above list..you want in Indian Food____")
            spicy=input("what kind of food you want..spicy or medium:- ")
            print("Ok..Your order will reach you soon..thank you!")
        elif mt == 2:
            print("<<<  List of South Indian Food  >>>")
            l1= ['Masala Dosa', 'Vada-Sambar', 'Idli-Sambar', 'Uttapam']
            for i in l1:
                print("---", i ,"---")
            veg_food2=input("____Enter the name of dish above list..you want in South-Indian Food____")
            spicy=input("what kind of food you want..spicy or medium:- ")
            print("Ok..Your order will reach you soon..thank you!")
        elif mt == 3:
            print("<<<  List of Chinese Food  >>>")
            l1= ['Noodles','Manchurian','Soyabean-Chilli', 'Paneer-Chilli', 'Soup']
            for i in l1:
                print("---", i ,"---")
            veg_food3=input("Enter the name of dish above list..you want in Chinese Food..")
            spicy=input("what kind of food you want..spicy or medium:- ")
            print("Ok..Your order will reach you soon..thank you!")
       
    elif meal==2:
        print("<<< Non-Veg Menu >>>")
        
        list1 = ['1.Chiken tikka', '2.Fish fry', '3.Chiken Noodles',]
        for i in list1:
            print("---", i ,"---")
        nVeg_food=int(input("Enter choice..What kind of food you want.."))
        spicy=input("what kind of food you want..spicy or medium:- ")
        print("Ok..Your order will reach you soon..thank you!")
    else:
        print("Invalid choice..")

print("_________________________________________________________________________________")        
if meal==1 or meal==2:
    dessert=int(input("You want some delicious Dessert's: 1.yes or 2.no  "))
    if dessert==1:
        print("*********List of some delicious dessert's: ***********")
        dessert_list=['Daisy cupcakes','Banana Pudding','Ice-Cream Sunday','Red Velvet Cheese cake']
        for i in dessert_list:
            print("---", i ,"---")
        dessert_want=input("Enter choice....What kind of dessert you want...")
        print("Okay..Your order will reach you soon..thank you!")
    elif dessert==2:
        print("Okay...No problem thank you!")
    else:
        print("Invalid choice..")
else:
    print("Invalid choice..")

print("------------------------Thank's for visiting us..Hope you Enjoy!!---------------------------")




