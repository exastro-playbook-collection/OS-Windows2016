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
| `- ifDesc` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティの接続の方法に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`connection_name` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスの表示名に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPEnabled` | ネットワークデバイスのIPアドレス設定<br>true ： IPアドレスが設定されている<br>false ： IPアドレスが設定されていない<br>※ 構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv4DHCPEnabled` | IPv4の動的ホスト構成プロトコル（DHCP）のIPインターフェイスの有効状態に該当<br>1 ： 有効<br>0 ： 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv6DHCPEnabled` | IPv6の動的ホスト構成プロトコル（DHCP）のIPインターフェイスの有効状態に該当<br>1 ： 有効<br>0 ： 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultIPv4Gateway` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン4(TCP/IPv4)」のプロパティボタン押下、「インターネットプロトコルバージョン4(TCP/IPv4)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「IP設定」「デフォルトゲートウェイ」のIPアドレスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultIPv6Gateway` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン6(TCP/IPv6)」のプロパティボタン押下、「インターネットプロトコルバージョン6(TCP/IPv6)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「IP設定」「デフォルトゲートウェイ」のIPアドレスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv4DNS` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン4(TCP/IPv4)」のプロパティボタン押下、「インターネットプロトコルバージョン4(TCP/IPv4)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「DNS」「DNSサーバアドレス(使用順)」のIPアドレスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv6DNS` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン6(TCP/IPv6)」のプロパティボタン押下、「インターネットプロトコルバージョン6(TCP/IPv6)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「DNS」「DNSサーバアドレス(使用順)」のIPアドレスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RegisterThisConnectionsAddress` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン4(TCO/IPv4)」か「インターネットプロトコルバージョン6(TCP/IPv6)」のプロパティボタン押下、「インターネットプロトコルバージョン4(TCP/IPv4)のプロパティ」か「インターネットプロトコルバージョン6(TCP/IPv6)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「DNS」「この接続のアドレスをDNSに登録する」に該当<br>true ： 登録する<br>false ： 登録しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`UseSuffixWhenRegistering` | 「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン4(TCO/IPv4)」か「インターネットプロトコルバージョン6(TCP/IPv6)」のプロパティボタン押下、「インターネットプロトコルバージョン4(TCP/IPv4)のプロパティ」か「インターネットプロトコルバージョン6(TCP/IPv6)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「DNS」「この接続のDNSサフィックスをDNSに使う」に該当<br>true ： 登録する<br>false ： 登録しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NetBIOSSetting` |「コントロール パネル」「すべてのコントロール パネル項目」「ネットワークと共有センター」「アダプターの設定の変更」で選択したネットワークデバイスのプロパティ、「この接続は次の項目を使用します」の「インターネットプロトコルバージョン4(TCP/IPv4)」のプロパティボタン押下、「インターネットプロトコルバージョン4(TCP/IPv4)のプロパティ」の詳細設定ボタン押下、「TCP/IP 詳細設定」「WINS」「NetBIOS設定」に該当<br>0 ： 規定値<br>1 ： NetBIOS over TPC/IPを有効にする<br>2 ： NetBIOS over TPC/IPを無効にする | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv4MTU` | IPv4のMTUを指定する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IPv6MTU` | IPv6のMTUを指定する |  

### Example
~~~
WIN_NetAdapterConfiguration:
- DefaultIPv4Gateway:
  - 192.168.0.1
  IPEnabled: true
  IPv4DHCPEnabled: 1
  IPv4DNS:
  - 192.168.0.2
  IPv4MTU: 9001
  IPv6DHCPEnabled: 1
  IPv6DNS: []
  IPv6MTU: 9001
  NetBIOSSetting: 0
  RegisterThisConnectionsAddress: true
  UseSuffixWhenRegistering: true
  connection_name: Ethernet
  ifDesc: 'AWS PV Network Device #0'
- DefaultIPv4Gateway: []
  DefaultIPv6Gateway: []
  IPEnabled: false
  IPv4DNS: []
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

## パラメータ再利用

以下の例では、生成したパラメータを使用してOSの設定を変更します。

- マスターPlaybook サンプル[master_playbook.yml]

~~~
#master_playbook.yml
---
- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetAdapterConfiguration.yml  # パラメータ
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
