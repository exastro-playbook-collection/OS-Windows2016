Ansible Role: OS-Windows2016/WIN_ErrorReporting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するエラーレポーティング設定についての情報の設定を行います。

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
OS-Windows2016/WIN_ErrorReporting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_ErrorReporting` |     | 
| `- Key` | エラーレポーティングに関連するレジストリパス | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Values` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- ValueName` | レジストリ名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ValueType` | レジストリ種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | レジストリ値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present ： 作成、更新<br>absent ： 削除 | 

### Example
~~~
VAR_WIN_ErrorReporting:
- Key: HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting
  Values:
  - Action: present
    Value: 1
    ValueName: EnableZip
    ValueType: REG_DWORD
  - Action: present
    Value: \WindowsErrorReportingServicePort
    ValueName: ErrorPort
    ValueType: REG_SZ
  ・・・
- Key: HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\Assert Filtering Policy
  Values:
  - Action: present
    Value: 1
    ValueName: ReportAndContinue
    ValueType: REG_DWORD
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
    │         └── WIN_ErrorReporting/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_ErrorReporting.yml
    │                   │      build_ErrorReporting_item.yml
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
    - role: OS-Windows2016/WIN_ErrorReporting/OS_build
      VAR_WIN_ErrorReporting:
      - Key: HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting
        Values:
        - Action: present
          Value: 1
          ValueName: EnableZip
          ValueType: REG_DWORD
        - Action: present
          Value: \WindowsErrorReportingServicePort
          ValueName: ErrorPort
          ValueType: REG_SZ
        ・・・
      - Key: HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\Assert Filtering Policy
        Values:
        - Action: present
          Value: 1
          ValueName: ReportAndContinue
          ValueType: REG_DWORD
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
    - role: OS-Windows2016/WIN_ErrorReporting/OS_build
      VAR_WIN_ErrorReporting:
      - Key: HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting
        Values:
        - Action: present
          Value: 1
          ValueName: EnableZip
          ValueType: REG_DWORD
        - Action: present
          Value: \WindowsErrorReportingServicePort
          ValueName: ErrorPort
          ValueType: REG_SZ
        ・・・
      - Key: HKLM:\SOFTWARE\Microsoft\Windows\Windows Error Reporting\Assert Filtering Policy
        Values:
        - Action: present
          Value: 1
          ValueName: ReportAndContinue
          ValueType: REG_DWORD
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_ErrorReporting/OS_gathering
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
    │              └── WIN_ErrorReporting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_ErrorReporting.yml
~~~

# Remarks
-------
取得パラメタの値によっては、時間経過で動的に値が変わるものがあり、設定変更されたことを表すメッセージ「changed」が出力されますが、<br>
設定後自動的に戻るため影響はないものになります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
