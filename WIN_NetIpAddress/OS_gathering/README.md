Ansible Role: OS-Windows2016/WIN_NetIpAddress/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するネットワーク基本情報についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NetIpAddress/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NetIpAddress.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetIpAddress.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetIpAddress` |     | 
| `- ifDesc` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティの接続方法に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ipaddr` | ネットワークデバイスのプロパティの接続方法「インターネットプロトコルバージョン4」または「インターネットプロトコルバージョン6」のプロパティのIPアドレス、Microsoft ISATAP AdapterのIPアドレスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`prefix` | ネットワークアドレス部分の長さ（プレフィックス）<br>プレフィックス値として指定可能な数値を指定する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`PolicyStore` | IPアドレスを有効にするタイミング<br>1 ： ActiveStore　IPアドレス情報が有効<br>0 ： PersistentStore　再起動時に有効とする<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AddressState` | IPアドレスの重複アドレス検出（DAD）状態値<br>0 ： Invalid  有効でなく、使用されないアドレス<br>1 ： Tentative  通信に使用されていないアドレス<br>2 ： Duplicate  重複するアドレス<br>3 ： Deprecated 新しい接続を確立できなくなるアドレス <br>4 ： Preferred  有効で使用可能なアドレス<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AddressFamily` | IPアドレスファミリ<br>2 ： IPv4を使用<br>23 ： IPv6を使用 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Type` | IPアドレスタイプ<br>1 ： Unicastを使用<br>2 ： Anycastを使用 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present:  IPｖ4、IPv6をネットワークデバイスに追加<br>absent: IPｖ4、IPv6をネットワークデバイスから削除 | 

### Example
~~~
VAR_WIN_NetIpAddress:
- Action: present
  AddressFamily: 23
  AddressState: 4
  PolicyStore: 1
  Type: 1
  ifDesc: Teredo Tunneling Pseudo-Interface
  ipaddr: 0:0:0:0:0:0:0:0
  prefix: 64
- Action: present
  AddressFamily: 23
  AddressState: 4
  PolicyStore: 1
  Type: 1
  ifDesc: Teredo Tunneling Pseudo-Interface
  ipaddr: 0:0:0:0:0:0:0:0
  prefix: 64
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
    │         └── WIN_NetIpAddress/
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
    - role: OS-Windows2016/WIN_NetIpAddress/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NetIpAddress/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetIpAddress.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_NetIpAddress/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetIpAddress.yml  # パラメータ
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
