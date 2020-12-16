Ansible Role: OS-Windows2016/WIN_Services/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するWindowsサービスについての情報の取得を行います。

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
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス。 | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス。 | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド。 | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_Services/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_Services.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_Services.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_Services` |     | 
| `- Name` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「サービス名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayName` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「表示名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Status` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「サービスの状態」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`StartType` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「全般」の「スタートアップの種類」に該当<br>Auto ： 自動／自動（遅延開始)<br>Manual ： 手動<br>Disabled ： 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FailureAction1` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「最初のエラー」に該当<br>RUN ： プログラムを実行する<br>RESTART ： サービスを再起動する<br>REBOOT ： コンピュータを再起動する<br>設定なし ： 何もしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Delay1(msec)` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「最初のエラー」が「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「次の時間を経過後、コンピュータを再起動する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FailureAction2` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「次のエラー」に該当<br>RUN ： プログラムを実行する<br>RESTART ： サービスを再起動する<br>REBOOT ： コンピュータを再起動する<br>設定なし ： 何もしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Delay2(msec)` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「次のエラー」が「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「次の時間を経過後、コンピュータを再起動する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FailureAction3` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「その後のエラー」に該当<br>RUN ： プログラムを実行する<br>RESTART ： サービスを再起動する<br>REBOOT ： コンピュータを再起動する<br>設定なし ： 何もしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Delay3(msec)` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「その後のエラー」が「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「次の時間を経過後、コンピュータを再起動する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RebootMessage` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「コンピュータを再起動する」で「コンピュータの再起動オプション」を押下、「コンピュータの再起動オプション」の「再起動する前に、このメッセージをネットワーク上のコンピュータに送信する」のチェックボックスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ResetPeriod(sec)` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「エラーカウントのリセット」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`CmdLine` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「サービス」の選択したサービスのプロパティ「回復」の「プログラムの実行」の「プログラム」 「コマンドラインのパラメタ―」 「コマンドラインにエラーカウントのオプションを追加」のチェックボックスに該当する<br>プログラム ： プログラム実行パス<br>コマンドラインのパラメタ― ： パラメタ―値<br>コマンドラインにエラーカウントのオプションを追加 ： 追加の場合は/fail=%1%'を記載、追加しない場合は記載しない | 

### Example
~~~
VAR_WIN_Services:
- CmdLine: ''
  Delay1(msec): '3000'
  Delay2(msec): '3000'
  DisplayName: AllJoyn Router Service
  FailureAction1: RESTART
  FailureAction2: RESTART
  Name: AJRouter
  RebootMessage: ''
  ResetPeriod(sec): '86400'
  StartType: Manual
  Status: Stopped
- CmdLine: ''
  Delay1(msec): '120000'
  Delay2(msec): '300000'
  DisplayName: Application Layer Gateway Service
  FailureAction1: RESTART
  FailureAction2: RESTART
  Name: ALG
  RebootMessage: ''
  ResetPeriod(sec): '900'
  StartType: Manual
  Status: Stopped
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
    │         └── WIN_Services/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── meta/
    │                   │      main.yml
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
    - role: OS-Windows2016/WIN_Services/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_Services/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_Services.yml  # パラメータ
~~~


# Remarks
-------
取得パラメタの値によっては、時間経過で動的に値が変わるものがあります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
