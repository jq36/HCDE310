#### HCDE 310
#### HW5 - Exercises

import urllib.parse, urllib.request, urllib.error, json
import pprint # Module that allows you print complicated data in a more readable way

#### Exercises: A web API

# SunriseSunset.org has an API that will give you sunrise and sunset
# information for a given latitude and longitude and, optionally, a
# specific date.
#
# You can find documentation here: https://sunrise-sunset.org/api
# But we'll cover the basics in this document. 
#
# Base URL: https://api.sunrise-sunset.org/json
#
# Parameters
# - lat (float): Latitude in decimal degrees. Required.
# - lng (float): Longitude in decimal degrees. Required.
# - date (string): Date in YYYY-MM-DD format. Also accepts other date
#   formats and even relative date formats. If not present, date defaults
#   to the current date. Optional.
# - callback (string): Callback function name. Optional. We'll omit it for these exercises.
# - formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.

# For an example, point your web browser to the following URL: 
# https://api.sunrise-sunset.org/json?lat=47.658502&lng=-122.309483&date=2023-03-09
#
# That's sunrise/sunset info for Denny Hall on the last class session of 310
# this quarter.
#
# But, if you look at it, you'll see a *small* surprise: it says sunrise
# will be at 2:32:19 PM and sunset at 2:07:08 AM.
# That's because the API returns time in Universal Coordinated Time (UTC),
# without any adjustments for time zone or things like daylight savings
# time. We won't worry about that for our exercises.
#
# The exercise below guides you through the process of writing Python
# code that uses this API to extract information about some
# sunrises and sunsets

print('-------1a--------')
## Encoding query parameters in a URL
# (1a) Use urllib.parse.urlencode() to generate the query parameter string
#      with lat and lng for Rainier Vista on campus:
#      latitude: 47.658502
#      longitude: -122.309483
#
#      Store the query parameter string in a variable called paramstr
#      and print it out. 
#
# Your output should look like:
# lat=47.658502&lng=-122.309483
# (order of parameters and values may vary, the names and values should match!)
#
latitude = 47.658502
longitude = -122.309483

params = {
    'lat': latitude,
    'lng': longitude
}
result = urllib.parse.urlencode(params)
print(result)

print('-------1b--------')
# (1b) Add (concatenate) the paremter string (the variable you created
#      above: paramstr) to the base URL, separated by a question mark:
#      https://api.sunrise-sunset.org/json
#      Store the string in a variable called sun_request and print it out.
#
# Your output should look something like: 
# https://api.sunrise-sunset.org/json?lat=47.658502&lng=-122.309483

baseurl = 'https://api.sunrise-sunset.org/json'
# Put your code here
request_url = baseurl + "?" + result
print(request_url)

print('-------2--------')
## Grabbing data off the web
# (2)  Use urllib.request.urlopen() retrieve data from the URL you created
#      above (sun_request)
#
#      Read and store the result as a *string* called sun_response_str.  
#      Print it out.
# 
# Put your code here
with urllib.request.urlopen(request_url) as response:
    request_url_response = response.read().decode()

print(request_url_response)

print('-------3--------')
## Converting a JSON string to a dictionary
# (3)  Use json.loads() to convert sun_response_str into a dictionary.
#      Store the dictionary in a variable called sun_data.
#
#      Then, print the dictionary, using the pprint.pprint() function (I have
#      imported pprint above) to turn it into a nicely indented, more readable format
#
# json.loads() read as string into a dictionary, in contrast to json.load() which
# turns an opened file into a dictionary.
#

# Put your code here
data = json.loads(request_url_response)
pprint.pprint(data)


print('-------4--------')
## Extracting relevant information from a dictionary
# (4)  Extract and print the sunrise, sunset, and day_length fields from sun_data
#
#      Print them as:
#      {{Key}}: {{Value}}
#
#      Your output format should match the sample output in the readme
#      instructions, though the contents will different, depending on
#      when you query.

# put your code here
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
day_length = data['results']['day_length']

print(f"sunrise: {sunrise}")
print(f"sunset: {sunset}")
print(f"day_length: {day_length}")

print('-------5a--------')

