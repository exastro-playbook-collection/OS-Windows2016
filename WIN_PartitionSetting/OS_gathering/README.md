Ansible Role: OS-Windows2016/WIN_PartitionSetting/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するPartitionSettingについての情報の取得を行います。

# Supports
- 管理マシン(Ansibleサーバ)
  * Linux系OS（RHEL7）
  * Ansible バージョン 2.7 以上 (動作確認バージョン 2.7, 2.9)
  * Python バージョン 3.x  (動作確認バージョン 3.6)
- 管理対象マシン
  * Windows Server 2016

# Requirements
- 管理マシン(Ansibleサーバ)
  * Ansibleサーバは管理対象マシンへPowershell接続できる必要があります。
- 管理対象マシン
  * Windows Server 2016
  * Powershell3.0+

# Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- gathering ロール
- パラメータ生成共通部品(parameter_generate)

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_PartitionSetting/`

本ロールを既定値で利用した場合、以下のように設定情報を格納します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _gathered_data/
         └── 管理対象マシンホスト名 or IPアドレス/
              └── OS/  # OS設定ロール向け専用のフォルダ
                   └── パラメータ生成対象/  # 収集データ
                        └── command/
                               ・・・
~~~

## 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_PartitionSetting.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PartitionSetting.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_PartitionSetting` |     | 
| `- OperationalStatus:` |「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「記憶域」「ディスクの管理」の「各ディスクを選択してのプロパティ」「ボリューム」の「状態」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Type` | パーティション種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DiskNumber` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「記憶域」「ディスクの管理」の「各ディスクを選択してのプロパティ」「ボリューム」の「ディスク」に該当  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DriveLetter` | システム内のドライブまたはボリュームを識別するために使用される文字 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`GptType` | GPTパーティションのタイプ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Guid` | GPTパーティションのGUID | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IsActive` | パーティションのアクティブ状態<br>true ： パーティションがアクティブ<br>false ： パーティションがアクティブでない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IsBoot` | ブートパーティション<br>true ： ブートパーティション<br>false ： ブートパーティションでない |
| &nbsp;&nbsp;&nbsp;&nbsp;`IsHidden` | パーティションの非表示<br>true ： パーティションはマウントマネージャーによって検出されていない<br>false ： パーティションはマウントマネージャーによって検出されている |
| &nbsp;&nbsp;&nbsp;&nbsp;`IsOffline` | パーティションのオフライン<br>true ： パーティションはオフライン<br>false ： パーティションはオフラインでない |
| &nbsp;&nbsp;&nbsp;&nbsp;`IsShadowCopy` | パーティションのシャドウコピー<br>true ： パーティションは別パーティションのシャドウコピー<br>false ： パーティションは別パーティションのシャドウコピーでない |
| &nbsp;&nbsp;&nbsp;&nbsp;`IsSystem` | システムパーティション<br>true ： パーティションはシステムパーティション<br>false ： パーティションはシステムパーティションでない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MbrType` | MBRパーティションのタイプ<br>1 ： FAT12<br>4 ： FAT16<br>5 ： Extended<br>6 ： Huge<br>7 ： IFS<br>12 ： FAT32 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NoDefaultDriveLetter` | ドライブ文字の自動割り当ての無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Offset` | オフセット | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PartitionNumber` | パーティションの番号 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Size` | パーティションの合計サイズ (byte) |
| &nbsp;&nbsp;&nbsp;&nbsp;`TransitionState` | パーティションの遷移状態<br>0 ： パーティションはシステムで使用するために予約されています<br>1 ： パーティションは安定しています。現在進行中の構成アクティビティはありません<br>2 ： パーティションが拡張されています<br>3 ： パーティションが縮小されています<br>4 ： パーティションは自動的に再構成されています<br>8 ： パーティションは再ストライピングされています | 

### Example
~~~
VAR_WIN_PartitionSetting:
- DiskNumber: 0
  DriveLetter: C
  GptType: null
  Guid: null
  IsActive: true
  IsBoot: true
  IsHidden: false
  IsOffline: false
  IsShadowCopy: false
  IsSystem: true
  MbrType: 7
  NoDefaultDriveLetter: false
  Offset: 1048576
  OperationalStatus: Online
  PartitionNumber: 1
  Size: 32210157568
  TransitionState: 1
  Type: IFS
~~~

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2016
    │         └── WIN_PartitionSetting/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition.yml
    │                   └─ README.md
    └─ master_playbook.yml
~~~

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_PartitionSetting/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_PartitionSetting/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PartitionSetting.yml  # パラメータ
~~~

# Remarks
-------

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
