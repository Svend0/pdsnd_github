import time
import pandas as pd
print ('Program Info:')
print ('Your pandas version is: ',pd.__version__,' This file was created using pandas 1.4.2')
print ('Please place python file in same directory as python data files. Thank you')

# Bikeshare Data Python Assignment for
# Programming for Data Science with Python Nanodegree Program
# Written by Svend White
#
# NB Please place python file in same diectory as python data files.
#
# As of 14-Nov-22 Using GitHub to control version

def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('-'*80)
    
    print('Hello! Let\'s explore some US bikeshare data!!')   
    
    print('-'*80)
    
    # get user input for city (chicago, new york city, washington).

    while True:

        city = input("Which City would you like to explore;\n (C) Chicago, (N) New York, (W) Washington or (Q) Quit\n => ")
        if city.lower() in ("c","n","w","q"):
            break

        else:
            print("Please enter C or N or W or Q")
    
    if city.lower() == 'q':
        city = 'quit'
        month = 'quit'
        day = "quit"
        return city, month, day

    if city.lower() == 'c':
        city = 'chicago'
    
    if city.lower() == 'n':
        city = 'new_york_city'

    if city.lower() == 'w':
        city = 'washington'

    print('It appears you have entered: ',city)
        
    # get user input for month (all, january, february, ... , june)
  
    while True:
        print('Which Month would you like to explore;\n (1) January,  (4) April, (7) July,      (10) October,')
        print(' (2) February, (5) May,   (8) August,    (11) November,\n (3) March,    (6) June,  (9) September, (12) December,')
        print(' (A) All,      (Q) Quit.')
        month = input('=>')
        if month in ("1","2","3","4","5","6","7","8","9","10","11","12","A","a","Q","q"):
            break
        else:
            print("Please enter a number between 1 and 12, or A or Q")
    
    if month in ('1','2','3','4','5','6','7','8','9','10','11','12'):
        month = month
        
    if month.lower() == 'q':
        month = "quit"
        city = "quit"
        day = "quit"
        return city, month, day

    if month.lower() == 'a':
        month = 'all'
    
# get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        print('Which Day would you like to explore;\n (1) Monday, (2) Tuesday,  (3) Wednesday, (4) Thursday,\n (5) Friday, (6) Saturday, (7) Sunday,') 
        print(' (A) All,    (Q) Quit.')
        day = input('=>')
        if day in ("1","2","3","4","5","6","7","A","a","Q","q"):
            break
        else:
            print("Please enter a number between 1 and 7, or A or Q")
    
    if day in ('1','2','3','4','5','6','7'):
        day = day
    
    if day.lower() == 'q':
        month = "quit"
        city = "quit"
        day = "quit"
        return city, month, day

    if day.lower() == 'a':
        day = 'all'    
                
    print('You entered city: ',city,' month: ',month,' day: ',day,'. Lets go ... \n')

    print('-'*80)
    
    return city, month, day        

def load_data(city, month, day):

    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load the relevant database
    
    citydb = (city+'.csv')

    print('Loading from database',citydb,'\n')

    # Adjust directory of BikeShare data files here
    
    # loaddf = ('C:/Users/svend/Python-Sandpit/BikeShare/'+citydb)

    loaddf = (citydb)
    
    dfa = pd.read_csv(loaddf)

    # Modifying Database, Converting to Date Time

    dfa['Start Time']=pd.to_datetime(dfa['Start Time'])

    # Adding Extra Column Month

    dfa['Month']=dfa['Start Time'].dt.month

    # Adding Extra Column Hour

    dfa['Hour']=dfa['Start Time'].dt.hour

    # Adding Extra Column Day

    dfa['Day']=dfa['Start Time'].dt.day

    # Adding Extra Column DayOfWeek

    dfa['DayOfWeek']=dfa['Start Time'].dt.dayofweek

    # Adding Extra Column Weekday

    dfa['Weekday']=dfa['Start Time'].dt.day_name()

    # Apply filters depending on if Month or Day is 'all', or both Month and Day are 'all', or a specific Month and Day.
    
    if month != 'all' and day != 'all':
    
        #Convert Month and Day to integer and correct month and day number to align with database time assignments
    
        month_int = int(month)-1
    
        day_int = int(day)-1
    
        dfb = dfa[((dfa.Month == month_int) & (dfa.DayOfWeek == day_int))] 

        print ('Here\'s a sneek preview of the data:\n', dfb.head(5))

        #Check if database is empty and return message

        if dfb.empty:
            
            print('\nThere is not data available for the fitlers you have set, try selecting a different day or month.\n')

    elif month == 'all' and day.isdigit():
    
        #Convert day to integer and correct day number to align with database time assignments
    
        day_int = int(day)-1
    
        dfb = dfa[(dfa.DayOfWeek == day_int)] 

        print ('Here\'s a sneek preview of the data:\n', dfb.head(5))

        #Check if database is empty and return message

        if dfb.empty:
            
            print('\nThere is not data available for the fitlers you have set, try selecting a different day.\n')

    elif day == 'all' and month.isdigit():

        #Convert month to integer and correct month number to align with database time assignments
        
        month_int = int(month)-1

        dfb = dfa[(dfa.Month == month_int)] 

        print ('Here\'s a sneek preview of the data:\n', dfb.head(5))        

        #Check if database is empty and return message

        if dfb.empty:
            
            print('\nThere is not data available for the fitlers you have set, try selecting a different month.\n')
        
    else:
    
        dfb = dfa

        #Check if database is empty and return message
        
        if dfb.empty:
            
            print('\nIt appears is no data available for the fitlers you have set, try selecting a different day and month or even a different database.\n')
        
    return dfb     
    
