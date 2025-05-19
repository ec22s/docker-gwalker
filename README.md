# Docker-gwalker
Containers for Kanaries' [Graphic Walker](https://github.com/Kanaries/graphic-walker) and [PyGWalker](https://github.com/Kanaries/pygwalker).

[2025/5/16 PyData.Fukuoka Meetup #24](https://pydatafukuoka.connpass.com/event/349791/) のLT用に作った、Graphic Walker と PyGWalker のコンテナです。Graphic Walker は an open source alternative to Tableau を自称するReactコンポーネントで、PyGWalker はその Python binding です。

- LTタイトル「Tableau から PyGWalker への移行を検討してみた」

- [スライドPDF](https://ec22s.github.io/docker-gwalker/20250516_PyGWalker_small.pdf)（6.1MB, 発表後に PyGWalker の画面など追加しました）

- LTで再生した短い動画（Tableauで積み上げ棒グラフを作る際に戸惑う様子。スライドPDFに埋め込めないため別掲）

  https://github.com/user-attachments/assets/baaec721-7046-43da-b1cf-a5aa9483a972

<br>

### コンテナの詳細

1. 動作確認環境 2025.5.16

   - macOS 15.4.1 (Intel, M2)

   - docker 28.1.1

   - docker-compose 2.35.1

<br>

2. Graphic Walker

   - ディレクトリ `gwalker`

   - 元イメージ `node:18-alpine`

   - 使い方
     ```sh
     # build
     docker-compose build

     # start
     docker-compose up -d
     ```

   - ビルド時に https://github.com/Kanaries/graphic-walker のソースを取得し、起動時に `num run dev` して `0.0.0.0:2002` で待ち受けます。ホストマシン以外からもアクセスできるのでご注意下さい

     <img width=512 src=https://github.com/user-attachments/assets/ddfb8d19-d54d-4eac-b4c5-a85d6f5769a7>

   - 上の画面は動作確認時（2025.5.16）のものです。その後、元ソースの変更により差異が出る可能性があります

   - 既知の不具合（2025.5.16）🙇

     - 上部メニューで Create Dataset > Public Datasets からデータを選択しても動きません。外部リソース情報の `JSON` が元ソースにないようです

     - 公式のサンプルサイト https://graphic-walker.kanaries.net では正常に機能しています

<br>

3. PyGWalker
   - ディレクトリ `pygwalker`
   - 元イメージ `python:3.12-slim` または `python:3.12`

     - Apple M2では、ビルド中（Pythonパッケージのインストール）に `gcc not found` エラーが出て、slimでないイメージを使うと解消しました。そう対処する場合、すみませんが `Dockerfile` を修正して下さい 🙇

   - 使い方
     ```sh
     # build
     docker-compose build

     # start
     docker-compose up -d
     ```

   - 起動すると下記画面のように4つのサーバが起動します

     - 詳細は[スライドPDF](https://ec22s.github.io/docker-gwalker/20250516_PyGWalker_small.pdf)のp.6以降にあります

     - Graphic Walker同様、各サーバはホストマシン以外からもアクセスできるのでご注意下さい

     <img width=512 src=https://github.com/user-attachments/assets/4e60e06d-fbc5-45fc-95ee-65b10037948d>

   - 各サーバのソースとデータについて

     - ソース（`.py` または `.ipynb`）は[公式のexamples](https://github.com/Kanaries/pygwalker/tree/main/examples)を参考にしました

     - データは上記 example が用いている下記2つです

       - https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv

       - https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset/data
      
   - ディレクトリ `wip-or-todo` について

     - 前項と同じ examples にあったけど現状、動かない or 詳細が未把握なソース群です

<br>

### 連絡・問い合わせ先

- 不具合等はIssuesへ、それ以外は[プロフィール](https://github.com/ec22s)のメールアドレスへお願いします
