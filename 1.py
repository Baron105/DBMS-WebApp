import random
names = [
    'Adam', 'John', 'Mike', 'David', 'Steve', 'Daniel', 'Brian', 'Tyler', 'Kevin', 'Jake', 'Eric', 'Tom', 'Luke', 'Jeff', 'Frank', 'Charlie', 'Scott', 'Matt', 'Jack', 'Justin',
    'Aarav', 'Aryan', 'Arjun', 'Amit', 'Aniket', 'Ankit', 'Alok', 'Anuj', 'Avinash', 'Aditya', 'Akash', 'Ajit', 'Bharat', 'Bhuvan', 'Brijesh', 'Chirag', 'Chetan', 'Dhruv', 'Dinesh',
    'Deepak', 'Dhananjay', 'Dev', 'Devendra', 'Dharmesh', 'Darshan', 'Eklavya', 'Gaurav', 'Gopal', 'Ganesh', 'Hemant', 'Harsh', 'Harshal', 'Hrishikesh', 'Indrajeet', 'Ishaan', 'Jatin',
    'Jagdish', 'Kartik', 'Kamal', 'Karan', 'Kunal', 'Krishna', 'Kumar', 'Lalit', 'Lakshya', 'Manish', 'Mukesh', 'Mayank', 'Mahesh', 'Mohan', 'Naveen', 'Nirav', 'Nishant', 'Om', 'Omkar',
    'Prashant', 'Pramod', 'Pankaj', 'Parth', 'Pranav', 'Pradeep', 'Piyush', 'Rahul', 'Rakesh', 'Rohit', 'Rajesh', 'Rajendra', 'Sagar', 'Sandeep', 'Saurabh', 'Sanjay', 'Shubham', 'Shreyas',
    'Sumit', 'Sushant', 'Siddharth', 'Sudhir', 'Suraj', 'Sushil', 'Sunil', 'Tanmay', 'Tarun', 'Uday', 'Umesh', 'Vikas', 'Vivek', 'Vinay', 'Vaibhav', 'Vikrant', 'Yash', 'Yuvraj'
]

dept = ["CSE","ECE","MA","EE","BT","AG"]

roll = [i for i in range(11, 100)]

for i in range(100):
    x = random.choice(names)
    y = random.choice(dept)
    z = random.choice(roll)
    
    print(f"INSERT into student values('21{y[0:2]}100{z}',{i+1},'{x}','{y}')")

