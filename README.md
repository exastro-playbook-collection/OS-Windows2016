OS-Windows2016
===============================
# Trademarks
-----------
* Linuxは、Linus Torvalds氏の米国およびその他の国における登録商標または商標です。
* RedHat、RHEL、CentOSは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* Windows、PowerShell、IIS、.NET Frameworkは、Microsoft Corporation の米国およびその他の国における登録商標または商標です。
* Ansibleは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* pythonは、Python Software Foundationの登録商標または商標です。
* NECは、日本電気株式会社の登録商標または商標です。
* その他、本ロールのコード、ファイルに記載されている会社名および製品名は、各社の登録商標または商標です。

# Description
-----------
Windows Server 2016に関する情報の収集および設定を行うためのロールを提供します。
情報の収集は、OS_gatheringロールを使って収集を行います。情報の設定は、OS_buildロールを使って設定を行います。
OS_gatheringで収集結果情報として出力されるyamlファイルのパラメタを編集し、OS_buildロールの設定情報として利用できます。
ソフトウェア製品向けロールと異なり、利用者が設定時に必要となるロールを適宜選択して設定を行ってください。
またOS全ての情報設定を行う事ができるわけではありませんので、設定に必要となるロールが提供されていない場合は、自作することをご検討ください。

-------------

## 注意
OS関連のロール利用は、パラメータ内容を十分に確認し、事前評価を行ってからご利用ください。パラメータ値が誤っていると、ターゲットマシンへのアクセスができなくなるなど、トラブルが発生する可能性があります。

-------------

# Specification

## Ansibleサーバ

* Ansible バージョン 2.7 以上 (動作確認バージョン 2.7, 2.9)
* Python バージョン 3.x  (動作確認バージョン 3.6)

# OS用ロールを使うまでの前準備
OS用ロールを利用する前に、ターゲットマシン(管理対象サーバ)へ事前に実施してください。

## ターゲットマシンの条件
* PowerShell のバージョンが3以上であること
* WinRM での接続が許可されていること
* PowerShell のリモート実行が許可されていること
* 管理者グループに属したAnsibleからの接続用ユーザーがあること

## WinRM の接続設定
Ansible-PJが公式に提供しているセットアップスクリプトでWinRMの接続設定を行います。

1. PowerShell を管理者権限で起動してください。
   * スタートメニューで[Windows PowerShell]アイコンを右クリックして「管理者として実行」でPowerShell を起動してください。
2. セットアップスクリプトのダウンロード
   * 以下のコマンドラインで、`ConfigureRemotingForAnsible.ps1` を入手します。

~~~
 PS C:\tmp> Invoke-WebRequest -Uri https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1 -OutFile ConfigureRemotingForAnsible.ps1
~~~

3. セットアップスクリプトを実行

~~~
 PS C:\tmp> powershell -ExecutionPolicy RemoteSigned .\ConfigureRemotingForAnsible.ps1
~~~


# 提供ロール一覧
## 情報取得ロール一覧
情報の取得に使用する以下のロールを提供します。

