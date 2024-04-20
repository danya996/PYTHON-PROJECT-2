# Final-Project-Statistical-Modelling-with-Python

## Project/Goals
The goal of this project is to analyze data from urban bike-sharing stations to explore the relationship between bike station usage and nearby Points of Interest (POIs). The main objectives of the project include collecting data using CityBikes, Foursquare, and Yelp APIs, building regression models to predict bike usage at different locations, and comparing the data quality and coverage of different APIs in the selected area.

## Process
Data Collection and Preprocessing

Collect bike station data from the CityBikes API and gather information about nearby Points of Interest (POIs) from the Foursquare and Yelp APIs. Data preprocessing involves cleaning, merging data from different sources, and processing latitude and longitude data to ensure accurate matching.
Data Exploration and Visualization

Conduct exploratory data analysis (EDA), including exploring the geographical distribution of bike stations using visualization methods and analyzing the relationship between POI categories and the number of bike stations.
Model Building and Evaluation

Build regression models to analyze the relationship between the bike quantity and POI features (such as ratings) and evaluate model performance. Explore potential approaches to transform the regression problem into a classification problem.
Results

## Results
When comparing the Foursquare and Yelp APIs, it was observed that Foursquare provided richer information about Points of Interest (POIs) in the selected area. Regression model analysis revealed that there is no statistically significant relationship between the ratings of POIs and the usage quantity of bike stations. While some trends were observed, the model's ability to explain these relationships was limited.

## Challenges 
During the course of the project, I encountered several significant challenges that had a notable impact on data collection and analysis:
Data Matching and Geographic Precision API Request Limits and Data Volume Handling Adjusting Analytical Strategies Unexplored Influencing Factors

## Future Goals
(what would you do if you had more time?)
If I had more time, I would explore additional external factors that could potentially impact bike usage, including weather conditions, traffic flow, and more. Additionally, I am interested in further developing the model by transforming it into a classification model to provide a more intuitive prediction of usage patterns
