Ansible Role: OS-Windows2016/WIN_NetFirewallProfile/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するファイアウォール基本設定についての情報の設定を行います。

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
OS-Windows2016/WIN_NetFirewallProfile/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NetFirewallProfile` |     | 
| `- Name` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」の各プロファイル | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Enabled` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「ファイアウォールの状態」に該当<br>1 ： 有効<br>0 ： 無効 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AllowInboundRules` | 各プロファイルのファイアウォールの受信規則の設定<br>1 ： 受信規則が有効<br>0 ： 受信規則が無効<br>2 ： 既定値 or グループポリシーの設定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultInboundAction` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「受信接続」に該当<br>0 ： 既定値 or グループポリシーの設定<br>2 ： 許可<br>4 ： ブロック | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DefaultOutboundAction` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「送信接続」に該当<br>0 ： 既定値 or グループポリシーの設定<br>2 ： 許可<br>4 ： ブロック | 
| &nbsp;&nbsp;&nbsp;&nbsp;`NotifyOnListen` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「設定」のカスタマイズボタン押下、「ドメイン　プロファイルの設定のカスタマイズ」の「通知を表示する」に該当<br>1 ： する<br>0 ： しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AllowUnicastResponseToMulticast` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「設定」のカスタマイズボタン押下、「ドメイン　プロファイルの設定のカスタマイズ」「ユニキャスト応答」の「ユニキャスト応答の許可」に該当<br>1 ： 許可する<br>0 ： 許可しない<br>2 ： 既定値 or グループポリシーの設定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AllowLocalFirewallRules` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「設定」のカスタマイズボタン押下、「ドメイン　プロファイルの設定のカスタマイズ」「規則のマージ」の「ローカルファイアウォールの規則を適用する」に該当<br>1 ： 適用する<br>0 ： 適用しない<br>2 ： 既定値 or グループポリシーの設定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AllowLocalIPsecRules` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「設定」のカスタマイズボタン押下、「ドメイン　プロファイルの設定のカスタマイズ」「規則のマージ」の「ローカル接続のセキュリティ規則を適用する」に該当<br>1 ： 適用する<br>0 ： 適用しない<br>2 ： 既定値 or グループポリシーの設定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LogFileName` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「ログ」のカスタマイズボタン押下、「ドメイン　プロファイルのログのカスタマイズ」の「名前」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`LogMaxSizeKilobytes` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「ログ」のカスタマイズボタン押下、「ドメイン　プロファイルのログのカスタマイズ」の「サイズ制限(KB)」に該当<br>※ 設定値は1～32767 

### Example
~~~
VAR_WIN_NetFirewallProfile:
- AllowInboundRules: 2
  AllowLocalFirewallRules: 2
  AllowLocalIPsecRules: 2
  AllowUnicastResponseToMulticast: 2
  DefaultInboundAction: 0
  DefaultOutboundAction: 0
  Enabled: 1
  LogFileName: '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'
  LogMaxSizeKilobytes: 4096
  Name: Domain
  NotifyOnListen: 0
- AllowInboundRules: 2
  AllowLocalFirewallRules: 2
  AllowLocalIPsecRules: 2
  AllowUnicastResponseToMulticast: 2
  DefaultInboundAction: 0
  DefaultOutboundAction: 0
  Enabled: 1
  LogFileName: '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'
  LogMaxSizeKilobytes: 4096
  Name: Private
  NotifyOnListen: 0
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
    │         └── WIN_NetFirewallProfile/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_NetFirewallProfile.yml
    │                   │      build_NetFirewallProfile_each.yml
    │                   │      build_NetFirewallProfile_item.yml
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
    - role: OS-Windows2016/WIN_NetFirewallProfile/OS_build
      VAR_WIN_NetFirewallProfile:
      - AllowInboundRules: 2
        AllowLocalFirewallRules: 2
        AllowLocalIPsecRules: 2
        AllowUnicastResponseToMulticast: 2
        DefaultInboundAction: 0
        DefaultOutboundAction: 0
        Enabled: 1
        LogFileName: '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'
        LogMaxSizeKilobytes: 4096
        Name: Domain
        NotifyOnListen: 0
      - AllowInboundRules: 2
        AllowLocalFirewallRules: 2
        AllowLocalIPsecRules: 2
        AllowUnicastResponseToMulticast: 2
        DefaultInboundAction: 0
        DefaultOutboundAction: 0
        Enabled: 1
        LogFileName: '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'
        LogMaxSizeKilobytes: 4096
        Name: Private
        NotifyOnListen: 0
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
    - role: OS-Windows2016/WIN_NetFirewallProfile/OS_build
      VAR_WIN_NetFirewallProfile:
      - AllowInboundRules: 2
        AllowLocalFirewallRules: 2
        AllowLocalIPsecRules: 2
        AllowUnicastResponseToMulticast: 2
        DefaultInboundAction: 0
        DefaultOutboundAction: 0
        Enabled: 1
        LogFileName: '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'
        LogMaxSizeKilobytes: 4096
        Name: Domain
        NotifyOnListen: 0
      - AllowInboundRules: 2
        AllowLocalFirewallRules: 2
        AllowLocalIPsecRules: 2
        AllowUnicastResponseToMulticast: 2
        DefaultInboundAction: 0
        DefaultOutboundAction: 0
        Enabled: 1
        LogFileName: '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'
        LogMaxSizeKilobytes: 4096
        Name: Private
        NotifyOnListen: 0
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NetFirewallProfile/OS_gathering
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
    │              └── WIN_NetFirewallProfile/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NetFirewallProfile.yml
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
