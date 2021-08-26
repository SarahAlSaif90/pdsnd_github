import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    flag=True
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Please specify a city: Chicago, New York City or Washington: " ).lower().strip()
    cities=['chicago','new york city','washington']
    if city not in cities :
        flag=False
    
    while flag is False:
        city=input(" please try again. Specify one of the following cities:Chicago, New York City or Washington: ").lower().strip()
        if city not in cities :
            flag=False
        else: 
            flag=True
        
        
       

    # get user input for month (all, january, february, ... , june)
    month=input("Please specify a  month (all, january, february, ... , june) " ).lower().strip()
    all_months=["january", "february", "march", "april", "may", "june","all"]
    if month not in all_months :
        flag=False
    
    while flag is False:
       
        month=input("Please try again. Specify a month (all, january, february, ... , june) " ).lower().strip()
        if month not in all_months :
            flag=False
        else: 
            flag=True
    
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Please specify a day of week (all, monday, tuesday, ... sunday) ").lower().strip()
    days=["Saturday", "sunday", "monday", "tuesday", "wendnesday", "thursday","friday","all"]
    if day not in days :
        flag=False
    
    while flag is False:
     
        day=input("please try again. Specify a day of week (all, monday, tuesday, ... sunday) ").lower().strip()
        if day not in days :
            flag=False
        else: 
            flag=True

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    popular_month = df['month'].mode()[0]


    # display the most common day of week
 
    popular_day = df['day_of_week'].mode()[0]


    # display the most common start hour
    
    popular_hour = df['hour'].mode()[0]
    
    
    print('1)Most common month of travel:', popular_month)
    print('2)Most common day of week travel:', popular_day)
    print('3)Most common start hour of travel:', popular_hour)    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]


    # display most frequent combination of start station and end station trip
    Combo_StartEnd=df.groupby('Start Station')['End Station'].value_counts().idxmax()
    
    
    print('1)Most commonly used start station:', popular_start_station)
    print('2)Most commonly used end station:', popular_end_station)
    print('3)Most frequent combination of start station and end station of travel:', Combo_StartEnd)    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_dur=df['Trip Duration'].sum()
    print("1)Total travel time:",total_dur )
   


    # display mean travel time
    mean_dur= df['Trip Duration'].mean()
    print("2)Mean travel time: ", mean_dur) 
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:")
    print(df['User Type'].value_counts())


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\n\nCounts of genderare given below:\n", gender)
    except:
        print ("No gender information in this city")
       
    


    # Display earliest, most recent, and most common year of birth
    try:
        earliest= df['Birth Year'].min()
        recent= df['Birth Year'].max()
        common= df['Birth Year'].mode()[0]
        print("\n\n1)The earliest year of birth: ", earliest)
        print("2)The most recent year of birth: ", recent)
        print ("3)The most common year of birth: ", common)
       
    except:
        print("No birth year infmrmation in this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def rawdata(df):
    flag1 =True
    count=5
    rowdata = input("Do you want to see the raw data? Enter Yes or No\n").lower()
    print(df.head())
    while flag1==True:
        rowdata = input("Do you want to see more raw data? Enter Yes or No\n").lower()
        if rowdata == 'yes':
           print(df[count:count+5])
           count += 5
        elif rowdata == 'no':
            flag1= False 
        else: 
            rowdata = input("Your input is incorect").lower()
            


    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        rawdata(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
