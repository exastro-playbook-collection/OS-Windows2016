Ansible Role: OS-Windows2016/WIN_NICTeaming_VLAN/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するNICチーミング設定（VLAN）についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NICTeaming_VLAN/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NICTeaming_VLAN.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NICTeaming_VLAN.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NICTeaming_VLAN` |     | 
| `- Team:` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「選択したチームインターフェース」の「NICチーミング」「チーム インターフェース」の「チーム」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Name` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「選択したチームインターフェース」の「NICチーミング」「一般情報」のVLAN名に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ifDesc` | VLANのInterface　Description<br>「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「選択したチームインターフェース」の「NICチーミング」「一般情報」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Primary` | プライマリ インターフェースの有無<br>true ： プライマリ インターフェース<br>false ： セカンダリ インターフェース |
| &nbsp;&nbsp;&nbsp;&nbsp;`Default` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「VLAN メンバーシップ」の「既定」に該当<br>true ： 既定<br>false ： 既定でない<br>※既定はプライマリのVLANのみ設定可能 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`VlanID` | 「サーバー マネージャー」「ローカルサーバー」「NICチーミング」「アダプターとインターフェース」「チーム インターフェース」「VLAN メンバーシップ」の「特定のVLAN」に該当<br>※Defaultがfalseの場合のみVlanIDの設定が有効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`TransmitLinkSpeed` | アダプタの伝送速度<br>※構築で使用しない |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ReceiveLinkSpeed` | アダプタの受信速度<br>※構築で使用しない |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present：作成、更新<br>absent：削除 | 

### Example
~~~
VAR_WIN_NICTeaming_VLAN: 
- Action: present
  Default: true
  Name: PF_BUILD_TEST
  Primary: true
  ReceiveLinkSpeed: 1 Gbps
  TransmitLinkSpeed: 1 Gbps
  VlanID: null
  ifDesc: Microsoft Network Adapter Multiplexor Driver
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
    │         └── WIN_NICTeaming_VLAN/
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
    - role: OS-Windows2016/WIN_NICTeaming_VLAN/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NICTeaming_VLAN/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NICTeaming_VLAN.yml  # パラメータ
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
