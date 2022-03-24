import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'New_york_city.csv',
             'washington': 'washington.csv'}


def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no? ")
    start_loc = 0
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    while True:
        if view_data == "no":
            break
        else:
            print(df.iloc[start_loc: start_loc + 5])
            view_display = input("Do you wish to continue? ").lower()
            if view_display == "no":
                break
            else:
                start_loc += 5


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = str(input("please choose a city : ")).lower()
        if city in CITY_DATA:

            print("that is a valid city")
            break
        else:
            print("try another city from the set CITY_DATA ")

            # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("please choose a month: ")).lower()
        months = ["january", "february", "march", "april", "may", "june"]
        if month != "all" and month not in months:
            print("try another month")
        else:
            print("it is a valid month")
            break

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("please choose a day: ")).lower()
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        if day != "all" and day not in days:
            print("try another day")

        else:
            print("it is a valid day")
            break
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df["month"] = df["Start Time"].dt.month
    popular_month = df["month"].mode()[0]
    print("the most common month = "+str(popular_month))
    # TO DO: display the most common day of week
    df["day"] = df["Start Time"].dt.day_name()
    popular_day = df["day"].mode()[0]
    print("the most common day of week = " + str(popular_day))
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    popular_hour = df["hour"].mode()[0]
    print("the most common start hour = "+str(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df["Start Station"].mode()[0]
    print("most commonly used start station = " + str(popular_start))
    # TO DO: display most commonly used end station
    popular_end = df["End Station"].mode()[0]
    print("most commonly used end station = "+str(popular_end))
    # TO DO: display most frequent combination of start station and end station trip
    a = (df["Start Station"]+" to "+df["End Station"]).value_counts().idxmax()
    print("most frequent combination of start station and end station trip = "+str(a))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = sum(df["Trip Duration"])
    print("total travel time = "+str(total))
    # TO DO: display mean travel time
    Mean = np.mean(df["Trip Duration"])
    print("mean travel time = "+str(Mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    a = df["User Type"].value_counts()
    print("counts of user types = "+str(a))

    # TO DO: Display counts of gender
    if city == 'washington':
        print("there is data for this city")
    else:
        b = df["Gender"].value_counts()
        print("counts of gender = "+str(b))

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print("there is no data for this city")
    else:
        Min_year = min(df["Birth Year"])
        print("earliest birth year = "+str(Min_year))
        Max_year = max(df["Birth Year"])
        print("most recent birth year = " + str(Max_year))
        popular_year = df["Birth Year"].mode()[0]
        print("most common year of birth = "+str(popular_year))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('-' * 40)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
