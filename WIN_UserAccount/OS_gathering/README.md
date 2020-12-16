Ansible Role: OS-Windows2016/WIN_UserAccount/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するローカルユーザについての情報の取得を行います。

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
| `VAR_OS_gathering_dest` | '{{ playbook_dir }}/_gathered_data' | 収集した設定情報の格納先パス。 | 
| `VAR_OS_extracting_dest` | '{{ playbook_dir }}/_parameters' | 生成したパラメータの出力先パス。 | 
| `VAR_OS_python_cmd` | 'python3' | Ansible実行マシン上で、パラメータファイル作成時に使用するpythonのコマンド。 | 

# Results

本ロールの出力について説明します。

## 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_UserAccount/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_UserAccount.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_UserAccount.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_UserAccount` |     | 
| `- Name` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FullName` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「フルネーム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Description` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordRequired` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「ユーザーは次回ログオン時にパスワードの変更が必要」のチェックボックスに該当<br>true ： パスワードの変更が必要<br>false ： パスワードの変更が必要でない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordChangeable` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「ユーザーはパスワードを変更できない」のチェックボックスに該当<br>true ： パスワードを変更できる<br>false ： パスワードを変更できない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordExpires` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「パスワードを無期限にする」のチェックボックスに該当<br>true ： パスワードを無期限にしない<br>false ： パスワードを無期限にする | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Disabled` | 「コントロール パネル」「すべてのコントロール パネル項目」「管理ツール」「コンピュータの管理」「コンピュータの管理(ローカル)」「システムツール」「ローカルユーザーとグループ」「ユーザー」「ユーザーのプロパティ」「全般」の「アカウントを無効にする」のチェックボックスに該当<br>true ： アカウントを無効にする<br>false ： アカウントを無効にしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Password` | ユーザー作成時に設定するパスワード | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PasswordApply` | パスワード変更情報フラグ<br>true ： ユーザー作成、パスワードを含めたユーザー更新の際に設定<br>false ： パスワードを含めないユーザー更新時に設定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present ： ユーザー作成、更新<br>absent ： ユーザーの削除 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Lockout` | ユーザー アカウントが、Windows オペレーティング システムロックされているかどうか<br>true ： ロックされている<br>false ： ロックされていない<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalAccount` | ローカルコンピュータに定義されたユーザーアカウント<br>true ：ローカルコンピュータに定義されているユーザーアカウント<br>false ： ローカルコンピュータに定義されていないユーザーアカウント<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Domain` | ユーザー アカウントが属している Windows ドメイン名<br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AccountType` | Windows ユーザー アカウントの特性フラグ<br>Temporary duplicate account (256)<br>Normal account (512)<br>Interdomain trust account (2048)<br>Workstation trust account (4096)<br>Server trust account (8192)<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`InstallDate` | オブジェクトがインストールされた日<br>※構築で使用しない | 

### Example
~~~
VAR_WIN_UserAccount:
- AccountType: 512
  Action: present
  Description: Built-in account for administering the computer/domain
  Disabled: false
  Domain: EC2AMAZ-3FLM24H
  FullName: ''
  InstallDate: null
  LocalAccount: true
  Lockout: false
  Name: Administrator
  Password: ''
  PasswordApply: false
  PasswordChangeable: true
  PasswordExpires: true
  PasswordRequired: true
- AccountType: 512
  Action: present
  Description: ''
  Disabled: false
  Domain: EC2AMAZ-3FLM24H
  FullName: ansible
  InstallDate: null
  LocalAccount: true
  Lockout: false
  Name: ansible
  Password: ''
  PasswordApply: false
  PasswordChangeable: true
  PasswordExpires: false
  PasswordRequired: true
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
    │         └── WIN_UserAccount/
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
    - role: OS-Windows2016/WIN_UserAccount/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_UserAccount/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_UserAccount.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_UserAccount/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_UserAccount.yml  # パラメータ
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
