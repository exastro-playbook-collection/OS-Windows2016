Ansible Role: OS-Windows2016/WIN_FileProtectionSetting/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するファイル保護設定についての情報の取得を行います。

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
| `VAR_OS_python_cmd` | 'python3' | パラメータファイル作成時に使用するpythonのコマンド | 
| `VAR_OS_gathering_file_path_recurse` |#- 'C:\Users\Public'<br>配列で設定 | ファイル情報を再帰的に取得するディレクトリパス  | 
| `VAR_OS_gathering_file_path` | #- 'C:\Users\Public'<br>#- 'C:\Users\Public\Pictures\Sample Pictures\Penguins.jpg'<br>配列で設定  | ファイル情報を再帰的に取得しないディレクトリパス<br>情報取得したいファイル名 |

# Results

本ロールの出力について説明します。

## ファイル情報を取得する方法
- roles/OS-Windows2016/WIN_FileProtectionSetting/OS_gathering/defaults/main.ymlに以下のように設定

~~~
VAR_OS_gathering_file_path_recurse:
 - 'C:\Test\test01'

VAR_OS_gathering_file_path:
 - 'C:\Test\test02'
 - 'C:\Test\test03\test.txt'
~~~

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_FileProtectionSetting/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_FileProtectionSetting.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_FileProtectionSetting.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_FileProtectionSetting` |     | 
| `- Name:` | ファイル名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AccessToString` | エクスプローラーでファイル選択「プロパティ」「セキュリティ」「詳細設定」「アクセス許可エントリ」の「種類」+「プリンシバル」+「アクセス」に該当<br>※ 表示順は「プリンシパル 種類 アクセス許可1, アクセス許可2・・・」<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Owner` | エクスプローラーでファイル選択「プロパティ」「セキュリティ」「詳細設定」の「所有者」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Encrypt` | 暗号化<br>E ： 暗号化されている<br>U ： 暗号化されていない<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>file ： ファイルの作成、更新<br>absent ：ファイルの削除 | 

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

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2016
    │         └── WIN_FileProtectionSetting/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
    │                   │── tasks/
    │                   │      check.yml
    │                   │      gathering_definition_copy.yml
    │                   │      gathering_definition_set.yml
    │                   │      gathering.yml
    │                   │      generate.yml
    │                   │      main.yml
    │                   │── vars/
    │                   │      gathering_definition_base.yml
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
    - role: OS-Windows2016/WIN_FileProtectionSetting/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_FileProtectionSetting/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_FileProtectionSetting.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_FileProtectionSetting/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_FileProtectionSetting.yml  # パラメータ
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
