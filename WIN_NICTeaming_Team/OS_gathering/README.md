Ansible Role: OS-Windows2016/WIN_NICTeaming_Team/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するNICチーミング設定（チーム）についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NICTeaming_Team/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NICTeaming_Team.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NICTeaming_Team.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NICTeaming_Team` |     | 
| `- Name:` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「チーム」のチームに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Members` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「チーム」「各チームのプロパティ」「メンバー アダプター」のチーム内がチェックされているアダプタに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`TeamingMode` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「チーム」「各チームのプロパティ」「追加のプロパティ」「チーミングモード」に該当<br>0 ： 静的チーミング<br>1 ： スイッチに依存しない<br>2 ： LACP | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LoadBalancingAlgorithm` |「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「チーム」「各チームのプロパティ」「追加のプロパティ」「負荷分散モード」に該当<br>0 ： アドレスのハッシュ<br>2 ： IPアドレス<br>3 ： MACアドレス<br>4 ： Hyper-V ポート<br>5 ： 動的 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Standby` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「チーム」「各チームのプロパティ」「追加のプロパティ」「スタンバイアダプター」に該当<br>※なし(すべてのアダプターがアクティブ)の場合はnull | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present：作成、更新<br>absent：削除 | 

### Example
~~~
VAR_WIN_NICTeaming_Team:
- Action: present
  LoadBalancingAlgorithm: 5
  Members:
  - イーサネット
  Name: PF_BUILD_TEST
  Standby: null
  TeamingMode: 1
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
    │         └── WIN_NICTeaming_Team/
    │              └── OS_gathering/
    │                   │── defaults/
    │                   │      main.yml
    │                   │── files/
    │                   │      extracting.py
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
    - role: OS-Windows2016/WIN_NICTeaming_Team/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NICTeaming_Team/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NICTeaming_Team.yml  # パラメータ
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
