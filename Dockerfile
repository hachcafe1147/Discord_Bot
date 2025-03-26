FROM python:3.11
WORKDIR /bot

# 更新・日本語化
RUN apt-get update && apt-get -y install locales && apt-get -y upgrade && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ Asia/Tokyo
ENV TERM xterm

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y python3-dev build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# pip のアップグレード
RUN pip install --upgrade pip

# pip install (キャッシュ無効化)
COPY requirements.txt /bot/
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルのコピー
COPY . /bot

# 実行
CMD ["python", "/bot/app/nakayama.py"]
