# QuoraMining: topics evolution on Quora

We propose a new model – Weight Biterm Topic Model (WBTM) by weighting the question answering text with user behavior data. The results show that our model has higher coherence values. The trend chart of theme evolution is drawn and analyzed by means of thermal map to make personal suggestions on recommendation and advertising of Quora Film and Television and other topics. 

For more details about QuoraMining, see [the full paper](https://github.com/heming-zhang/QuoraMining/blob/master/paper/QuoraMining.pdf).

### Dependencies

* python 3.7.2; 
* bs4, urllib.request, pymysql
* Navicat for MySQL 11.1.13

Please ensure the local database is connected before running the code. And you may also want to add an account to crawl data from Quora.

## 1. Crawling Q&A Data from Quora
Crawl text from Quora
```
python3 main_crawl.py
```

## 2. Topics Mining with WBTM
Initiate topic mining with WBTM
```
python3 main_mining.py
```

Plot the figure 
```
python3 main_plot.py
```

  
  
  
  
