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
		<Item Name="G-Sensitivity.vi" Type="VI" URL="../G-Sensitivity.vi"/>
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
			<Item Name="ADODBCommand Create.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBCommand Create.vi"/>
			<Item Name="ADODBCommand Destroy.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBCommand Destroy.vi"/>
			<Item Name="ADODBCommand Execute.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBCommand Execute.vi"/>
			<Item Name="ADODBCommand Set Active Connection.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBCommand Set Active Connection.vi"/>
			<Item Name="ADODBCommand Set Command Text.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBCommand Set Command Text.vi"/>
			<Item Name="ADODBConnection Close.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBConnection Close.vi"/>
			<Item Name="ADODBConnection Create.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBConnection Create.vi"/>
			<Item Name="ADODBConnection Destroy.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBConnection Destroy.vi"/>
			<Item Name="ADODBConnection Open.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBConnection Open.vi"/>
			<Item Name="ADODBRecordset Destroy.vi" Type="VI" URL="../SQLToolkitG.llb/ADODBRecordset Destroy.vi"/>
			<Item Name="SQL CloseG.vi" Type="VI" URL="../SQLToolkitG.llb/SQL CloseG.vi"/>
			<Item Name="SQL ExecuteG.vi" Type="VI" URL="../SQLToolkitG.llb/SQL ExecuteG.vi"/>
			<Item Name="SQL OpenG.vi" Type="VI" URL="../SQLToolkitG.llb/SQL OpenG.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
