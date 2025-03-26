FROM python:3.11
WORKDIR /bot

# 更新・日本語化
RUN apt-get update && apt-get -y install locales && apt-get -y upgrade && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ Asia/Tokyo
ENV TERM xterm

# 必要なパッケージのインストール（mecab 追加）
RUN apt-get update && apt-get install -y \
    python3-dev build-essential \
    mecab libmecab-dev mecab-ipadic-utf8 \
    && apt-get clean

# pip のアップグレード
RUN pip install --upgrade pip

# pip install（キャッシュ無効化 & system package の制約回避）
COPY requirements.txt /bot/
RUN pip install --no-cache-dir -r requirements.txt  # `--break-system-packages` を削除

# アプリケーションファイルのコピー
COPY . /bot

# ポート開放
EXPOSE 8080

# 実行
CMD ["python", "app/nakayama.py"]
