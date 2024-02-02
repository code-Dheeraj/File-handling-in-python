"""Data handling in python 
   three steps in data handlling
   
   1. open file 
   2. perform read and write operation
   3. close the file 

   Operation { "w" -> to write into file }
             { "r" -> to read from the file }
             { "a" -> to append the file }
             
    function { f.open -> to open the file }
             { f.write -> to write into file }
             { f.writelines -> to write into file in multiple line }
             { f.close -> to close the file }
             
           
"""
f = open("temp.txt",'w')
f.write("my name is dheeraj")
f.close()
# once the file is closed you cant perform read and write operation 
f.write("rewriting is not possible")


# writing multiline string

f = open("multiFile.txt",'w')
f.write("Inserting into multiFile \n")
f.write("inserting into second line of multiFile\n")
f.write("inserting into third line of multiFile")
f.close()

# using append functionality to add into a file

f = open("temp.txt","a")
f.write("  ....this is append text")
f.close()


#if you want to add muliple lines in a file , you can use list or tuple 

# if you are using dictionary , then it will only insert the keys not its values
# for inserting both key and values you can use "f.writelines(str(dictionary))"

l = ["dfsfdf : 20bcs8\n","dfsdf : 20bcs9\n","patty : 20bcs7"]
d = {'1\n':"dkj",'2\n':"anddda",'3\n':"patty",'4\n':"sms"}
t = ("dkj","\nnddda","patty\n","sms")
f = open("temp2.txt",'w')
f.writelines(d)   # you can use list,dict or tuple 
f.close()
