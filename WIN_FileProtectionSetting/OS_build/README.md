Ansible Role: OS-Windows2016/WIN_FileProtectionSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するファイル保護設定についての情報の設定を行います。

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
OS-Windows2016/WIN_FileProtectionSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_FileProtectionSetting` |     | 
| `- Name:` | ファイル名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AccessToString` | エクスプローラーでファイル選択「プロパティ」「セキュリティ」「詳細設定」「アクセス許可エントリ」の「種類」+「プリンシバル」+「アクセス」に該当<br>※ 表示順は「プリンシパル 種類 アクセス許可1, アクセス許可2・・・」<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Owner` | エクスプローラーでファイル選択「プロパティ」「セキュリティ」「詳細設定」の「所有者」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Encrypt` | 暗号化<br>E ： 暗号化されている<br>U ： 暗号化されていない<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>file ： ファイルの更新<br>absent ：ファイルの削除 | 

### Example
~~~
VAR_WIN_FileProtectionSetting:
- AccessToString:
  - NT AUTHORITY\SYSTEM Allow  FullControl
  - BUILTIN\Administrators Allow  FullControl
  - BUILTIN\Users Allow  ReadAndExecute, Synchronize
  - APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
  - APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
  Action: file
  Encrypt: U
  Name: C:\Windows\Temp\Amazon_SSM_Agent_20200610005533.log
  Owner: BUILTIN\Administrators
- AccessToString:
  - NT AUTHORITY\SYSTEM Allow  FullControl
  - BUILTIN\Administrators Allow  FullControl
  - BUILTIN\Users Allow  ReadAndExecute, Synchronize
  - APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
  - APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
  Action: file
  Encrypt: U
  Name: C:\Windows\Temp\Amazon_SSM_Agent_20200610005533_000_AmazonSSMAgentMSI.log
  Owner: BUILTIN\Administrators
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
    │         └── WIN_FileProtectionSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_FileProtectionSetting_item.yml
    │                   │      build_FileProtectionSetting.yml
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
    - role: OS-Windows2016/WIN_FileProtectionSetting/OS_build
      VAR_WIN_FileProtectionSetting:
      - AccessToString:
        - NT AUTHORITY\SYSTEM Allow  FullControl
        - BUILTIN\Administrators Allow  FullControl
        - BUILTIN\Users Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        Action: file
        Encrypt: U
        Name: C:\Windows\Temp\Amazon_SSM_Agent_20200610005533.log
        Owner: BUILTIN\Administrators
      - AccessToString:
        - NT AUTHORITY\SYSTEM Allow  FullControl
        - BUILTIN\Administrators Allow  FullControl
        - BUILTIN\Users Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        Action: file
        Encrypt: U
        Name: C:\Windows\Temp\Amazon_SSM_Agent_20200610005533_000_AmazonSSMAgentMSI.log
        Owner: BUILTIN\Administrators
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
    - role: OS-Windows2016/WIN_FileProtectionSetting/OS_build
      VAR_WIN_FileProtectionSetting:
      - AccessToString:
        - NT AUTHORITY\SYSTEM Allow  FullControl
        - BUILTIN\Administrators Allow  FullControl
        - BUILTIN\Users Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        Action: file
        Encrypt: U
        Name: C:\Windows\Temp\Amazon_SSM_Agent_20200610005533.log
        Owner: BUILTIN\Administrators
      - AccessToString:
        - NT AUTHORITY\SYSTEM Allow  FullControl
        - BUILTIN\Administrators Allow  FullControl
        - BUILTIN\Users Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        - APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
        Action: file
        Encrypt: U
        Name: C:\Windows\Temp\Amazon_SSM_Agent_20200610005533_000_AmazonSSMAgentMSI.log
        Owner: BUILTIN\Administrators
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_FileProtectionSetting/OS_gathering
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
    │              └── WIN_FileProtectionSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_FileProtectionSetting.yml
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
