Ansible Role: OS-Windows2016/WIN_NetIpAddress/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するネットワーク基本情報についての情報の設定を行います。

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
OS-Windows2016/WIN_NetIpAddress/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

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
    │         └── WIN_NetIpAddress/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_NetIpAddress.yml
    │                   │      build_NetIpAddress_adapter.yml
    │                   │      build_NetIpAddress_item.yml
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
    - role: OS-Windows2016/WIN_NetIpAddress/OS_build
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
    - role: OS-Windows2016/WIN_NetIpAddress/OS_build
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
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetIpAddress/OS_gathering
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
    │              └── WIN_NetIpAddress/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetIpAddress.yml
~~~

# Remarks
-------
ipaddrに指定したIPアドレスが該当のネットワークアダプターに追加されるため、すでにIPアドレスが設定されている場合は複数のIPアドレスが追加されるため注意してください。
誤って追加した場合は、本ロールで削除してください。
IPv6のアドレス設定はRFC5952推奨の省略形で記載します。（記載しない場合は、エラー）
次のサイトにある「IPv6アドレスの推奨テキスト表記」を参照してください。
https://www.nic.ad.jp/ja/newsletter/No46/0800.html
IPアドレスの削除は、収集したネットワークデバイスのIPアドレスを変更せずに実施した場合のみ削除されます。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