| ロール名 | Description | 
| ------- | ----------- | 
| [WIN_ALL/OS_gathering](WIN_ALL/OS_gathering) | OS情報一括取得 | 
| [WIN_AutoShareServer/OS_gathering](WIN_AutoShareServer/OS_gathering) | 管理共有設定 | 
| [WIN_ComponentService/OS_gathering](WIN_ComponentService/OS_gathering) | コンポーネントサービス設定 | 
| [WIN_ComputerSetting/OS_gathering](WIN_ComputerSetting/OS_gathering) | Windows基本設定（コンピューター名） | 
| [WIN_DataCollectorSet/OS_gathering](WIN_DataCollectorSet/OS_gathering) | データコレクタ | 
| [WIN_Defender/OS_gathering](WIN_Defender/OS_gathering) | WindowsDefender設定 | 
| [WIN_DeviceInstallSetting/OS_gathering](WIN_DeviceInstallSetting/OS_gathering) | デバイスインストール設定 | 
| [WIN_DeviceManager/OS_gathering](WIN_DeviceManager/OS_gathering) | デバイスのシステム状態 | 
| [WIN_DirectorySetting/OS_gathering](WIN_DirectorySetting/OS_gathering) | ディレクトリ設定 | 
| [WIN_EnvSetting/OS_gathering](WIN_EnvSetting/OS_gathering) | 環境変数 | 
| [WIN_ErrorReporting/OS_gathering](WIN_ErrorReporting/OS_gathering) | エラーレポーティング設定 | 
| [WIN_EventLog/OS_gathering](WIN_EventLog/OS_gathering) | イベントログ | 
| [WIN_FileProtectionSetting/OS_gathering](WIN_FileProtectionSetting/OS_gathering) | ファイル保護設定 | 
| [WIN_Group/OS_gathering](WIN_Group/OS_gathering) | ローカルグループ | 
| [WIN_GroupPolicy/OS_gathering](WIN_GroupPolicy/OS_gathering) | ローカルグループポリシー | 
| [WIN_Hosts/OS_gathering](WIN_Hosts/OS_gathering) | hosts設定 | 
| [WIN_HotFix/OS_gathering](WIN_HotFix/OS_gathering) | 更新プログラム一覧 | 
| [WIN_InstallPP/OS_gathering](WIN_InstallPP/OS_gathering) | インストールプログラム一覧 | 
| [WIN_NetAdapterAdvancedProperty/OS_gathering](WIN_NetAdapterAdvancedProperty/OS_gathering) | ネットワークアダプタ詳細設定 | 
| [WIN_NetAdapterBinding/OS_gathering](WIN_NetAdapterBinding/OS_gathering) | ネットワーク接続の詳細設定 | 
| [WIN_NetAdapterConfiguration/OS_gathering](WIN_NetAdapterConfiguration/OS_gathering) | ネットワークアダプタ設定 | 
| [WIN_NetFirewallProfile/OS_gathering](WIN_NetFirewallProfile/OS_gathering) | ファイアウォール基本設定 | 
| [WIN_NetFirewallRule_Inbound/OS_gathering](WIN_NetFirewallRule_Inbound/OS_gathering) | ファイアウォール設定（受信規則） | 
| [WIN_NetFirewallRule_Outbound/OS_gathering](WIN_NetFirewallRule_Outbound/OS_gathering) | ファイアウォール設定（送信規則） | 
| [WIN_NetIpAddress/OS_gathering](WIN_NetIpAddress/OS_gathering) | ネットワーク基本情報 | 
| [WIN_NetIPv4Protocol/OS_gathering](WIN_NetIPv4Protocol/OS_gathering) | IPv4の設定 | 
| [WIN_NetIPv6Protocol/OS_gathering](WIN_NetIPv6Protocol/OS_gathering) | IPv6の設定 | 
| [WIN_NetOffloadGlobalSetting/OS_gathering](WIN_NetOffloadGlobalSetting/OS_gathering) | TCPの設定 | 
| [WIN_NetworkDrive/OS_gathering](WIN_NetworkDrive/OS_gathering) | ネットワークドライブ設定 | 
| [WIN_NetworkManagement/OS_gathering](WIN_NetworkManagement/OS_gathering) | ネットワーク管理 | 
| [WIN_NICTeaming_Team/OS_gathering](WIN_NICTeaming_Team/OS_gathering) | NICチーミング設定（チーム） | 
| [WIN_NICTeaming_VLAN/OS_gathering](WIN_NICTeaming_VLAN/OS_gathering) | NICチーミング設定（VLAN） | 
| [WIN_NtpClientSetting/OS_gathering](WIN_NtpClientSetting/OS_gathering) | 時刻同期（Windows Timeサービス） | 
| [WIN_OSRecoveryConfiguration/OS_gathering](WIN_OSRecoveryConfiguration/OS_gathering) | Windows詳細情報（起動と回復） | 
| [WIN_PagefileSetting/OS_gathering](WIN_PagefileSetting/OS_gathering) | 仮想メモリ設計 | 
| [WIN_PartitionSetting/OS_gathering](WIN_PartitionSetting/OS_gathering) | PartitionSetting | 
| [WIN_PrinterInfo/OS_gathering](WIN_PrinterInfo/OS_gathering) | プリンタ―情報 | 
| [WIN_ProcessorScheduling/OS_gathering](WIN_ProcessorScheduling/OS_gathering) | プロセッサスケジュール（パフォーマンスオプション） | 
| [WIN_RemoteDesktop/OS_gathering](WIN_RemoteDesktop/OS_gathering) | リモートデスクトップ設定 | 
| [WIN_SecurityPolicy/OS_gathering](WIN_SecurityPolicy/OS_gathering) | ローカルセキュリティポリシー | 
| [WIN_Services/OS_gathering](WIN_Services/OS_gathering) | Windowsサービス | 
| [WIN_SharedFolder/OS_gathering](WIN_SharedFolder/OS_gathering) | 共有フォルダ設定 | 
| [WIN_SNMPService/OS_gathering](WIN_SNMPService/OS_gathering) | SNMPService | 
| [WIN_StartUp/OS_gathering](WIN_StartUp/OS_gathering) | スタートアップのプログラム起動 | 
| [WIN_UserAccount/OS_gathering](WIN_UserAccount/OS_gathering) | ローカルユーザー | 
| [WIN_VolumeSetting/OS_gathering](WIN_VolumeSetting/OS_gathering) | ディスク管理 | 
| [WIN_WindowsFeature/OS_gathering](WIN_WindowsFeature/OS_gathering) | サーバの役割と機能 | 

