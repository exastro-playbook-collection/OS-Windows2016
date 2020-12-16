Ansible Role: OS-Windows2016/WIN_NetworkManagement/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するネットワーク管理についての情報の設定を行います。

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
OS-Windows2016/WIN_NetworkManagement/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetworkManagement` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`EnableLMHOSTS` | 「TCP/IP 詳細設定」「WINS」の「LMHOSTSの参照を有効にする」のチェックボックスに該当<br>1 ： 有効にする<br>0 ： 有効にしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisabledComponents` | LAN インタフェースのIPv6 接続、およびトンネル機能<br>1 ： 有効にする<br>0 ： 有効にしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`EnableICMPRedirect` | ICMP による攻撃からの保護<br>1 ： 保護する<br>0 ： 保護しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NoNameReleaseOnDemand` | NetBIOS 名の保護<br>1 ： 保護する<br>0 ： 保護しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`MaxDenials` | リモートアクセスユーザーロックアウトしきい値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`ResetTime` | リモートアクセスユーザーロックアウト再ログオン所要時間（分単位 | 

### Example
~~~
VAR_WIN_NetworkManagement:
  DisabledComponents: 0
  EnableICMPRedirect: 1
  EnableLMHOSTS: 0
  MaxDenials: 0
  NoNameReleaseOnDemand: 0
  ResetTime: 3000
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
    │         └── WIN_NetworkManagement/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_NetworkManagement.yml
    │                   │      build_Registry_present.yml
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
    - role: OS-Windows2016/WIN_NetworkManagement/OS_build
      VAR_WIN_NetworkManagement:
        DisabledComponents: 0
        EnableICMPRedirect: 1
        EnableLMHOSTS: 0
        MaxDenials: 0
        NoNameReleaseOnDemand: 0
        ResetTime: 3000
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
    - role: OS-Windows2016/WIN_NetworkManagement/OS_build
      VAR_WIN_NetworkManagement:
        DisabledComponents: 0
        EnableICMPRedirect: 1
        EnableLMHOSTS: 0
        MaxDenials: 0
        NoNameReleaseOnDemand: 0
        ResetTime: 3000
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetworkManagement/OS_gathering
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
    │              └── WIN_NetworkManagement/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetworkManagement.yml
~~~

# Remarks
-------
実際のレジストリ値は0が設定されていますが、収集でnullが取得されるパラメタがあります。
下記レジストリは、パラメタ値がnullで設定を実行した際にメッセージとしてchangeとなりますが、設定値は変わりなく0のままとなります。
・NoNameReleaseOnDemand： NetBIOS 名の保護（GUIなし）
・DisabledComponents： LAN インタフェースのIPv6 接続、およびトンネル機能（GUIなし）
・EnableICMPRedirect: ICMP による攻撃からの保護（GUIなし）

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
