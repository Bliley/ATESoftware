<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="24008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Testing.vi" Type="VI" URL="../Testing.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="instr.lib" Type="Folder">
				<Item Name="Abort.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Abort.vi"/>
				<Item Name="Agilent 532XX Series.lvlib" Type="Library" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Agilent 532XX Series.lvlib"/>
				<Item Name="Clear Register .vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Utility/Clear Register .vi"/>
				<Item Name="Close.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Close.vi"/>
				<Item Name="Configure Channel (Auto Threshold Voltage).vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Channel (Auto Threshold Voltage).vi"/>
				<Item Name="Configure Channel.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Channel.vi"/>
				<Item Name="Configure Frequency Burst Gate.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Frequency Burst Gate.vi"/>
				<Item Name="Configure Frequency Gate.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Frequency Gate.vi"/>
				<Item Name="Configure Gate External Source.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Gate External Source.vi"/>
				<Item Name="Configure Gate Start.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Gate Start.vi"/>
				<Item Name="Configure Gate Stop.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Gate Stop.vi"/>
				<Item Name="Configure Histogram.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Calculate/Configure Histogram.vi"/>
				<Item Name="Configure Limit.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Calculate/Configure Limit.vi"/>
				<Item Name="Configure Measurement (Burst).vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Measurement/Configure Measurement (Burst).vi"/>
				<Item Name="Configure Measurement.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Measurement/Configure Measurement.vi"/>
				<Item Name="Configure Roscillator.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Roscillator.vi"/>
				<Item Name="Configure Sample Count.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Sample Count.vi"/>
				<Item Name="Configure Scale.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Calculate/Configure Scale.vi"/>
				<Item Name="Configure Smoothing.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Calculate/Configure Smoothing.vi"/>
				<Item Name="Configure Statistics.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Calculate/Configure Statistics.vi"/>
				<Item Name="Configure Time Interval Gate.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Time Interval Gate.vi"/>
				<Item Name="Configure Timestamp Rate.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Timestamp Rate.vi"/>
				<Item Name="Configure Totalize Gate.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Totalize Gate.vi"/>
				<Item Name="Configure Trigger.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Configure/Configure Trigger.vi"/>
				<Item Name="Error Query.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Utility/Error Query.vi"/>
				<Item Name="Fetch Histogram.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Fetch Histogram.vi"/>
				<Item Name="Fetch Limit Test Result.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Fetch Limit Test Result.vi"/>
				<Item Name="Fetch Measurement (Single).vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Fetch Measurement (Single).vi"/>
				<Item Name="Fetch Measurement.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Fetch Measurement.vi"/>
				<Item Name="Initialize.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Initialize.vi"/>
				<Item Name="Initiate.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Initiate.vi"/>
				<Item Name="Read Histogram.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Read Histogram.vi"/>
				<Item Name="Read Limit Test Result.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Read Limit Test Result.vi"/>
				<Item Name="Read Measurement (Single).vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Read Measurement (Single).vi"/>
				<Item Name="Read Measurement.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Read Measurement.vi"/>
				<Item Name="Reset.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Utility/Reset.vi"/>
				<Item Name="Revision Query.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Utility/Revision Query.vi"/>
				<Item Name="Rohde&amp;Schwarz Power Meter.lvlib" Type="Library" URL="/&lt;instrlib&gt;/Rohde&amp;Schwarz Power Meter/Rohde&amp;Schwarz Power Meter.lvlib"/>
				<Item Name="Self-Test.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Utility/Self-Test.vi"/>
				<Item Name="Wait for Acquisition Complete.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Wait for Acquisition Complete.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Delimited String to 1D String Array.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Delimited String to 1D String Array.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="GOOP Object Repository Method.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Method.ctl"/>
				<Item Name="GOOP Object Repository Statistics.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Statistics.ctl"/>
				<Item Name="GOOP Object Repository.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="NI_Database_API.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/database/NI_Database_API.lvlib"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Select Event Type.ctl" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/Select Event Type.ctl"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Trim Whitespace One-Sided.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace One-Sided.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
			</Item>
			<Item Name="ADODBCommand CreateOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBCommand CreateOF.vi"/>
			<Item Name="ADODBCommand DestroyOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBCommand DestroyOF.vi"/>
			<Item Name="ADODBCommand ExecuteOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBCommand ExecuteOF.vi"/>
			<Item Name="ADODBCommand Set Active ConnectionOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBCommand Set Active ConnectionOF.vi"/>
			<Item Name="ADODBCommand Set Command TextOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBCommand Set Command TextOF.vi"/>
			<Item Name="ADODBConnection CloseOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBConnection CloseOF.vi"/>
			<Item Name="ADODBConnection CreateOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBConnection CreateOF.vi"/>
			<Item Name="ADODBConnection DestroyOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBConnection DestroyOF.vi"/>
			<Item Name="ADODBConnection ExecuteOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBConnection ExecuteOF.vi"/>
			<Item Name="ADODBConnection OpenOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBConnection OpenOF.vi"/>
			<Item Name="ADODBField Get String ValueOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBField Get String ValueOF.vi"/>
			<Item Name="ADODBFields Get CountOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBFields Get CountOF.vi"/>
			<Item Name="ADODBFields ItemOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBFields ItemOF.vi"/>
			<Item Name="ADODBRecordset DestroyOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBRecordset DestroyOF.vi"/>
			<Item Name="ADODBRecordset Get FieldsOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBRecordset Get FieldsOF.vi"/>
			<Item Name="ADODBRecordset Get Row String ValueOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBRecordset Get Row String ValueOF.vi"/>
			<Item Name="ADODBRecordset Get Table String ValueOF.vi" Type="VI" URL="../SQLToolkitOF.llb/ADODBRecordset Get Table String ValueOF.vi"/>
			<Item Name="Agilent 532XX Series.lvlib" Type="Library" URL="../Agilent 532XX Series/Agilent 532XX Series.lvlib"/>
			<Item Name="Arduino Command Builder.vi" Type="VI" URL="../Arduino Command Builder.vi"/>
			<Item Name="Databse State Checker Testing.vi" Type="VI" URL="../Databse State Checker Testing.vi"/>
			<Item Name="Frequency Counter Waveform.vi" Type="VI" URL="../Frequency Counter Waveform.vi"/>
			<Item Name="FVT.vi" Type="VI" URL="../FVT.vi"/>
			<Item Name="OscTest.vi" Type="VI" URL="../OscTest.vi"/>
			<Item Name="Output Powers Saving.vi" Type="VI" URL="../Output Powers Saving.vi"/>
			<Item Name="Output Powers.vi" Type="VI" URL="../Output Powers.vi"/>
			<Item Name="PHN.vi" Type="VI" URL="../PHN.vi"/>
			<Item Name="Read Saunders Temperature.vi" Type="VI" URL="../../Amazon Parts/Sub-VIs/Read Saunders Temperature.vi"/>
			<Item Name="Set Temperature and Rise Time.vi" Type="VI" URL="../../Amazon Parts/Sub-VIs/Set Temperature and Rise Time.vi"/>
			<Item Name="SQL CloseOF.vi" Type="VI" URL="../SQLToolkitOF.llb/SQL CloseOF.vi"/>
			<Item Name="SQL ExecuteOF.vi" Type="VI" URL="../SQLToolkitOF.llb/SQL ExecuteOF.vi"/>
			<Item Name="SQL OpenOF.vi" Type="VI" URL="../SQLToolkitOF.llb/SQL OpenOF.vi"/>
			<Item Name="SQL SelectOF.vi" Type="VI" URL="../SQLToolkitOF.llb/SQL SelectOF.vi"/>
			<Item Name="Tek PS2520G Check Volt and Current24.vi" Type="VI" URL="../Tek PS2520G Check Volt and Current24.vi"/>
			<Item Name="Tek PS2520G Configure Supply24.vi" Type="VI" URL="../Tek PS2520G Configure Supply24.vi"/>
			<Item Name="Testing Functional Test.vi" Type="VI" URL="../Testing Functional Test.vi"/>
			<Item Name="Testing Run.vi" Type="VI" URL="../Testing Run.vi"/>
			<Item Name="TimeToSeconds.vi" Type="VI" URL="../TimeToSeconds.vi"/>
			<Item Name="TKPS252XG Close24.vi" Type="VI" URL="../TKPS252XG Close24.vi"/>
			<Item Name="TKPS252XG Configure Current-Voltage24.vi" Type="VI" URL="../TKPS252XG Configure Current-Voltage24.vi"/>
			<Item Name="TKPS252XG Configure OVP-OCP24.vi" Type="VI" URL="../TKPS252XG Configure OVP-OCP24.vi"/>
			<Item Name="TKPS252XG Initialize24.vi" Type="VI" URL="../TKPS252XG Initialize24.vi"/>
			<Item Name="TKPS252XG Output on-off24.vi" Type="VI" URL="../TKPS252XG Output on-off24.vi"/>
			<Item Name="TKPS252XG Read Current-Voltage24.vi" Type="VI" URL="../TKPS252XG Read Current-Voltage24.vi"/>
			<Item Name="TKPS252XG Reset24.vi" Type="VI" URL="../TKPS252XG Reset24.vi"/>
			<Item Name="Turn Saunders Chamber Off.vi" Type="VI" URL="../../Amazon Parts/Sub-VIs/Turn Saunders Chamber Off.vi"/>
			<Item Name="Update DatabaseF.vi" Type="VI" URL="../Update DatabaseF.vi"/>
			<Item Name="Update DatabaseO.vi" Type="VI" URL="../Update DatabaseO.vi"/>
			<Item Name="Update DatabaseP.vi" Type="VI" URL="../Update DatabaseP.vi"/>
			<Item Name="Warmup Saving.vi" Type="VI" URL="../Warmup Saving.vi"/>
			<Item Name="Warmup.vi" Type="VI" URL="../Warmup.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Testing" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{0E30408B-2832-4C06-A8D4-8205A2C5E276}</Property>
				<Property Name="App_INI_GUID" Type="Str">{BB96621E-07E4-4918-B886-13DFE737E9BF}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{AD901AD4-06D5-4436-BB07-9F143CAB3DA7}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Testing</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Testing</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{5C61B780-B532-4AF1-A519-E5E27CD1C090}</Property>
				<Property Name="Bld_version.build" Type="Int">39</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Testing.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Testing/Testing.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Testing/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{9F1FB8D3-9654-487B-9988-0C1FED7FBA93}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Testing.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Testing</Property>
				<Property Name="TgtF_internalName" Type="Str">Testing</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2023 Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_productName" Type="Str">Testing</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{A4319A23-29C3-4E07-9BF6-9C1F51347E6B}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Testing.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
