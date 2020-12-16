Ansible Role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するネットワークアダプタ設定についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NetAdapterConfiguration/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NetAdapterConfiguration.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetAdapterConfiguration.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetAdapterConfiguration` |     | 
| `- ifDesc:` | NetIPAddressのifDescの説明と同様 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`connection_name` | ネットワーク接続の表示名に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPEnabled` | IPの有効／無効を示す | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv4DHCPEnabled` | 「TCP/IP 詳細設定」のに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv6DHCPEnabled` | 「TCP/IP 詳細設定」のに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultIPv4Gateway` | 「TCP/IP 詳細設定」の「IP設定」の「デフォルトゲートウェイ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultIPv6Gateway` | 「TCP/IP 詳細設定」の「IP設定」の「デフォルトゲートウェイ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv4DNS` | 「TCP/IP 詳細設定」の「DNS」の「DNSサーバーアドレス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv6DNS` | 「TCP/IP 詳細設定」の「DNS」の「DNSサーバーアドレス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv4MTU` | IPv4のMTUを指定する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv6MTU` | IPv4のMTUを指定する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RegisterThisConnectionsAddress` | 「TCP/IP 詳細設定」の「DNS」の「この接続のアドレスをDNSに登録する」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`UseSuffixWhenRegistering` | 「TCP/IP 詳細設定」の「DNS」の「この接続のDNSサフィックスをDNSに使う」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NetBIOSSetting` | 「TCP/IP 詳細設定」の「WINS」の「NetBIOS設定」に該当 | 

### Example
~~~
WIN_NetAdapterConfiguration:
- DefaultIPv4Gateway:
  - 10.70.0.1
  IPEnabled: true
  IPv4DHCPEnabled: 1
  IPv4DNS:
  - 10.70.0.2
  IPv4MTU: 9001
  IPv6DHCPEnabled: 1
  IPv6MTU: 9001
  NetBIOSSetting: 0
  RegisterThisConnectionsAddress: true
  UseSuffixWhenRegistering: true
  connection_name: Ethernet
  ifDesc: 'AWS PV Network Device #0'
- IPEnabled: false
  NetBIOSSetting: null
  connection_name: Local Area Connection* 1
  ifDesc: Microsoft Kernel Debug Network Adapter
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
    │         └── WIN_NetAdapterConfiguration/
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
    - role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NetAdapterConfiguration/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetAdapterConfiguration.yml  # パラメータ
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
