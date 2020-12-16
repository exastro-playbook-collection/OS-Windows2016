Ansible Role: OS-Windows2016/WIN_NtpClientSetting/OS_build
=======================================================
# Description
本ロールは、Windows Server 2016に関する時刻同期（Windows Timeサービス）についての情報の設定を行います。

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
OS-Windows2016/WIN_NtpClientSetting/OS_gatheringロールを利用します。

# Role Variables

本ロールで指定できる変数値について説明します。

## Mandatory Variables

ロール利用時に以下の変数値を指定する必要があります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_NtpClientSetting` |     | 
| `- Key` | レジストリパス | 
| &nbsp;&nbsp;&nbsp;&nbsp;`Values` |  | 
| &nbsp;&nbsp;&nbsp;&nbsp;`- ValueName` | レジストリ名 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`ValueType` | レジストリ種別 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Value` | レジストリ値 | 

### Example
~~~
VAR_WIN_NtpClientSetting:
- Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpClient
  Values:
  - Value: 1
    ValueName: AllowNonstandardModeCombinations
    ValueType: REG_DWORD
  - Value: 2147483648
    ValueName: CompatibilityFlags
    ValueType: REG_DWORD
  ・・・
- Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Parameters
  Values:
  - Value: 192.168.0.1,0x9
    ValueName: NtpServer
    ValueType: REG_SZ
  - Value: C:\Windows\system32\w32time.dll
    ValueName: ServiceDll
    ValueType: REG_EXPAND_SZ
  ・・・
- Key: HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config
  Values:
  - Value: 10
    ValueName: AnnounceFlags
    ValueType: REG_DWORD
  - Value: 2
    ValueName: EventLogFlags
    ValueType: REG_DWORD
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
    │         └── WIN_NtpClientSetting/
    │              └── OS_build/
    │                   │── meta/
    │                   │      main.yml
    │                   │── tasks/
    │                   │      build_NtpClientSetting.yml
    │                   │      build_NtpClientSetting_item.yml
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
    - role: OS-Windows2016/WIN_NtpClientSetting/OS_build
      VAR_WIN_NtpClientSetting:
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpClient
        Values:
        - Value: 1
          ValueName: AllowNonstandardModeCombinations
          ValueType: REG_DWORD
        - Value: 2147483648
          ValueName: CompatibilityFlags
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Parameters
        Values:
        - Value: 192.168.0.1,0x9
          ValueName: NtpServer
          ValueType: REG_SZ
        - Value: C:\Windows\system32\w32time.dll
          ValueName: ServiceDll
          ValueType: REG_EXPAND_SZ
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config
        Values:
        - Value: 10
          ValueName: AnnounceFlags
          ValueType: REG_DWORD
        - Value: 2
          ValueName: EventLogFlags
          ValueType: REG_DWORD
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
    - role: OS-Windows2016/WIN_NtpClientSetting/OS_build
      VAR_WIN_NtpClientSetting:
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\TimeProviders\NtpClient
        Values:
        - Value: 1
          ValueName: AllowNonstandardModeCombinations
          ValueType: REG_DWORD
        - Value: 2147483648
          ValueName: CompatibilityFlags
          ValueType: REG_DWORD
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\services\W32Time\Parameters
        Values:
        - Value: 192.168.0.1,0x9
          ValueName: NtpServer
          ValueType: REG_SZ
        - Value: C:\Windows\system32\w32time.dll
          ValueName: ServiceDll
          ValueType: REG_EXPAND_SZ
        ・・・
      - Key: HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config
        Values:
        - Value: 10
          ValueName: AnnounceFlags
          ValueType: REG_DWORD
        - Value: 2
          ValueName: EventLogFlags
          ValueType: REG_DWORD
        ・・・
  strategy: free

- hosts: all
  gather_facts: true
  roles:
    - role: OS-Windows2016/WIN_NtpClientSetting/OS_gathering
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
    │              └── WIN_NtpClientSetting/
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/
                        WIN_NtpClientSetting.yml
~~~

# Remarks
-------
レジストリ種別がREG_MULTI_SZの場合でかつ、Valueの配列に対して空文字列が含まれていた場合、設定時にエラーとなります。<br>
Valueの配列より空文字列を削除して設定を行うようにしてください。<br>
取得パラメタの値によっては、時間経過で動的に値が変わるものがあり、設定変更されたことを表すメッセージ「changed」が出力されますが、<br>
設定後自動的に戻るため影響はないものになります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
