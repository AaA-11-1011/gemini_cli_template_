# 軽量な Python イメージ
FROM python:3.12-slim

# uv をインストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Node.js をインストール (Gemini CLI の実行に必要)
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /app

# Python パッケージをインストール
RUN uv pip install --system google-genai

# Gemini CLI (Node.js版) をグローバルにインストール (コンテナ内)
RUN npm install -g @google/gemini-cli

# コンテナ起動時にbashを維持
CMD ["bash"]