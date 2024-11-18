from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher
from pybaseball import statcast_pitcher_spin
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pybaseball import player_search_list

import sys
import os

# All the pitchers in the MLB
pitchers = [
    "Clayton Kershaw", "Max Scherzer", "Justin Verlander", "Gerrit Cole",
    "Chris Sale", "Stephen Strasburg", "Aaron Nola", "Luis Severino", "Zack Greinke",
    "Yu Darvish", "Noah Syndergaard", "Blake Snell", "Corey Kluber", "Charlie Morton",
    "Patrick Corbin", "Kyle Hendricks", "Dallas Keuchel", "Masahiro Tanaka", "Robbie Ray",
    "Lance Lynn", "Sonny Gray", "David Price", "Hyun-Jin Ryu", "Jose Berrios",
    "Mike Clevinger", "Shohei Ohtani", "Julio Urias", "James Paxton", "Tyler Glasnow",
    "Mike Soroka", "Jack Flaherty", "Walker Buehler", "Trevor Bauer", "Lucas Giolito",
    "Zack Wheeler", "Eduardo Rodriguez", "Carlos Carrasco", "Shane Bieber", "Sean Manaea",
    "Jose Quintana", "Jon Lester", "Rick Porcello", "Dylan Bundy", "Kyle Freeland",
    "German Marquez", "Chris Archer", "Jordan Zimmermann", "Brandon Woodruff", "Michael Wacha",
    "Taijuan Walker", "Alex Wood", "Joe Musgrove", "Yusei Kikuchi", "Andrew Heaney",
    "Marcus Stroman", "Rich Hill", "Adam Wainwright", "Jordan Montgomery", "Tyler Mahle",
    "Pablo Lopez", "Trevor Rogers", "Zach Plesac", "Anthony DeSclafani", "Nick Pivetta",
    "Steven Matz", "Griffin Canning", "Brady Singer", "Chris Bassitt", "Max Fried",
    "Ryan Yarbrough", "Ian Anderson", "Casey Mize", "Nate Pearson", "Michael Kopech",
    "Spencer Turnbull", "Tarik Skubal", "Tony Gonsolin", "Garrett Richards", "Jake Odorizzi",
    "Miles Mikolas", "Mike Minor", "Tanner Roark", "Vince Velasquez", "Jose Urena",
    "Drew Smyly", "Kenta Maeda", "Marco Gonzales", "Brad Keller", "Adam Plutko",
    "Daniel Ponce de Leon", "Tanner Houck", "Jameson Taillon", "Mitch Keller", "Reynaldo Lopez",
    "Cal Quantrill", "Elieser Hernandez", "Sandy Alcantara", "Devin Smeltzer", "Aaron Civale",
    "Nick Lodolo", "David Peterson", "Josiah Gray", "Michael Fulmer", "Matt Boyd",
    "Trevor Williams", "Kyle Gibson", "Chris Paddack", "Corbin Burnes", "Joe Ross",
    "Cole Irvin", "J.P. Feyereisen", "Justin Dunn", "Brandon Bielak", "Josh Fleming",
    "Paul Blackburn", "Triston McKenzie", "Kyle Muller", "Dane Dunning", "Randy Dobnak",
    "Merrill Kelly", "Tylor Megill", "Johan Oviedo", "Nick Margevicius", "Garrett Whitlock",
    "Jared Shuster", "Bailey Ober", "Jimmy Lambert", "Kris Bubic", "Daulton Jefferies",
    "Luis Garcia", "Cody Poteet", "Tucker Davidson", "Alec Mills", "Adbert Alzolay",
    "Jonathan Loaisiga", "Nestor Cortes", "Matt Strahm", "Miguel Yajure", "Jose Suarez",
    "Matt Manning", "Bryse Wilson", "Tyler Beede", "Austin Gomber", "Keegan Akin",
    "Adrian Houser", "Jake Junis", "Jeff Hoffman", "Dillon Peters", "Josh Winckowski",
    "Bruce Zimmermann", "Dean Kremer", "Chris Rodriguez", "Justin Steele", "Aaron Sanchez",
    "Blake Taylor", "JT Brubaker", "David Hale", "Josh Sborz", "Brandon Finnegan",
    "Luis Perdomo", "Andrew Kittredge", "Taylor Widener", "Casey Lawrence", "Corey Oswalt",
    "Drew Rasmussen", "Konnor Pilkington", "Tyler Alexander", "Hunter Harvey", "Anthony Kay",
    "Kohl Stewart", "Matt Shoemaker", "Ryan Weathers", "Michael King", "Jose De Leon",
    "Sean Newcomb", "Collin McHugh", "Trevor Megill", "Jordan Lyles", "Chris Ellis",
    "Nick Martinez", "Jose Castillo", "Brett Anderson", "Daniel Mengden", "Chris Flexen",
    "Mike Foltynewicz", "Tim Mayza", "Jose Alvarez", "Chi Chi Gonzalez", "Erick Fedde",
    "Chad Kuhl", "Robert Gsellman", "Jason Adam", "Stephen Gonsalves", "A.J. Alexy",
    "Cody Stashak", "Luis Cessa", "Frankie Montas", "Trey Wingenter", "Tyler Gilbert",
    "Luis Severino", "Brad Peacock", "Scott Blewett", "Jordan Hicks", "Andre Pallante",
    "Conner Greene", "Matt Andriese", "Nick Tropeano", "Ben Heller", "Dylan Covey",
    "Yacksel Rios", "Zach Thompson", "R.J. Alvarez", "Luis Avilan", "David Bednar",
    "Ben Bowden", "Aaron Slegers", "Brian Johnson", "Alex Young", "Luis Patino",
    "Humberto Castellanos", "Emilio Pagan", "Zach Eflin", "A.J. Puk", "Ryne Harper",
    "Steven Brault", "Jared Koenig", "Jay Jackson", "Sam Hentges", "Austin Voth",
    "Lucas Luetge", "Chasen Shreve", "Tyler Duffey", "Jake Faria", "James Marvel",
    "Jorge Lopez", "Edwin Uceta", "Chris Devenski", "Cory Abbott", "Brooks Raley",
    "Parker Dunshee", "Nick Goody", "Adam Kolarek", "Tommy Milone", "Max Kranick",
    "Adam Oller", "Logan Gilbert", "Elieser Hernandez", "Daniel Norris", "Javy Guerra",
    "Mitch White", "Zach Logue", "Spencer Howard", "Shane Greene", "Tommy Hunter",
    "Zach Jackson", "Joey Lucchesi", "Joel Kuhnel", "Austin Davis", "Brandon Kintzler",
    "Ross Stripling", "Matt Wisler", "Justin Miller", "Oliver Drake", "Alex Claudio",
    "David Hess", "Seth Lugo", "Ty Blach", "Lucas Sims", "Steven Okert",
    "Gabe Speier", "Phil Bickford", "Bryan Abreu", "Seth Elledge", "Phil Maton",
    "Michael Lorenzen", "Tanner Rainey", "Vladimir Gutierrez", "Sam Coonrod", "Zach Littell",
    "Genesis Cabrera", "Matt Foster", "Nick Wittgren", "Jake Diekman", "James Norwood",
    "Pierce Johnson", "Justin Topa", "Trevor Kelley", "Hunter Strickland", "Colin Poche",
    "Nick Anderson", "Kyle Crick", "Joe Jimenez", "Josh Tomlin", "Ryan Hendrix",
    "Matt Koch", "Brad Hand", "Jesse Hahn", "Hunter Wood", "Austen Williams",
    "Shawn Armstrong", "Wandy Peralta", "Aaron Loup", "Luis Rojas", "Cam Bedrosian",
    "Paul Fry", "Dustin May", "Jandel Gustave", "Daniel Hudson", "Ryan Brasier",
    "Dario Agrazal", "Luis Escobar", "Francisco Rios", "Danny Salazar", "Trevor Cahill",
    "Joe Biagini", "Victor Gonzalez", "Justin Shafer", "Manny Banuelos", "Derek Holland",
    "John Curtiss", "T.J. Zeuch", "Francis Martes", "Austin Brice", "Daniel Camarena",
    "Spenser Watkins", "Jason Foley", "Sam Selman", "Beau Burrows", "Luis Rengifo",
    "Cam Hill", "Adam Conley", "Trevor Gott", "David Phelps", "Keone Kela",
    "Ben Rowen", "Cole Sulser", "Richard Bleier", "Matt Magill", "Tyler Rogers",
    "Edwin Diaz", "Blake Treinen", "Diego Castillo", "Josh Hader", "Jose Leclerc",
    "Ty Buttrey", "Scott Barlow", "Ken Giles", "Emmanuel Clase", "Alex Reyes",
    "Taylor Rogers", "Amir Garrett", "Craig Kimbrel", "Raisel Iglesias", "Liam Hendriks",
    "Drew Steckenrider", "Jake McGee", "Giovanny Gallegos", "Tanner Scott", "Joe Kelly",
    "John Means", "Michael Kopech", "Huascar Ynoa", "Ranger Suárez", "Tarik Skubal",
    "Casey Mize", "Triston McKenzie", "Cal Quantrill", "Drew Smyly", "Tony Gonsolin",
    "José Urquidy", "Zach Plesac", "Garrett Whitlock", "Kendall Graveman", "Aroldis Chapman",
    "Paul Sewald", "Camilo Doval", "David Price", "Luis Severino", "Steven Matz",
    "Jon Gray", "Tylor Megill", "Madison Bumgarner", "Michael Wacha", "JT Brubaker",
    "Brad Keller", "Zach Davies", "Wade Miley", "Danny Duffy", "Chris Flexen",
    "Elieser Hernandez", "Adrian Houser", "Carlos Martínez", "J.P. Feyereisen", "Erick Fedde",
    "Ryan Yarbrough", "Dane Dunning", "Nick Pivetta", "Cole Irvin", "John Gant",
    "Jake Odorizzi", "Domingo Germán", "Chad Kuhl", "James Kaprielian", "Tyler Anderson",
    "Tanner Houck", "Dylan Bundy", "Trevor Cahill", "Kwang Hyun Kim", "Brett Anderson",
    "Bartolo Colon", "Aníbal Sánchez", "Jake Arrieta", "Marco Estrada", "Jason Vargas",
    "Tommy Milone", "Matt Harvey", "Ivan Nova", "Andrew Miller", "Jeremy Hellickson",
    "Edwin Jackson", "Chris Archer", "Homer Bailey", "Yovani Gallardo", "Lance McCullers Jr.",
    "Jeff Samardzija", "Derek Holland", "Mike Fiers", "Felix Hernandez", "Brandon Morrow",
    "Shelby Miller", "Jordan Zimmermann", "Danny Salazar", "Trevor Bauer", "Wade LeBlanc",
    "CC Sabathia", "Ricky Nolasco", "Josh Tomlin", "Ervin Santana", "Francisco Liriano",
    "Tim Lincecum", "John Lackey", "Clay Buchholz", "Daisuke Matsuzaka", "Gio Gonzalez",
    "Scott Kazmir", "Dan Straily", "Ubaldo Jiménez", "Michael Pineda", "Robbie Erlin",
    "Tyler Chatwood", "Chris Young", "Joe Kelly", "A.J. Griffin", "Trevor May",
    "Mat Latos", "Colby Lewis", "Aaron Sanchez", "Doug Fister", "Jaime Garcia",
    "Scott Feldman", "Drew Pomeranz", "Nathan Eovaldi", "Sean Newcomb", "Alex Cobb",
    "Trevor Hildenberger", "Jake McGee", "Dan Otero", "Bud Norris", "Clayton Richard",
    "Brandon McCarthy", "Doug Davis", "Logan Morrison", "Brandon Kintzler", "Adam Morgan",
    "Ty Blach", "Rafael Montero", "Miguel Castro", "Kyle Barraclough", "Matt Andriese",
    "Ryan Madson", "Fernando Rodney", "Sergio Romo", "Hunter Strickland", "Tyson Ross",
    "Brian Matusz", "Luis Avilán", "Jesse Chavez", "Tom Koehler", "Heath Hembree",
    "Luke Hochevar", "Blake Treinen", "Mark Melancon", "David Phelps", "Hector Santiago",
    "Jeremy Guthrie", "Ryan Buchter", "Vance Worley", "Chris Capuano", "Wilmer Font",
    "Pedro Baez", "Dustin McGowan", "Jim Johnson", "Jhoulys Chacín", "Oliver Pérez",
    "Jason Hammel", "Nick Tropeano", "Francisco Rodríguez", "Scott Downs", "Zach Britton",
    "Chase Anderson", "Randy Dobnak", "Joakim Soria", "Jake Peavy", "Mike Montgomery",
    "Craig Stammen", "Joe Nathan", "Ryan Pressly", "Javier López", "Tommy Hunter",
    "Tony Watson", "Neftalí Feliz", "Phil Coke", "Dillon Gee", "Boone Logan",
    "Brad Ziegler", "Kevin Jepsen", "Chris Hatcher", "Tim Collins", "Jason Marquis",
    "Tyler Lyons", "Jerry Blevins", "Carlos Villanueva", "Matt Garza", "Brett Cecil",
    "Erasmo Ramírez", "Jorge de la Rosa", "Aaron Harang", "Vin Mazzaro", "Michael Lorenzen",
    "Antonio Bastardo", "Ryan Dempster", "J.A. Happ", "Mark Buehrle", "Ross Detwiler",
    "Pat Neshek", "Eric O'Flaherty", "Joel Peralta", "Vicente Padilla", "Eddie Guardado",
    "Jeff Francis", "Zach Duke", "Andrew Chafin", "Mike Adams", "Luis Perdomo",
    "Randy Choate", "Chris Perez", "Tom Gorzelanny", "Aaron Crow", "Ricky Romero",
    "Scott Baker", "Daisuke Matsuzaka", "Kerry Wood", "Rich Harden", "Shaun Marcum",
    "Jake Westbrook", "Justin Masterson", "Brad Penny", "Aaron Cook", "Jon Rauch",
    "Chris Volstad", "Tom Gorzelanny", "Carlos Marmol", "George Kontos", "Blake Beavan",
    "Paul Maholm", "Brad Lincoln", "Felipe Paulino", "Jarrod Parker", "Nick Blackburn",
    "Clayton Blackburn", "Jaime Barria", "Wilmer Flores", "Andrew Triggs", "Ryan Weber",
    "Tyler Skaggs", "Sean O'Sullivan", "Drew Storen", "Scott Carroll", "Logan Ondrusek",
    "Josh Outman", "Lucas Harrell", "Henderson Alvarez", "Esmerling Vasquez", "Dustin Moseley",
    "Luis Mendoza", "David Hernandez", "Brandon Beachy", "Tom Wilhelmsen", "Brian Duensing",
    "Kyle Lobstein", "Ross Ohlendorf", "Alfredo Aceves", "Luis Cruz", "Zach Stewart",
    "Brian Wilson", "Tyler Thornburg", "Andrew Bailey", "Jeff Karstens", "Dallas Braden",
    "Jason Schmidt", "Aaron Heilman", "Armando Galarraga", "Barry Zito", "Kyle Farnsworth",
    "Jonathan Sánchez", "Cory Lidle", "Kevin Correia", "Freddy García", "Chien-Ming Wang",
    "Mike Pelfrey", "Vicente Padilla", "Sidney Ponson", "Jason Jennings", "Jorge Sosa",
    "Byung-Hyun Kim", "Cliff Politte", "Jeff Weaver", "Julio Teheran", "Vladimir Nunez",
    "Tony Armas Jr.", "Esteban Loaiza", "John Parrish", "Chris Sampson", "Frank Francisco",
    "Matt Albers", "Bobby Jenks", "Octavio Dotel", "Bruce Chen", "Miguel Batista",
    "Horacio Ramírez", "Tim Redding", "R.A. Dickey", "Joel Hanrahan", "Kyle Kendrick",
    "Ryan Vogelsong", "Dan Wheeler", "Mark Prior", "Brad Hennessey", "Jason Isringhausen",
    "Matt Capps", "Todd Coffey", "Brian Bannister", "Chan Ho Park", "Scott Kazmir",
    "Jorge Julio", "Clay Meredith", "Dan Meyer", "Carlos Silva", "Kelvim Escobar"
]


