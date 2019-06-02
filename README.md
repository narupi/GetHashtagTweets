## 概要
特定ユーザのツイートから特定のハッシュタグの付いたツイートを取得するツール  
ツイート本文とツイート時刻をactivity.txtに保存します  
```bash

test1
2019 May/31(Fri) 14:40:53

test
2019 May/31(Fri) 14:40:38


てすとー
2019 Jun/02(Sun) 11:13:32

test
2019 Jun/02(Sun) 11:47:39

```


  
## 使い方
※このツールはTwitterApiキーが必要です  

1. 以下のライブラリをインストールします  

```bash

$ pip install requests requests-oauthlib

```

2. config.pyを作成し各種設定を書きます  

```python

#config.py

#TweitterApi
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

#Twitter id
SCREEN_NAME = ""

#Hashtag(#はつけない)
#KEYWORD_HASHTAG = "test"
KEYWORD_HASHTAG = ""

```

3. main.pyを実行します

```

$python3 main.py

````