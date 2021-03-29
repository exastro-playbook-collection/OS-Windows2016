Ansible Role: OS-Windows2016/WIN_NetFirewallProfile/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するファイアウォール基本設定についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_NetFirewallProfile/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_NetFirewallProfile.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetFirewallProfile.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

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
| &nbsp;&nbsp;&nbsp;&nbsp;`LogMaxSizeKilobytes` | 「コントロール パネル」「すべてのコントロール パネル項目」「Windows ファイアウォール」「詳細設定」「セキュリティが強化されたWindows ファイアウォール」「Windows ファイアウォールのプロパティ」各プロファイルの「ログ」のカスタマイズボタン押下、「ドメイン　プロファイルのログのカスタマイズ」の「サイズ制限(KB)」に該当<br>※ 設定値は1～32767 | 

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

# Usage

本ロールの利用例について説明します。

## 既定値で設定情報収集およびパラメータ生成を行う場合

本ロールを"roles"ディレクトリに配置して、以下のようなPlaybookを作成してください。

- フォルダ構成

~~~
 - playbook/
    │── roles/
    │    └── OS-Windows2016
    │         └── WIN_NetFirewallProfile/
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
    - role: OS-Windows2016/WIN_NetFirewallProfile/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_NetFirewallProfile/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetFirewallProfile.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_NetFirewallProfile/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_NetFirewallProfile.yml  # パラメータ
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
