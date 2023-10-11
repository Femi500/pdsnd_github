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
   
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle     invalid inputs
    city = input("Enter a city name (chicago, new york city, washington\n\n) : ").lower()
    while city not in CITY_DATA.keys():
        print('Please Enter a valid city')
        city = input("Enter a city name(chicago, new york city, washington\n\n) : ").lower()
  
    # get user input for month (all, january, february, ... , june)
    months = ['january','febuary','march','april','may','june','all']
    while True:
        month = input("choose a month:(all,january,febuary,march,april,may,june)").lower()
        if month in months:
            break
        else:
            print('Invalid input!')
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while True:
        day = input('choose a day:(monday,tuesday,wednesday,thursday,friday,saturday,sunday,all)').lower()
        if day in days:
            break
        else:
            print('Invalid input!')                
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
    df['Start_hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','febuary','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is: {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('The most common day_of_week is: {}'.format(df['day_of_week'].mode()[0]))


    # display the most common start hour
    print('The most common start_hour is: {}'.format(df['Start_hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common Start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most common End station is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['Route'] = df['Start Station'] + ',' + df['End Station']
    print('The most common Route is: {}'.format(df['Route'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time : ', (df['Trip Duration'].sum()).round())

    # display mean travel time
    print('Average travel time : ', (df['Trip Duration'].mean()).round())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    print(df['User Type'].value_counts().to_frame())    
    
    # display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())
        
    # display earliest, most recent, and most common year of birth
        print('The most common year of birth is : ', int(df['Birth Year'].mode()[0]))
        print('The most recent year of birth is : ', int(df['Birth Year'].max()))
        print('The earliest year of birth is : ', int(df['Birth Year'].min()))
    else:
        print('There is no user for this city!')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

        
    
def display_data(df):
    # Prompt if user would like to display the raw data of that city as chucks of 5 rows based on user_input
    print('\nRaw data is available to check... \n')
    
    i = 0
    user_input = input('Would you like to display 5 rows of raw data?, please type yes or no: ').lower()
    if user_input not in ['yes','no']:
        print('That\'s invalid input!, please type yes or no')
        user_input = input('Would you like to display 5 rows of raw data?, please type yes or no').lower()
    elif user_input != 'yes':
        print('Thank you!')
    else:
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5
            user_input = input('Would you like to display more 5 rows of raw data? ').lower()
            if user_input != 'yes':
                print('Thank you!')
                break
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