## 情報取得ロールのマニュアル一覧
各ロールで情報取得可能なパラメータは、以下の各ロールのマニュアル内のResultセクションに記載されたものとなります。

| 情報取得ロールのマニュアル | 
| ------- |  
| [WIN_AutoShareServer/OS_gathering マニュアル](WIN_AutoShareServer/OS_gathering/README.md) | 
| [WIN_ComponentService/OS_gathering マニュアル](WIN_ComponentService/OS_gathering/README.md) | 
| [WIN_ComputerSetting/OS_gathering マニュアル](WIN_ComputerSetting/OS_gathering/README.md) | 
| [WIN_DataCollectorSet/OS_gathering マニュアル](WIN_DataCollectorSet/OS_gathering/README.md) | 
| [WIN_Defender/OS_gathering マニュアル](WIN_Defender/OS_gathering/README.md) | 
| [WIN_DeviceInstallSetting/OS_gathering マニュアル](WIN_DeviceInstallSetting/OS_gathering/README.md) | 
| [WIN_DeviceManager/OS_gathering マニュアル](WIN_DeviceManager/OS_gathering/README.md) | 
| [WIN_DirectorySetting/OS_gathering マニュアル](WIN_DirectorySetting/OS_gathering/README.md) | 
| [WIN_EnvSetting/OS_gathering マニュアル](WIN_EnvSetting/OS_gathering/README.md) | 
| [WIN_ErrorReporting/OS_gathering マニュアル](WIN_ErrorReporting/OS_gathering/README.md) | 
| [WIN_EventLog/OS_gathering マニュアル](WIN_EventLog/OS_gathering/README.md) | 
| [WIN_FileProtectionSetting/OS_gathering マニュアル](WIN_FileProtectionSetting/OS_gathering/README.md) | 
| [WIN_Group/OS_gathering マニュアル](WIN_Group/OS_gathering/README.md) | 
| [WIN_GroupPolicy/OS_gathering マニュアル](WIN_GroupPolicy/OS_gathering/README.md) | 
| [WIN_Hosts/OS_gathering マニュアル](WIN_Hosts/OS_gathering/README.md) | 
| [WIN_HotFix/OS_gathering マニュアル](WIN_HotFix/OS_gathering/README.md) | 
| [WIN_InstallPP/OS_gathering マニュアル](WIN_InstallPP/OS_gathering/README.md) | 
| [WIN_NetAdapterAdvancedProperty/OS_gathering マニュアル](WIN_NetAdapterAdvancedProperty/OS_gathering/README.md) | 
| [WIN_NetAdapterBinding/OS_gathering マニュアル](WIN_NetAdapterBinding/OS_gathering/README.md) | 
| [WIN_NetAdapterConfiguration/OS_gathering マニュアル](WIN_NetAdapterConfiguration/OS_gathering/README.md) |  
| [WIN_NetFirewallProfile/OS_gathering マニュアル](WIN_NetFirewallProfile/OS_gathering/README.md) |  
| [WIN_NetFirewallRule_Inbound/OS_gathering マニュアル](WIN_NetFirewallRule_Inbound/OS_gathering/README.md) | 
| [WIN_NetFirewallRule_Outbound/OS_gathering マニュアル](WIN_NetFirewallRule_Outbound/OS_gathering/README.md) | 
| [WIN_NetIpAddress/OS_gathering マニュアル](WIN_NetIpAddress/OS_gathering/README.md) | 
| [WIN_NetIPv4Protocol/OS_gathering マニュアル](WIN_NetIPv4Protocol/OS_gathering/README.md) | 
| [WIN_NetIPv6Protocol/OS_gathering マニュアル](WIN_NetIPv6Protocol/OS_gathering/README.md) | 
| [WIN_NetOffloadGlobalSetting/OS_gathering マニュアル](WIN_NetOffloadGlobalSetting/OS_gathering/README.md) | 
| [WIN_NetworkDrive/OS_gathering マニュアル](WIN_NetworkDrive/OS_gathering/README.md) |  
| [WIN_NetworkManagement/OS_gathering マニュアル](WIN_NetworkManagement/OS_gathering/README.md) | 
| [WIN_NICTeaming_Team/OS_gathering マニュアル](WIN_NICTeaming_Team/OS_gathering/README.md) | 
| [WIN_NICTeaming_VLAN/OS_gathering マニュアル](WIN_NICTeaming_VLAN/OS_gathering/README.md) | 
| [WIN_NtpClientSetting/OS_gathering マニュアル](WIN_NtpClientSetting/OS_gathering/README.md) |  
| [WIN_OSRecoveryConfiguration/OS_gathering マニュアル](WIN_OSRecoveryConfiguration/OS_gathering/README.md) | 
| [WIN_PagefileSetting/OS_gathering マニュアル](WIN_PagefileSetting/OS_gathering/README.md) | 
| [WIN_PartitionSetting/OS_gathering マニュアル](WIN_PartitionSetting/OS_gathering/README.md) | 
| [WIN_PrinterInfo/OS_gathering マニュアル](WIN_PrinterInfo/OS_gathering/README.md) | 
| [WIN_ProcessorScheduling/OS_gathering マニュアル](WIN_ProcessorScheduling/OS_gathering/README.md) |  
| [WIN_RemoteDesktop/OS_gathering マニュアル](WIN_RemoteDesktop/OS_gathering/README.md) | 
| [WIN_SecurityPolicy/OS_gathering マニュアル](WIN_SecurityPolicy/OS_gathering/README.md) | 
| [WIN_Services/OS_gathering マニュアル](WIN_Services/OS_gathering/README.md) | 
| [WIN_SharedFolder/OS_gathering マニュアル](WIN_SharedFolder/OS_gathering/README.md) | 
| [WIN_SNMPService/OS_gathering マニュアル](WIN_SNMPService/OS_gathering/README.md) | 
| [WIN_StartUp/OS_gathering マニュアル](WIN_StartUp/OS_gathering/README.md) | 
| [WIN_UserAccount/OS_gathering マニュアル](WIN_UserAccount/OS_gathering/README.md) | 
| [WIN_VolumeSetting/OS_gathering マニュアル](WIN_VolumeSetting/OS_gathering/README.md) | 
| [WIN_WindowsFeature/OS_gathering マニュアル](WIN_WindowsFeature/OS_gathering/README.md) 

