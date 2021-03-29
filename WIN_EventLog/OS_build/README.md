Ansible Role: OS-Windows2016/WIN_EventLog/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するイベントログについての情報の設定を行います。

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

本ロールでは、他のロールは必要ありません。
ただし、本READMEに書かれている「エビデンスを取得する場合」の手順を行う場合は、
OS-Windows2016/WIN_EventLog/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_EventLog` |     | 
| `- Log` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「フルネーム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LogPath` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「ログのパス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MaximumKilobytes` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「最大ログサイズ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`OverflowAction` | 最大ファイル サイズに達したイベント ログ内のエントリの処理方法<br>対象のログがmcファイルで定義されているログの場合に設定される<br>DoNotOverwrite ： イベントログがいっぱいになった場合、既存のエントリを保持し、新規のエントリが破棄される。この設定を行う場合は、Retentionをtrueに設定してください。<br> OverwriteAsNeeded ： イベントログがいっぱいになった場合、最も古いエントリが新規のエントリで上書きされる。この設定を行う場合は、RetentionおよびAutoBackupをfalseに設定してください。<br> OverwriteOlder : イベントログがいっぱいになった場合、MinimumRetentionDays プロパティ値の指定よりも古いイベントが新規のイベントで上書きされ、イベント ログがいっぱいになり、MinimumRetentionDaysプロパティ値の指定よりも古いイベントが存在しない場合、新規のイベントは破棄される。この設定を行う場合は、RetentionおよびAutoBackupをfalseに設定してください。 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MinimumRetentionDays` | イベントログ内のエントリが保持される日数<br>対象のログがmcファイルで定義されているログの場合に設定される | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Retention`<br>&nbsp;&nbsp;&nbsp;&nbsp;`AutoBackup` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「イベントビューアー」「イベントビューアー(ローカル)」の選択したログの「プロパティ」「全般」の「イベントログサイズが最大値に達したとき」に該当<br>Retention=false, AutoBackup=false : 必要に応じてイベントを上書きする<br>Retention=true, AutoBackup=true : イベントを上書きしないでログをアーカイブする<br>Retention=true, AutoBackup=false : イベントを上書きしない | 

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


## Optional Variables

特にありません。

# Usage

1. 本ロールを用いたPlaybookを作成します。
2. 変数を必要に応じて設定します。
3. Playbookを実行します。

# Example Playbook

## ■エビデンスを取得しない場合の呼び出す方法

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2016
    │         └── WIN_EventLog/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_EventLog_item.yml
    │                   │      build_EventLog_win_eventlog_item.yml
    │                   │      build_EventLog_win_eventlog.yml
    │                   │      build_EventLog_win_shell_item.yml
    │                   │      build_EventLog_win_shell.yml
    │                   │      build_EventLog.yml
    │                   │      check_parameter.yml
    │                   │      check.yml
    │                   │      main.yml
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
    - role: OS-Windows2016/WIN_EventLog/OS_build
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
  strategy: free
~~~

- Running Playbook

~~~
> ansible-playbook master_playbook.yml
~~~

## ■エビデンスを取得する場合の呼び出す方法

エビデンスを収集する場合、以下のようなエビデンス収集用のPlaybookを作成してください。  

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_EventLog/OS_build
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
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_EventLog/OS_gathering
  strategy: free
~~~

- エビデンス収集結果一覧

エビデンス収集結果は、以下のように格納されます。
エビデンス収集結果の詳細は、OS_gatheringロールを確認してください。

~~~
#エビデンス構成
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_EventLog/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_EventLog.yml
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
