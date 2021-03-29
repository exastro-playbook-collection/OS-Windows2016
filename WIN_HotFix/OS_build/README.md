Ansible Role: OS-Windows2016/WIN_HotFix/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関する更新プログラム一覧についての情報の設定を行います。

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
OS-Windows2016/WIN_HotFix/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_HotFix` |     | 
| `- HotFixID` | 更新プログラムファイルのHotFixID | 
| &nbsp;&nbsp;&nbsp;&nbsp;`HotFixType` | 更新プログラムの型<br>構築で使用しない | 

### Example
~~~
VAR_WIN_HotFix:
- HotFixID: KB3176936
  HotFixType: Update
- HotFixID: KB3186568
  HotFixType: Update
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
    │         └── WIN_HotFix/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_HotFix.yml
    │                   │      build_HotFix_each.yml
    │                   │      build_HotFix_item.yml
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
    - role: OS-Windows2016/WIN_HotFix/OS_build
      VAR_WIN_HotFix:
      - HotFixID: KB3176936
        HotFixType: Update
      - HotFixID: KB3186568
        HotFixType: Update
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
    - role: OS-Windows2016/WIN_HotFix/OS_build
      VAR_WIN_HotFix:
      - HotFixID: KB3176936
        HotFixType: Update
      - HotFixID: KB3186568
        HotFixType: Update
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_HotFix/OS_gathering
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
    │              └── WIN_HotFix/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_HotFix.yml
~~~

# Remarks
-------
更新プログラムファイルが「windows8-rt-kb3139852-x64_223bbf5a3e4505288d8c2d9c8d2bc2258eb40a13.cab」の場合、更新プログラムファイルのHotFixIDは「KB3139852」となります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
