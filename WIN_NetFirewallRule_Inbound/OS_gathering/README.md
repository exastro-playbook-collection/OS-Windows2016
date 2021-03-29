Ansible Role: OS-Windows2016/WIN_NetFirewallRule_Inbound/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するファイアウォール設定（受信規則）についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NetFirewallRule_Inbound/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NetFirewallRule_Inbound.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetFirewallRule_Inbound.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetFirewallRule_Inbound` |     | 
| `- DisplayName:` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Name` | DisplayNameのOS内情報 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RuleDescription` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」「各ファイアウォールの受診の規則のプロパティ」「全般」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayGroup` |「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「グループ」に該当 <br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Group` | DisplayGroupのOS内情報<br>※構築では受信規則の新規作成時にのみ使用し、更新時には使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Enabled` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「有効」に該当<br>1 ： はい<br>2 ： いいえ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FirewallAction` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「操作」に該当<br>2 ： 許可<br>4 ： 不許可 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Profile` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「プロファイル」に該当<br>0 ： すべて<br>1 ： ドメイン<br>2 ： プライベート<br>3 ： ドメイン、プライベート<br>4 ： パブリック<br>5 ： ドメイン、パブリック<br>6 ： プライベート、パブリック<br>7 ： ドメイン、プライベート、パブリック | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalUser` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」「各ファイアウォールの受診の規則のプロパティ」「ローカル プリンシパル」の「承認されているユーザー」に該当 <br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalAddress` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「ローカルアドレス」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalPort` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「ローカルポート」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteUser` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」「各ファイアウォールの受診の規則のプロパティ」「リモートユーザー」の「承認されているユーザー」に該当 <br>※構築で使用しない |  
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteAddress` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「リモートアドレス」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemotePort` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「リモートポート」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteMachine` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」「各ファイアウォールの受診の規則のプロパティ」「リモートコンピューター」の「承認されているコンピューター」に該当 <br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Program` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「プログラム」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Protocol` |「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」の「プロトコル」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Service` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「受信の規則」「各ファイアウォールの受診の規則のプロパティ」「プログラムおよびサービス」「サービス」の設定ボタン押下、「サービス設定のカスタマイズ」で設定したサービスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present：作成、更新<br>absent：削除 | 

### Example
~~~
VAR_WIN_NetFirewallRule_Inbound:
- Action: present
  DisplayGroup: Virtual Machine Monitoring
  DisplayName: Virtual Machine Monitoring (DCOM-In)
  Enabled: 2
  FirewallAction: 2
  Group: '@icsvc.dll,-700'
  LocalAddress:
  - Any
  LocalPort:
  - '135'
  LocalUser: Any
  Name: vm-monitoring-dcom
  Profile: 0
  Program: '%SystemRoot%\system32\svchost.exe'
  Protocol: TCP
  RemoteAddress:
  - Any
  RemoteMachine: Any
  RemotePort:
  - Any
  RemoteUser: Any
  RuleDescription: Allow DCOM traffic for remote Windows Management Instrumentation.
  Service: RpcSs
- Action: present
  DisplayGroup: Virtual Machine Monitoring
  DisplayName: Virtual Machine Monitoring (Echo Request - ICMPv4-In)
  Enabled: 2
  FirewallAction: 2
  Group: '@icsvc.dll,-700'
  LocalAddress:
  - Any
  LocalPort:
  - Any
  LocalUser: Any
  Name: vm-monitoring-icmpv4
  Profile: 0
  Program: Any
  Protocol: ICMPv4
  RemoteAddress:
  - Any
  RemoteMachine: Any
  RemotePort:
  - Any
  RemoteUser: Any
  RuleDescription: Echo Request messages are sent as ping requests to other nodes.
  Service: Any
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
    │         └── WIN_NetFirewallRule_Inbound/
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
    - role: OS-Windows2016/WIN_NetFirewallRule_Inbound/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NetFirewallRule_Inbound/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetFirewallRule_Inbound.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_NetFirewallRule_Inbound/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetFirewallRule_Inbound.yml  # パラメータ
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
