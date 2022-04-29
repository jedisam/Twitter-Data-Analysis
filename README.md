# Twitter-Data-Analysis

It is an analysis done on data extracted from twitter based on chosen hashtags. The tweets focuses on war between Ukraine and Russia as well as global inflation rates.

## Usage
1. Manual build
   Run the extract and clean modules
```python
python extract_dataframe.py
python clean_tweets_dataframe.py
```
2. Docker(Recommonded)
   1. git clone https://github.com/jedisam/Twitter-Data-Analysis.git
   2. Extract file

```python
cd Twitter-Data-Analysis
docker-compose up
```
    This will up a postgres database in on local pc and connect with streamlit app

## Test
To test the methods written in the modules use the pytest package and run:
```python
pytest
```
## Screenshots
![Wordcloud](Images/wordcloud.png?raw=true "Word Cloud")



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)