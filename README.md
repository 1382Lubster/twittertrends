# twittertrends
Get twitter trends by location


The script obtains a list of all available locations as a JSON file 
#### available_locs_for_trend.json
and enables accessing top trends on Twitter by location.

The main function can be saved as a python file and run from the terminal as:
#### python filename.py loc
or 
#### !python filename.py loc
if running on colab.

----------------------------------

loc could assume any of the country/ location codes available in the JSON file. 
To obtain trends for GB the following code will fetch the top 50 twitter trends 
#### python filename.py GB
and save them in JSON format with a file name
#### twitter_GB_trends.json
