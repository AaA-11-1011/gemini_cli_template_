# Gemini CLI Docker Template

このリポジトリは、Docker を使用して Gemini CLI 環境を構築するためのテンプレートです。

## セットアップ手順

1. **環境変数の準備**
   `.env.example` をコピーして `.env` を作成し、Google AI Studio で取得した API キーを記入してください。
   ```bash
   cp .env.example .env
   ```

2. **Docker イメージのビルド**
   ```bash
   docker-compose build
   ```

3. **コンテナの起動と実行**
   ```bash
   docker-compose run gemini-cli
   ```

4. **Gemini CLI の使用**
   コンテナ内で以下のコマンドを実行します。
   ```bash
   gemini
   ```

## ファイル構成
- `Dockerfile`: Node.js と Python 環境の定義
- `docker-compose.yml`: コンテナとホストの同期設定
- `.env.example`: API キー設定のテンプレート
- `main.py` / `chat.py`: Python からの利用サンプル
