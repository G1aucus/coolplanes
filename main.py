from FlightRadar24 import FlightRadar24API
import pyttsx3
import time

nato_phonetic_alphabet = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu'
}

fr_api = FlightRadar24API()
bounds = fr_api.get_bounds_by_point(1, 1, 35000)

coolplanes = ("C130", "SB39", "SB05", "A20N")

while True:
    flights = fr_api.get_flights(bounds = bounds)
    for planes in flights:
        aircrafttype = planes.aircraft_code 
        print(aircrafttype)
        if aircrafttype in coolplanes:
            code = planes.registration
            print(code)
            name = ""
            for letters in code:
                try: 
                    name += nato_phonetic_alphabet[letters]
                except:
                    name += letters
            info = str(name) + planes.aircraft_code + "Heding" + str(planes.heading) + "at" + str(planes.altitude) + "feet"
            engine = pyttsx3.init()
            engine.setProperty('rate', 150) 
            engine.say(info)
            engine.runAndWait()
    time.sleep(30)
# two ship viggen headding north bearing 290 100 ft 

