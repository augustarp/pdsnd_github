import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    cities = ['chicago','new york city','washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
     city = input("Would you like to see the data for which city? Chicago, New York City or Washington?: ").lower()
     if city not in cities:
      print("This city is not available. Please try again")
      continue
     else:
      break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
     month = input("Which month? Choose a month from January to June or All for all months:").lower()
     if month not in months:    
      print("This month is not available. Please try again")
      continue
     else:
      break
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:    
     day = input("Which day of the week? Choose from Monday to Friday or All for all days: ").lower().title()
     if day not in days:    
      print("This day is not available. Please try again")
      continue
     else:
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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]   

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print('Most frequent month:', most_month)

    # TO DO: display the most common day of the week
    most_day = df['day_of_week'].mode()[0]
    print('Most frequent day of the week:', most_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print('Most frequent Hour:', most_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_ststation = df['Start Station'].mode()[0]
    print('Most popular start station used:', most_ststation)

    # TO DO: display most commonly used end station
    most_endstation = df['End Station'].mode()[0]
    print('Most popular end station used:', most_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " and " + df['End Station']
    print('The most frequent combination of start station and end station trip is:\n {}'.format((df['combination'].mode()[0])))
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Time = sum(df['Trip Duration'])/3660
    print('Total travel time: ', int(Total_Time), ' hours')   
    
    # TO DO: display mean travel time
    Avg_Time = df['Trip Duration'].mean()
    print('Average travel time: ', int(Avg_Time/60), ' minutes')
    print("\nThis took %s seconds." % (time.time() - start_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User Types:', user_type)
    # TO DO: Display counts of gender (only available for NYC and Chicago)
    try:
      gender_type = df['Gender'].value_counts()
      print("\nGender Types:\n", gender_type)
    except KeyError:
      print('Gender Types: No data available for this selection.')

    # TO DO: Display earliest, most recent, and most common year of birth (only available for NYC and Chicago)
    try:
      earliest_year = df['Birth Year'].min()
      print("\nEarliest year:", int(earliest_year))
    except KeyError:
      print('Earliest year: No data available for this selection.')
   
    try:
      recent_year = df['Birth Year'].max()
      print('Most recent year:',  int(recent_year))
    except KeyError:
      print('Most recent year: No data available for this selection.')
    
    try:
      frequent_year = df['Birth Year'].mode()[0]
      print('Most common year:', int(frequent_year) )
    except KeyError:
      print('Most common year: No data available for this selection.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def see_raw_data(df):
    
    """prompt the user if they want to see 5 lines of raw data
       Display that data if the answer is 'yes'
       Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration
       Stop when the user says 'no' or there is no more raw data to display"""
    
    load_data = input('\nWould you like to see the first 5 rows of data? Please enter yes or no:\n').lower()
    i = 0
    while load_data == 'yes':
        if i >= len(df):
            print(df.iloc[i-4:len(df)])
            print ("There is no more data available")
            break
        print(df.iloc[i:i+5])
        i += 5
        more_data = input('Would you like to see the next 5 rows? Please enter yes or no:\n').lower()
        if more_data != 'yes':
            break         
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
