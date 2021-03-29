Ansible Role: OS-Windows2016/WIN_NetIPv4Protocol/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するIPv4の設定についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NetIPv4Protocol/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NetIPv4Protocol.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetIPv4Protocol.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetIPv4Protocol` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultHopLimit` | デフォルトのホップ制限値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NeighborCacheLimit` | ネイバーキャッシュエントリの最大数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RouteCacheLimit` | ルートキャッシュエントリの最大数 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ReassemblyLimit` | 再構成バッファーの最大サイズ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IcmpRedirects` | ICMPリダイレクト<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SourceRoutingBehavior` | ソースルーティングされたパケットの動作<br>0 ： Forward<br>1 ： DontForward<br>2 ： Drop | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DhcpMediaSense` | MediaSense<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MediaSenseEventLog` | MediaSenseイベントログ<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IGMPLevel` | インターネットグループ管理プロトコル（IGMP）レベル<br>0 ： None<br>1 ： SendOnly<br>2 ： All | 
| &nbsp;&nbsp;&nbsp;&nbsp;`IGMPVersion` | IGMPバージョン番号<br>2 ： Version1<br>3 ： Version2<br>4 ： Version3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MulticastForwarding` | マルチキャスト転送<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`GroupForwardedFragments` | グループ転送フラグメント<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RandomizeIdentifiers` | 識別子のランダム化<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AddressMaskReply` | アドレスマスク応答<br>1 ： Enabled　有効<br>0 ： Disabled　無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MinimumMtu` | ネットワーク層の最大伝送ユニット（MTU）の値をバイト単位数 | 

### Example
~~~
VAR_WIN_NetIPv4Protocol:
  AddressMaskReply: 0
  DefaultHopLimit: 128
  DhcpMediaSense: 1
  GroupForwardedFragments: 0
  IGMPLevel: 2
  IGMPVersion: 4
  IcmpRedirects: 1
  MediaSenseEventLog: 0
  MinimumMtu: 576
  MulticastForwarding: 0
  NeighborCacheLimit: 1024
  RandomizeIdentifiers: 1
  ReassemblyLimit: 33551232
  RouteCacheLimit: 32768
  SourceRoutingBehavior: 1
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
    │         └── WIN_NetIPv4Protocol/
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
    - role: OS-Windows2016/WIN_NetIPv4Protocol/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NetIPv4Protocol/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetIPv4Protocol.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_NetIPv4Protocol/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetIPv4Protocol.yml  # パラメータ
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
