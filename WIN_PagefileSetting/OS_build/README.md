Ansible Role: OS-Windows2016/WIN_PagefileSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関する仮想メモリ設計についての情報の設定を行います。

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
OS-Windows2016/WIN_PagefileSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_PagefileSetting` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`AutomaticManagedPagefile Setting` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AutomaticManagedPagefile` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「パフォーマンス」の設定を押下、「パフォーマンスオプション」「詳細設定」の「仮想メモリ」の変更を押下、「仮想メモリ」の「すべてのドライブのページングファイルのサイズを自動的に管理する」のチェックボックスに該当<br>true ： すべてのドライブのページングファイルのサイズを自動的に管理する<br>false  ： すべてのドライブのページングファイルのサイズを自動的に管理しない<br>※trueを設定した場合はDriveを設定できない | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Drive` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- DriveName` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「パフォーマンス」の設定を押下、「パフォーマンスオプション」「詳細設定」の「仮想メモリ」「各ドライブのページングファイルのサイズ」の「選択したドライブ」に該当 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`PageFileSettingType` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「パフォーマンス」の設定を押下、「パフォーマンスオプション」「詳細設定」の「仮想メモリ」「各ドライブのページングファイルのサイズ」の「ページングファイルサイズ」の選択に該当<br>CustomSize ： カスタムサイズ<br>SystemManagedSize ： システム管理サイズ<br>NoPagingfile ： ページングファイルなし | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Name` | ページファイルのパス情報<br>構築には使用しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`InitialSize` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「パフォーマンス」の設定を押下、「パフォーマンスオプション」「詳細設定」の「仮想メモリ」「各ドライブのページングファイルのサイズ」の「ページングファイルサイズ」「カスタムサイズ」の「初期サイズ」に該当<br>PageFileSettingTypeでCustomSize選択時 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MaximumSize` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「パフォーマンス」の設定を押下、「パフォーマンスオプション」「詳細設定」の「仮想メモリ」「各ドライブのページングファイルのサイズ」の「ページングファイルサイズ」「カスタムサイズ」の「最大サイズ」に該当<br>PageFileSettingTypeでCustomSize選択時 | 

### Example
~~~
VAR_WIN_PagefileSetting:
  AutomaticManagedPagefileSetting:
    AutomaticManagedPagefile: false
  Drive:
  - DriveName: 'c:'
    InitialSize: 1024
    MaximumSize: 2048
    Name: c:\pagefile.sys
    PageFileSettingType: CustomSize
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
    │         └── WIN_PagefileSetting/
    │              └── OS_build/
    │                   │── tasks/
    │                   │      build_AutomaticManagedPagefileSetting.yml
    │                   │      build_Drive_info.yml
    │                   │      build_Drive.yml
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
    - role: OS-Windows2016/WIN_PagefileSetting/OS_build
      VAR_WIN_PagefileSetting:
        AutomaticManagedPagefileSetting:
          AutomaticManagedPagefile: false
        Drive:
        - DriveName: 'c:'
          InitialSize: 1024
          MaximumSize: 2048
          Name: c:\pagefile.sys
          PageFileSettingType: CustomSize
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
    - role: OS-Windows2016/WIN_PagefileSetting/OS_build
      VAR_WIN_PagefileSetting:
        AutomaticManagedPagefileSetting:
          AutomaticManagedPagefile: false
        Drive:
        - DriveName: 'c:'
          InitialSize: 1024
          MaximumSize: 2048
          Name: c:\pagefile.sys
          PageFileSettingType: CustomSize
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_PagefileSetting/OS_gathering
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
    │              └── WIN_PagefileSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_PagefileSetting.yml
~~~

# Remarks
-------
仮想メモリ設計の設定の反映にはOS再起動が必要となります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
