# medsearch
Python 3.8, Windows 10で動作確認しています．

## 類義語検索 CLI版
### Setup
[Wikipedia2Vec](https://wikipedia2vec.github.io/wikipedia2vec/) をインストール
```
$ pip install wikipedia2vec
```
[jawiki_20180420_100d.pkl.bz2](http://wikipedia2vec.s3.amazonaws.com/models/ja/2018-04-20/jawiki_20180420_100d.pkl.bz2)
をダウンロードして，解凍し，`models/jawiki_20180420_100d.pkl`に配置します．

以下を実行します．
```
python wiki2vec_search.py 膵癌 10
```
引数は，`entity` `類義語の個数`です．  
entityとは，Wikipediaのページタイトルです．
