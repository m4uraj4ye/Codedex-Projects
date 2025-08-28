#global variable
zodiac_list = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces"
    ]

def zodiac_checker():
    birth_month = int(input("\nWhich number month were you born in?: "))
    birth_date = int(input("\nWhat date were you born on?: "))  
    # nested if/elif/else statements to calculate the zodiac sign
    if birth_month == 1:
        if birth_date >= 21:
            zodiac = "Aquarius"
        elif birth_date < 21:
            zodiac = "Capricorn"   
    elif birth_month == 2:
        if birth_date >= 19:
            zodiac = "Pisces"
        elif birth_date < 19:
            zodiac = "Aquarius"
    elif birth_month == 3:
        if birth_date >= 21:
            zodiac = "Aries"
        elif birth_date < 21:
            zodiac = "Pisces"
    elif birth_month == 4:
        if birth_date >= 20:
            zodiac = "Taurus"
        elif birth_date < 20:
            zodiac = "Aries"
    elif birth_month == 5:
        if birth_date >= 21:
            zodiac = "Gemini"
        elif birth_date < 21:
            zodiac = "Taurus"
    elif birth_month == 6:
        if birth_date >= 21:
            zodiac = "Cancer"
        elif birth_date < 21:
            zodiac = "Gemini"
    elif birth_month == 7:
        if birth_date >= 23:
            zodiac = "Leo"
        elif birth_date < 22:
            zodiac = "Cancer"
    elif birth_month == 8:
        if birth_date >= 23:
            zodiac = "Virgo"
        elif birth_date < 23:
            zodiac = "Leo"
    elif birth_month == 9:
        if birth_date >= 23:
            zodiac = "Libra"
        elif birth_date < 23:
            zodiac = "Virgo"
    elif birth_month == 10:
        if birth_date >= 23:
            zodiac = "Scorpio"
        elif birth_date < 23:
            zodiac = "Libra"
    elif birth_month == 11:
        if birth_date >= 22:
            zodiac = "Sagittarius"
        elif birth_date < 22:
            zodiac = "Scorpio"
    elif birth_month == 12:
        if birth_date >= 21:
            zodiac = "Capricorn"
        elif birth_date < 19:
            zodiac = "Sagittarius"
    #validation for inputting birthdates
    elif birth_month > 13 or birth_month < 1 or birth_date > 31 or birth_date < 1:
        print("\nError: invalid input, please try again")
        zodiac_checker()
    #outputs user's zodiac sign in an f-string
    zodiac_message = f"\nYour zodiac sign is {zodiac}! "
    print(zodiac_message)
    continue_playing()
    
#class to initialise zodiac signs
class Information:
    def __init__(self,sign,symbol,element,traits):
        self.sign = sign
        self.symbol = symbol
        self.element = element
        self.traits = traits
#function for an interchangable message depending on sign chosen
    def info_dump(self):
        print("\n" + self.sign + " are "+ self.element + " sign, their symbol is " + self.symbol + ". They are known for their: " + self.traits + ".")

#defining each zodiac sign as an object
aries = Information("Aries","the ram","a fire","boldness, energy, and leadership")
taurus = Information("Taurus","the bull","an earth","perseverance, patience, and stubborness")
gemini = Information("Gemini", "the twins","an air","curiousity, quick-wit, and adaptibility")
cancer = Information("Cancer", "the crab", "a water", "generosity, sensitivity, and intuition")
leo = Information("Leo","the lion","a fire","charisma, loyalty, and creativity")
virgo = Information("Virgo", "the virgin","an earth","practicality, adaptability, and diligence")
libra = Information("Libra","the scales","an air","diplomacy, empathy, and charm")
scorpio = Information("Scorpio","the scorpion","a water","determination, intuition, and intensity")
sagittarius = Information("Sagittarius", "the archer","a fire","integrity, independence, and compassion")
capricorn = Information("Capricorn","the sea-goat","an earth","perseverance, discipline, and loyalty")
aquarius = Information("Aquarius","the water-bearer","an air","intellect, independence, and uniqueness")
pisces = Information("Pisces","the two fishes","a water","intuition, sensitvity, and adaptability")

def learn_more():
    #function to find out more about the zodiac signs
    print("Zodiac list:")
    print(zodiac_list)
    answer = str(input("\nWhich sign would you like to learn about?: "))
    #nested if/elif/else to select a sign using list index
    if answer == zodiac_list[0]:
        aries.info_dump()
    elif answer == zodiac_list[1]:
        taurus.info_dump()
    elif answer == zodiac_list[2]:
        gemini.info_dump()
    elif answer == zodiac_list[3]:
        cancer.info_dump()
    elif answer == zodiac_list[4]:
        leo.info_dump()
    elif answer == zodiac_list[5]:
        virgo.info_dump()
    elif answer == zodiac_list[6]:
        libra.info_dump()
    elif answer == zodiac_list[7]:
        scorpio.info_dump()
    elif answer == zodiac_list[8]:
        sagittarius.info_dump()
    elif answer == zodiac_list[9]:
        capricorn.info_dump()
    elif answer == zodiac_list[10]:
        aquarius.info_dump()
    elif answer == zodiac_list[11]:
        pisces.info_dump()
    else:
      print("\nError: Please enter a zodiac sign - ensure your input is capitalised")
      learn_more()  
    #asks to resume playing after information has been given
    continue_playing()

#selection menu
def start_menu():
    print("======================")
    print("    Zodiac library    ")
    print("======================")
    print("\n1) Find out my zodiac sign")
    print("2) Learn more about my zodiac sign")
    print("3) Quit")
    #functions called for selection
    menu_choice = int(input("\nPlease select a number: "))
    if menu_choice == 1:
        zodiac_checker()
    elif menu_choice == 2:
        learn_more()
    elif menu_choice == 3:
        print("\nGoodbye!")
    else:
        print("Error: please input a number select the option")

#function to go back to homepage
def continue_playing():
    go_back = str(input("\nWould you like to continue playing? yes or no: "))
    if go_back == "yes":
        start_menu()
    else:
        print("\nThanks for playing!")


start_menu()