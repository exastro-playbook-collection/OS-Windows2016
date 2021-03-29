Ansible Role: OS-Windows2016/WIN_WindowsFeature/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関するサーバーの役割と機能についての情報の設定を行います。

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
OS-Windows2016/WIN_WindowsFeature/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_WindowsFeature` |     | 
| `- Name` | 役割と機能の名称 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Value` | 「サーバーマネージャー」「ダッシュボード」「役割と機能の追加」「役割と機能の追加ウィザード」「サーバーの役割」の「役割のチェックボックス」に該当<br>true ： 対象の役割・機能をインストールする<br>false ： 対象の役割・機能をアンインストールする 

### Example
~~~
VAR_WIN_WindowsFeature:
- Name: AD-Certificate
  Value: false
- Name: ADCS-Cert-Authority
  Value: true
・・・
~~~


## Optional Variables

ロール利用時に以下の変数値を指定することができます。

| Name | Default Value | Description | 
| ---- | ------------- | ----------- | 
| `VAR_OS_build_include_management_tools` | true | 「サーバーマネージャー」「ダッシュボード」「役割と機能の追加」「役割と機能の追加ウィザード」「サーバーの役割」の「管理ツールを含める(存在する場合)」に該当<br>true ： 管理ツールを含める<br>false ： 管理ツールを含めない| 

# Usage

1. 本Roleを用いたPlaybookを作成します。
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
    │         └── WIN_WindowsFeature/
    │              └── OS_build/
    │                   │── default/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_WindowsFeature_item.yml
    │                   │      build_WindowsFeature.yml
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
    - role: OS-Windows2016/WIN_WindowsFeature/OS_build
      VAR_WIN_WindowsFeature:
      - Name: AD-Certificate
        Value: false
      - Name: ADCS-Cert-Authority
        Value: true
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
    - role: OS-Windows2016/WIN_WindowsFeature/OS_build
      VAR_WIN_WindowsFeature:
      - Name: AD-Certificate
        Value: false
      - Name: ADCS-Cert-Authority
        Value: true
      ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_WindowsFeature/OS_gathering
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
    │              └── WIN_WindowsFeature/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_WindowsFeature.yml
~~~

# Remarks
-------
サーバーの役割と機能では、関連する機能を一括でインストール、アンインストールを実施する機能があるため設定の際には注意が必要です。
例として一括で処理を行う機能はWCF Servicesなどがあります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
