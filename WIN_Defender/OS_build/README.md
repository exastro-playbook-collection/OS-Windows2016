Ansible Role: OS-Windows2016/WIN_Defender/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するWindowsDefender設定についての情報の設定を行います。

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
OS-Windows2016/WIN_Defender/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_Defender` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisableRealtimeMonitoring` | 「設定」「WindowsDefender」の「リアルタイム保護」に該当<br>false ： オン<br>true ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MAPSReporting` | 「設定」「WindowsDefender」の「クラウドベースの保護」に該当<br>2 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SubmitSamplesConsent` | 「設定」「WindowsDefender」の「サンプルの自動送信」に該当<br>1 ： オン<br>0 ： オフ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`EnableControlledFolderAccess` | 「設定」「WindowsDefender」の「ランサムウェア防止のフォルダアクセスコントロール」に該当<br>1 ： オン<br>0 ： オフ<br>※ OSのビルドバージョンによって取得/反映が行えない場合がある | 

### Example
~~~
VAR_WIN_Defender:
  DisableRealtimeMonitoring: false
  EnableControlledFolderAccess: 0
  MAPSReporting: 2
  SubmitSamplesConsent: 1
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
    │         └── WIN_Defender/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_Defender.yml
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
    - role: OS-Windows2016/WIN_Defender/OS_build
      VAR_WIN_Defender:
        DisableRealtimeMonitoring: false
        EnableControlledFolderAccess: 0
        MAPSReporting: 2
        SubmitSamplesConsent: 1
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
    - role: OS-Windows2016/WIN_Defender/OS_build
      VAR_WIN_Defender:
        DisableRealtimeMonitoring: false
        EnableControlledFolderAccess: 0
        MAPSReporting: 2
        SubmitSamplesConsent: 1
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_Defender/OS_gathering
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
    │              └── WIN_Defender/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_Defender.yml
~~~

# Remarks
-------
Windows Defenderをインストールしていない場合は、本ロール実行時にエラーとなるため実行しないでください。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
