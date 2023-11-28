[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/9XopXBnF)
# Homework 5: Accessing API data

We can be flexible on part 2 if you need a couple more days (e.g., if you have bad luck with the first API you pick), but please get part 1 turned in by the deadline. 

What to hand in, on Github:

* hw5-exercises.py: Exercises that use a web API to get sunrise/sunset time
* hw5-application.py: An application that uses a web API of your choice. You'll have to create this file. 
* hw5-writeup.pdf or hw5-writeup.md: A short description of what your application does and sample output (see part 2)
* If you used your app to make an HTML page, a chart, or some other output, please include that as well by adding it to the Git repository. And feel free to share on the Slack group.

In this assignment, you will process live data from the Web. Six exercises will guide you through the process of writing an application that uses a web API. It will cover basic building blocks that are used in any application that uses data from the Web: constructing queries, downloading data via HTTP, handling errors, and extracting relevant information. After you've completed the exercises you will be asked to use a web API of your choice to make your own application.


Before diving in, review grading comments from previous homeworks. We have been pointing out potential issues that, if not fixed, will make this part of the quarter more difficult. Questions? Please come to office hours.	

# Part 1: Exercises
Look at hw5-exercises.py. It contains all the instructions and guidance you need to do the exercises. An example your program's output is included at the end of the assignment, but, now that we are using live data, your output will vary!
 
# Part 2: Your own application

