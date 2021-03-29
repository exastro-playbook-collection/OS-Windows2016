Ansible Role: OS-Windows2016/WIN_RemoteDesktop/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するリモートデスクトップ設定についての情報の設定を行います。

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
OS-Windows2016/WIN_RemoteDesktop/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_RemoteDesktop` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`fDenyTSConnections` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「リモート」の「リモートデスクトップ」のオプション選択に該当<br>0 ： 「このコンピューターへのリモート接続を許可する」<br>1 ： 「このコンピューターへのリモート接続を許可しない」 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`UserAuthenticationRequired` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「リモート」の「リモートデスクトップ」の「ネットワークレベル認証でリモートデスクトップを実行しているコンピュータからのみ接続を許可する（推奨）」のチェックボックスに該当<br>0 ： ネットワークレベル認証を実行していないコンピュータからでも接続を許可する<br>1 ： ネットワークレベル認証でリモートデスクトップを実行しているコンピュータからのみ接続を許可する<br>※ fDenyTSConnectionsで0を設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PortNumber` | リスニングポート<br>リスニングポートはHKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp のPortNumberに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisableRestrictedAdmin` | リモートデスクトップ接続の制限管理機能無効化<br>0 ： リモートデスクトップ接続の制限管理機能を有効にする<br>1 ： リモートデスクトップ接続の制限管理機能を無効にする | 

### Example
~~~
VAR_WIN_RemoteDesktop:
  DisableRestrictedAdmin: 1
  PortNumber: 3389
  UserAuthenticationRequired: 1
  fDenyTSConnections: 0
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
    │         └── WIN_RemoteDesktop/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_Registry_present.yml
    │                   │      build_RemoteDesktop.yml
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
    - role: OS-Windows2016/WIN_RemoteDesktop/OS_build
      VAR_WIN_RemoteDesktop:
        DisableRestrictedAdmin: 1
        PortNumber: 3389
        UserAuthenticationRequired: 1
        fDenyTSConnections: 0
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
    - role: OS-Windows2016/WIN_RemoteDesktop/OS_build
      VAR_WIN_RemoteDesktop:
        DisableRestrictedAdmin: 1
        PortNumber: 3389
        UserAuthenticationRequired: 1
        fDenyTSConnections: 0
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_RemoteDesktop/OS_gathering
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
    │              └── WIN_RemoteDesktop/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_RemoteDesktop.yml
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
