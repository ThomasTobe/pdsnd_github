import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for the city (chicago, new york city, washington) with input validation
    while True:
        city = input("Enter the name of the city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the name of the month (all, January, February, ..., June): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid input. Please enter a valid month.")

    # TO DO: get user input for day of the week (all, monday,tuesday,... sunday)
    while True:
        day = input("Enter the name of the day of the week (all, Monday, Tuesday, ..., Sunday): ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid input. Please enter a valid day of the week.")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Create an empty DataFrame to avoid errors
    df = pd.DataFrame()

    if city not in CITY_DATA:
        print("Invalid city name. Exiting.")
        return df

    # Load data based on the city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of the week from the 'Start Time' column
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.strftime('%A')

    if month != 'all':
        # Filter by month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_num = months.index(month) + 1
        df = df[df['Month'] == month_num]

    if day != 'all':
        # Filter by day of the week
        df = df[df['Day of Week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['Month'].mode()[0]
    print("The most common month: {}".format(common_month))

    # Display the most common day of the week
    common_day = df['Day of Week'].mode()[0]
    print("The most common day of the week: {}".format(common_day))

    # Display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print("The most common start hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: {}".format(common_start_station))

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(common_end_station))

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print("The most frequent combination of start station and end station trip: {}".format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {} seconds".format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {} seconds".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n{}".format(user_types))

    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n{}".format(gender_counts))
    else:
        print("Gender data not available for this city.")

    # Display the earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("Earliest birth year: {}".format(earliest_birth_year))
        print("Most recent birth year: {}".format(most_recent_birth_year))
        print("Most common birth year: {}".format(common_birth_year))
    else:
        print("Birth year data not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon user request."""
    print('\nDisplaying Raw Data...\n')
    start_time = time.time()

    i = 0
    raw_data = df.to_dict('records')

    while True:
        view_data = input("Would you like to view 5 rows of raw data? Enter yes or no: ")
        if view_data.lower() == 'yes':
            if i < len(raw_data):
                for j in range(i, i + 5):
                    print(raw_data[j])
                i += 5
            else:
                print("No more raw data to display.")
        else:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        if not city:
            break
        df = load_data(city, month, day)

        if not df.empty:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)
        else:
            print("No data available for the selected filters.")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
