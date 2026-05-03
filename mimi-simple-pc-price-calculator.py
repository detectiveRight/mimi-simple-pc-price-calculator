#   mimi is a nice cat 🐱

#   Welcome text /  نص ترحيبي

print("Welcome to the computer price determination application :)")

#   Ask questions to the user /طرح اسئلة على المستخدم

question1 = input("Enter the device type pc / laptop : \n")
question2 = input("Enter the device source used / new : \n")

print("Great information to continue now")
print("I'll ask for some hardware info, okay :)")

question3 = input("cpu : \n")
question4 = input("Gpu : \n")
question5 = input("RAM space: \n")
question6 = input("Storage space : \n")
question7 = input("Storage type ssd / hdd : \n")
question8 = input("motherboard type : \n")

print("Great now I will ask you some necessary information :)")

#   Ask some questions about accessories / طرح بعض اسئلة خاصة بالاكسيسوارات

question9 = input("Desired screen frequency : \n")
question10 = input("Keyboard type 100% 80% 75% 60% : \n")
question11 = input("Is it a keyboard and mouse? With or without backlighting? light up / not light up  : \n")

#   Questions about AI results / اسئلة خاصة بمخرجات الذكاء الإصطناعي


question12 = input("Do you want to know if there are any bottlenecks in your device and how they will affect the price? tell me / Don't tell me : \n")
question13 = input("What language would you prefer artificial intelligence to speak to you in? : \n")
question14 = input("Enter your country : \n")

#   Instructions for how to use / تعليمات لطريقة استخدام

print("Excellent, here's a request you can make to any AI tool to determine the price of this device. :)")

#   Preparing the indoctrination  / تجهيز التلقينة  

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Hello, please act as if you are an expert in hardware, software, and programming. Please provide us with your device specifications as follows :")
print("Device type " + question1 )
print("Device source " + question2  )
print("cpu " + question3 )
print("Gpu " + question4 )
print("ram space " + question5 )
print("storage space " + question6 )
print("Storage type " + question7 )
print("motherboard type " + question8  )
print("Desired screen frequency " + question9  )
print("Keyboard type " + question10 )
print("keyboard & mouse " + question11 )
print("Is there a problem with the device, and will that affect the price? : " + question12 )
print("Speak to me in this language : " + question13 )
print("Using this information, please provide me with the detailed and accurate market price of the device in this country" + "(" + question14 + ")")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#   Additional instructions on how to use / تعليمات اضافية لطريقة استخدام

print("Copy this text and send it to any artificial intelligence program.")

#   Thanks user  / شكر مستخدم 

print("Thank you for using the program :)")

#   Program logout system / نظام تسجيل خروج من برنامج

print("Press Enter to exit !")

input()


