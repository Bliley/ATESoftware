<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="23008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Control Panel.vi" Type="VI" URL="../Control Panel.vi"/>
		<Item Name="Old Aging.vi" Type="VI" URL="../Old Aging.vi"/>
		<Item Name="Functional Test.vi" Type="VI" URL="../Functional Test.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
			</Item>
			<Item Name="Close HP3488A Switcher(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/Close HP3488A Switcher(GPIB).vi"/>
			<Item Name="Convert Oscillator Position to HP3488A Channel Command.vi" Type="VI" URL="../Bliley Switcher Library.llb/Convert Oscillator Position to HP3488A Channel Command.vi"/>
			<Item Name="HP3488A Close Channels(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/HP3488A Close Channels(GPIB).vi"/>
			<Item Name="HP3488A Close(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/HP3488A Close(GPIB).vi"/>
			<Item Name="HP3488A Delay(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/HP3488A Delay(GPIB).vi"/>
			<Item Name="HP3488A Display Card Monitor(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/HP3488A Display Card Monitor(GPIB).vi"/>
			<Item Name="HP3488A Initialize(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/HP3488A Initialize(GPIB).vi"/>
			<Item Name="HP3488A Reset(GPIB).vi" Type="VI" URL="../Bliley Switcher Library.llb/HP3488A Reset(GPIB).vi"/>
			<Item Name="HP53131 Measure Frequency.vi" Type="VI" URL="../HP53131 Measure Frequency.vi"/>
			<Item Name="Position Adding.vi" Type="VI" URL="../Position Adding.vi"/>
			<Item Name="Serial Number Entering.vi" Type="VI" URL="../Serial Number Entering.vi"/>
			<Item Name="Verify Serial Number.vi" Type="VI" URL="../Verify Serial Number.vi"/>
			<Item Name="Position Removing.vi" Type="VI" URL="../Position Removing.vi"/>
			<Item Name="Aging System Summary.vi" Type="VI" URL="../Aging System Summary.vi"/>
			<Item Name="SQL OpenMC.vi" Type="VI" URL="../SQLToolkit.llb/SQL OpenMC.vi"/>
			<Item Name="ADODBConnection CreateMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBConnection CreateMC.vi"/>
			<Item Name="ADODBConnection OpenMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBConnection OpenMC.vi"/>
			<Item Name="SQL ExecuteMC.vi" Type="VI" URL="../SQLToolkit.llb/SQL ExecuteMC.vi"/>
			<Item Name="ADODBCommand CreateMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBCommand CreateMC.vi"/>
			<Item Name="ADODBCommand Set Active ConnectionMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBCommand Set Active ConnectionMC.vi"/>
			<Item Name="ADODBCommand Set Command TextMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBCommand Set Command TextMC.vi"/>
			<Item Name="ADODBCommand ExecuteMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBCommand ExecuteMC.vi"/>
			<Item Name="ADODBRecordset DestroyMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBRecordset DestroyMC.vi"/>
			<Item Name="ADODBCommand DestroyMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBCommand DestroyMC.vi"/>
			<Item Name="SQL CloseMC.vi" Type="VI" URL="../SQLToolkit.llb/SQL CloseMC.vi"/>
			<Item Name="ADODBConnection CloseMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBConnection CloseMC.vi"/>
			<Item Name="ADODBConnection DestroyMC.vi" Type="VI" URL="../SQLToolkit.llb/ADODBConnection DestroyMC.vi"/>
			<Item Name="Database Saver.vi" Type="VI" URL="../Database Saver.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Control Panel" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{14ABA97C-FCA5-44E2-845C-423F09863B51}</Property>
				<Property Name="App_INI_GUID" Type="Str">{F88ACF7F-245E-489C-AC58-62A528CEC88B}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{EA3D9680-A595-498E-8288-CC4C643B6881}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Control Panel</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Control Panel</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{9F96CA1E-BFF3-42F9-A4DF-8B72E698C206}</Property>
				<Property Name="Bld_version.build" Type="Int">9</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Main Controls.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Control Panel/Main Controls.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Control Panel/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{9B4A132E-6C77-49DC-BF66-A3A3E1CA6B99}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Control Panel.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Control Panel</Property>
				<Property Name="TgtF_internalName" Type="Str">Control Panel</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2024 </Property>
				<Property Name="TgtF_productName" Type="Str">Control Panel</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{BB1A83E2-D318-4819-88FB-3B6198FDA532}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Main Controls.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="Old Aging" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{507DBF5D-8D8E-408D-B59D-535E6B8110B6}</Property>
				<Property Name="App_INI_GUID" Type="Str">{F2F705F2-F566-4D8D-AD9C-B0B061DFF37C}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{562BFEA9-BBF6-48AD-90AE-724F9B8CFF9A}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Old Aging</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Old Aging</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{E481FE41-79B0-48E7-8D49-143BA0263516}</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">DAQ.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Old Aging/DAQ.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Old Aging/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{20806672-EF75-4F69-970A-F3A95BE56D15}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Old Aging.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Old Aging</Property>
				<Property Name="TgtF_internalName" Type="Str">Old Aging</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2024 </Property>
				<Property Name="TgtF_productName" Type="Str">Old Aging</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{27A26760-950B-41D6-A61C-5B045C1C9588}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">DAQ.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="Functional Test" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{2F0DA590-0023-4EC1-B24F-45FCCFCA214D}</Property>
				<Property Name="App_INI_GUID" Type="Str">{DA0F2900-5A06-4626-945D-781337861F75}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{86E7E6E0-4F7B-4ECC-B8F5-D54449DBE178}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Functional Test</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Functional Test</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{9602CB4E-EF09-4A7A-BAAE-5BAED70F0DBF}</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Functional Test.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Functional Test/Functional Test.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Functional Test/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{20806672-EF75-4F69-970A-F3A95BE56D15}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Functional Test.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Functional Test</Property>
				<Property Name="TgtF_internalName" Type="Str">Functional Test</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2024 </Property>
				<Property Name="TgtF_productName" Type="Str">Functional Test</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{502530F3-17AC-4497-BA4E-2DF66155EA6C}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Functional Test.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
