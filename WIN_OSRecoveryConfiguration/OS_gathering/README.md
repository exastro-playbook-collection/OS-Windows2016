Ansible Role: OS-Windows2016/WIN_OSRecoveryConfiguration/OS_gathering
=======================================================
# Description
本ロールは、Windows Server 2016に関するWindows詳細情報（起動と回復）についての情報の取得を行います。

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

- `<VAR_OS_gathering_dest>/<ホスト名/IP>/OS/WIN_OSRecoveryConfiguration/`

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

- `<VAR_extracting_dest>/<ホスト名/IP>/OS/WIN_OSRecoveryConfiguration.yml`

本ロールを既定値で利用した場合、以下のようにパラメータを出力します。

- 構成は以下のとおり

~~~
 - playbook/
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_OSRecoveryConfiguration.yml  # パラメータ
~~~

パラメータとして出力される情報は以下となります。

| Name | Description | 
| ---- | ----------- | 
| `VAR_WIN_OSRecoveryConfiguration` |     | 
| &nbsp;&nbsp;&nbsp;&nbsp;`BootSystem` | 起動と回復 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`default` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「起動システム」の「既定のオペレーティングシステム」に該当<br>ブートエントリの識別子を設定する。ブートエントリの識別子は、「bcdedit」または「bcdedit /v」コマンドで出力される、ブート構成データ (BCD)」の「Windowsブートローダー」-「identifier」の値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`timeout` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「起動システム」の「オペレーティングシステムの一覧を表示する時間」に該当<br>該当の設定項目で入力できる数値 | 
| &nbsp;&nbsp;&nbsp;&nbsp;`SystemError` | システムエラー | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AutoReboot` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「自動的に再起動する」のチェックボックスに該当<br>true ： 自動的に再起動する<br>false ： 自動的に再起動しない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DebugInfoType` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「デバッグ情報の書き込み」に該当<br>0 ： なし<br>1 ： 完全メモリ ダンプ/アクティブメモリダンプ<br>2 ： カーネル メモリ ダンプ<br>3 ： 最小メモリ ダンプ (64KB)<br>7 ： 自動メモリ ダンプ | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`FilterPages` | DebugInfoTypeで完全メモリ/アクティブメモリを設定した場合に設定する<br>1<br>※ 完全メモリダンプ/アクティブメモリダンプを設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`DebugFilePath` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「ダンプファイル」に該当<br>DebugInfoTypeで完全メモリ ダンプ、アクティブメモリダンプ、カーネル メモリ ダンプ、自動メモリ ダンプを設定した際のダンプファイル出力先<br>※ 完全メモリ ダンプ、アクティブメモリダンプ、カーネル メモリ ダンプ、自動メモリ ダンプを設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MiniDumpDirectory` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「ダンプファイル」に該当<br>DebugInfoTypeで 最小メモリ ダンプ (64KB)を設定した際のダンプファイル出力先<br>※  最小メモリ ダンプ (64KB)を設定した場合は必須 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`OverwriteExistingDebugFile` |「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「既存のファイルに上書きする」に該当<br>true ： 上書きする<br>false ： 上書きしない | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`AlwaysKeepMemoryDump` | 「コントロール パネル」「すべてのコントロール パネル項目」「システム」「システムのプロパティ」「詳細設定」の「起動と回復」の設定を押下、「システムエラー」の「ディスク領域が少ないときでもメモリダンプの自動削除を無効にする」のチェックボックスに該当<br>1 ： 無効にする<br>1以外の数字(0など) ： 無効にしない | 

### Example
~~~
VAR_WIN_OSRecoveryConfiguration:
  BootSystem:
    default: '{0daf9bba-94c8-11e6-b1fd-0e5bdc9ce43b}'
    timeout: '30'
  SystemError:
    AlwaysKeepMemoryDump: null
    AutoReboot: true
    DebugFilePath: '%SystemRoot%\MEMORY.DMP'
    DebugInfoType: 7
    FilterPages: null
    MiniDumpDirectory: '%SystemRoot%\Minidump'
    OverwriteExistingDebugFile: true
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
    │         └── WIN_OSRecoveryConfiguration/
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
    - role: OS-Windows2016/WIN_OSRecoveryConfiguration/OS_gathering
  strategy: free
~~~

- 以下のように設定情報とパラメータを出力します。
  格納される情報の詳細は、Resultの項目を確認してください。

~~~
 - playbook/
    │── _gathered_data/
    │    └── 管理対象マシンホスト名 or IPアドレス/
    │         └── OS/
    │              └── WIN_OSRecoveryConfiguration/  # 収集データ
    │                   │── command/
    │                   │      ・・・
    │                   └── file/
    │                          ・・・
    └── _parameters/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_OSRecoveryConfiguration.yml  # パラメータ
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
    - role: OS-Windows2016/WIN_OSRecoveryConfiguration/OS_build
  strategy: free
~~~

- パラメータを格納

~~~
 - playbook/
    └── host_vars/
            └── 管理対象マシンホスト名 or IPアドレス/
                 └── OS/  # OS設定ロール向け専用のフォルダ
                        WIN_OSRecoveryConfiguration.yml  # パラメータ
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