## Generalizing your code
# (5a) Write a function called get_day_data() that accepts the following
#      parameters:
#      - lat (float): Latitude in decimal degrees. Optional, defaults to
#        47.653457 for Rainier Vista.
#      - lng (float): Longitude in decimal degrees. Optional, defaults to
#        -122.307550 for Rainier Vista.
#      - date: date in YYYY-MM-DD format. Optional. Default to None.
#      - formatted: this parameter is passed to the API. Default to 0
#        (this is *opposite of the API's default behavior)
#
# And returns the JSON you get back. 
#
# If the function is called without a date, it should default to today
# (which is the API's default behavior if you do not pass in a date! Your
# code does not need to determine the current date!)
#
# You may find it helpful to look at the flickrREST function from class 
# when writing this code, but keep in mind that the Sunrise Sunset API 
# differs in some important ways, such as not requiring an API key.
#
# Put your code here
def get_day_data(lat=47.653457, lng=-122.307550, date=None, formatted=0):
    params = {
        'lat': lat,
        'lng': lng,
        'formatted': formatted
    }

    if date:
        params['date'] = date

    append_url = urllib.parse.urlencode(params)
    full_url = baseurl + '?' + append_url

    with urllib.request.urlopen(full_url) as response:
        return json.loads(response.read().decode())

# The following line of code tests get_day_data() with all default values:
pprint.pprint(get_day_data())

print('-------5b--------')
# (5b) Write another function called compare_day_lengths().
#
#      It should take the following parameters:
#      - date1: date in YYYY-MM-DD format. Required.
#      - date2: date in YYYY-MM-DD format. Optional, defaults to None.
#      - latlng1 (tuple of two floats): Optional, defaults to
#        (47.653457,-122.307550) for Rainier Vista.
#      - latlng2 (tuple of two floats): Optional, defaults to None.
#
# In your function, use latlng1 as the coordinates for date1 and latlng2
# as the coordinates for date 2. If latlng2 was not provided (i.e., if it 
# is None), you should use the same coordinates as latlng1.
#
# If date2 is not provided, your function should use date1's value for
# date2.
#
# Your function should print the difference between the length of date1 and
# the length of date2, i.e.,
#   day1's day_length at latlng1 - day2's day_length at latlng2
# in the format: 
#
# {{date2}}, at {{lat2}}, {{lng2}}, will be {{absolute value of(date2's
# daylength - date1's daylength)}} seconds {{shorter/longer}} than {{date1}} 
# at {{lat1}}, {{lng1}}.
#
# You do not have to worry about about past versus present tense (i.e.,
# "will be" versus "was") for this assignment!
#
# Your function should adapt the output to reduce redundancy (i.e., if location
# is the same, print it once; if the date is the same, print it once).  Examples:
#
# Examples:
# Compare Halloween and Thanksgiving 2022 at Rainier Vista:
# compare_day_lengths(date1="2022-10-31",date2="2022-11-24")
# 2022-11-24, at 47.6535, -122.3076, will be 3862 seconds shorter than 2022-10-31.
# 
# Compare first day of the quarter at UW with the first day of the quarter at UofO:
# compare_day_lengths(date1="2023-01-03",date2="2023-01-04",latlng2=(44.04468909342273,-123.07273968820778))
# 2023-01-04, at 44.0447, -123.0727, will be 1643 seconds longer than 2023-01-03 at 47.6535, -122.3076.
#
# Compare the last day of our quarter at UW and WSU:
# compare_day_lengths(date1="2023-03-09",latlng2=(46.73176814034095,-117.1605623031192))
# 2023-03-09, at 46.7318, -117.1606, will be 57 seconds longer than at 47.6535, -122.3076.
#
# Compare the same day and time:
# compare_day_lengths(date1="2022-10-31")
# Cannot compare the same date and location.
#
# I decided to round to four digits after the decimal in my output for lat, lng.
# You can round too if you want.
#
# This function should call get_day_data(). After you write it, uncomment
# the test code to try it out.
#
# Put your code here
def compare_day_lengths(date1, date2=None, latlng1=(47.653457, -122.307550), latlng2=None):
    if date2 is None:
        date2 = date1
    if latlng2 is None:
        latlng2 = latlng1

    day_data1 = get_day_data(latlng1[0], latlng1[1], date1)
    day_data2 = get_day_data(latlng2[0], latlng2[1], date2)

    day_length1 = day_data1['results']['day_length']
    day_length2 = day_data2['results']['day_length']

    gap = abs(day_length2 - day_length1)

    if day_length2 > day_length1:
        difference = "longer"
    else:
        difference = "shorter"

    # Creating the output message
    if date1 == date2 and latlng1 == latlng2:
        print("Cannot compare the same date and location.")
    elif date1 == date2 and latlng1 != latlng2:
        print(f"{date2}, at {round(latlng2[0], 4)}, {round(latlng2[1], 4)}, will be {gap} seconds {difference} than at {round(latlng1[0], 4)}, {round(latlng1[1], 4)}.")
    elif date1 != date2 and latlng1 != latlng2:
        print(f"{date2}, at {round(latlng2[0], 4)}, {round(latlng2[1], 4)}, will be {gap} seconds {difference} than {date1} at {round(latlng1[0], 4)}, {round(latlng1[1], 4)}.")
    elif date1 != date2 and latlng1 == latlng2:
        print(f"{date2}, at {round(latlng2[0], 4)}, {round(latlng2[1], 4)}, will be {gap} seconds {difference} than {date1}.")
