import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze bikesharing data.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input("Which cities data would you like to see? (Chicago, New York City, Washington)")).lower()
            if city in CITY_DATA:
                print("Great choice: {} it is.".format(city.title()))
                break
            else:
                print("Thats not valid. Please choose between Chicago, New York City, Washington.")
                continue
        except:
            print("Thats not valid.")
    
    while True:
        try:
            month = str(input("Which months data would you like to see? (January through June or 'all' to choose data for all months)")).lower()
            if month in ("january", "february", "march", "april", "may", "june", "all"):
                print("Great choice: {} it is.".format(month.title()))
                break
            else:
                print("Thats not valid. Please choose between January, February, March, April, May, June, all.")
                continue
        except:
            print("Thats not valid.")
    
    while True:
        try:
            day = str(input("Which days data would you like to see? (Monday through Sunday or 'all' to choose data for all weekdays)")).lower()
            if day in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" , "all"):
                print("Great choice: {} it is.".format(day.title()))
                break
            else:
                print("Thats not valid. Please choose between Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, all.")
                continue
        except:
            print("Thats not valid.")
    
    print("You will see data for {}, month(s): {}, day(s): {}.\n".format(city.title(), month.title(), day.title()) + "-"*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing bikesharing data filtered by city, month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df["month"] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]
    
    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""
    
    months = ("January", "February", "March", "April", "May", "June", "All")
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    
    # TO DO: display the most common month
    if month == "all":
        df['Month'] = df["Start Time"].dt.month
        
        # find the most common month
        popular_month = df["Month"].mode()[0]
        print('Most Common Month: {} ({})'.format(popular_month, months[popular_month-1]))
        
    # TO DO: display the most common day of week
    # extract day from the Start Time column to create a week day column
    if day == "all":
        df['Week Day'] = df["Start Time"].dt.weekday_name

        # find the most common week day
        popular_day = df["Week Day"].mode()[0]
        print('Most Common Week Day: ', popular_day)
        
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df["Start Time"].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df["hour"].mode()[0]
    print('Most Frequent Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular start and end stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print("Most Common Start Station: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print("Most Common End Station: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["Trip"] = df["Start Station"] + " to " + df["End Station"]
    popular_trip = df["Trip"].mode()[0]
    print("Most Common Trip: ", popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The Total Travel Time is {:.2f} seconds, which equals {:.2f} minutes, {:.2f} hours, {:.2f} days.".format(total_travel_time, total_travel_time/60, total_travel_time/(60*60), total_travel_time/(60*60*24)))

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("The Average Trip Duration is {:.2f} seconds or {:.2f} minutes.".format(mean_travel_time, mean_travel_time/60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print(user_types, "\n")    

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_counts = df["Gender"].fillna("Unspecified").value_counts()
        print(gender_counts, "\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth_date = int(df["Birth Year"].min())
        most_recent_birth_date = int(df["Birth Year"].max())
        most_common_birth_date = int(df["Birth Year"].mode()[0])
        print("The oldest user was born in {}. \nThe youngest user was born in {}. \nThe most common birth year was {}.\n".format(earliest_birth_date, most_recent_birth_date, most_common_birth_date) )

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """Displays 5 rows of underlying raw data for the analysis and asks user if he/she wants to see more."""
    
    #get user input whether they want to see raw data
    while True:
        try:
            view_data = str(input("Would you like to view 5 rows of individual trip data? Enter yes or no.")).lower()
            if view_data in ("yes", "no"):
                break
        except:
            print("This was not a valid entry. Please choose from yes or no.")
            continue
     
    #display raw data by 5 rows if the user keeps answering yes
    start_loc = 0
    while (view_data == "yes"):
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_data = input("Do you wish to continue? (Yes or no): ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
