Ansible Role: OS-Windows2016/WIN_EventLog/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するイベントログについての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_EventLog/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_EventLog.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_EventLog.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_EventLog` |     | 
| `- Log` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「フルネーム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LogPath` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「ログのパス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MaximumKilobytes` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「最大ログサイズ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`OverflowAction` | 最大ファイル サイズに達したイベント ログ内のエントリの処理方法<br>DoNotOverwrite ： イベントログがいっぱいになった場合、既存のエントリを保持し、新規のエントリが破棄される<br> OverwriteAsNeeded ： イベントログがいっぱいになった場合、最も古いエントリが新規のエントリで上書きされる<br> OverwriteOlder : イベントログがいっぱいになった場合、MinimumRetentionDays プロパティ値の指定よりも古いイベントが新規のイベントで上書きされ、イベント ログがいっぱいになり、MinimumRetentionDaysプロパティ値の指定よりも古いイベントが存在しない場合、新規のイベントは破棄される | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MinimumRetentionDays` | イベントログ内のエントリが保持される日数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Retention` | イベントログの消去の指定<br>true ： イベントログを消去する<br>false ： イベントログを消去しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AutoBackup` | イベントログの消去を行うときに自動バックアップの指定<br>true ： 自動バックアップを行う<br>false ： 自動バックアップを行わない | 

### Example
~~~
VAR_WIN_EventLog:
- AutoBackup: true
  Log: Application
  LogPath: '%SystemRoot%\System32\Winevt\Logs\Application.evtx'
  MaximumKilobytes: 20480
  MinimumRetentionDays: -1
  OverflowAction: DoNotOverwrite
  Retention: true
- AutoBackup: false
  Log: HardwareEvents
  LogPath: '%SystemRoot%\System32\Winevt\Logs\HardwareEvents.evtx'
  MaximumKilobytes: 20480
  MinimumRetentionDays: 0
  OverflowAction: OverwriteAsNeeded
  Retention: false
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
    │         └── WIN_EventLog/
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
    - role: OS-Windows2016/WIN_EventLog/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_EventLog/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_EventLog.yml  # パラメータ
~~~

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_EventLog/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_EventLog.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
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