# The following lines test compare_day_lengths():

print("Compare the day the assignment is posted to when it is due:")
compare_day_lengths(date1="2023-02-15",date2="2023-02-22")
print("Compare the first day of class to the last:")
compare_day_lengths(date1="2023-01-03",date2="2023-03-09")
print("Compare Halloween and Thanksgiving 2022 at Rainier Vista")
compare_day_lengths(date1="2022-10-31",date2="2022-11-24")
print("Compare first day of the quarter at UW with the first day of the quarter at UofO:")
compare_day_lengths(date1="2023-01-03",date2="2023-01-04",latlng2=(44.04468909342273,-123.07273968820778))
print("Compare the last day of our quarter at UW and WSU:")
compare_day_lengths(date1="2023-03-09",latlng2=(46.73176814034095,-117.1605623031192))
print("Compare the same day and time:")
compare_day_lengths(date1="2022-10-31")

print('-------6--------')
print( '-------6a--------')
# (6a) Uncomment the bogus URL request below.  It should cause an
#      exception. This exception occurs when you request an invalid URL.
#      Wrap the urlopen() call in a try/except block similar to what we
#      did in the safe_get() example from class -- by "wrap",
#      I mean write code around it. Your code should catch
#      urllib.error.URLError exceptions, and print out the appropriate
#      reason or error code
#
try:
    x = urllib.request.urlopen('http://hcde.washington.edu/hcdestuff')
except urllib.error.HTTPError as e:
    print("The server couldn't fulfill the request.")
    print('HTTP Error:', e.code, e.reason)

print('-------6b--------')
# (6b) Define a function get_day_data_safe(). It calls get_day_data, but
#      catches any errors that might occur (i.e., use try/except around
#      the whole get_day_data function call). If an error occurs, your
#      function should print 'Error trying to retrieve data.', followed by
#      information about the error, and return None. If it fails to reach
#      a server, it should say that.
#
# Put your code here
def get_day_data_safe(lat=47.653457, lng=-122.307550, date=None, formatted=0):
    try:
        return get_day_data(lat, lng, date, formatted)
    except urllib.error.HTTPError as e:
        print("Error trying to retrieve data.")
        print("HTTP Error:", e.code, e.reason)
    except urllib.error.URLError as e:
        print("Error trying to retrieve data.")
        print('Reason:', e.reason)
    except Exception as e:
        print("Error trying to retrieve data.")
        print("Error details:", str(e))
    return None

# Uncomment the following code to test get_day_data_safe():
# There's no 13th month, so this last one should generate an error.
pprint.pprint(get_day_data_safe())
pprint.pprint(get_day_data_safe(date="2022-13-01"))

print('-------6c--------')
# (6c) Now define a function compare_day_lengths_safe() that calls
#      get_day_data_safe() or that calls compare_day_lengths() and handles
#      errors. It should handle errors, giving feedback about errors
#      (see example output in readme, but yours may differ if you
#      implemented it differently!).
#
# HINT: The base exception class for urllib operations is urllib.error.URLError
# More information: https://docs.python.org/3/library/urllib.error.html
# 
# Put your code here
def compare_day_lengths_safe(date1, date2):
    try:
        return compare_day_lengths(date1, date2)
    except urllib.error.HTTPError as e:
        print("Error trying to retrieve data.")
        print("HTTP Error:", e.code, e.reason)
    except urllib.error.URLError as e:
        print("Error trying to retrieve data.")
        print('Reason:', e.reason)
    except Exception as e:
        print("Error trying to retrieve data.")
        print("Error details:", str(e))
    return None
# Uncomment the following code to test it.
compare_day_lengths_safe(date1="2023-01-03",date2="2023-03-09")
compare_day_lengths_safe(date1="2023-13-25",date2="2023-12-43")

print('-------6d--------')
# (6d) Now, compare two dates at locations/dates of interest to you.
#      That location should not be Rainier Vista or Odegaard -- I 
#      know you love campus, but some variety is good!
#
# To get latitude and longitude for a location, you can use this website: 
# https://www.latlong.net
# or you can click on a point in Google maps and it *usually* will bring
# up a small box with latitude and longitude in the bottom center, or right click.
# on a point to copy the location. 
#
# Put your code here
print("I picked how much days shortened at the start/end point at Hongkong.")
compare_day_lengths(date1="2023-01-01", date2="2023-12-30", latlng1=(22.396427,114.109497))