## Code
Find a web API that returns JSON-formatted data. If you need a little more guidance, you can use the OpenWeatherMap API if you want, but you need to use an endpoint (or base URL) other than [http://api.openweathermap.org/data/2.5/weather](http://api.openweathermap.org/data/2.5/weather) or [https://openweathermap.org/forecast5](https://openweathermap.org/forecast5). You cannot use the Sunrise Sunset API from the exercise or the NASA APOD API or the Wikipedia API or the Zippopotamus API.

Also, we strongly recommend that, for this first API assignment, you avoid APIs that require authentication beyond a simple API key. In particular, unless you have previously worked with OAuth, we recommend avoiding APIs that require it for this assignment. 

**Note:** Do not add/commit/push your API key in your Github repository. If your work in part 2 requires an API key, use the approach outlined in the Canvas page called “Working with API keys and other secrets in your projects” to write your code.  

Many services (like the OpenWeatherMap API that we used in class) require that you register for an API key, so you may have to go through a registration process before you can start using their API. We encourage you to share any of your experiences with APIs on the HCDE310 Slack group, in the #projects channel: what steps you used to create an account (if any), what problems you came across, and what queries you used to gather data. But please don't share complete code for using an API.

Also, for this assignment, we want you to get practice directly accessing API data, including using your code to build the URLs that you must call and processing the JSON. Because of this, **you may not use third-party modules to access the API for HW5** (though you are welcome to for the project). You may (and should!) use modules included in Python 3, like json and urllib. You may also use the [Requests module](https://pypi.org/project/requests/), which you would need to install and which has some similar functionality to urllib - some API documentation uses Requests.

The assignment is open-ended, but your application should meet these minimum requirements:
1.	Handle any errors due to HTTP or connection related exceptions (e.g., use `try/except` or reuse `safe_get()` that we discussed in class).
2.	Have at least one function that takes in at least one parameter and uses the parameter to invoke a call to a web API of your choosing. The function should return a dictionary or list with data from the API call.
3.	Have at least one function that extracts and outputs information of interest. This information may either be printed out (which is easiest), written to a CSV-formatted file (which you can then plot in Google Docs or another tool) or used to generate an HTML page. For example, a function that fulfills this requirement might take in a stock symbol as a parameter and print its price. A more complicated function or set of functions might write out a file with the price of the stock over the past 30 days.
4. Repeatedly call one or more of the functions in (2) or (3) using data from a list of values. For example, your code might contain a list of your favorite restaurants in Seattle. Your program would then iterate over this list and print out a review for each restaurant. Alternatively, you can accept a user input that determines the query parameter (e.g., asking the user for their latitude and longitude and then using that for your API call). For user input, you can use the `input()` function in Python.

Put your application in the file `hw5-application.py`.

## Write-up

You should also submit a PDF (`hw5-writeup.pdf`) or markdown (`hw5-writeup.md`) file that contains a short description of what your program does, a sample screenshot of your program's output, and any plots you might have generated. If you generated any output files, include those as well.

_If you are wondering what a “markdown” file is, Markdown is a simple, markup language for documents that can be easily transformed into other formats (HTML, Word document, PDF, etc.). This document, for example, is written in Markdown. A tutorial for getting started with Markdown can be found [here](https://www.markdownguide.org/getting-started/).

## Note
Yes. This is like a mini-project, and would fulfill many of the requirements except for making the output useful for someone, and by not having a friendly way for users to customize their input. For the final project, we encourage you to (1) think about how your system adds value — not required for this assignment — and (2) to push yourself to make something that goes beyond the requirements, both to learn a bit more and to have a better entry in your portfolio.

In the coming weeks, we'll also be talking about how to make interactive websites (i.e., websites where users can enter data and get results), which we expect will be a useful way to make many of your projects available.

# Example Part 1 Output
```
-------1a--------
lat=47.658502&lng=-122.309483
-------1b--------
https://api.sunrise-sunset.org/json?lat=47.658502&lng=-122.309483
-------2--------
b'{"results":{"sunrise":"3:12:59 PM","sunset":"1:33:39 AM","solar_noon":"8:23:19 PM","day_length":"10:20:40","civil_twilight_begin":"2:42:54 PM","civil_twilight_end":"2:03:45 AM","nautical_twilight_begin":"2:06:49 PM","nautical_twilight_end":"2:39:49 AM","astronomical_twilight_begin":"1:31:08 PM","astronomical_twilight_end":"3:15:30 AM"},"status":"OK"}'
-------3--------
{'results': {'astronomical_twilight_begin': '1:31:08 PM',
             'astronomical_twilight_end': '3:15:30 AM',
             'civil_twilight_begin': '2:42:54 PM',
             'civil_twilight_end': '2:03:45 AM',
             'day_length': '10:20:40',
             'nautical_twilight_begin': '2:06:49 PM',
             'nautical_twilight_end': '2:39:49 AM',
             'solar_noon': '8:23:19 PM',
             'sunrise': '3:12:59 PM',
             'sunset': '1:33:39 AM'},
 'status': 'OK'}
-------4--------
sunrise: 3:12:59 PM
sunset: 1:33:39 AM
day_length: 10:20:40
-------5a--------
{'results': {'astronomical_twilight_begin': '2023-02-15T13:31:08+00:00',
             'astronomical_twilight_end': '2023-02-16T03:15:30+00:00',
             'civil_twilight_begin': '2023-02-15T14:42:53+00:00',
             'civil_twilight_end': '2023-02-16T02:03:45+00:00',
             'day_length': 37242,
             'nautical_twilight_begin': '2023-02-15T14:06:48+00:00',
             'nautical_twilight_end': '2023-02-16T02:39:49+00:00',
             'solar_noon': '2023-02-15T20:23:19+00:00',
             'sunrise': '2023-02-15T15:12:58+00:00',
             'sunset': '2023-02-16T01:33:40+00:00'},
 'status': 'OK'}
-------5b--------
Compare the day the assignment is posted to when it is due:
2023-02-22, at 47.6535, -122.3076, will be 1381 seconds longer than 2023-02-15.
Compare the first day of class to the last:
2023-03-09, at 47.6535, -122.3076, will be 10707 seconds longer than 2023-01-03.
Compare Halloween and Thanksgiving 2022 at Rainier Vista
2022-11-24, at 47.6535, -122.3076, will be 3862 seconds shorter than 2022-10-31.
Compare first day of the quarter at UW with the first day of the quarter at UofO:
2023-01-04, at 44.0447, -123.0727, will be 1643 seconds longer than 2023-01-03 at 47.6535, -122.3076.
Compare the last day of our quarter at UW and WSU:
2023-03-09, at 46.7318, -117.1606, will be 57 seconds longer than at 47.6535, -122.3076.
Compare the same day and time:
Cannot compare the same date and location.
-------6--------
-------6a--------
The server couldn't fulfill the request.
Error code:  404
-------6b--------
{'results': {'astronomical_twilight_begin': '2023-02-15T13:31:08+00:00',
             'astronomical_twilight_end': '2023-02-16T03:15:30+00:00',
             'civil_twilight_begin': '2023-02-15T14:42:53+00:00',
             'civil_twilight_end': '2023-02-16T02:03:45+00:00',
             'day_length': 37242,
             'nautical_twilight_begin': '2023-02-15T14:06:48+00:00',
             'nautical_twilight_end': '2023-02-16T02:39:49+00:00',
             'solar_noon': '2023-02-15T20:23:19+00:00',
             'sunrise': '2023-02-15T15:12:58+00:00',
             'sunset': '2023-02-16T01:33:40+00:00'},
 'status': 'OK'}
Error trying to retrieve data: HTTP Error 400: Bad Request
None
-------6c--------
2023-03-09, at 47.6535, -122.3075, will be 10707 seconds longer than 2023-01-03.
There was an error with this request
-------6d--------
I picked how much days shortened at the start/end point of a recent trip to India.
2022-12-27, at 22.5726, 88.3639, will be 253 seconds shorter than 2022-12-04.
```

Note: You also may get slight (a few seconds) variations in the sunrise / sunset times and, consequently, the comparison on day lengths. It seems the API has some variability.

---

> _Based on material developed by Prof. Sean Munson._