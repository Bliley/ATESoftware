<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="21008000">
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
		<Item Name="Main Controls Systemv9.vi" Type="VI" URL="../Main Controls Systemv9.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Read Lines From File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="Open_Create_Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/Open_Create_Replace File.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="compatOpenFileOperation.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOpenFileOperation.vi"/>
				<Item Name="compatCalcOffset.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatCalcOffset.vi"/>
				<Item Name="compatOverwrite.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOverwrite.vi"/>
				<Item Name="Write File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write File+ (string).vi"/>
				<Item Name="compatWriteText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatWriteText.vi"/>
				<Item Name="Write Characters To File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Characters To File.vi"/>
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
			</Item>
			<Item Name="Main Controls.rtm" Type="Document" URL="../Main Controls.rtm"/>
			<Item Name="AutoAge Globals.vi" Type="VI" URL="../../Main Controls System v8.0/AutoAge Globals.vi"/>
			<Item Name="UpdateSystemNumber.vi" Type="VI" URL="../UpdateSystemNumber.vi"/>
			<Item Name="Read AutoAge_ini.vi" Type="VI" URL="../Read AutoAge_ini.vi"/>
			<Item Name="Get Intermediate String.vi" Type="VI" URL="../Get Intermediate String.vi"/>
			<Item Name="remove preceeding spaces.vi" Type="VI" URL="../remove preceeding spaces.vi"/>
			<Item Name="Main Control Globals.vi" Type="VI" URL="../Main Control Globals.vi"/>
			<Item Name="About Program.vi" Type="VI" URL="../About Program.vi"/>
			<Item Name="Check All Positions" Type="VI" URL="../Check All Positions"/>
			<Item Name="Load Rack Config" Type="VI" URL="../../Main Controls System v8.0/Load Rack Config"/>
			<Item Name="Show Rack Details" Type="VI" URL="../Show Rack Details"/>
			<Item Name="Read Data From run Files.vi" Type="VI" URL="../Read Data From run Files.vi"/>
			<Item Name="Multiline String to 1D String Array.vi" Type="VI" URL="../Multiline String to 1D String Array.vi"/>
			<Item Name="List Units Panel 2.vi" Type="VI" URL="../List Units Panel 2.vi"/>
			<Item Name="Convert Booleans to 2s (F) and 0s (T)" Type="VI" URL="../Convert Booleans to 2s (F) and 0s (T)"/>
			<Item Name="Check Config for Active Positions.vi" Type="VI" URL="../Check Config for Active Positions.vi"/>
			<Item Name="Remove Units Prompt" Type="VI" URL="../Remove Units Prompt"/>
			<Item Name="Remove Units Panel 2.vi" Type="VI" URL="../Remove Units Panel 2.vi"/>
			<Item Name="Start - Stop Postions" Type="VI" URL="../Start - Stop Postions"/>
			<Item Name="Read Data From &apos;.id&apos; Files" Type="VI" URL="../Read Data From &apos;.id&apos; Files"/>
			<Item Name="Enter Serial Number Prompt" Type="VI" URL="../Enter Serial Number Prompt"/>
			<Item Name="IssueRunID.vi" Type="VI" URL="../IssueRunID.vi"/>
			<Item Name="FileLockAlert.vi" Type="VI" URL="../FileLockAlert.vi"/>
			<Item Name="StringToArray.vi" Type="VI" URL="../StringToArray.vi"/>
			<Item Name="TestCreateNewDirectory.vi" Type="VI" URL="../TestCreateNewDirectory.vi"/>
			<Item Name="Globals" Type="VI" URL="../Globals"/>
			<Item Name="Check and Remove Current Row Status.vi" Type="VI" URL="../Check and Remove Current Row Status.vi"/>
			<Item Name="Select All Positions for Curve Fit.vi" Type="VI" URL="../Select All Positions for Curve Fit.vi"/>
			<Item Name="Add Units Prompt" Type="VI" URL="../Add Units Prompt"/>
			<Item Name="Add Units Panel 2.vi" Type="VI" URL="../Add Units Panel 2.vi"/>
			<Item Name="Convert Booleans to 2s (T) and 0s (F)" Type="VI" URL="../Convert Booleans to 2s (T) and 0s (F)"/>
			<Item Name="Select All Status.vi" Type="VI" URL="../Select All Status.vi"/>
			<Item Name="Start Functional Test.vi" Type="VI" URL="../Start Functional Test.vi"/>
			<Item Name="Check Current Row Status.vi" Type="VI" URL="../Check Current Row Status.vi"/>
			<Item Name="Start - Stop Postions1.vi" Type="VI" URL="../Start - Stop Postions1.vi"/>
			<Item Name="Read Data From &apos;.id&apos; Files1.vi" Type="VI" URL="../Read Data From &apos;.id&apos; Files1.vi"/>
			<Item Name="Enter Serial Number Prompt1.vi" Type="VI" URL="../Enter Serial Number Prompt1.vi"/>
			<Item Name="Status Message.vi" Type="VI" URL="../Status Message.vi"/>
			<Item Name="Enter Oscillator Type Prompt" Type="VI" URL="../Enter Oscillator Type Prompt"/>
			<Item Name="Functional Test Prompt.vi" Type="VI" URL="../Functional Test Prompt.vi"/>
			<Item Name="Functional Test Panel.vi" Type="VI" URL="../Functional Test Panel.vi"/>
			<Item Name="Aging Analysis Summary" Type="VI" URL="../Aging Analysis Summary"/>
			<Item Name="Read Data From &apos;.dat&apos; Files" Type="VI" URL="../Read Data From &apos;.dat&apos; Files"/>
			<Item Name="Calculate Aging Over Time Period" Type="VI" URL="../Calculate Aging Over Time Period"/>
			<Item Name="Fix Tabs on Array of Strings" Type="VI" URL="../Fix Tabs on Array of Strings"/>
			<Item Name="CMF - View Warmer.vi" Type="VI" URL="../CMF - View Warmer.vi"/>
			<Item Name="Warm Up.rtm" Type="Document" URL="../Warm Up.rtm"/>
			<Item Name="Collect and Analyze Warm-Up Data.vi" Type="VI" URL="../Collect and Analyze Warm-Up Data.vi"/>
			<Item Name="Parse Delimited String into 5 Strings" Type="VI" URL="../Parse Delimited String into 5 Strings"/>
			<Item Name="Extract Nom Frequency.vi" Type="VI" URL="../Extract Nom Frequency.vi"/>
			<Item Name="Filter and Remove Tabs and Spaces.vi" Type="VI" URL="../Filter and Remove Tabs and Spaces.vi"/>
			<Item Name="Start Date and Time.vi" Type="VI" URL="../Start Date and Time.vi"/>
			<Item Name="Convert Units.vi" Type="VI" URL="../Convert Units.vi"/>
			<Item Name="Calc Plot.vi" Type="VI" URL="../Calc Plot.vi"/>
			<Item Name="Check for Data File Exists.vi" Type="VI" URL="../Check for Data File Exists.vi"/>
			<Item Name="Datafilename.vi" Type="VI" URL="../Datafilename.vi"/>
			<Item Name="Create Datafile Path.vi" Type="VI" URL="../Create Datafile Path.vi"/>
			<Item Name="System Audit.vi" Type="VI" URL="../System Audit.vi"/>
			<Item Name="Positions in Use.vi" Type="VI" URL="../Positions in Use.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="My Application" Type="EXE">
				<Property Name="App_INI_aliasGUID" Type="Str">{2F8F6A4C-626C-46CC-B308-A3BAC087A22D}</Property>
				<Property Name="App_INI_GUID" Type="Str">{FB44BFA1-CA5F-4B42-A43A-7B1B0B46C168}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">1</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{61380269-B9F4-4BDF-9352-188389E7B190}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">My Application</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeTypedefs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/My Application</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{F48EC34F-FA3A-4170-8C89-610D32666626}</Property>
				<Property Name="Bld_targetDestDir" Type="Path"></Property>
				<Property Name="Bld_version.major" Type="Int">9</Property>
				<Property Name="Destination[0].destName" Type="Str">T0045_MainControlsLite(v9).exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application/T0045_MainControlsLite(v9).exe</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application/data</Property>
				<Property Name="Destination[2].destName" Type="Str">Destination Directory</Property>
				<Property Name="Destination[2].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application</Property>
				<Property Name="DestinationCount" Type="Int">3</Property>
				<Property Name="Source[0].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[0].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[0].Container.applyProperties" Type="Bool">true</Property>
				<Property Name="Source[0].itemID" Type="Str">{C855E39D-5C9D-4A00-9AED-311B4DAC4896}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/Main Controls Systemv9.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies</Property>
				<Property Name="TgtF_internalName" Type="Str">My Application</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2019 Bliley Technologies</Property>
				<Property Name="TgtF_productName" Type="Str">My Application</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{4C39A3DE-279E-4957-822C-DA63755CA988}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">T0045_MainControlsLite(v9).exe</Property>
			</Item>
		</Item>
	</Item>
</Project>
