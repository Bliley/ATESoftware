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
		<Item Name="Mating.vi" Type="VI" URL="../Mating.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="subDisplayMessage.vi" Type="VI" URL="/&lt;vilib&gt;/express/express output/DisplayMessageBlock.llb/subDisplayMessage.vi"/>
			</Item>
			<Item Name="ADODBCommand CreateM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBCommand CreateM.vi"/>
			<Item Name="ADODBCommand DestroyM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBCommand DestroyM.vi"/>
			<Item Name="ADODBCommand ExecuteM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBCommand ExecuteM.vi"/>
			<Item Name="ADODBCommand Set Active ConnectionM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBCommand Set Active ConnectionM.vi"/>
			<Item Name="ADODBCommand Set Command TextM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBCommand Set Command TextM.vi"/>
			<Item Name="ADODBConnection CloseM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBConnection CloseM.vi"/>
			<Item Name="ADODBConnection CreateM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBConnection CreateM.vi"/>
			<Item Name="ADODBConnection DestroyM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBConnection DestroyM.vi"/>
			<Item Name="ADODBConnection ExecuteM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBConnection ExecuteM.vi"/>
			<Item Name="ADODBConnection OpenM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBConnection OpenM.vi"/>
			<Item Name="ADODBField Get String ValueM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBField Get String ValueM.vi"/>
			<Item Name="ADODBFields Get CountM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBFields Get CountM.vi"/>
			<Item Name="ADODBFields ItemM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBFields ItemM.vi"/>
			<Item Name="ADODBRecordset DestroyM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBRecordset DestroyM.vi"/>
			<Item Name="ADODBRecordset Get FieldsM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBRecordset Get FieldsM.vi"/>
			<Item Name="ADODBRecordset Get Row String ValueM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBRecordset Get Row String ValueM.vi"/>
			<Item Name="ADODBRecordset Get Table String ValueM.vi" Type="VI" URL="../SQLToolkitM.llb/ADODBRecordset Get Table String ValueM.vi"/>
			<Item Name="SQL CloseM.vi" Type="VI" URL="../SQLToolkitM.llb/SQL CloseM.vi"/>
			<Item Name="SQL ExecuteM.vi" Type="VI" URL="../SQLToolkitM.llb/SQL ExecuteM.vi"/>
			<Item Name="SQL OpenM.vi" Type="VI" URL="../SQLToolkitM.llb/SQL OpenM.vi"/>
			<Item Name="SQL SelectM.vi" Type="VI" URL="../SQLToolkitM.llb/SQL SelectM.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="Mating" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{9B830630-380D-4D6E-B6F6-5A28FC7AB0CB}</Property>
				<Property Name="App_INI_GUID" Type="Str">{7A6872CD-51D7-4318-87AC-7EDD4656F29E}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">0</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{02CE24FF-5157-40E5-9E57-94EB131759D4}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">Mating</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/Mating</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{55C214E3-6409-4A19-B762-2C023CAC5A08}</Property>
				<Property Name="Bld_version.build" Type="Int">2</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">Mating.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/Mating/Mating.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/Mating/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{260DA5EC-42F6-49AD-AA1B-ADB39C84D0F8}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Mating.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">Mating</Property>
				<Property Name="TgtF_internalName" Type="Str">Mating</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2023 Bliley Technologies, Inc.</Property>
				<Property Name="TgtF_productName" Type="Str">Mating</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{53227697-EF05-4394-89F8-683877E81530}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">Mating.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
