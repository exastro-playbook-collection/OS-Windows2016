Ansible Role: OS-Windows2016/WIN_ComputerSetting/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するWindows基本設定（コンピュータ名）についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_ComputerSetting/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_ComputerSetting.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_ComputerSetting.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_ComputerSetting` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Description` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の「コンピュータの説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Name` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の「フルコンピュータ名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DNSDomainSuffixSearchOrder` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の詳細ボタン押下、「DNSサフィックスとNETBIOSコンピュータ名」の「このコンピュータのプライマリDNSサフィックス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SyncDomainWithMembership` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の詳細ボタン押下、「DNSサフィックスとNETBIOSコンピュータ名」の「ドメインが変更されるときに、プライマリDNSサフィックスを変更する」のチェックボックスに該当<br>0 ： ドメインが変更されるときに、プライマリDNSサフィックスを変更する<br>1 ： ドメインが変更されるときに、プライマリDNSサフィックスを変更しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainOrWorkgroup` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の「所属するグループ」に該当<br>true ：  ドメイン指定<br>false ： ワークグループ指定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainOrWorkgroupName` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の「所属するグループ」のドメイン名／ワークグループ名に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainUser` | ドメイン指定時のドメインユーザー名<br>収集では取得されないため、ドメイン指定時には設定は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainPassword` | ドメイン指定時のドメインユーザーのパスワード<br>収集では取得されないため、ドメイン指定時には設定は必須 | 

### Example
~~~
VAR_WIN_ComputerSetting:
  DNSDomainSuffixSearchOrder: ''
  Description: AWS Win2016-01 TEST
  DomainOrWorkgroup: false
  DomainOrWorkgroupName: WORKGROUP
  Name: EC2AMAZ-3FLM24H
  SyncDomainWithMembership: 1
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
    │         └── WIN_ComputerSetting/
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
    - role: OS-Windows2016/WIN_ComputerSetting/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_ComputerSetting/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_ComputerSetting.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_ComputerSetting/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_ComputerSetting.yml  # パラメータ
~~~

- 生成したパラメータを指定してplaybookを実行

~~~
> ansible-playbook master_playbook.yml -i hosts
~~~

# Remarks
-------
レジストリキーが存在しないパラメタの値はnullとして取得されます。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
