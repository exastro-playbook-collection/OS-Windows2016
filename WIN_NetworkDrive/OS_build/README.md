Ansible Role: OS-Windows2016/WIN_NetworkDrive/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するネットワークドライブ設定についての情報の設定を行います。

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
OS-Windows2016/WIN_NetworkDrive/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetworkDrive` |     | 
| `- Name` | ネットワークドライブ割り当ての「ドライブ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ProviderName` | ネットワークドライブ割り当ての「フォルダー」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`User` | ネットワークドライブ割り当て時の「資格情報」の「ユーザ名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Password` | ネットワークドライブ割り当て時の「資格情報」の「パスワード」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築のアクション設定値<br>present ： 作成、更新<br>absent ： 削除 | 

### Example
~~~
VAR_WIN_NetworkDrive:
- Action: present
  Name: Z
  Password: Passw0rd123
  ProviderName: \\192.168.0.1\TESTPF
  User: TestUser
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
    │         └── WIN_NetworkDrive/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_NetworkDrive.yml
    │                   │      build_NetworkDrive_item.yml
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
    - role: OS-Windows2016/WIN_NetworkDrive/OS_build
      VAR_WIN_NetworkDrive:
      - Action: present
        Name: Z
        Password: Passw0rd123
        ProviderName: \\192.168.0.1\TESTPF
        User: TestUser
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
    - role: OS-Windows2016/WIN_NetworkDrive/OS_build
      VAR_WIN_NetworkDrive:
      - Action: present
        Name: Z
        Password: Passw0rd123
        ProviderName: \\192.168.0.1\TESTPF
        User: TestUser
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetworkDrive/OS_gathering
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
    │              └── WIN_NetworkDrive/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetworkDrive.yml
~~~

# Remarks
-------
ネットワークドライブの割り当て設定の反映にはOS再起動が必要となります。
ネットワークドライブの割り当てには、接続ユーザの設定のみ追加・削除可能です。
設定したネットワークドライブの割り当ては、設定後にサインインしたセッションからしか利用できません。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