def create_folder(folder_path):
    """Creates a folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully!")
    else:
        print(f"Folder '{folder_path}' already exists.")

def download_all_injured_players_data():
    create_folder("./.data/injured")
    injured_players_data = pd.read_csv('./player_info/MLB_Tommy_John_Surgery_List.csv')

    print(injured_players_data.head())

    # Iterate through injury data
    MLB_TJ = (injured_players_data.query("Level == 'MLB' and Position == 'P' and Year >= 2016"))

    print(list(injured_players_data.columns))
    print(list(MLB_TJ.columns))
    i = 1
    for row in MLB_TJ.index:
        year = MLB_TJ['Year'][row]
        name = MLB_TJ['Player'][row]
        id = MLB_TJ['mlbamid'][row]
        
        player_id = str(int(id))
        print(i, player_id, name, year)
        data = statcast_pitcher(str(year-1)+'-01-01', str(year)+'-01-01', player_id=id)
        csv_file_name= './.data/injured/'+player_id+"-"+name+"-"+str(year)+".csv"
        print("csv_file_name=", csv_file_name)  
        data.to_csv(csv_file_name)
        i+=1

def download_all_healthy_players_data():
    print("Downloaing healthy players data")

    create_folder("./.data/healthy")

    injured_players_data = pd.read_csv('./player_info/MLB_Tommy_John_Surgery_List.csv')
    pitchers_tuples = []
    healthy_pitchers = [p for p in pitchers if p not in injured_players_data['Player'].values]
    for i in healthy_pitchers:
        pitchers_tuples.append(i.split())

    print(pitchers_tuples)

    values = []
    for i in range(len(pitchers_tuples)):
        x = playerid_lookup(pitchers_tuples[i][1], pitchers_tuples[i][0])
        values.append(x)
    MLB_healthy = pd.concat(values, ignore_index=True)
    print(MLB_healthy.head())
    print(MLB_healthy.shape)

    i = 1
    for row in MLB_healthy.index:
        year = 2024
        name = MLB_healthy['name_first'].iloc[row] + MLB_healthy['name_last'].iloc[row]
        id = MLB_healthy['key_mlbam'].iloc[row]        
        player_id = str(int(id))
        print(i, player_id, name, year)
        data = statcast_pitcher(str(year-1)+'-01-01', str(year)+'-01-01', player_id=id)
        csv_file_name= './.data/healthy/'+player_id+"-"+name+"-"+str(year)+".csv"
        print("csv_file_name=", csv_file_name)  
        data.to_csv(csv_file_name)
        i+=1


if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "injured":
        download_all_injured_players_data()
    elif arg == "healthy":
        download_all_healthy_players_data()
    else:
        print("Please provide arg: injured or healthy")
