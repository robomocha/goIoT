pins = ['5V', '5V', 'GND', 'GPIO 14', 'GPIO 15', 'GPIO 18', 'GND', 'GPIO 23', 'GPIO 24', 'GND', 'GPIO 25', 'GPIO 8', 'GPIO 7', 'ID EEPROM', 'GND', 'GPIO 12', 'GND', 'GPIO 16', 'GPIO 20', 'GPIO 21', '3.3V', 'GPIO 2', 'GPIO 3', 'GPIO 4', 'GND', 'GPIO 17', 'GPIO 27', 'GPIO 22', '3.3V', 'GPIO 10', 'GPIO 9', 'GPIO 11', 'GND', 'ID EEPROM', 'GPIO 5', 'GPIO 6', 'GPIO 13', 'GPIO 19', 'GPIO 26', 'GND']

c = 0

while c < len(pins):
    print(c+1, pins[c])
    c+=1

    
