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
		<Item Name="FVT (New Counter).vi" Type="VI" URL="../FVT (New Counter).vi"/>
		<Item Name="FVT.vi" Type="VI" URL="../FVT.vi"/>
		<Item Name="Moveover.vi" Type="VI" URL="../../Moveover.vi"/>
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
				<Item Name="Self-Test.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Utility/Self-Test.vi"/>
				<Item Name="Wait for Acquisition Complete.vi" Type="VI" URL="/&lt;instrlib&gt;/Agilent 532XX Series/Public/Data/Low Level/Wait for Acquisition Complete.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Dynamic To Waveform Array.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Dynamic To Waveform Array.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="FormatTime String.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/FormatTime String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="subBuildXYGraph.vi" Type="VI" URL="/&lt;vilib&gt;/express/express controls/BuildXYGraphBlock.llb/subBuildXYGraph.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="subElapsedTime.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/ElapsedTimeBlock.llb/subElapsedTime.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Trim Whitespace One-Sided.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace One-Sided.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Waveform Array To Dynamic.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/transition.llb/Waveform Array To Dynamic.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
			</Item>
			<Item Name="ADODBCommand CreateMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBCommand CreateMC.vi"/>
			<Item Name="ADODBCommand DestroyMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBCommand DestroyMC.vi"/>
			<Item Name="ADODBCommand ExecuteMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBCommand ExecuteMC.vi"/>
			<Item Name="ADODBCommand Set Active ConnectionMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBCommand Set Active ConnectionMC.vi"/>
			<Item Name="ADODBCommand Set Command TextMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBCommand Set Command TextMC.vi"/>
			<Item Name="ADODBConnection CloseMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBConnection CloseMC.vi"/>
			<Item Name="ADODBConnection CreateMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBConnection CreateMC.vi"/>
			<Item Name="ADODBConnection DestroyMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBConnection DestroyMC.vi"/>
			<Item Name="ADODBConnection OpenMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBConnection OpenMC.vi"/>
			<Item Name="ADODBRecordset DestroyMC.vi" Type="VI" URL="../SQLToolkitMC.llb/ADODBRecordset DestroyMC.vi"/>
			<Item Name="Agilent 532XX Series.lvlib" Type="Library" URL="../Agilent 532XX Series/Agilent 532XX Series.lvlib"/>
			<Item Name="Close HP3488A Switcher(GPIB).vi" Type="VI" URL="../TempRun2023.llb/Close HP3488A Switcher(GPIB).vi"/>
			<Item Name="Convert Oscillator Position to HP3488A Channel Command.vi" Type="VI" URL="../TempRun2023.llb/Convert Oscillator Position to HP3488A Channel Command.vi"/>
			<Item Name="Database Sending.vi" Type="VI" URL="../Database Sending.vi"/>
			<Item Name="DC_SN Verification.vi" Type="VI" URL="../DC_SN Verification.vi"/>
			<Item Name="HP3488A Close Channels(GPIB).vi" Type="VI" URL="../TempRun2023.llb/HP3488A Close Channels(GPIB).vi"/>
			<Item Name="HP3488A Close(GPIB).vi" Type="VI" URL="../TempRun2023.llb/HP3488A Close(GPIB).vi"/>
			<Item Name="HP3488A Delay(GPIB).vi" Type="VI" URL="../TempRun2023.llb/HP3488A Delay(GPIB).vi"/>
			<Item Name="HP3488A Display Card Monitor(GPIB).vi" Type="VI" URL="../TempRun2023.llb/HP3488A Display Card Monitor(GPIB).vi"/>
			<Item Name="HP3488A Initialize(GPIB).vi" Type="VI" URL="../TempRun2023.llb/HP3488A Initialize(GPIB).vi"/>
			<Item Name="HP3488A Reset(GPIB).vi" Type="VI" URL="../TempRun2023.llb/HP3488A Reset(GPIB).vi"/>
			<Item Name="HP53131 Measure Frequency2023.vi" Type="VI" URL="../HP53131 Measure Frequency2023.vi"/>
			<Item Name="Parameter Setup( Single Functional).vi" Type="VI" URL="../Parameter Setup( Single Functional).vi"/>
			<Item Name="Parameter Setup(Functional).vi" Type="VI" URL="../Parameter Setup(Functional).vi"/>
			<Item Name="Parameter Setup.vi" Type="VI" URL="../Parameter Setup.vi"/>
			<Item Name="Read Saunders Temperature2023.vi" Type="VI" URL="../Read Saunders Temperature2023.vi"/>
			<Item Name="Serial Numbers.vi" Type="VI" URL="../Serial Numbers.vi"/>
			<Item Name="Set Temperature and Rise Time2023.vi" Type="VI" URL="../Set Temperature and Rise Time2023.vi"/>
			<Item Name="SQL CloseMC.vi" Type="VI" URL="../SQLToolkitMC.llb/SQL CloseMC.vi"/>
			<Item Name="SQL ExecuteMC.vi" Type="VI" URL="../SQLToolkitMC.llb/SQL ExecuteMC.vi"/>
			<Item Name="SQL OpenMC.vi" Type="VI" URL="../SQLToolkitMC.llb/SQL OpenMC.vi"/>
			<Item Name="Warmup.vi" Type="VI" URL="../Warmup.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="FVT" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{103ABC7E-0E92-4535-9A1B-8C5B18761E0F}</Property>
				<Property Name="App_INI_GUID" Type="Str">{BAAEF8AF-995D-4EAC-B000-71CD6D645964}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{9DE54265-FB48-4F2C-8734-23E9555C1395}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">FVT</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/FVT</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{4FC60DB1-153B-4E51-88B1-B166DE10F672}</Property>
				<Property Name="Bld_version.build" Type="Int">102</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">FVT.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/FVT/FVT.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/FVT/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{323D1589-7152-4132-9735-C18A96F9890F}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/FVT.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">FVT</Property>
				<Property Name="TgtF_internalName" Type="Str">FVT</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2023 </Property>
				<Property Name="TgtF_productName" Type="Str">FVT</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{CEC240A2-EDB9-46B4-A833-6A585C37BBE6}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">FVT.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="FVT_New Counter" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{0CCC16B8-A67F-4419-822A-4053F3198EB3}</Property>
				<Property Name="App_INI_GUID" Type="Str">{A45B23D1-BDE0-40B8-BEDC-60942E2D42D5}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{28D9D23A-B33F-4C48-9B52-4AB25FA0F5CF}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">FVT_New Counter</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/FVT (New Counter)</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{7B7B496F-3BAE-4610-9573-F5800388A9B3}</Property>
				<Property Name="Bld_version.build" Type="Int">2</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">FVT.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/FVT (New Counter)/FVT.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/FVT (New Counter)/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{7A4DB371-3F04-4604-9F56-BD88D27FCDC4}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/FVT (New Counter).vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">FVT_New Counter</Property>
				<Property Name="TgtF_internalName" Type="Str">FVT_New Counter</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2024 Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_productName" Type="Str">FVT_New Counter</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{C319B49F-0DB3-4243-B2D3-4CCA9F0800E2}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">FVT.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
