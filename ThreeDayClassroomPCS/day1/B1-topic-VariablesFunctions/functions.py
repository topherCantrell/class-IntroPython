def say_ha_why():
    print("HA!")
    print("Why,")
    
def say_hi():
    #print("HA!")
    #print("Why,")
    say_ha_why()
    print("Hello")
    print("There")

def say_bye():
    #print("HA!")
    #print("Why,")
    say_ha_why()
    print("Bye")
    print("Bye")
    
def come_and_go():
    say_ha_why()
    say_hi()
    say_bye()
    say_ha_why()
    
print('Start')
say_ha_why()
come_and_go()
print('Done')
