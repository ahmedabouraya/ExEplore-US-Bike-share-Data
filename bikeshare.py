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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('please choose one of the city "Chicago, New York City or Washington" and write it down:', ).lower()
    while city not in CITY_DATA:
        city = input('invalid city. Please, enter your chosen city again:',).lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('Write one of six months "January, February, March, April, May or June" to filter or write "All":', ).lower()
    while month not in months:
        month = input('invalid month. Please, enter your chosen month again:',).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'saturday', 'sunday', 'friday', 'all']
    day = input('Write any day of week to filter by days or just write "All":',).lower()
    while day not in days:
        day = input('invalid day. Please, enter your chosen day again:',).lower()

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
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common Month:', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Most common Day of Week:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most Common Hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common used Start Station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most common used End Station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] =   df['Start Station'] + ", " + df['End Station']
    print('Most common used start and end trip:', df['start_end'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time:', df['hour'].sum(), 'Hours')

    # TO DO: display mean travel time
    print('Average Travel Time:', df['hour'].mean(), 'Hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n', df['User Type'].value_counts())
    print()
    
    # TO DO: Display counts of gender
    try:
        print('Counts of Gender:\n', df['Gender'].value_counts())
    except:
        print('No "Gender" data in this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    try:
        print('Most Earliest year of birth:', int(df['Birth Year'].min()))
        print('Most Recent year of birth:', int(df['Birth Year'].max()))
        print('Most Common year of birth:', int(df['Birth Year'].mean()))
    except:
        print('No "Gender" data in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data (df):

    display = input('\nWould you like to display 5 rows of data? Enter yes or no.:\n',).lower()
    start_iloc = 0
    while display == 'yes':
        print(df.iloc[start_iloc:(start_iloc+5)])
        start_iloc += 5
        display = input('Do you wish to continue? Enter yes or no.:',).lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
