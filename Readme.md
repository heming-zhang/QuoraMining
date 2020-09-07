# QuoraMining: topics evolution on Quora

We propose a new model – Weight Biterm Topic Model (WBTM) by weighting the question answering text with user behavior data. The results show that our model has higher coherence values. The trend chart of theme evolution is drawn and analyzed by means of thermal map to make personal suggestions on recommendation and advertising of Quora Film and Television and other topics. 

For more details about QuoraMing, see [the full paper](https://github.com/heming-zhang/QuoraMining/blob/master/paper/QuoraMining.pdf).

### Environment

* python 3.7.2; (packages: bs4, urllib.request, pymysql)
* Navicat for MySQL 11.1.13

Please ensure the local database is connected before running the code. And you may also want to add an account to crawl data from Quora.

### Running QuoraMining
Crawl text from Quora
```
python3 main_crawl.py
```

Initiate topic mining with WBTM
```
python3 main_mining.py
```

Plot the figure 
```
python3 main_plot.py
```

  
  
  
  
