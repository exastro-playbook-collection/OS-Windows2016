Ansible Role: OS-Windows2016/WIN_NetIPv6Protocol/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するIPv6の設定についての情報の設定を行います。

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
OS-Windows2016/WIN_NetIPv6Protocol/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetIPv6Protocol` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultHopLimit` | デフォルトのホップ制限値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NeighborCacheLimit` | ネイバーキャッシュエントリの最大数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RouteCacheLimit` | ルートキャッシュエントリの最大数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ReassemblyLimit` | 再構成バッファーの最大サイズ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IcmpRedirects` | ICMPリダイレクト<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SourceRoutingBehavior` | ソースルーティングされたパケットの動作<br>0 ： Forward<br>1 ： DontForward<br>2 ： Drop | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DhcpMediaSense` | MediaSense<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MediaSenseEventLog` | MediaSenseイベントログ<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MldLevel` | マルチキャストリスナ発見（MLD）サポートのレベル<br>0 ： None<br>1 ： SendOnly<br>2 ： All | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MldVersion` | ホストがサポートするマルチキャストリスナ発見の最大バージョン<br>3 ： Version1<br>4 ： Version2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MulticastForwarding` | マルチキャスト転送<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`GroupForwardedFragments` | グループ転送フラグメント<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RandomizeIdentifiers` | 識別子のランダム化<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AddressMaskReply` | アドレスマスク応答<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`UseTemporaryAddresses` | 一時アドレス<br>0 ： Disabled  使用しない<br>1 ： Enabled 使用する<br>2 ： Always　常に一時アドレスを生成する | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MaxDadAttempts` | 一時アドレスの重複アドレス検出の最大試行回数 | 

### Example
~~~
VAR_WIN_NetIPv6Protocol:
  AddressMaskReply: 0
  DefaultHopLimit: 128
  DhcpMediaSense: 1
  GroupForwardedFragments: 0
  IcmpRedirects: 1
  MaxDadAttempts: 3
  MaxPreferredLifetime: 1.00:00:00
  MaxRandomTime: 00:10:00
  MaxValidLifetime: 7.00:00:00
  MediaSenseEventLog: 0
  MldLevel: 2
  MldVersion: 4
  MulticastForwarding: 0
  NeighborCacheLimit: 1024
  RandomizeIdentifiers: 1
  ReassemblyLimit: 33551232
  RegenerateTime: 00:00:05
  RouteCacheLimit: 32768
  SourceRoutingBehavior: 1
  UseTemporaryAddresses: 0
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
    │         └── WIN_NetIPv6Protocol/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetIPv6Protocol.yml
    │                   │      build_NetIPv6Protocol_each.yml
    │                   │      build_NetIPv6Protocol_item.yml
    │                   │      build_NetIPv6Protocol_time.yml
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
    - role: OS-Windows2016/WIN_NetIPv6Protocol/OS_build
      VAR_WIN_NetIPv6Protocol:
        AddressMaskReply: 0
        DefaultHopLimit: 128
        DhcpMediaSense: 1
        GroupForwardedFragments: 0
        IcmpRedirects: 1
        MaxDadAttempts: 3
        MaxPreferredLifetime: 1.00:00:00
        MaxRandomTime: 00:10:00
        MaxValidLifetime: 7.00:00:00
        MediaSenseEventLog: 0
        MldLevel: 2
        MldVersion: 4
        MulticastForwarding: 0
        NeighborCacheLimit: 1024
        RandomizeIdentifiers: 1
        ReassemblyLimit: 33551232
        RegenerateTime: 00:00:05
        RouteCacheLimit: 32768
        SourceRoutingBehavior: 1
        UseTemporaryAddresses: 0
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
    - role: OS-Windows2016/WIN_NetIPv6Protocol/OS_build
      VAR_WIN_NetIPv6Protocol:
        AddressMaskReply: 0
        DefaultHopLimit: 128
        DhcpMediaSense: 1
        GroupForwardedFragments: 0
        IcmpRedirects: 1
        MaxDadAttempts: 3
        MaxPreferredLifetime: 1.00:00:00
        MaxRandomTime: 00:10:00
        MaxValidLifetime: 7.00:00:00
        MediaSenseEventLog: 0
        MldLevel: 2
        MldVersion: 4
        MulticastForwarding: 0
        NeighborCacheLimit: 1024
        RandomizeIdentifiers: 1
        ReassemblyLimit: 33551232
        RegenerateTime: 00:00:05
        RouteCacheLimit: 32768
        SourceRoutingBehavior: 1
        UseTemporaryAddresses: 0
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetIPv6Protocol/OS_gathering
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
    │              └── WIN_NetIPv6Protocol/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetIPv6Protocol.yml
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
