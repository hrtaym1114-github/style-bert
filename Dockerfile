# ベースイメージ
FROM python:3.11-slim AS base

# 作業ディレクトリを設定
WORKDIR /app

# 必要最小限のツールだけインストール
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# リポジトリをクローン
RUN git clone https://github.com/litagin02/Style-Bert-VITS2.git /app/Style-Bert-VITS2

# 依存関係のインストールと初期化
WORKDIR /app/Style-Bert-VITS2

# 仮想環境を使わず直接インストール
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir -r requirements.txt

# 必要に応じてコンパイラをインストール（initialize.pyの実行に必要な場合）
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python initialize.py
