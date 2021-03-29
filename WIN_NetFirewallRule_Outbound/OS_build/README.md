Ansible Role: OS-Windows2016/WIN_NetFirewallRule_Outbound/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するファイアウォール設定（送信規則）についての情報の設定を行います。

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
OS-Windows2016/WIN_NetFirewallRule_Outbound/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetFirewallRule_Outbound` |     | 
| `- DisplayName:` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Name` | DisplayNameのOS内情報 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RuleDescription` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」「各ファイアウォールの受診の規則のプロパティ」「全般」の「説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DisplayGroup` |「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「グループ」に該当 <br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Group` | DisplayGroupのOS内情報<br>※構築では送信規則の新規作成時にのみ使用し、更新時には使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Enabled` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「有効」に該当<br>1 ： はい<br>2 ： いいえ | 
| &nbsp;&nbsp;&nbsp;&nbsp;`FirewallAction` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「操作」に該当<br>2 ： 許可<br>4 ： 不許可 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Profile` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「プロファイル」に該当<br>0 ： すべて<br>1 ： ドメイン<br>2 ： プライベート<br>3 ： ドメイン、プライベート<br>4 ： パブリック<br>5 ： ドメイン、パブリック<br>6 ： プライベート、パブリック<br>7 ： ドメイン、プライベート、パブリック | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalUser` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」「各ファイアウォールの受診の規則のプロパティ」「ローカル プリンシパル」の「承認されているユーザー」に該当 <br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalAddress` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「ローカルアドレス」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LocalPort` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「ローカルポート」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteUser` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」「各ファイアウォールの受診の規則のプロパティ」「リモートユーザー」の「承認されているユーザー」に該当 <br>※構築で使用しない |  
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteAddress` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「リモートアドレス」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemotePort` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「リモートポート」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`RemoteMachine` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」「各ファイアウォールの受診の規則のプロパティ」「リモートコンピューター」の「承認されているコンピューター」に該当 <br>※構築で使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Program` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「プログラム」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Protocol` |「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」の「プロトコル」に該当<br>※任意の場合はAny | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Service` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「送信の規則」「各ファイアウォールの受診の規則のプロパティ」「プログラムおよびサービス」「サービス」の設定ボタン押下、「サービス設定のカスタマイズ」で設定したサービスに該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Action` | 構築時の設定<br>present：作成、更新<br>absent：削除 | 

### Example
~~~
WIN_NetFirewallRule_Outbound:
- Action: present
  DisplayGroup: Windows Media Player
  DisplayName: Windows Media Player x86 (UDP-Out)
  Enabled: 2
  FirewallAction: 2
  Group: '@FirewallAPI.dll,-31002'
  LocalAddress:
  - Any
  LocalPort:
  - Any
  LocalUser: Any
  Name: WMP-Out-UDP-x86
  Profile: 0
  Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
  Protocol: UDP
  RemoteAddress:
  - Any
  RemoteMachine: Any
  RemotePort:
  - Any
  RemoteUser: Any
  RuleDescription: Outbound rule for Windows Media Player to allow UDP Media Streaming. [UDP]
  Service: Any
- Action: present
  DisplayGroup: Windows Media Player
  DisplayName: Windows Media Player x86 (TCP-Out)
  Enabled: 2
  FirewallAction: 2
  Group: '@FirewallAPI.dll,-31002'
  LocalAddress:
  - Any
  LocalPort:
  - Any
  LocalUser: Any
  Name: WMP-Out-TCP-x86
  Profile: 0
  Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
  Protocol: TCP
  RemoteAddress:
  - Any
  RemoteMachine: Any
  RemotePort:
  - Any
  RemoteUser: Any
  RuleDescription: Outbound rule for Windows Media Player to allow TCP/HTTP Media Streaming. [TCP]
  Service: Any
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
    │         └── WIN_NetFirewallRule_Outbound/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetFirewallRule_Outbound_adapter_absent.yml
    │                   │      build_NetFirewallRule_Outbound_adapter_present.yml
    │                   │      build_NetFirewallRule_Outbound_adapter.yml
    │                   │      build_NetFirewallRule_Outbound_item.yml
    │                   │      build_NetFirewallRule_Outbound.yml
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
    - role: OS-Windows2016/WIN_NetFirewallRule_Outbound/OS_build
      WIN_NetFirewallRule_Outbound:
      - Action: present
        DisplayGroup: Windows Media Player
        DisplayName: Windows Media Player x86 (UDP-Out)
        Enabled: 2
        FirewallAction: 2
        Group: '@FirewallAPI.dll,-31002'
        LocalAddress:
        - Any
        LocalPort:
        - Any
        LocalUser: Any
        Name: WMP-Out-UDP-x86
        Profile: 0
        Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
        Protocol: UDP
        RemoteAddress:
        - Any
        RemoteMachine: Any
        RemotePort:
        - Any
        RemoteUser: Any
        RuleDescription: Outbound rule for Windows Media Player to allow UDP Media Streaming. [UDP]
        Service: Any
      - Action: present
        DisplayGroup: Windows Media Player
        DisplayName: Windows Media Player x86 (TCP-Out)
        Enabled: 2
        FirewallAction: 2
        Group: '@FirewallAPI.dll,-31002'
        LocalAddress:
        - Any
        LocalPort:
        - Any
        LocalUser: Any
        Name: WMP-Out-TCP-x86
        Profile: 0
        Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
        Protocol: TCP
        RemoteAddress:
        - Any
        RemoteMachine: Any
        RemotePort:
        - Any
        RemoteUser: Any
        RuleDescription: Outbound rule for Windows Media Player to allow TCP/HTTP Media Streaming. [TCP]
        Service: Any
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
    - role: OS-Windows2016/WIN_NetFirewallRule_Outbound/OS_build
      WIN_NetFirewallRule_Outbound:
      - Action: present
        DisplayGroup: Windows Media Player
        DisplayName: Windows Media Player x86 (UDP-Out)
        Enabled: 2
        FirewallAction: 2
        Group: '@FirewallAPI.dll,-31002'
        LocalAddress:
        - Any
        LocalPort:
        - Any
        LocalUser: Any
        Name: WMP-Out-UDP-x86
        Profile: 0
        Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
        Protocol: UDP
        RemoteAddress:
        - Any
        RemoteMachine: Any
        RemotePort:
        - Any
        RemoteUser: Any
        RuleDescription: Outbound rule for Windows Media Player to allow UDP Media Streaming. [UDP]
        Service: Any
      - Action: present
        DisplayGroup: Windows Media Player
        DisplayName: Windows Media Player x86 (TCP-Out)
        Enabled: 2
        FirewallAction: 2
        Group: '@FirewallAPI.dll,-31002'
        LocalAddress:
        - Any
        LocalPort:
        - Any
        LocalUser: Any
        Name: WMP-Out-TCP-x86
        Profile: 0
        Program: '%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe'
        Protocol: TCP
        RemoteAddress:
        - Any
        RemoteMachine: Any
        RemotePort:
        - Any
        RemoteUser: Any
        RuleDescription: Outbound rule for Windows Media Player to allow TCP/HTTP Media Streaming. [TCP]
        Service: Any
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetFirewallRule_Outbound/OS_gathering
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
    │              └── WIN_NetFirewallRule_Outbound/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetFirewallRule_Outbound.yml
~~~

# Remarks
-------
パラメタ値がnullで設定を実行した際に、設定変更されたことを表すメッセージ「changed」が出力され、値に0が設定されますが、<br>
OSの動作としてはレジストリキーが存在しない場合と同等になります。<br>
本ロールの実行により値を変更したくない場合は、入力パラメタから値がnullのパラメタを手動で削除してください。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
