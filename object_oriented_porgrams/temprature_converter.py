# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
def main():
   class Temprature():
     def  convertFahrenhiet(self,celsius):
       funk=(celsius*(9/5))+32
       return f"your temperature in fahrenheat is {funk}"
     def convertCelsius(self,farenhiet):
         funk2=(farenhiet-32)*(5/9)
         return f"your temperature in celcius is {funk2}"
   temp=Temprature()
   var=float(input("please enter\n 1-for Fahrenhiet to celcius conversion.. \n 2-for celcicus to fahrenheat conversion..=> "))
   if var==1:
      var2=float(input("please enter value for Fahrenhiet temprature => "))
      print(f"your temperature in Fahrenhiet is = {var2}")
      print(temp.convertCelsius(var2))
   elif var==2:
      var2=float(input("please enter value for celcius temprature => "))
      print(f"your temperature in celcicus is = {var2}")
      print(temp.convertFahrenhiet(var2))
   elif var!= 1&2:
      print("wrong input ")
      main()
main() 

      

