import pyttsx3 
import speech_recognition as sr 
import webbrowser 
import datetime 
import smtplib
from database import *
import mysql.connector
from numpy import random
from PIL import Image


database = Database()
connection = database.getConnection()


# this method is for taking the commands 
# and recognizing the command from the 
# speech_Recognition module we will use 
# the recongizer method for recognizing 

def takeCommand(): 

	r = sr.Recognizer() 

	# from the speech_Recognition module 
	# we will use the Microphone module 
	# for listening the command 
	with sr.Microphone() as source: 
		print('Listening...')
		
		r.adjust_for_ambient_noise(source,duration=1)
		r.pause_threshold = 0.7
		
		audio = r.listen(source) 
		
		# seconds of non-speaking audio before 
		# a phrase is considered complete 

		# Now we will be using the try and catch 
		# method so that if sound is recognized 
		# it is good else we will have exception 
		# handling 
		try: 
			
			print("Recognizing") 
			
			# for Listening the command in indian 
			# english we can also use 'hi-In' 
			# for hindi recognizing 
			Query = r.recognize_google(audio, language='en-in') 
			
			print("the command is printed=", Query) 
			
		except Exception as e: 
			print(e) 
			speak("Say that again sir") 
			return "None"
		
		return Query 

def speak(audio): 
	
	engine = pyttsx3.init() 
	# getter method(gets the current value 
	# of engine property) 
	voices = engine.getProperty('voices') 
		
	# setter method .[0]=male voice and 
	# [1]=female voice in set Property. 
	engine.setProperty('voice', voices[1].id) 
	
	# Method for the speaking of the the assistant 
	engine.say(audio) 
	
	# Blocks while processing all the currently 
	# queued commands 
	engine.runAndWait() 
def print_order():
	id = 34
	order=""
	mysql_query = """SELECT order_name,quantity FROM `orders` WHERE customer_id= %s"""
	val = (id,)
	cursor = connection.cursor()
	cursor.execute(mysql_query,val)
	record = cursor.fetchall()
	order="Order:"+str(record)

	mysql_query = """SELECT take_away FROM `orders` WHERE customer_id=%s"""
	val = (id,)
	cursor = connection.cursor()
	cursor.execute(mysql_query,val)
	record = cursor.fetchall()
	order=order+"take-away:"+str(record)
	server=smtplib.SMTP_SSL("smtp.gmail.com",465)
	server.login("naikshashank12.sn@gmail.com","Shashank@18")



	sender = 'naikshashank12.sn@gmail.com'
	receivers = ['naikshashank12.sn@gmail.com']

	message = """From: From Person <naikshashank12.sn@gmail.com>
To: To Person <naikshashank12.sn@gmail.com>
Subject: New Order placed

			"""+order

	
	



	server.sendmail(sender, receivers, message)         
	print ("Successfully sent email")


	server.quit()

def tellDay(): 
	
	# This function is for telling the 
	# day of the week 
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number 
	# that will help us in telling the day 
	Day_dict = {1: 'Monday', 2: 'Tuesday', 
				3: 'Wednesday', 4: 'Thursday', 
				5: 'Friday', 6: 'Saturday', 
				7: 'Sunday'} 
	
	if day in Day_dict.keys(): 
		day_of_the_week = Day_dict[day] 
		print(day_of_the_week) 
		speak("The day is " + day_of_the_week) 


def tellTime(): 
	
	# This method will give the time 
	time = str(datetime.datetime.now()) 
	
	# the time will be displayed like 
	# this "2020-06-05 17:50:14.582630" 
	#nd then after slicing we can get time 
	print(time) 
	hour = time[11:13] 
	min = time[14:16] 
	speak("The time is sir" + hour + "Hours and" + min + "Minutes")	 

def details():
	token = random.randint(100)
	while(True):
		speak("can you tell me your name")
		query = takeCommand().lower()
		if query == "none" :
			continue
		else:
			name = query
			break
	speak("hello " + name)
	sql = """insert into customers(name,token) values (%s,%s)"""
	cursor = connection.cursor()
	val = (name,token)
	cursor.execute(sql,val)
	connection.commit()


def Hello():
	
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12 :
		speak("Good Morning")

	elif hour>=12 and hour<18 :
		speak("Good afternoon")

	else:
		speak("Good Evening")

	speak("hii it's me gordon your personal waiter")
	speak("welcome to our restaurant")
	details()
	
	flag = True
	while(True):
		speak("would you like to dine in or you want to use the take away ")
		query = takeCommand().lower()
		if "take away" in query:
			#flag=False
			speak("Okay, we also have take away")
			speak(" There will be menu on your screen")
			im = Image.open(r"C:\Users\naiks\Desktop\VA\Menu.png") 
  
			# This method will show image in any image viewer 
			im.show() 

			query = takeCommand().lower()
			if "order" or "no" or "take away" in query:
				order("yes")
			elif "okay" or "ok" in query:
				speak("Thank you , have a nice day")
			break
				

		elif "dine in" or "dine" or "dinong" in query:
			flag=False
			speak(" There will be menu on your screen")
			im = Image.open(r"C:\Users\naiks\Desktop\VA\Menu.png") 
  
			# This method will show image in any image viewer 
			im.show() 
			
			order("no")
			break
		else:
			continue
		
		#speak("still inside while loop")
