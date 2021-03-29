Ansible Role: OS-Windows2016/WIN_NICTeaming_Team/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するNICチーミング設定（チーム）についての情報の設定を行います。

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
OS-Windows2016/WIN_NICTeaming_Team/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

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
    │         └── WIN_NICTeaming_Team/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NICTeaming_Team_adapter.yml
    │                   │      build_NICTeaming_Team_item_create.yml
    │                   │      build_NICTeaming_Team_item_delete.yml
    │                   │      build_NICTeaming_Team_item_update_Members.yml
    │                   │      build_NICTeaming_Team_item_update.yml
    │                   │      build_NICTeaming_Team.yml
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
    - role: OS-Windows2016/WIN_NICTeaming_Team/OS_build
      VAR_WIN_NICTeaming_Team:
      - Action: present
        LoadBalancingAlgorithm: 5
        Members:
        - イーサネット
        Name: PF_BUILD_TEST
        Standby: null
        TeamingMode: 1
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
    - role: OS-Windows2016/WIN_NICTeaming_Team/OS_build
      VAR_WIN_NICTeaming_Team:
      - Action: present
        LoadBalancingAlgorithm: 5
        Members:
        - イーサネット
        Name: PF_BUILD_TEST
        Standby: null
        TeamingMode: 1
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NICTeaming_Team/OS_gathering
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
    │              └── WIN_NICTeaming_Team/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NICTeaming_Team.yml
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
