## 1. Reading our MoMA Data Set ##


from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below
#Convert the Date values to int
for row in moma:
    date = row[6]
    if date !="":
        date = int(date)
        row[6]= date










## 2. Calculating Artist Ages ##

ages=[]
for row in moma:
    date=row[6]
    birth = row[3]
    if birth !="":
        age=date-birth
        ages.append(age)
    else:
        age=0
        ages.append(age)
        
#create final age list
final_ages=[]
for age in ages:
    if age>20:
        final_age=age
        final_ages.append(final_age)
    else:
        final_age="Unknown"
        final_ages.append(final_age)
        
        
        
        
        
        
        
        
        
   

## 3. Converting Ages to Decades ##

# The final_ages variable is available
# from the previous screen
decades=[]
for age in final_ages:
    if age =="Unknown":
        decade = "Unknown"
        
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade + "0s"
    decades.append(decade)
        
    

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency={}
for decade in decades:
    if decade not in decade_frequency:
        decade_frequency[decade]=1
    else:
        decade_frequency[decade]+=1


## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
template = "{name}'s birth year is {year}"
output= template.format(name=artist,year=birth_year)
print(output)

## 6. Creating an Artist Frequency Table ##

artist_freq = {}
for row in moma:
    artist = row[1]
    if artist not in artist_freq:
        artist_freq[artist]=1
    else:
        artist_freq[artist]+=1


## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    num_of_arts = artist_freq[artist]
    template = "There are {} artworks by {} in the dataset".format(num_of_arts,artist)
    return template
print(artist_summary("Henri Matisse"))

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]


for items in pop_millions:
    country = items[0]
    population = items[1]
    template = "The population of {} is {:,.2f} million".format(country,population)
    print (template)
    

## 9. Challenge: Summarizing Artwork Gender Data ##

gender_freq={}
for row in moma:
    Gender = row[5]
    if Gender not in gender_freq:
        gender_freq[Gender]=1
    else:
        gender_freq[Gender]+=1
        
for Gender,artwork in gender_freq.items():
    template = "There are {freq:,} artworks by {gender} artists".format(gender=Gender,freq=artwork)
    print(template)
    