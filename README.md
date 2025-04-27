# MacでStyle-Bert-VITS2をセットアップする方法

Style-Bert-VITS2は感情豊かな音声合成ができるツールですが、公式ではWindows向けの説明が中心となっています。しかし、Macでも利用可能な方法がいくつかあります。このガイドでは、MacでStyle-Bert-VITS2をセットアップする主な方法を解説します。

## 目次

1. [Dockerを使用したセットアップ方法](#dockerを使用したセットアップ方法)
2. [直接インストールする方法](#直接インストールする方法)
3. [pyenvを使用したPythonバージョン管理](#pyenvを使用したpythonバージョン管理)
4. [Macでの学習について](#macでの学習について)
5. [モデルの配置](#モデルの配置)
6. [結論](#結論)

## Dockerを使用したセットアップ方法

Dockerを使うと、環境差異を気にせず簡単にStyle-Bert-VITS2を実行できます。この方法が最も安定しています。

### 必要なファイル作成

このリポジトリには、すでに必要な`Dockerfile`と`docker-compose.yml`が含まれています。

### Docker起動

以下のコマンドでDockerコンテナを起動します：

```bash
$ docker-compose up
```

起動したら、ブラウザで`localhost:8000`にアクセスすればStyle-Bert-VITS2の画面が表示されます。

## 直接インストールする方法

Dockerを使わず、直接Macにインストールすることも可能です。

### 環境要件

* Python 3.10または3.11（3.9以上推奨）
* POSIX準拠のシェル用ターミナル（bash等）

### インストール手順

```bash
# リポジトリをクローン
git clone https://github.com/litagin02/Style-Bert-VITS2.git
cd Style-Bert-VITS2/

# Pythonの仮想環境を作成（venvを使用する場合）
python -m venv .venv
source .venv/bin/activate

# または、uvを使用する場合
# uv venv --python=3.11
# source .venv/bin/activate

# 依存関係のインストール
pip install -r requirements.txt

# 初期設定とデフォルトモデルのダウンロード
python initialize.py
```

インストール後、以下のコマンドでWebUIを起動できます：

```bash
python app.py
```

もしくはエディター機能を使いたい場合：

```bash
python server_editor.py --inbrowser --device cpu
```

## pyenvを使用したPythonバージョン管理

システムのPythonバージョンが適切でない場合、pyenvを使ってバージョンを管理できます：

```bash
# pyenvで適切なPythonバージョンをインストール
pyenv install 3.10.14 #もしくは3.11.9など
pyenv local 3.10.14 #特定のディレクトリのみに適用
```

`pyenv local`は現在のディレクトリでのみ、このバージョンを適用します。システム全体に適用したい場合は`pyenv global`を使います。

## Macでの学習について

現時点（2025年4月）では、MacでのStyle-Bert-VITS2の学習はCPU専用となっています。GPUを活用した高速な学習はWindows+NVIDIA GPUの環境が必要です。

Intel Macの場合、追加の修正が必要になることがあります：

```python
# train_ms_jp_extra_cpu.pyを修正
# from torch.amp import GradScaler, autocast
from torch.cuda.amp import GradScaler, autocast

# with autocast('cpu', enabled=hps.train.bf16_run, dtype=torch.bfloat16): を全て
with autocast('cpu', dtype=torch.bfloat16):
# に変更
```

## モデルの配置

セットアップが完了したら、使用したいモデルを適切なディレクトリに配置します：

```
Style-Bert-VITS2/
└ model_assets/
  └ {model_name}
    ├ xxxx.safetensors
    ├ config.json
    └ style_vectors.npy
```

モデルはBOOTHやHugging Faceなどから入手できます。

## 結論

MacでStyle-Bert-VITS2を使用する場合、Dockerを利用する方法が最も簡単で安定しています。直接インストールする場合は、適切なPythonバージョンと依存関係の管理に注意が必要です。学習機能を使う場合は現状CPUのみの対応となっており、処理速度に制限があることを念頭に置いてください。

Style-Bert-VITS2は継続的に更新されているため、最新の情報は[公式GitHubリポジトリ](https://github.com/litagin02/Style-Bert-VITS2)を確認することをお勧めします。

## 参考リンク

- [Style-Bert-VITS2公式リポジトリ](https://github.com/litagin02/Style-Bert-VITS2)
- [Style-Bert-VITS2 FAQ](https://github.com/litagin02/Style-Bert-VITS2/blob/master/docs/FAQ.md)
- [Style-Bert-VITS2リリースページ](https://github.com/litagin02/Style-Bert-VITS2/releases)
