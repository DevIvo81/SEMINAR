from random import choice

def get_all_readings():
    
    temperatures = [x for x in range(8, 39)]
    temp = choice(temperatures)

    phs = [x for x in range(3, 15)]
    ph = choice(phs)

    humidities = [x for x in range(15, 90)]
    hum = choice(humidities)
    
    return [temp, ph, hum]