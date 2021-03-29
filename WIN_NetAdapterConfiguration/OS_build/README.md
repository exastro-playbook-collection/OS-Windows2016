Ansible Role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するネットワークアダプタ詳細設定についての情報の設定を行います。

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
OS-Windows2016/WIN_NetAdapterConfiguration/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

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
  DefaultIPv6Gateway: []
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
    │         └── WIN_NetAdapterConfiguration/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetAdapterConfiguration.yml
    │                   │      build_NetAdapterConfiguration_adapter.yml
    │                   │      build_NetAdapterConfiguration_item.yml
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
    - role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_build
      WIN_NetAdapterConfiguration:
      - DefaultIPv4Gateway:
        - 192.168.0.1
        DefaultIPv6Gateway: []
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
    - role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_build
      WIN_NetAdapterConfiguration:
      - DefaultIPv4Gateway:
        - 192.168.0.1
        DefaultIPv6Gateway: []
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
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetAdapterConfiguration/OS_gathering
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
    │              └── WIN_NetAdapterConfiguration/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetAdapterConfiguration.yml
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
