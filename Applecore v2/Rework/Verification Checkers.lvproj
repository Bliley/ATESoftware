<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="23008000">
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
		<Item Name="Scrap.vi" Type="VI" URL="../Scrap.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="GOOP Object Repository Method.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Method.ctl"/>
				<Item Name="GOOP Object Repository Statistics.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository Statistics.ctl"/>
				<Item Name="GOOP Object Repository.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/_goopsup.llb/GOOP Object Repository.vi"/>
				<Item Name="NI_Database_API.lvlib" Type="Library" URL="/&lt;vilib&gt;/addons/database/NI_Database_API.lvlib"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
			</Item>
			<Item Name="ADODBCommand Create.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBCommand Create.vi"/>
			<Item Name="ADODBCommand Destroy.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBCommand Destroy.vi"/>
			<Item Name="ADODBCommand Execute.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBCommand Execute.vi"/>
			<Item Name="ADODBCommand Set Active Connection.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBCommand Set Active Connection.vi"/>
			<Item Name="ADODBCommand Set Command Text.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBCommand Set Command Text.vi"/>
			<Item Name="ADODBConnection Close.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBConnection Close.vi"/>
			<Item Name="ADODBConnection Create.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBConnection Create.vi"/>
			<Item Name="ADODBConnection Destroy.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBConnection Destroy.vi"/>
			<Item Name="ADODBConnection Open.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBConnection Open.vi"/>
			<Item Name="ADODBRecordset Destroy.vi" Type="VI" URL="../../../Mating Program/SQLToolkitM.llb/ADODBRecordset Destroy.vi"/>
			<Item Name="SQL CloseVC.vi" Type="VI" URL="../SQLToolkitVC.llb/SQL CloseVC.vi"/>
			<Item Name="SQL ExecuteVC.vi" Type="VI" URL="../SQLToolkitVC.llb/SQL ExecuteVC.vi"/>
			<Item Name="SQL OpenVC.vi" Type="VI" URL="../SQLToolkitVC.llb/SQL OpenVC.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Scrap" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{70573AF3-20D1-4073-8C05-A23E028A5B96}</Property>
				<Property Name="App_INI_GUID" Type="Str">{1ABE7EBC-0B7E-486B-BDAC-D54FAEA4966A}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{219A5EA4-863A-4B5E-BDFE-19E03E578A66}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Scrap</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Scrap</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{B88F97C9-EB81-4463-B564-945FDC7DDACB}</Property>
				<Property Name="Bld_version.build" Type="Int">8</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Scrap.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Scrap/Scrap.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Scrap/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{64F24BC3-C742-4928-A3BA-C8E75F59972C}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Scrap.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Scrap</Property>
				<Property Name="TgtF_internalName" Type="Str">Scrap</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2023 Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_productName" Type="Str">Scrap</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{FE649566-5F46-43E8-9CB5-8B21238588AB}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Scrap.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