## WIN_ALL/OS_gathering(OS情報一括取得)の情報取得ロール確認方法
WIN_ALL/OS_gathering(OS情報一括取得)ロールで情報取得を行うデフォルトのロールは、下記ファイルのコメントされていないロールとなります。

| ファイル名                            |
| ----------------------------------- |
| [WIN_ALL/OS_gathering/defaults/main.yml](WIN_ALL/OS_gathering/defaults/main.yml) |

## 情報設定ロール一覧
情報の設定に使用する以下のロールを提供します。

| ロール名                            | Description                      | 
| ----------------------------------- | -------------------------------- | 
| [WIN_ALL/OS_build](WIN_ALL/OS_build) | OS情報一括設定 | 
| [WIN_AutoShareServer/OS_build](WIN_AutoShareServer/OS_build) | 管理共有設定 | 
| [WIN_ComponentService/OS_build](WIN_ComponentService/OS_build) | コンポーネントサービス設定 | 
| [WIN_ComputerSetting/OS_build](WIN_ComputerSetting/OS_build) | Windows基本設定(コンピューター名) | 
| [WIN_DataCollectorSet/OS_build](WIN_DataCollectorSet/OS_build) | データコレクタ | 
| [WIN_Defender/OS_build](WIN_Defender/OS_build) | WindowsDefender設定 | 
| [WIN_DeviceInstallSetting/OS_build](WIN_DeviceInstallSetting/OS_build) | デバイスインストール設定 | 
| [WIN_DirectorySetting/OS_build](WIN_DirectorySetting/OS_build) | ディレクトリ設定 | 
| [WIN_EnvSetting/OS_build](WIN_EnvSetting/OS_build) | 環境変数 | 
| [WIN_ErrorReporting/OS_build](WIN_ErrorReporting/OS_build) | エラーレポーティング設定 | 
| [WIN_EventLog/OS_build](WIN_EventLog/OS_build) | イベントログ | 
| [WIN_FileProtectionSetting/OS_build](WIN_FileProtectionSetting/OS_build) | ファイル保護設定 | 
| [WIN_Group/OS_build](WIN_Group/OS_build) | ローカルグループ | 
| [WIN_GroupPolicy/OS_build](WIN_GroupPolicy/OS_build) | ローカルグループポリシー | 
| [WIN_Hosts/OS_build](WIN_Hosts/OS_build) | hosts設定 | 
| [WIN_HotFix/OS_build](WIN_HotFix/OS_build) | 更新プログラム一覧 | 
| [WIN_NetAdapterAdvancedProperty/OS_build](WIN_NetAdapterAdvancedProperty/OS_build) | ネットワークアダプタ詳細設定 | 
| [WIN_NetAdapterBinding/OS_build](WIN_NetAdapterBinding/OS_build) | ネットワーク接続の詳細設定 | 
| [WIN_NetAdapterConfiguration/OS_build](WIN_NetAdapterConfiguration/OS_build) | ネットワークアダプタ設定 | 
| [WIN_NetFirewallProfile/OS_build](WIN_NetFirewallProfile/OS_build) | ファイアウォール基本設定 | 
| [WIN_NetFirewallRule_Inbound/OS_build](WIN_NetFirewallRule_Inbound/OS_build) | ファイアウォール設定（受信規則） | 
| [WIN_NetFirewallRule_Outbound/OS_build](WIN_NetFirewallRule_Outbound/OS_build) | ファイアウォール設定（送信規則） | 
| [WIN_NetIpAddress/OS_build](WIN_NetIpAddress/OS_build) | ネットワーク基本情報 | 
| [WIN_NetIPv4Protocol/OS_build](WIN_NetIPv4Protocol/OS_build) | IPv4の設定 | 
| [WIN_NetIPv6Protocol/OS_build](WIN_NetIPv6Protocol/OS_build) | IPv6の設定 | 
| [WIN_NetOffloadGlobalSetting/OS_build](WIN_NetOffloadGlobalSetting/OS_build) | TCPの設定 | 
| [WIN_NetworkDrive/OS_build](WIN_NetworkDrive/OS_build) | ネットワークドライブ設定 | 
| [WIN_NetworkManagement/OS_build](WIN_NetworkManagement/OS_build) | ネットワーク管理 | 
| [WIN_NICTeaming_Team/OS_build](WIN_NICTeaming_Team/OS_build) | NICチーミング設定（チーム） | 
| [WIN_NICTeaming_VLAN/OS_build](WIN_NICTeaming_VLAN/OS_build) | NICチーミング設定（VLAN） | 
| [WIN_NtpClientSetting/OS_build](WIN_NtpClientSetting/OS_build) | 時刻同期（Windows Timeサービス） | 
| [WIN_OSRecoveryConfiguration/OS_build](WIN_OSRecoveryConfiguration/OS_build) | Windows詳細情報（起動と回復）| 
| [WIN_PagefileSetting/OS_build](WIN_PagefileSetting/OS_build) | 仮想メモリ設計 | 
| [WIN_ProcessorScheduling/OS_build](WIN_ProcessorScheduling/OS_build) | プロセッサスケジュール（パフォーマンスオプション） | 
| [WIN_RemoteDesktop/OS_build](WIN_RemoteDesktop/OS_build) | リモートデスクトップ設定 | 
| [WIN_SecurityPolicy/OS_build](WIN_SecurityPolicy/OS_build) | ローカルセキュリティポリシー | 
| [WIN_Services/OS_build](WIN_Services/OS_build) | Windowsサービス | 
| [WIN_UserAccount/OS_build](WIN_UserAccount/OS_build) | ローカルユーザー | 
| [WIN_WindowsFeature/OS_build](WIN_WindowsFeature/OS_build) | サーバの役割と機能 | 

