# musketeer
Trains a neural network with TSLA stock price data and Elon Musk's tweets in order to forecast the rise/fall of TSLA stock price given the content of a new tweet.

## Inspiration
After looking at the challenges provided, it seemed that using `CockroachDB` as a cloud-based database would be a fun idea. We threw some project proposals around and thought it would be interesting to see how machine learning could predict TSLA stock price based on Elon Musk's tweets. The eventual goal is for the neural network to be trained on many more CEO Twitter accounts so that it could forecast the stock prices of more companies.

## What it does
`musketeer` currently reads TSLA stock price data from a `.csv` file and tweets from the Twitter API. The data is cleaned and pushed into our Google Cloud hosted instance of CockroachDB.

For faster model compile times, we used a Jupyter Notebook in Google Colab. Importing data to the notebook was simple because we were able to make a few queries to our database and gather all the necessary data. From there, we indexed and padded the tweets in order to put the data through a neural network and the model was trained.

For our frontend, we built a simple flask app that would allow a user to input a user-defined "tweet" and display whether or not our model would predict an increase in stock price after the tweet. Unfortunately, we were not able to connect the model to the frontend, so it exists for purely cosmetic reasons.

## How we built it
Each team member had different tasks to complete. Here were a few that we had:
 - Find stock price data
 - Find tweet data
 - Clean stock price data
 - Clean tweet data
 - Set up CockroachDB in the cloud
 - Push stock price data into the cloud
 - Push tweet data into the cloud
 - Pull data and compile model
 - Build frontend app
 - Link frontend app with model

The only one we were not able to complete was the last one. We ran many of our tasks in parallel, though. For example, while data was being gathered and cleaned, our database was being set up. Also, when the model was being compiled and built, our frontend app was being built.

## Challenges we ran into
One challenge that we were not ready for was finding stock price data. While at first it seems like something simple, finding intraday stock data (that is hourly/minute-by-minute stock price data) is very difficult to do without paying a fair bit of money. We spent several hours just finding a dataset, but the best we could do was find TSLA stock prices from 9:00-15:00 and from `2021-12-06` to the present. This narrowed down the amount of data we could use at the end of the day.

Because of limits on Twitter's API, we were constantly having to wait for our API token to be reset, but more importantly, we were not able to gather more than 500 tweets.

Sleep deprivation proved to be an obvious challenge when we spent 1.5 hours trying to fit our word embeddings into the neural network. The problem was that we didn't correctly specify the maximum length of the embeddings.

As you may have predicted, our model had nowhere near as much data as it needed, so our validation set accuracy was pathetic.

## Accomplishments that we're proud of
 - Cleaning the data
 - Getting CockroachDB to hold all of our data
 - Interfacing with Twitter API
 - Training the model (even if it didn't do well)
 - Working as a team

## What we learned
For all of us, this was our first time using a cloud based SQL-like database. Learning how to get the certificates in order as well as connect and query the database was a fun experience.

We learned how to split up work and use GitHub to manage a large project.

None of us had ever done any sort of NLP before, so creating a classifier model using tweets was quite exciting.

## What's next for musketeer
We need to write up the `README.md`. Besides that, we plan on connecting the frontend app to the backend and seeing if we can feed the model data from different companies and see if that improves accuracy.

