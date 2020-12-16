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
Windows Server 2016に関する情報の取得および設定を行うロールを提供します。

# OS用ロールを使うまでの前準備
OS用ロールを利用する前に、ターゲットマシン(管理対象サーバ)へ事前に実施してください。

## ターゲットマシンの条件
* PowerShell のバージョンが3以上であること
* WinRM での接続が許可されていること
* PowerShell のリモート実行が許可されていること
* 管理者グループに属したAnsibleからの接続用ユーザがあること

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
## 情報の取得に使用するロール一覧
情報の取得に使用する以下のロールを提供します。

| ロール名 | Description | 
| ------- | ----------- | 
| [WIN_ALL/OS_gathering](WIN_ALL/OS_gathering) | OS情報一括設定 | 
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
| [WIN_UserAccount/OS_gathering](WIN_UserAccount/OS_gathering) | ローカルユーザ | 
| [WIN_VolumeSetting/OS_gathering](WIN_VolumeSetting/OS_gathering) | ディスク管理 | 
| [WIN_WindowsFeature/OS_gathering](WIN_WindowsFeature/OS_gathering) | サーバの役割と機能 | 

## 情報の設定に使用するロール一覧
情報の設定に使用する以下のロールを提供します。

| ロール名                            | Description                      | 
| ----------------------------------- | -------------------------------- | 
| [WIN_ALL/OS_build](WIN_ALL/OS_build) | OS情報一括設定 | 
| [WIN_AutoShareServer/OS_build](WIN_AutoShareServer/OS_build) | 管理共有設定 | 
| [WIN_ComponentService/OS_build](WIN_ComponentService/OS_build) | コンポーネントサービス設定 | 
| [WIN_ComputerSetting/OS_build](WIN_ComputerSetting/OS_build) | Windows基本設定(コンピューター名) | 
| [WIN_Defender/OS_build](WIN_Defender/OS_build) | WindowsDefender設定 | 
| [WIN_DeviceInstallSetting/OS_build](WIN_DeviceInstallSetting/OS_build) | デバイスインストール設定 | 
| [WIN_DirectorySetting/OS_build](WIN_DirectorySetting/OS_build) | ディレクトリ設定 | 
| [WIN_EnvSetting/OS_build](WIN_EnvSetting/OS_build) | 環境変数 | 
| [WIN_ErrorReporting/OS_build](WIN_ErrorReporting/OS_build) | エラーレポーティング設定 | 
| [WIN_EventLog/OS_build](WIN_EventLog/OS_build) | イベントログ | 
| [WIN_Group/OS_build](WIN_Group/OS_build) | ローカルグループ | 
| [WIN_GroupPolicy/OS_build](WIN_GroupPolicy/OS_build) | ローカルグループポリシー | 
| [WIN_Hosts/OS_build](WIN_Hosts/OS_build) | hosts設定 | 
| [WIN_HotFix/OS_build](WIN_HotFix/OS_build) | 更新プログラム一覧 | 
| [WIN_NetAdapterBinding/OS_build](WIN_NetAdapterBinding/OS_build) | ネットワーク接続の詳細設定 | 
| [WIN_NetFirewallProfile/OS_build](WIN_NetFirewallProfile/OS_build) | ファイアウォール基本設定 | 
| [WIN_NetIpAddress/OS_build](WIN_NetIpAddress/OS_build) | ネットワーク基本情報 | 
| [WIN_NetIPv4Protocol/OS_build](WIN_NetIPv4Protocol/OS_build) | IPv4の設定 | 
| [WIN_NetIPv6Protocol/OS_build](WIN_NetIPv6Protocol/OS_build) | IPv6の設定 | 
| [WIN_NetOffloadGlobalSetting/OS_build](WIN_NetOffloadGlobalSetting/OS_build) | TCPの設定 | 
| [WIN_NetworkDrive/OS_build](WIN_NetworkDrive/OS_build) | ネットワークドライブ設定 | 
| [WIN_NetworkManagement/OS_build](WIN_NetworkManagement/OS_build) | ネットワーク管理 | 
| [WIN_NtpClientSetting/OS_build](WIN_NtpClientSetting/OS_build) | 時刻同期（Windows Timeサービス） | 
| [WIN_OSRecoveryConfiguration/OS_build](WIN_OSRecoveryConfiguration/OS_build) | Windows詳細情報（起動と回復）| 
| [WIN_PagefileSetting/OS_build](WIN_PagefileSetting/OS_build) | 仮想メモリ設計 | 
| [WIN_ProcessorScheduling/OS_build](WIN_ProcessorScheduling/OS_build) | プロセッサスケジュール（パフォーマンスオプション） | 
| [WIN_RemoteDesktop/OS_build](WIN_RemoteDesktop/OS_build) | リモートデスクトップ設定 | 
| [WIN_SecurityPolicy/OS_build](WIN_SecurityPolicy/OS_build) | ローカルセキュリティポリシー | 
| [WIN_UserAccount/OS_build](WIN_UserAccount/OS_build) | ローカルユーザ | 
| [WIN_WindowsFeature/OS_build](WIN_WindowsFeature/OS_build) | サーバの役割と機能 | 

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
