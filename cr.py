
password = input()
number = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0
number7 = 0
number8 = 0
number9 = 0
true = True
var2 = ""
var1 = ""
var3 = ""
var4 = ""
var5 = ""
var6 = ""
var7 = ""
var8 = ""
var9 = ""

letters_numbers_and_wird_signs = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","X","Y","Z","1","2","3","4","5","6","7","8","9","0","#","!","§","$","%","&","/","(",")","=","?","*","+",";",":","€","-","_",".",","]


def better():
    while true == True:
        global var9
        global var8
        global var7
        global var6
        global var5
        global var4
        global var3
        global var2
        global var1
        global number9
        global number8
        global number7
        global number6
        global number5
        global number4
        global number3
        global number2
        global number
        global letters_numbers_and_wird_signs
        number = number + 1
        var1 = letters_numbers_and_wird_signs[number]
        print (var2 + var1 + var3 + var4 + var5 + var6 + var7 + var8 + var9)
        if var2 + var1 + var3 + var4 + var5 + var6 + var7 + var8 + var9 == password:
         print(password + " : cracked")
         break
        if number == 80:
            number = 0
            number2 = number2 + 1
            var2 = letters_numbers_and_wird_signs[number2]
            print(var1 + var2)
            if number2 == 80:
                number2 = 0
                number3 = number3 + 1
                var3 = letters_numbers_and_wird_signs[number3]
                if number3 == 80:
                    number3 = 0
                    number4 = number4 + 1
                    var4 = letters_numbers_and_wird_signs[number4]
                    if number4 == 80:
                      number4 = 0
                      number5 = number5 + 1
                      var5 = letters_numbers_and_wird_signs[number5]
                      if number5 == 80:
                          number5 = 0
                          number6 = number6 + 1
                          var6 = letters_numbers_and_wird_signs[number6]
                          if number6 == 80:
                              number6 = 0
                              number7 = number7 + 1
                              var7 = letters_numbers_and_wird_signs[number7]
                              if number7 == 80:
                                  number7 = 0
                                  number8 = number8 + 1
                                  var8 = letters_numbers_and_wird_signs[number8]
                                  if number8 == 80:
                                      number8 = 0
                                      number9 = number9 + 1
                                      var9 = letters_numbers_and_wird_signs[number9]
                                      if number9 == 80:
                                          break
                


    

better()

input()


