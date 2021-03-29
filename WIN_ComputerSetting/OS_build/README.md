Ansible Role: OS-Windows2016/WIN_ComputerSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するWindows基本設定（コンピュータ名）についての情報の設定を行います。

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
OS-Windows2016/WIN_ComputerSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_ComputerSetting` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Description` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の「コンピュータの説明」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Name` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の「フルコンピュータ名」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DNSDomainSuffixSearchOrder` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の詳細ボタン押下、「DNSサフィックスとNETBIOSコンピュータ名」の「このコンピュータのプライマリDNSサフィックス」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SyncDomainWithMembership` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の詳細ボタン押下、「DNSサフィックスとNETBIOSコンピュータ名」の「ドメインが変更されるときに、プライマリDNSサフィックスを変更する」のチェックボックスに該当<br>0 ： ドメインが変更されるときに、プライマリDNSサフィックスを変更する<br>1 ： ドメインが変更されるときに、プライマリDNSサフィックスを変更しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainOrWorkgroup` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の「所属するグループ」に該当<br>true ：  ドメイン指定<br>false ： ワークグループ指定 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainOrWorkgroupName` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「コンピュータ名」の変更ボタン押下、「コンピュータ名/ドメイン名の変更」の「所属するグループ」のドメイン名／ワークグループ名に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainUser` | ドメイン指定時のドメインユーザー名<br>収集では取得されないため、ドメイン指定時には設定は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`DomainPassword` | ドメイン指定時のドメインユーザーのパスワード<br>収集では取得されないため、ドメイン指定時には設定は必須 | 

### Example
~~~
VAR_WIN_ComputerSetting:
  DNSDomainSuffixSearchOrder: ''
  Description: AWS Win2016-01 TEST
  DomainOrWorkgroup: false
  DomainOrWorkgroupName: WORKGROUP
  Name: EC2AMAZ-3FLM24H
  SyncDomainWithMembership: 1
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
    │         └── WIN_ComputerSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_Description.yml
    │                   │      build_DNSDomainSuffixSearchOrder.yml
    │                   │      build_DomainOrWorkgroup.yml
    │                   │      build_Name.yml
    │                   │      build_Registry_present.yml
    │                   │      build_SyncDomainWithMembership.yml
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
    - role: OS-Windows2016/WIN_ComputerSetting/OS_build
      VAR_WIN_ComputerSetting:
        DNSDomainSuffixSearchOrder: ''
        Description: AWS Win2016-01 TEST
        DomainOrWorkgroup: false
        DomainOrWorkgroupName: WORKGROUP
        Name: EC2AMAZ-3FLM24H
        SyncDomainWithMembership: 1
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
    - role: OS-Windows2016/WIN_ComputerSetting/OS_build
      VAR_WIN_ComputerSetting:
        DNSDomainSuffixSearchOrder: ''
        Description: AWS Win2016-01 TEST
        DomainOrWorkgroup: false
        DomainOrWorkgroupName: WORKGROUP
        Name: EC2AMAZ-3FLM24H
        SyncDomainWithMembership: 1
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_ComputerSetting/OS_gathering
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
    │              └── WIN_ComputerSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_ComputerSetting.yml
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
