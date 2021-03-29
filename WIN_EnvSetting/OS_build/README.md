Ansible Role: OS-Windows2016/WIN_EnvSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関する環境変数についての情報の設定を行います。

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
OS-Windows2016/WIN_EnvSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_EnvSetting` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Machine` | システム環境変数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- Name` | 環境変数の変数名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | 環境変数の設定値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present ： 作成、更新<br>absent ： 削除 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`User` | 接続ユーザー環境変数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- Name` | 環境変数の変数名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | 環境変数の設定値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present ： 作成、更新<br>absent ： 削除 | 

### Example
~~~
VAR_WIN_EnvSetting:
  Machine:
  - Action: present
    Name: TEST_PROGRAM
    Value: 'c:\TEST_PRPGRAM'
  - Action: absent
    Name: TEST_PROGRAM2
    Value: 'c:\TEST_PRPGRAM2'
  ・・・
  User:
  - Action: present
    Name: Path
    Value: '%USERPROFILE%\AppData\Local\PF\PF_APP;'
  - Action: absent
    Name: Path
    Value: '%USERPROFILE%\AppData\Local\PF\PF_APP2;'
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
    │         └── WIN_EnvSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_Environment_item_absent.yml
    │                   │      build_Environment_item_present.yml
    │                   │      build_Environment_item.yml
    │                   │      build_Environment.yml
    │                   │      build_Machine.yml
    │                   │      build_User.yml
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
    - role: OS-Windows2016/WIN_EnvSetting/OS_build
      VAR_WIN_EnvSetting:
        Machine:
        - Action: present
          Name: TEST_PROGRAM
          Value: 'c:\TEST_PRPGRAM'
        - Action: absent
          Name: TEST_PROGRAM2
          Value: 'c:\TEST_PRPGRAM2'
        ・・・
        User:
        - Action: present
          Name: Path
          Value: '%USERPROFILE%\AppData\Local\PF\PF_APP;'
        - Action: absent
          Name: Path
          Value: '%USERPROFILE%\AppData\Local\PF\PF_APP2;'
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
    - role: OS-Windows2016/WIN_EnvSetting/OS_build
      VAR_WIN_EnvSetting:
        Machine:
        - Action: present
          Name: TEST_PROGRAM
          Value: 'c:\TEST_PRPGRAM'
        - Action: absent
          Name: TEST_PROGRAM2
          Value: 'c:\TEST_PRPGRAM2'
        ・・・
        User:
        - Action: present
          Name: Path
          Value: '%USERPROFILE%\AppData\Local\PF\PF_APP;'
        - Action: absent
          Name: Path
          Value: '%USERPROFILE%\AppData\Local\PF\PF_APP2;'
        ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_EnvSetting/OS_gathering
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
    │              └── WIN_EnvSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_EnvSetting.yml
~~~

# Remarks
-------
環境変数の設定の反映にはOS再起動が必要となります。
値に変更が無い場合でも、ansible-playbookの結果としてchangedとなる場合があります。実際に値が変更されたかどうかはエビデンス収集を行い、その結果を確認してください。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