## 情報設定ロールのマニュアル一覧
各ロールで情報設定可能なパラメータは、以下の各ロールのマニュアル内のRole Variablesセクションに記載されたものとなります。

| 情報設定ロールのマニュアル | 
| ------- |  
| [WIN_AutoShareServer/OS_build マニュアル](WIN_AutoShareServer/OS_build/README.md) | 
| [WIN_ComponentService/OS_build マニュアル](WIN_ComponentService/OS_build/README.md) | 
| [WIN_ComputerSetting/OS_build マニュアル](WIN_ComputerSetting/OS_build/README.md) | 
| [WIN_DataCollectorSet/OS_build マニュアル](WIN_DataCollectorSet/OS_build/README.md) | 
| [WIN_Defender/OS_build マニュアル](WIN_Defender/OS_build/README.md) | 
| [WIN_DeviceInstallSetting/OS_build マニュアル](WIN_DeviceInstallSetting/OS_build/README.md) | 
| [WIN_DirectorySetting/OS_build マニュアル](WIN_DirectorySetting/OS_build/README.md) | 
| [WIN_EnvSetting/OS_build マニュアル](WIN_EnvSetting/OS_build/README.md) | 
| [WIN_ErrorReporting/OS_build マニュアル](WIN_ErrorReporting/OS_build/README.md) | 
| [WIN_EventLog/OS_build マニュアル](WIN_EventLog/OS_build/README.md) | 
| [WIN_FileProtectionSetting/OS_build マニュアル](WIN_FileProtectionSetting/OS_build/README.md) | 
| [WIN_Group/OS_build マニュアル](WIN_Group/OS_build/README.md) | 
| [WIN_GroupPolicy/OS_build マニュアル](WIN_GroupPolicy/OS_build/README.md) | 
| [WIN_Hosts/OS_build マニュアル](WIN_Hosts/OS_build/README.md) | 
| [WIN_HotFix/OS_build マニュアル](WIN_HotFix/OS_build/README.md) | 
| [WIN_NetAdapterAdvancedProperty/OS_build マニュアル](WIN_NetAdapterAdvancedProperty/OS_build/README.md) | 
| [WIN_NetAdapterBinding/OS_build マニュアル](WIN_NetAdapterBinding/OS_build/README.md) | 
| [WIN_NetAdapterConfiguration/OS_build マニュアル](WIN_NetAdapterConfiguration/OS_build/README.md) | 
| [WIN_NetFirewallProfile/OS_build マニュアル](WIN_NetFirewallProfile/OS_build/README.md) | 
| [WIN_NetFirewallRule_Inbound/OS_build マニュアル](WIN_NetFirewallRule_Inbound/OS_build/README.md) | 
| [WIN_NetFirewallRule_Outbound/OS_build マニュアル](WIN_NetFirewallRule_Outbound/OS_build/README.md) | 
| [WIN_NetIpAddress/OS_build マニュアル](WIN_NetIpAddress/OS_build/README.md) | 
| [WIN_NetIPv4Protocol/OS_build マニュアル](WIN_NetIPv4Protocol/OS_build/README.md) | 
| [WIN_NetIPv6Protocol/OS_build マニュアル](WIN_NetIPv6Protocol/OS_build/README.md) | 
| [WIN_NetOffloadGlobalSetting/OS_build マニュアル](WIN_NetOffloadGlobalSetting/OS_build/README.md) | 
| [WIN_NetworkDrive/OS_build マニュアル](WIN_NetworkDrive/OS_build/README.md) | 
| [WIN_NetworkManagement/OS_build マニュアル](WIN_NetworkManagement/OS_build/README.md) | 
| [WIN_NICTeaming_Team/OS_build マニュアル](WIN_NICTeaming_Team/OS_build/README.md) | 
| [WIN_NICTeaming_VLAN/OS_build マニュアル](WIN_NICTeaming_VLAN/OS_build/README.md) | 
| [WIN_NtpClientSetting/OS_build マニュアル](WIN_NtpClientSetting/OS_build/README.md) | 
| [WIN_OSRecoveryConfiguration/OS_build マニュアル](WIN_OSRecoveryConfiguration/OS_build/README.md) | 
| [WIN_PagefileSetting/OS_build マニュアル](WIN_PagefileSetting/OS_build/README.md) | 
| [WIN_ProcessorScheduling/OS_build マニュアル](WIN_ProcessorScheduling/OS_build/README.md) | 
| [WIN_RemoteDesktop/OS_build マニュアル](WIN_RemoteDesktop/OS_build/README.md) | 
| [WIN_SecurityPolicy/OS_build マニュアル](WIN_SecurityPolicy/OS_build/README.md) | 
| [WIN_Services/OS_build マニュアル](WIN_Services/OS_build/README.md) | 
| [WIN_UserAccount/OS_build マニュアル](WIN_UserAccount/OS_build/README.md) | 
| [WIN_WindowsFeature/OS_build マニュアル](WIN_WindowsFeature/OS_build/README.md) | 

## WIN_ALL/OS_build(OS情報一括設定)の情報設定ロール確認方法
WIN_ALL/OS_build(OS情報一括設定)ロールで情報設定を行うデフォルトのロールは、下記ファイルのコメントされていないロールとなります。

| ファイル名                            |
| ----------------------------------- |
| [WIN_ALL/OS_build/defaults/main.yml](WIN_ALL/OS_build/defaults/main.yml) |

# Remarks
-------
OS仕様に依存する情報の設定ロールでは、実行は成功するが設定したパラメタが反映されない場合があります。

# License
-------

# Copyright
---------
Copyright (c) 2020 NEC Corporation

# Author Information
------------------
NEC Corporation
