Ansible Role: OS-Windows2016/WIN_NICTeaming_VLAN/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するNICチーミング設定（VLAN）についての情報の設定を行います。

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
OS-Windows2016/WIN_NICTeaming_VLAN/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

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
    │         └── WIN_NICTeaming_VLAN/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NICTeaming_VLAN_adapter.yml
    │                   │      build_NICTeaming_VLAN_item_absent.yml
    │                   │      build_NICTeaming_VLAN_item_present_detail_Primary.yml
    │                   │      build_NICTeaming_VLAN_item_present_detail_Secondary.yml
    │                   │      build_NICTeaming_VLAN_item_present_Primary.yml
    │                   │      build_NICTeaming_VLAN_item_present_Secondary.yml
    │                   │      build_NICTeaming_VLAN.yml
    │                   │      check_parameter.yml
    │                   │      check.yml
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
    - role: OS-Windows2016/WIN_NICTeaming_VLAN/OS_build
      VAR_WIN_NICTeaming_VLAN: 
      - Action: present
        Default: true
        Name: PF_BUILD_TEST
        Primary: true
        ReceiveLinkSpeed: 1 Gbps
        TransmitLinkSpeed: 1 Gbps
        VlanID: null
        ifDesc: Microsoft Network Adapter Multiplexor Driver
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
    - role: OS-Windows2016/WIN_NICTeaming_VLAN/OS_build
      VAR_WIN_NICTeaming_VLAN: 
      - Action: present
        Default: true
        Name: PF_BUILD_TEST
        Primary: true
        ReceiveLinkSpeed: 1 Gbps
        TransmitLinkSpeed: 1 Gbps
        VlanID: null
        ifDesc: Microsoft Network Adapter Multiplexor Driver
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NICTeaming_VLAN/OS_gathering
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
    │              └── WIN_NICTeaming_VLAN/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NICTeaming_VLAN.yml
~~~

# Remarks
-------
チームが設定されていないと、VLANは追加できません。<br>
プライマリ インターフェースのVLANは作成、削除できません。<br>
セカンダリ インターフェースのVLANを作成する際には、ifDescを空文字としてください。　設定内容： ifDesc: ''

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