def newCustomer():
	Hello()
def total():
	id = customerid()
	mysql_query = """select sum(price) from orders where customer_id = %s"""
	val = (id,)
	cursor = connection.cursor()
	cursor.execute(mysql_query,val)
	record = cursor.fetchall()
	for row in record:
		totalAmount = row[0]
	speak("your total amount is  ")
	speak(totalAmount)
	insert_query=""" update customers set total= %s where customer_id = %s """
	value = (totalAmount,id)
	cursor.execute(insert_query,value)
	connection.commit()
		
def order(takeaway):
	
	quantity = ["one","two","three","four","five","six","seven","eight"]
	quant = 1
	orders = {}
	while(True):
		
		speak("what would you like to order from biryani,kebab,starter,curries")
		query = takeCommand().lower()
		
		if "biryani" in query:
			flag = 0
			listt = []
			
			while True:
				speak("what you want to order from biryani")
				query1 = takeCommand().lower()
				words = query1.split()
				if words in quantity:
					quant = int(quantity)
				mySql_Query = """ select B_name,price from biryanis"""
				cursor = connection.cursor()
				cursor.execute(mySql_Query)
				record = cursor.fetchall()
				for row in record:
					if row[0] in query1:
						total = quant * int(row[1])
						listt.append(quant)
						listt.append(total)
						orders[row[0]] = listt
						flag=1

				if flag == 1:
					speak("do you want add some more item from biryani please tell yes or no")
					query2 = takeCommand().lower()
					if "no" in query2:
						break
					elif query2 == "none":
						speak("if you dont want to add please say nothing")
						continue
					elif "yes" in query2:
						speak("please let me know ")
						continue
				elif "nothing" in query1 or "no" in query1:
					break
				else:
					speak("Please pardon")
				
				

		elif "kabab" in query:
			listt = []
			
			repeat = "yes"
			while(True):
				flag = 0
				speak("what you want to order from kebab")
				query1 = takeCommand().lower()
				
				mySql_Query = """ select kname,price from kebabs"""
				cursor = connection.cursor()
				cursor.execute(mySql_Query)
				record = cursor.fetchall()
				for row in record:
					if row[0] in query1:
						total = quant * int(row[1])
						listt.append(quant)
						listt.append(total)
						orders[row[0]] = listt
						flag = 1

				if flag==1:
					speak("do you want add some more item from kebab please tell yes or no")
					query2 = takeCommand().lower()
					if "no" in query2:
						repeat="no"
					elif "yes" in query2:
						speak("please let me know ")
						continue
				elif "nothing" in query1 or "no" in query1:
					break
				elif query1 == "none":
					speak("please tell me ")
				else:
					speak("Please pardon")
			
		elif "starter" in query:
			listt = []
			while(repeat!="no"):
				speak("what you want to order from starter")
				query1 = takeCommand().lower()
				words = query1.split()
				if words in quantity:
					quant = int(quantity)
				mySql_Query = """ select sname,price from starter"""
				cursor = connection.cursor()
				cursor.execute(mySql_Query)
				record = cursor.fetchall()
				for row in record:
					if row[0] in query1:
						total = quant * int(row[1])
						listt.append(quant)
						listt.append(total)
						orders[row[0]] = listt
						flag =1
				if flag==1:
					speak("do you want add some more item from starter? please tell yes or no")
					query = takeCommand().lower()
					if "no" in query:
						repeat="no"
					else:
						speak("please let me know ")
						continue
				elif "nothing" in query1:
					break
				else:
					speak("Please pardon")

		elif "curries" in query:
			listt = []
			while(repeat!="no"):
				speak("what you want to order from curries")
				query1 = takeCommand().lower()
				words = query1.split()
				if words in quantity:
					quant = int(quantity)
				mySql_Query = """ select cname,price from curries"""
				cursor = connection.cursor()
				cursor.execute(mySql_Query)
				record = cursor.fetchall()
				for row in record:
					if row[0] in query1:
						total = quant * int(row[1])
						listt.append(quant)
						listt.append(total)
						orders[row[0]] = listt
						flag =1
				if flag==1:
					speak("do you want add some more item from curries? please tell yes or no")
					query = takeCommand().lower()
					if "no" in query:
						repeat="no"
					else:
						speak("please let me know ")
						continue
				elif "nothing" in query1:
					break
				else:
					speak("Please pardon")
					
		
		elif "nothing" in query :
			while(True):
				speak("May i confirm your order please tell yes or no")
				queryy = takeCommand().lower()
				if "yes" in queryy:
					confirmed(orders,takeaway)
					
					speak("Thank you for order, your order will be ready in 20 minutes")
					break
				elif "no" in queryy:
					speak("please let me know")
					order()
				else:
					continue
			break
	
	speak("Thank you. Have a great time ")
	print_order()
	exit()
	
	
