## 概要
特定ユーザのツイートから特定のハッシュタグの付いたツイートを取得するツール  


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

KEYWORD_HASHTAG = "test"

```

3. main.pyを実行します

```

$python3 main.py

````