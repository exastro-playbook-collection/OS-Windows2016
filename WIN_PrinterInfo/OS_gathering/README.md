Ansible Role: OS-Windows2016/WIN_PrinterInfo/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するプリンタ情報についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_PrinterInfo/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_PrinterInfo.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PrinterInfo.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_PrinterInfo` |     | 
| `- Name` | 各プリンタの「プロパティ」「全般」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Comment` | 各プリンタの「プロパティ」「全般」の「コメント」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Location` | 各プリンタの「プロパティ」「全般」の「場所」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Shared` | 各プリンタの「プロパティ」「共有」の「このプリンターを共有する」のチェックボックスに該当<br>true：共有する<br>false：共有しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ShareName` | 各プリンタの「プロパティ」「共有」の「共有名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_UtilizationTime` | 各プリンタの「プロパティ」「詳細設定」の「常に利用可能」or「開始」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_Priority` | 各プリンタの「プロパティ」「詳細設定」の「優先順位」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_DriverName` | 各プリンタの「プロパティ」「詳細設定」の「ドライバ名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_SpoolEnabled` | 各プリンタの「プロパティ」「詳細設定」の「スプール設定」に該当<br>true：「印刷ドキュメントをスプールし、プログラムの印刷処理を高速に行う」のラジオボタンがON<br>false：「プリンタに直接データを送る」のラジオボタンがOFF | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_Queued` | 各プリンタの「プロパティ」「詳細設定」の「スプール設定_キュー」に該当<br>true：「全ページ分のデータをスプールしてから、印刷データをプリンターに送る」のラジオボタンがON<br>false：「すぐに印刷データをプリンターに送る」のラジオボタンがOFF | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_EnableDevQueryPrint` | 各プリンタの「プロパティ」「詳細設定」の「一致しないドキュメントを保留する」のチェックボックスに該当<br>true：保留する<br>false：保留しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_DoCompleteFirst` | 各プリンタの「プロパティ」「詳細設定」の「スプールされたドキュメントを最初に印刷する」のチェックボックスに該当<br>true：する<br>false：しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_KeepPrintedJobs` | 各プリンタの「プロパティ」「詳細設定」の「印刷ドキュメントを残す」のチェックボックスに該当<br>true：残す<br>false：残さない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Detail_RawOnly` | 各プリンタの「プロパティ」「詳細設定」の「詳細な印刷機能を有効にする」のチェックボックスに該当<br>true：有効にする<br>false：有効にしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PortName` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の「ポート名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`HostAddress` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の「プリンタ名またはIPアドレス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Protocol` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の「プロトコル」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RawPortNumber` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の Raw設定の「ポート番号」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LPRQueue` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の LPR設定の「キュー名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ByteCount` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の LPR設定の「LPRバイトカウントを有効にする」のチェックボックスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SNMPEnabled` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の SNMP設定の「SNMPステータスを有効にする」のチェックボックスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SNMPCommunity` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の SNMP設定の「コミュニティ名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SNMPDevIndex` | 各プリンタの「プロパティ」「ポート」「ポートの構成」ボタンを押下 「ポートの設定」の SNMP設定の「SNMPデバイスインデックス」に該当 | 

### Example
~~~
VAR_WIN_PrinterInfo:
- Comment: null
  Detail_DoCompleteFirst: true
  Detail_DriverName: Microsoft XPS Document Writer v4
  Detail_EnableDevQueryPrint: false
  Detail_KeepPrintedJobs: false
  Detail_Priority: 1
  Detail_Queued: false
  Detail_RawOnly: false
  Detail_SpoolEnabled: true
  Detail_UtilizationTime: always available
  Location: null
  Name: Microsoft XPS Document Writer
  PortName: 'PORTPROMPT:'
  ShareName: null
  Shared: false
- Comment: null
  Detail_DoCompleteFirst: true
  Detail_DriverName: Microsoft Print To PDF
  Detail_EnableDevQueryPrint: false
  Detail_KeepPrintedJobs: false
  Detail_Priority: 1
  Detail_Queued: false
  Detail_RawOnly: false
  Detail_SpoolEnabled: true
  Detail_UtilizationTime: always available
  Location: null
  Name: Microsoft Print to PDF
  PortName: 'PORTPROMPT:'
  ShareName: null
  Shared: false
・・・
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
    │         └── WIN_PrinterInfo/
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
    - role: OS-Windows2016/WIN_PrinterInfo/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_PrinterInfo/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_PrinterInfo.yml  # パラメータ
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
