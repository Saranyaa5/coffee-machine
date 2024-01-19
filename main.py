MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 100,
}
coins_in_machine=0
def report():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money in machine: ${coins_in_machine}")
  coffee_machine()
def coffee_machine():
  
  def resources_avail():
    ok=True
    for i in resources:
      if ok==False :
       break
      for j in resOfCoffe:
         if(i==j):
          if(resources[i]>=resOfCoffe[j]):
           resources[i] -= resOfCoffe[j]
           ok=True
          else:
            ok=False
            break
    if ok:
       #print(f"resourse in machine:{resources}")
       get_coin=True
       return get_coin
    else:
        print("not available resoureces")
        get_coin=False
        return get_coin
  print("For resource avaliable in coffee machine type 'report'")
  coffee=input("what would you like to have?(espresso/latte/cappuccino): ")
  #print(f"resourse in machine:{resources}")
  if coffee=="report":
    report()
  resOfCoffe=(MENU[coffee]["ingredients"])
  get_coin=False
  change=0
  get_coin=resources_avail()
  while(get_coin):
   print("please insert the coin")
   quarters=int(input("how many quarters?: "))
   dimes=int(input("how many dimes?: "))
   nickles=int(input("how many nickles?: "))
   pennies=int(input("how many pennies?: "))
   collected_amount=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
   print(f"collected amount is {collected_amount}")
   if(collected_amount>MENU[coffee]["cost"]):
     change=collected_amount-MENU[coffee]["cost"]
     print(f"here is your change {format(change,'.2f')}")
     print(f"here is your {coffee} ☕ enjoy")
     get_coin=False
     global coins_in_machine
     coins_in_machine+=MENU[coffee]["cost"]
   elif(collected_amount==MENU[coffee]["cost"]):
     print(f"here is your {coffee} ☕  enjoy!")
     get_coin=False
     coins_in_machine+=MENU[coffee]["cost"]
   else:
     print("not enough money")
     for i in resources:
       for j in resOfCoffe:
          if(i==j):
            resources[i] += resOfCoffe[j]
     get_coin=False
  coffee_machine()
coffee_machine()