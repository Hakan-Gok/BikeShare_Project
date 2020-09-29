# edit test
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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    check_inp = 0

    while check_inp==0:
          city = input('Would you like to see data for CHICAGO, NEW YORK CITY, or WASHINGTON? Choose one option please\n')
          city = city.lower()
          if  city.upper() not in ("CHICAGO","NEW YORK CITY","WASHINGTON") :
            print ('This is not valid input! Valid options are CHICAGO, NEW YORK CITY, or WASHINGTON')
            continue
          else :
              check_inp=1
              break

    # TO DO: get user input for month (all, january, february, ... , june)
    while check_inp==1 :
          month = input('Which month? all, january, february, march, april, may, june? Choose one option please\n')
          month = month.lower()
          if  month.lower() not in ("all","january","february","march","april","may","june") :
            print ('This is not valid input! Valid options are all,january, february, march, april, may, june')
            continue
          else :
             check_inp=0
             break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while check_inp==0  :
          day = input('Which day? all,monday,tuesday,wednesday,thursday,friday,saturday,sunday? Choose one option please\n')
          day = day.lower()
          if  day.lower() not in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday") :
            print ('Valid options are all,monday,tuesday,wednesday,thursday,friday,saturday,sunday')
            continue
          else :
             check_inp=1
             break

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
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month
 

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time :", total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print("Counts of user types:", counts_of_user_types )

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("Counts of gender:", counts_of_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        birth_year = df['Birth Year']

        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)

        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input='yes'

    while user_input in ['yes'] and index+5 < df.shape[0]:
        user_input = input('would you like to display 5 rows of raw data? Enter yes or no.\n').lower()
        print(df.iloc[index:index+5])
        index += 5    
    

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