def customerid():
	
	mySql_Query = """SELECT customer_id FROM CUSTOMERS ORDER BY customer_id DESC LIMIT 1"""
	cursor = connection.cursor()
	cursor.execute(mySql_Query)
	record = cursor.fetchall()
	for row in record:
			id = row[0]
	return id


def confirmed(order,takeaway):
	cid = customerid()
	sql = """ insert into orders (customer_id,order_name,quantity,price,take_away) values(%s,%s,%s,%s,%s)"""
	for key,values in order.items():
		val = (cid,key,values[0],values[1],takeaway)
		cursor = connection.cursor()
		cursor.execute(sql,val)
		connection.commit()
	total()


def offer():
	orders = {}
	listt = []
	mysqlquery = """select dish1,dish2,actualPrice,offeerPrice from offers"""
	cursor = connection.cursor()
	cursor.execute(mysqlquery)
	record = cursor.fetchall()
	for row in record:
		dish1 = row[0]
		dish2 = row[1]
		actualP = row[2]
		offerp = row[3]
		#speak("we have combo in")
		#speak(dish1 + "plus" + dish2)
		#speak(" which actual price is "+ str(actualP))
		#speak("  and offer price is " + str(offerp) )
	speak("what would you like to order from offers")
	while(True):
		flag=0
		query = takeCommand().lower()
		if "nothing" in query:
			speak("okay")
			break
		elif query == "none":
			speak("please tell what you want to order from offers")
		else:
			for row in record:
				if row[0] in query:
					listt.append(row[1])
					listt.append(row[3])
					orders[row[0]] = listt
					flag=1

			if flag==1:
				while(True):

					speak(" do  you want to add some more item from offers please tell yes or no")
					query2 = takeCommand().lower()
					if "yes" in query2:
						speak("okay then continue for the next one")
						speak("next order please")
						offer()
					
					
					elif "no" in query2:
						while(True):
							speak("may i confirm your dish from offers please tell yes or no")
							query3 = takeCommand().lower()
							if "yes" in query3:
								cid = customerid()
								sql = """insert into orders (customer_id,order_name,quantity,price,take_away) values(%s,%s,%s,%s,%s)"""
								for x,y in orders.items():
									val = (cid,x+" "+y[0],1,y[1],"no")
									cursor.execute(sql,val)
									connection.commit()
									speak(" your oder from offer is confirmed ")
								break

							elif "no" in query3:
								speak("do you want to add some more item from offers")
								qury = takeCommand().lower()
								if "yes" in qury:
									offer()
								elif "no" in qury:
									speak("please tell me ")
									continue	
						break				
				speak("you can order anything from menu what ever you want")
				break
			else:
				speak("sorry we dont have this item in our offers ")
				speak("please order something from offers ")

	order("no")		
					

def dish():
	mySql_Query = """select order_name from special_order"""
	cursor = connection.cursor()
	cursor.execute(mySql_Query)
	record = cursor.fetchall()
	for row in record:
			speak(row[0])
	speak("this are dishes which would you like to order")

def biryani():
	mySql_Query = """ select B_name from biryanis"""
	cursor = connection.cursor()
	cursor.execute(mySql_Query)
	record = cursor.fetchall()
	for row in record:
		speak(row[0])

	speak("This are the biryani we have")

def dessert():
	query = """ select dname from dessert"""
	cursor = connection.cursor()
	cursor.execute(query)
	record = cursor.fetchall()
	for row in record:
		speak(row[0])
	speak("which dessert would you like to order")

def starter():
	query = """ select sname from starter """
	cursor = connection.cursor()
	cursor.execute(query)
	record = cursor.fetchall()
	for row in record:
		speak(row[0])

	speak("would you like to order from the stater")

def kebab():
	query = """ select kname from kebab"""
	cursor = connection.cursor()
	cursor.execute(query)
	record = cursor.fetchall()
	for row in record:
		speak(row[0])

	speak("we have this item for you in kebab")

def curries():
	query = """select cname from curries"""
	cursor = connection.cursor()
	cursor.execute(query)
	record = cursor.fetchall()
	for row in record:
		speak(row[0])

	speak("did you like something from curries ")


def wakeword(text):
	wakeWord = ["hii","hello","hey"]
	for phrase in wakeWord:
		if phrase in text:
			return True
	return False


def Take_query(): 

		#words = query.split()
		
		while(True):
			query = takeCommand().lower()
			if (wakeword(query) == True):
				
				Hello()
				
				while(True):
					speak("inside take query")
					query = takeCommand().lower()

					if "special dish" in query:
						dish()
						continue
							
					elif "day it is" in query:
						tellDay() 
						continue
					
					elif "tell me the time" in query: 
						tellTime() 
						continue

					elif "bye" in query: 
						speak("Bye have a nice day") 
						exit()

					elif "biryani" in query:
						biryani()
						continue
					
					elif "dessert" in query:
						dessert()
						continue

					elif "kebab" in query:
						kebab()
						continue

					elif "starter" in query:
						starter()
						continue

					elif "curries" in query:
						curries()
						continue

				
					
				
					
					 

		 

if __name__ == '__main__': 
	
	# main method for executing 
	# the functions 
	Take_query()