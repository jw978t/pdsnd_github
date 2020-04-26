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
    #JP: Take in city input and test to see if the input if one of the cities asked for
    city = input('Which city would you like to see data on? Please enter chicago, new york city, or washington: ').lower()
    while city not in ("chicago", "new york city", "washington"):
        print("Please enter one of the three cities provided: chicago, new york city, or washington: ")
        city = input().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    #JP: Take in month input and test to see if it is one of the entries asked for
    month = input("Which month would you like to see data on? all, january, february, march, april, or june? ").lower()
    while month not in ("all","january","february","march","april","june"):
        print("Please enter one of the following: all, january, february, march, april, or june: ")
        month =input().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    #JP: Take in day input and test to see if it is one of the entries asked for
    day = input("Which day would you like to see data on? all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday? ").lower()
    while day not in ("all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"):
        print("Please enter one of the following: all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday: ")
        day = input().lower()

    print('-'*40)

    #JP: Tell user what they selected for filters
    print("You chose to filter by the city: {}, in the month of: {}, on the day of the week: {}".format(city.title(), month.title(), day.title()))


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
    #JP: read data for selected city, month, day
    df = pd.read_csv(CITY_DATA[city])

    #JP: ask the user if they want to see the raw data
    print_data = input("Would you like to see the first 5 rows of data? yes or no: \n")
    x = 5
    #JP: if user says yes, show the first 5 rows
    if print_data == "yes":
        print(df[:x])

        #JP: ask the user if they want to see the next 5 rows of data
        print_more = input("Would you like to see the next 5 rows of data? yes or no: \n")
        #JP:if the user says yes, print the next 5 rows, then ask again and continue until they say no
        while print_more == "yes":
            print(df[x:x+5])
            x += 5
            print_more = input("Would you like to see the next 5 rows of data? yes or no: \n")
    print('-'*40)



#---------------------------------------------------------------------------------
#JP note to grader: code encolsed in "-" is taken from Practice Problem #3

    # convert the Start Time column to datetime
    #JP:(converts to datetime dataype)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    #JP:create two new columns 'month' and 'day_of_week' that holds month, and day name from 'Start Time' column, respectively
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    #JP:if user did not choose to look at all months Jan - Jun...
    if month != 'all':
        # use the index of the months list to get the corresponding int
        #JP: months is set to the months in the df and then given an index
        #JP: for ex january is index = 0 so month = 1
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        #JP: filter df to only show month where month is selected month by user
        df = df[df['month']==month]

    # filter by day of week if applicable
    #JP: if user did not want to view all days
    if day != 'all':
        # filter by day of week to create the new dataframe
        #JP: filter df to only show where day_of_week is selected day from user
        df = df[df['day_of_week']==day.title()]
 #---------------------------------------------------------------------------------


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #JP: find the most common month and display as month name
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].value_counts().idxmax()
    print("Most common month: ", months[most_common_month-1].title())

    # TO DO: display the most common day of week
    #JP: find most common day
    most_common_day = df['day_of_week'].value_counts().idxmax()
    print("Most common day of week: ", most_common_day)

    # TO DO: display the most common start hour
    #JP note to grader: code for most common start hour comes from Practice Problem #1 (few edits)
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most common hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Local Variables:
    start_time - holds start time of function call in order to calculate function duration stat
    popular_start_station - name of the most frequent station at the start of a trip
    popular_end_station - name of the most frequenct station at the end (desination) of a trip
    popular_trip - most frequent start and end trip stations """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #JP: find most frequent Start Station value
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print("Most popular start station: ", popular_start_station)

    # TO DO: display most commonly used end station
    #JP: find most frequent End Station value
    popular_end_station = df['End Station'].value_counts().idxmax()
    print("Most popular end station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #JP: create new column with trip including Start Station and End Station to use as column for finding most common trip
    #JP: added the 'to' to make readibility easier for user on output
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip'].value_counts().idxmax()
    print("The most popular trip: ",popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #JP: calculate sum of Trip Duration column
    total_duration = df['Trip Duration'].sum()
    print("Total travel time in seconds: ", total_duration)

    # TO DO: display mean travel time
    #JP: calculate mean of Trip Duration column
    mean_trip_duration = df['Trip Duration'].mean()
    print("Average travel time in seconds: ", mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #JP to grader: code for counts of user types from Practice Problem #2 (edits to remove extraneous output)
    user_types = df['User Type'].value_counts().to_frame()
    print("Count of user types: \n",user_types)
    print("\n")

    # TO DO: Display counts of gender
    #JP: only gender data for 2 cities, below code tries to run calculation, if the selected city does not have the Gender column, it will tell the user there is no data
    try:
        gender_count = df['Gender'].value_counts().to_frame()
    except:
        print("Sorry, there is no gender data for this city!")
    else:
        print("Count of gender: \n",gender_count)
        print("\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    #JP: only Birth Date data for 2 cities, below code tries to run calculation, if the selected city does not have the Birth Year column, it will tell the user there is no data
    try:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].value_counts().idxmax()
    except:
        print("Sorry, there is no birth year data for this city!")
    else:
        print("Earliest birth year: {} \nMost recent birth year: {} \nMost common birth year: {}".format(int(earliest_year),int(most_recent_year),int(most_common_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
