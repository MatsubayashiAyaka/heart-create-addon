# Heart Create（Blender Add-on）

Blender 上で、**ハート型の 3D メッシュを自動生成**するアドオンです。  
スムースな形状と宝石調の形状を切り替えながら、シンプルな操作でハートメッシュを配置できます。

ハート形状は数式による近似ではなく、**事前に作成した正解メッシュの頂点データを元に生成**しており、  
意図したシルエットを安定して再現できることを重視しています。

---

## 対応環境

- Blender: 3.6 以降（4.x / 5.0 動作確認済み）
- OS: Windows / macOS / Linux

---

## インストール

### 1) Releases から入れる（推奨）

1. GitHub の Releases ページから最新の  
   `Heart_Create_ver1_2_0.zip` をダウンロード
2. Blender → `Edit` → `Preferences` → `Add-ons`
3. 右上の `Install...` をクリック
4. ダウンロードした zip ファイルを選択
5. 一覧に表示される `Heart Create` を有効化

---

### 2) 手動で配置する（開発者向け）

1. `Heart_Create_ver1_2_0.py` をダウンロード
2. addons フォルダへコピー

```text
Windows: %APPDATA%\Blender Foundation\Blender\4.2\scripts\addons\
macOS:   ~/Library/Application Support/Blender/4.2/scripts/addons/
Linux:   ~/.config/blender/4.2/scripts/addons/
```

3. Blender を再起動し、Add-ons から有効化

---

## 使い方（基本フロー）

### パネルの場所

- 3D Viewport → サイドバー（Nキー）→ `Heart Create` タブ

### メッシュを生成する

1. パネル内でハートのタイプを選択
   - スムース
   - 宝石
2. サイズを調整
3. `Create` を押下

### メニューから追加する

- `Shift + A` → `Mesh` → `Heart Create`

---

## パラメータ

| 項目 | 内容 |
|---|---|
| Type | スムース / 宝石 の切替 |
| Size | ハートメッシュの全体スケール |

パラメータは **サイズのみに限定**しており、  
配置時に迷わず使用できることを目的としています。

---

## 生成されるメッシュについて

- 生成されるメッシュは **確定形状**です
- Modifier は使用しません
- Edit モードで自由に編集可能です

---

## 設計方針

- UI は最小限に抑える
- 見た目の再現性を最優先する
- 実務でそのまま使えるプリミティブを目指す

数式ベースのハート形状ではなく、  
**人の手で作られた見本メッシュを基準にしたデータ駆動生成**を採用しています。

---

## 技術的概要

- ハート形状は事前に作成したメッシュから
  - 頂点座標
  - 面構成
  を抽出してコード内に保持
- メッシュ生成時に bmesh を使用して再構築
- UI パネルとオペレーターを分離した構成
- 単一ファイル構成で、導入・管理が容易

---

## バージョン履歴

変更履歴は [CHANGELOG.md](CHANGELOG.md) を参照してください。

---

## ライセンス

MIT License