def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('-'*80)
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # display the most common month (using Mode)

    print('      Most Common Month:',df['Month'].mode()[0],'\n')

    # display the most common day of week (using Mode)

    print('      Most Common Day:',df['DayOfWeek'].mode()[0],'\n')

    # display the most common start hour (using Mode)

    print('      Most Common Start Hr:',df['Hour'].mode()[0],'\n')

    print('That took %s seconds.' % (time.time() - start_time),'\n')

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('-'*80)
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

    # Display most commonly used start station

    start_count = df['Start Station'].value_counts()

    # print ('\nStart Count:\n',start_count)
    
    start_mode = start_count.idxmax()
    
    print('      Most popular (mode) start station:',start_mode,'\n')

    # Display most commonly used end station

    end_count = df['End Station'].value_counts()

    # print ('\nEnd Count\n',end_count)
    
    end_mode = end_count.idxmax()
    
    print('      Most popular (mode) end station:',end_mode,'\n')

    # Display most frequent combination of start station and end station trip

    popular_route = df.groupby(['Start Station','End Station']).count()

    # print('\nPopular Route\n',popular_route)
    
    route_max = popular_route["Unnamed: 0"].idxmax()
    
    print('      Most popular start and end station combination:\n        ',route_max,'\n')

    print('That took %s seconds.' % (time.time() - start_time),'\n')


def trip_duration_stats(df):

    """Calculates and displays statistics on the total and average trip duration."""

    print('-'*80)
    
    print('\nCalculating Trip Duration...\n')
    
    start_time = time.time()

    # display total travel time

    print('      Total (cumulative) travel time:',((df['Trip Duration'].sum()/60)/60),' hours\n')

    # display mean travel time

    print('      Average trip travel time:',(df['Trip Duration'].mean()/60),' minutes\n')

    # Display time taken to perform calculations
    
    print('That took %s seconds.' % (time.time() - start_time),'\n')

def user_stats(df):

    """Calculates and displays statistics on bikeshare users."""

    print('-'*80)
    
    print('\nCalculating User Stats...\n')
    
    start_time = time.time()

    # Display counts of user types

    user_type_count = df['User Type'].value_counts()

    print('      Count of User Type\n',user_type_count,'\n')

    # Verify gender column is present

    col_names = list(df.columns)
    
    if 'Gender' in col_names:
    
        # Display counts of gender
    
        user_gender_count = df['Gender'].value_counts()

        print('      Count of Gender\n',user_gender_count,'\n')
        
    else:
        
        print('Gender column not present in selected database\n')

    if 'Birth Year' in col_names:
    
        # Display earliest, most recent, and most common year of birth

        print('\n      Earliest Date Of Birth:',df['Birth Year'].min(axis=0),'\n')

        print('      Most Recent Date of Birth:',df['Birth Year'].max(axis=0),'\n')

        print('      Most Common Year of Birth:',df['Birth Year'].mode()[0],'\n')

    else:
        
        print('Birth Year column not present in selected database\n')
        
    # Display time taken to perform calculations
    
    print('That took %s seconds.' % (time.time() - start_time),'\n')

def view_data(df):

    """Displays raw data, 5 lines at a time."""

    #Gather dimensions of array and set initial variables
    
    shape_info = df.shape
    
    max_rows_df = pd.DataFrame(shape_info)

    max_rows = max_rows_df.iloc[0,0]
    
    start_row = 0
    
    end_row = 4
    
    more_rows = 'n'

    #Display data in rows of 5 checking that maximum rows has not already been reached
    
    while end_row < max_rows:
 
        print('-'*80)

        more_rows = input('Would you like to step through the raw data? Enter (Y) Yes or (N) No: ')
    
        if more_rows.lower() == 'y':
                    
            if end_row >= max_rows:
                
                end_row = max_rows
            
            print('\nDisplaying ',start_row,' to ',end_row,' of possible',max_rows,'.\n')
                        
            # For loop to display column headings and data from database in groups of 5
            
            for i in range(0,5):
            
                for j in range(0,10):
                           
                    row_id = start_row + i
                    
                    column_title = df.columns.values.tolist()
                    
                    output = df.iloc[(row_id),(j)]
                            
                    print(column_title[j],': ',output)
                                        
                print('\n')
                    
            start_row += 5
            
            end_row += 5
                
            if end_row >= max_rows:
            
                print("\nEnd of List\n")
                    
        else:
            
            print("Returning to Main Program")

            break
    return

def main():

    """Core program, calls functions in ordder, checking for 'quit' or 'empty database' flags."""

    while True:
        city, month, day = get_filters()
    
        # Verify user does not want to quit, then load database
        
        if city != 'quit' and month != ' quit' and day != 'quit':
        
            df = load_data(city, month, day)
            
            if df.empty:
                
                restart = input('Would you like to restart? Enter (Y) Yes or (N) No:\n')
        
                if restart.lower() != 'y':
                
                    break
                
            else:    
                
                # Calculate information via functions
                
                time_stats(df)
        
                station_stats(df)
        
                trip_duration_stats(df)
        
                user_stats(df)
        
                view_data(df)

        else:

            # Check if user has reviewed enough raw data, if so return to start screen.

            restart = input('\nWould you like to restart? Enter (Y) Yes or (N) No:\n')
        
            if restart.lower() != 'y':
                
                break

if __name__ == "__main__":
    main()
