Ansible Role: OS-Windows2016/WIN_GroupPolicy/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するローカルグループポリシーについての情報の設定を行います。

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
OS-Windows2016/WIN_GroupPolicy/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_GroupPolicy` |     | 
| `- Key` | グループポリシーに関連するレジストリパス | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Values` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- ValueName` | レジストリ名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ValueType` | レジストリ種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | レジストリ値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present ： 作成、更新<br>absent ： 削除 | 

### Example
~~~
VAR_WIN_GroupPolicy:
- Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System
  Values:
  - Action: present
    Value: 5
    ValueName: ConsentPromptBehaviorAdmin
    ValueType: REG_DWORD
  - Action: present
    Value: 3
    ValueName: ConsentPromptBehaviorUser
    ValueType: REG_DWORD
  ・・・
- Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
  Values:
  - Action: present
    Value: 0
    ValueName: ForceActiveDesktopOn
    ValueType: REG_DWORD
  - Action: present
    Value: 1
    ValueName: NoActiveDesktop
    ValueType: REG_DWORD
  ・・・
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
    │         └── WIN_GroupPolicy/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_GroupPolicy.yml
    │                   │      build_GroupPolicy_item.yml
    │                   │      build_Registry.yml
    │                   │      build_Registry_absent.yml
    │                   │      build_Registry_present.yml
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
    - role: OS-Windows2016/WIN_GroupPolicy/OS_build
      VAR_WIN_GroupPolicy:
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System
        Values:
        - Action: present
          Value: 5
          ValueName: ConsentPromptBehaviorAdmin
          ValueType: REG_DWORD
        - Action: present
          Value: 3
          ValueName: ConsentPromptBehaviorUser
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
        Values:
        - Action: present
          Value: 0
          ValueName: ForceActiveDesktopOn
          ValueType: REG_DWORD
        - Action: present
          Value: 1
          ValueName: NoActiveDesktop
          ValueType: REG_DWORD
        ・・・
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
    - role: OS-Windows2016/WIN_GroupPolicy/OS_build
      VAR_WIN_GroupPolicy:
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System
        Values:
        - Action: present
          Value: 5
          ValueName: ConsentPromptBehaviorAdmin
          ValueType: REG_DWORD
        - Action: present
          Value: 3
          ValueName: ConsentPromptBehaviorUser
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
        Values:
        - Action: present
          Value: 0
          ValueName: ForceActiveDesktopOn
          ValueType: REG_DWORD
        - Action: present
          Value: 1
          ValueName: NoActiveDesktop
          ValueType: REG_DWORD
        ・・・
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_GroupPolicy/OS_gathering
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
    │              └── WIN_GroupPolicy/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_GroupPolicy.yml
~~~

# Remarks
-------
情報取得でレジストリ値では空白だが取得結果が"\0"と設定されるレジストリ値があります。<br>
例) HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\Systemのlegalnoticetext<br>
その情報取得結果のパラメターファイルで、情報設定を行った場合は情報は変更されません。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
