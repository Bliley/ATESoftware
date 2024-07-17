<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="24008000">
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
		<Item Name="Data AcquisitionA.vi" Type="VI" URL="../Data AcquisitionA.vi"/>
		<Item Name="Initialize and Functional.vi" Type="VI" URL="../Initialize and Functional.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Delimited String to 1D String Array.vi" Type="VI" URL="/&lt;vilib&gt;/AdvancedString/Delimited String to 1D String Array.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="NI_Database_API.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/database/NI_Database_API.lvlib"/>
				<Item Name="GOOP Object Repository Method.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Method.ctl"/>
				<Item Name="GOOP Object Repository Statistics.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Statistics.ctl"/>
				<Item Name="GOOP Object Repository.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository.vi"/>
			</Item>
			<Item Name="Update DatabaseA.vi" Type="VI" URL="../Update DatabaseA.vi"/>
			<Item Name="Calculate Dynamic VariablesA.vi" Type="VI" URL="../Calculate Dynamic VariablesA.vi"/>
			<Item Name="HP53220 Measure FrequencyA.vi" Type="VI" URL="../HP53220 Measure FrequencyA.vi"/>
			<Item Name="Aging Run.vi" Type="VI" URL="../Aging Run.vi"/>
			<Item Name="Databse State Checker.vi" Type="VI" URL="../Databse State Checker.vi"/>
			<Item Name="Functional Test Aging.vi" Type="VI" URL="../Functional Test Aging.vi"/>
			<Item Name="Arduino Command Builder.vi" Type="VI" URL="../Arduino Command Builder.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="AgingDAQ" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{5BDCDD22-DD53-4849-A1DE-DC5C37E260F6}</Property>
				<Property Name="App_INI_GUID" Type="Str">{597F5288-8010-4E66-91C9-8CFDB166D42F}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{793BA83D-8564-462F-ABE9-9B7753C3D032}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">AgingDAQ</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Aging</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{1CFDB6D3-7757-4F34-BBBB-2F268A9ACC0C}</Property>
				<Property Name="Bld_version.build" Type="Int">42</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">AgingDAQ.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Aging/AgingDAQ.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Aging/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{D3BF3982-7CDB-4F49-87BF-01D3F41E12F7}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Data AcquisitionA.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">AgingDAQ</Property>
				<Property Name="TgtF_internalName" Type="Str">AgingDAQ</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2023 Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_productName" Type="Str">AgingDAQ</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{89D65B2B-B7DB-4541-BAC9-AA5A1D4A61FC}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">AgingDAQ.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="Aging" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{F7960038-0228-4D81-BFD0-439A8E7757A6}</Property>
				<Property Name="App_INI_GUID" Type="Str">{8A9DB3A3-9B80-4987-B317-D6C97C7E9954}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{40A921E0-5758-47D3-9EC2-D3470E3C4050}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Aging</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Aging</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{72D18FBE-8374-4891-A5DB-8127747F5BAA}</Property>
				<Property Name="Bld_version.build" Type="Int">33</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Aging.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Aging/Aging.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Aging/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{D3BF3982-7CDB-4F49-87BF-01D3F41E12F7}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Initialize and Functional.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Aging</Property>
				<Property Name="TgtF_internalName" Type="Str">Aging</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2023 Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_productName" Type="Str">Aging</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{0ADF98A3-0E46-4F37-A5D1-F1B966752356}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Aging.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
