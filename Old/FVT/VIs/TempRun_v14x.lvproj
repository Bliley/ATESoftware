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
		<Item Name="TempRun.vi" Type="VI" URL="../TempRun.llb/TempRun.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="System Exec.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/System Exec.vi"/>
				<Item Name="Write Characters To File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Characters To File.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="Open_Create_Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/Open_Create_Replace File.vi"/>
				<Item Name="compatFileDialog.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatFileDialog.vi"/>
				<Item Name="compatOpenFileOperation.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatOpenFileOperation.vi"/>
				<Item Name="compatCalcOffset.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatCalcOffset.vi"/>
				<Item Name="Write File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write File+ (string).vi"/>
				<Item Name="compatWriteText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatWriteText.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="Trim Whitespace One-Sided.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace One-Sided.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
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
				<Item Name="Merge Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Merge Errors.vi"/>
				<Item Name="Beep.vi" Type="VI" URL="/&lt;vilib&gt;/Platform/system.llb/Beep.vi"/>
				<Item Name="LV70DateRecToTimeStamp.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/LV70DateRecToTimeStamp.vi"/>
				<Item Name="Open/Create/Replace File.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open/Create/Replace File.vi"/>
			</Item>
			<Item Name="Temprun.rtm" Type="Document" URL="../TempRun.llb/Temprun.rtm"/>
			<Item Name="Get System Number.vi" Type="VI" URL="../TempRun.llb/Get System Number.vi"/>
			<Item Name="Get Command Line.vi" Type="VI" URL="../TempRun.llb/Get Command Line.vi"/>
			<Item Name="Sytem Status.vi" Type="VI" URL="../TempRun.llb/Sytem Status.vi"/>
			<Item Name="Halt the Run.vi" Type="VI" URL="../TempRun.llb/Halt the Run.vi"/>
			<Item Name="Reset Run Status.vi" Type="VI" URL="../TempRun.llb/Reset Run Status.vi"/>
			<Item Name="RunProfile.vi" Type="VI" URL="../TempRun.llb/RunProfile.vi"/>
			<Item Name="Read Temprun Initialization File.vi" Type="VI" URL="../TempRun.llb/Read Temprun Initialization File.vi"/>
			<Item Name="Read Lines From File.vi" Type="VI" URL="../TempRun.llb/Read Lines From File.vi"/>
			<Item Name="General Error Handler.vi" Type="VI" URL="../../../Freq-V-Time/Frequency vs Time.llb/General Error Handler.vi"/>
			<Item Name="Read File+ (string).vi" Type="VI" URL="../TempRun.llb/Read File+ (string).vi"/>
			<Item Name="Close File+.vi" Type="VI" URL="../../../Freq-V-Time/Frequency vs Time.llb/Close File+.vi"/>
			<Item Name="Find First Error.vi" Type="VI" URL="../../../Freq-V-Time/Frequency vs Time.llb/Find First Error.vi"/>
			<Item Name="Open File+.vi" Type="VI" URL="../TempRun.llb/Open File+.vi"/>
			<Item Name="System Hardware Configuration.vi" Type="VI" URL="../TempRun.llb/System Hardware Configuration.vi"/>
			<Item Name="Create Schedule File Path.vi" Type="VI" URL="../TempRun.llb/Create Schedule File Path.vi"/>
			<Item Name="Write System Status.vi" Type="VI" URL="../TempRun.llb/Write System Status.vi"/>
			<Item Name="Open-Create-Replace File.vi" Type="VI" URL="../TempRun.llb/Open-Create-Replace File.vi"/>
			<Item Name="Simple Error Handler.vi" Type="VI" URL="../TempRun.llb/Simple Error Handler.vi"/>
			<Item Name="Is the file empty.vi" Type="VI" URL="../TempRun.llb/Is the file empty.vi"/>
			<Item Name="Read Characters From File.vi" Type="VI" URL="../TempRun.llb/Read Characters From File.vi"/>
			<Item Name="PASSWORD DIALOG.vi" Type="VI" URL="../TempRun.llb/PASSWORD DIALOG.vi"/>
			<Item Name="Create RVT.vi" Type="VI" URL="../TempRun.llb/Create RVT.vi"/>
			<Item Name="Creat a FVT Runfile.rtm" Type="Document" URL="../TempRun.llb/Creat a FVT Runfile.rtm"/>
			<Item Name="Construct RVT Runfile Loop.vi" Type="VI" URL="../TempRun.llb/Construct RVT Runfile Loop.vi"/>
			<Item Name="Write the Soak time.vi" Type="VI" URL="../TempRun.llb/Write the Soak time.vi"/>
			<Item Name="Write Get Temp Command.vi" Type="VI" URL="../TempRun.llb/Write Get Temp Command.vi"/>
			<Item Name="Write the reset relay command.vi" Type="VI" URL="../TempRun.llb/Write the reset relay command.vi"/>
			<Item Name="Write the End of Loop Command.vi" Type="VI" URL="../TempRun.llb/Write the End of Loop Command.vi"/>
			<Item Name="Write Resistance Command.vi" Type="VI" URL="../TempRun.llb/Write Resistance Command.vi"/>
			<Item Name="Write Temperature and Rise Time.vi" Type="VI" URL="../TempRun.llb/Write Temperature and Rise Time.vi"/>
			<Item Name="System Configuration Panel.vi" Type="VI" URL="../TempRun.llb/System Configuration Panel.vi"/>
			<Item Name="About Temprun.vi" Type="VI" URL="../TempRun.llb/About Temprun.vi"/>
			<Item Name="Bar Code Scanner Setup.vi" Type="VI" URL="../TempRun.llb/Bar Code Scanner Setup.vi"/>
			<Item Name="Bar Code.rtm" Type="Document" URL="../TempRun.llb/Bar Code.rtm"/>
			<Item Name="Device Addresses.vi" Type="VI" URL="../TempRun.llb/Device Addresses.vi"/>
			<Item Name="Temperature Chambers.vi" Type="VI" URL="../TempRun.llb/Temperature Chambers.vi"/>
			<Item Name="Frequency Counters.vi" Type="VI" URL="../TempRun.llb/Frequency Counters.vi"/>
			<Item Name="Relay Switch Boxes.vi" Type="VI" URL="../TempRun.llb/Relay Switch Boxes.vi"/>
			<Item Name="Power Supplies.vi" Type="VI" URL="../TempRun.llb/Power Supplies.vi"/>
			<Item Name="Digital Multimeters.vi" Type="VI" URL="../TempRun.llb/Digital Multimeters.vi"/>
			<Item Name="Read System Status.vi" Type="VI" URL="../TempRun.llb/Read System Status.vi"/>
			<Item Name="Functional Test.vi" Type="VI" URL="../TempRun.llb/Functional Test.vi"/>
			<Item Name="Functional Test Menu.rtm" Type="Document" URL="../TempRun.llb/Functional Test Menu.rtm"/>
			<Item Name="Measure Frequency.vi" Type="VI" URL="../TempRun.llb/Measure Frequency.vi"/>
			<Item Name="Select Frequency Counter.vi" Type="VI" URL="../TempRun.llb/Select Frequency Counter.vi"/>
			<Item Name="HP5313xA Initialize.vi" Type="VI" URL="../TempRun.llb/HP5313xA Initialize.vi"/>
			<Item Name="HP53131 Measure Frequency.vi" Type="VI" URL="../TempRun.llb/HP53131 Measure Frequency.vi"/>
			<Item Name="Request &amp; Read Frequency.vi" Type="VI" URL="../TempRun.llb/Request &amp; Read Frequency.vi"/>
			<Item Name="Set Switcher.vi" Type="VI" URL="../TempRun.llb/Set Switcher.vi"/>
			<Item Name="Set Bliley Relay - Fast.vi" Type="VI" URL="../TempRun.llb/Set Bliley Relay - Fast.vi"/>
			<Item Name="Close HP3488A Switcher(GPIB).vi" Type="VI" URL="../TempRun.llb/Close HP3488A Switcher(GPIB).vi"/>
			<Item Name="HP3488A Initialize(GPIB).vi" Type="VI" URL="../TempRun.llb/HP3488A Initialize(GPIB).vi"/>
			<Item Name="HP3488A Reset(GPIB).vi" Type="VI" URL="../TempRun.llb/HP3488A Reset(GPIB).vi"/>
			<Item Name="HP3488A Close(GPIB).vi" Type="VI" URL="../TempRun.llb/HP3488A Close(GPIB).vi"/>
			<Item Name="Convert Oscillator Position to HP3488A Channel Command.vi" Type="VI" URL="../TempRun.llb/Convert Oscillator Position to HP3488A Channel Command.vi"/>
			<Item Name="HP3488A Display Card Monitor(GPIB).vi" Type="VI" URL="../TempRun.llb/HP3488A Display Card Monitor(GPIB).vi"/>
			<Item Name="HP3488A Delay(GPIB).vi" Type="VI" URL="../TempRun.llb/HP3488A Delay(GPIB).vi"/>
			<Item Name="HP3488A Close Channels(GPIB).vi" Type="VI" URL="../TempRun.llb/HP3488A Close Channels(GPIB).vi"/>
			<Item Name="Select a Bliley Switcher.vi" Type="VI" URL="../TempRun.llb/Select a Bliley Switcher.vi"/>
			<Item Name="Functional Test Dialog.vi" Type="VI" URL="../TempRun.llb/Functional Test Dialog.vi"/>
			<Item Name="Get the Max Number of Oscillators.vi" Type="VI" URL="../TempRun.llb/Get the Max Number of Oscillators.vi"/>
			<Item Name="Return Instruments to Local.vi" Type="VI" URL="../TempRun.llb/Return Instruments to Local.vi"/>
			<Item Name="Read Chamber Temp.vi" Type="VI" URL="../TempRun.llb/Read Chamber Temp.vi"/>
			<Item Name="Read Thermotron Temperature(GPIB).vi" Type="VI" URL="../TempRun.llb/Read Thermotron Temperature(GPIB).vi"/>
			<Item Name="TH4800 Initialize(GPIB).vi" Type="VI" URL="../TempRun.llb/TH4800 Initialize(GPIB).vi"/>
			<Item Name="Load Output Terminator(GPIB).vi" Type="VI" URL="../TempRun.llb/Load Output Terminator(GPIB).vi"/>
			<Item Name="TH4800 Close(GPIB).vi" Type="VI" URL="../TempRun.llb/TH4800 Close(GPIB).vi"/>
			<Item Name="TH4800 Get CH Temp or Hum Process Var(GPIB).vi" Type="VI" URL="../TempRun.llb/TH4800 Get CH Temp or Hum Process Var(GPIB).vi"/>
			<Item Name="TH4800 Get Units(GPIB).vi" Type="VI" URL="../TempRun.llb/TH4800 Get Units(GPIB).vi"/>
			<Item Name="Read Saunders Temperature.vi" Type="VI" URL="../TempRun.llb/Read Saunders Temperature.vi"/>
			<Item Name="Frequency &amp; Voltage Check.vi" Type="VI" URL="../TempRun.llb/Frequency &amp; Voltage Check.vi"/>
			<Item Name="Frequency &amp; Voltage Test Dialog.vi" Type="VI" URL="../TempRun.llb/Frequency &amp; Voltage Test Dialog.vi"/>
			<Item Name="Set V Inject.vi" Type="VI" URL="../TempRun.llb/Set V Inject.vi"/>
			<Item Name="Set the Power Supply.vi" Type="VI" URL="../TempRun.llb/Set the Power Supply.vi"/>
			<Item Name="Set PS5004 Power Supply.vi" Type="VI" URL="../TempRun.llb/Set PS5004 Power Supply.vi"/>
			<Item Name="Initialize PS5004.vi" Type="VI" URL="../TempRun.llb/Initialize PS5004.vi"/>
			<Item Name="Set PS5004 Current Limit.vi" Type="VI" URL="../TempRun.llb/Set PS5004 Current Limit.vi"/>
			<Item Name="Set PS5004 Voltage.vi" Type="VI" URL="../TempRun.llb/Set PS5004 Voltage.vi"/>
			<Item Name="Output ON-OFF.vi" Type="VI" URL="../TempRun.llb/Output ON-OFF.vi"/>
			<Item Name="Display Voltage.vi" Type="VI" URL="../TempRun.llb/Display Voltage.vi"/>
			<Item Name="Set E3631A Supply.vi" Type="VI" URL="../TempRun.llb/Set E3631A Supply.vi"/>
			<Item Name="HPE363xA Initialize.vi" Type="VI" URL="../TempRun.llb/HPE363xA Initialize.vi"/>
			<Item Name="HPE363xA Reset.vi" Type="VI" URL="../TempRun.llb/HPE363xA Reset.vi"/>
			<Item Name="HPE363xA Close.vi" Type="VI" URL="../TempRun.llb/HPE363xA Close.vi"/>
			<Item Name="HPE363xA System Beep.vi" Type="VI" URL="../TempRun.llb/HPE363xA System Beep.vi"/>
			<Item Name="HPE3631A Read Measurement.vi" Type="VI" URL="../TempRun.llb/HPE3631A Read Measurement.vi"/>
			<Item Name="HPE3631A Configure Output.vi" Type="VI" URL="../TempRun.llb/HPE3631A Configure Output.vi"/>
			<Item Name="HPE363xA Error Query.vi" Type="VI" URL="../HPE363XA.LLB/HPE363xA Error Query.vi"/>
			<Item Name="Read Fixture Voltages.vi" Type="VI" URL="../TempRun.llb/Read Fixture Voltages.vi"/>
			<Item Name="Get Voltage.vi" Type="VI" URL="../TempRun.llb/Get Voltage.vi"/>
			<Item Name="Read Voltage.vi" Type="VI" URL="../TempRun.llb/Read Voltage.vi"/>
			<Item Name="Fluke 884XX Display On-Off.vi" Type="VI" URL="../TempRun.llb/Fluke 884XX Display On-Off.vi"/>
			<Item Name="Fluke 8840A Configure.vi" Type="VI" URL="../TempRun.llb/Fluke 8840A Configure.vi"/>
			<Item Name="Fluke 884XX Initialize.vi" Type="VI" URL="../TempRun.llb/Fluke 884XX Initialize.vi"/>
			<Item Name="Fluke 884XX Reset.vi" Type="VI" URL="../TempRun.llb/Fluke 884XX Reset.vi"/>
			<Item Name="Fluke 884XX Trigger &amp; Read Meas.vi" Type="VI" URL="../TempRun.llb/Fluke 884XX Trigger &amp; Read Meas.vi"/>
			<Item Name="Fluke 884XX Error Query.vi" Type="VI" URL="../TempRun.llb/Fluke 884XX Error Query.vi"/>
			<Item Name="Fluke 884XX Close.vi" Type="VI" URL="../TempRun.llb/Fluke 884XX Close.vi"/>
			<Item Name="Manual Function Test.vi" Type="VI" URL="../TempRun.llb/Manual Function Test.vi"/>
			<Item Name="Manual Function Test.rtm" Type="Document" URL="../TempRun.llb/Manual Function Test.rtm"/>
			<Item Name="Turn OFF Chamber.vi" Type="VI" URL="../TempRun.llb/Turn OFF Chamber.vi"/>
			<Item Name="Set Temperature and Rise Time.vi" Type="VI" URL="../TempRun.llb/Set Temperature and Rise Time.vi"/>
			<Item Name="Turn Saunders Chamber Off.vi" Type="VI" URL="../TempRun.llb/Turn Saunders Chamber Off.vi"/>
			<Item Name="Stop Thermotron.vi" Type="VI" URL="../TempRun.llb/Stop Thermotron.vi"/>
			<Item Name="TH4800 STOP(GPIB).vi" Type="VI" URL="../TempRun.llb/TH4800 STOP(GPIB).vi"/>
			<Item Name="Set Chamber Temperature.vi" Type="VI" URL="../TempRun.llb/Set Chamber Temperature.vi"/>
			<Item Name="Set Thermotron Temperature.vi" Type="VI" URL="../TempRun.llb/Set Thermotron Temperature.vi"/>
			<Item Name="TH4800 Manual(GPIB).vi" Type="VI" URL="../TempRun.llb/TH4800 Manual(GPIB).vi"/>
			<Item Name="TH4800 Set CH Set Point.vi" Type="VI" URL="../TempRun.llb/TH4800 Set CH Set Point.vi"/>
			<Item Name="Start a RVT Run.vi" Type="VI" URL="../TempRun.llb/Start a RVT Run.vi"/>
			<Item Name="Start FVT Run.rtm" Type="Document" URL="../TempRun.llb/Start FVT Run.rtm"/>
			<Item Name="Get List of Filenames.vi" Type="VI" URL="../TempRun.llb/Get List of Filenames.vi"/>
			<Item Name="Print Production Run Sheet.vi" Type="VI" URL="../TempRun.llb/Print Production Run Sheet.vi"/>
			<Item Name="New Report.vi" Type="VI" URL="../TempRun.llb/New Report.vi"/>
			<Item Name="Generate Report Create.vi" Type="VI" URL="../TempRun.llb/Generate Report Create.vi"/>
			<Item Name="Generate Report Object Reference.ctl" Type="VI" URL="../TempRun.llb/Generate Report Object Reference.ctl"/>
			<Item Name="font.ctl" Type="VI" URL="../TempRun.llb/font.ctl"/>
			<Item Name="HTML Report Generation Message.vi" Type="VI" URL="../TempRun.llb/HTML Report Generation Message.vi"/>
			<Item Name="Word Find Application Directory.vi" Type="VI" URL="../TempRun.llb/Word Find Application Directory.vi"/>
			<Item Name="Excel Find Application Directory.vi" Type="VI" URL="../TempRun.llb/Excel Find Application Directory.vi"/>
			<Item Name="Excel Error Helper.vi" Type="VI" URL="../TempRun.llb/Excel Error Helper.vi"/>
			<Item Name="Word Error Helper.vi" Type="VI" URL="../TempRun.llb/Word Error Helper.vi"/>
			<Item Name="Set Report Margins.vi" Type="VI" URL="../TempRun.llb/Set Report Margins.vi"/>
			<Item Name="Find First Error and Warning.vi" Type="VI" URL="../TempRun.llb/Find First Error and Warning.vi"/>
			<Item Name="Set Report Orientation.vi" Type="VI" URL="../TempRun.llb/Set Report Orientation.vi"/>
			<Item Name="Set Report Tab Width.vi" Type="VI" URL="../TempRun.llb/Set Report Tab Width.vi"/>
			<Item Name="Set Report Footer Text.vi" Type="VI" URL="../TempRun.llb/Set Report Footer Text.vi"/>
			<Item Name="HTML Report Token Converter.vi" Type="VI" URL="../TempRun.llb/HTML Report Token Converter.vi"/>
			<Item Name="Set Report Header Text.vi" Type="VI" URL="../TempRun.llb/Set Report Header Text.vi"/>
			<Item Name="Print Report.vi" Type="VI" URL="../TempRun.llb/Print Report.vi"/>
			<Item Name="Dispose Report.vi" Type="VI" URL="../TempRun.llb/Dispose Report.vi"/>
			<Item Name="Generate Report Destroy.vi" Type="VI" URL="../TempRun.llb/Generate Report Destroy.vi"/>
			<Item Name="Append Text Table to Report.vi" Type="VI" URL="../TempRun.llb/Append Text Table to Report.vi"/>
			<Item Name="HTML Report Labeled String Table.vi" Type="VI" URL="../TempRun.llb/HTML Report Labeled String Table.vi"/>
			<Item Name="HTML Report Text Alignment.ctl" Type="VI" URL="../TempRun.llb/HTML Report Text Alignment.ctl"/>
			<Item Name="HTML Report Table Cell.vi" Type="VI" URL="../TempRun.llb/HTML Report Table Cell.vi"/>
			<Item Name="HTML Report Numeric Tag Attributes.vi" Type="VI" URL="../TempRun.llb/HTML Report Numeric Tag Attributes.vi"/>
			<Item Name="HTML Report Vertical Cell Alignment.ctl" Type="VI" URL="../TempRun.llb/HTML Report Vertical Cell Alignment.ctl"/>
			<Item Name="HTML Report Table Row.vi" Type="VI" URL="../TempRun.llb/HTML Report Table Row.vi"/>
			<Item Name="HTML Report Table.vi" Type="VI" URL="../TempRun.llb/HTML Report Table.vi"/>
			<Item Name="HTML Report Text Tag Attribute.vi" Type="VI" URL="../TempRun.llb/HTML Report Text Tag Attribute.vi"/>
			<Item Name="HTML Report Filter Special Characters.vi" Type="VI" URL="../TempRun.llb/HTML Report Filter Special Characters.vi"/>
			<Item Name="HTML Report Replace Substring.vi" Type="VI" URL="../TempRun.llb/HTML Report Replace Substring.vi"/>
			<Item Name="HTML Report Get Literal Search Pattern.vi" Type="VI" URL="../TempRun.llb/HTML Report Get Literal Search Pattern.vi"/>
			<Item Name="HTML Report Case Matching.ctl" Type="VI" URL="../TempRun.llb/HTML Report Case Matching.ctl"/>
			<Item Name="HTML Report Get Case Matching.vi" Type="VI" URL="../TempRun.llb/HTML Report Get Case Matching.vi"/>
			<Item Name="HTML Report Get Case Insensitive Search Pattern.vi" Type="VI" URL="../TempRun.llb/HTML Report Get Case Insensitive Search Pattern.vi"/>
			<Item Name="HTML Report Get Wildcard Search Pattern.vi" Type="VI" URL="../TempRun.llb/HTML Report Get Wildcard Search Pattern.vi"/>
			<Item Name="New Report Page.vi" Type="VI" URL="../TempRun.llb/New Report Page.vi"/>
			<Item Name="tables.vi" Type="VI" URL="../TempRun.llb/tables.vi"/>
			<Item Name="Show table lines.vi" Type="VI" URL="../TempRun.llb/Show table lines.vi"/>
			<Item Name="headers.vi" Type="VI" URL="../TempRun.llb/headers.vi"/>
			<Item Name="Enter Row Cell Data.vi" Type="VI" URL="../TempRun.llb/Enter Row Cell Data.vi"/>
			<Item Name="Set Table Column Width.vi" Type="VI" URL="../TempRun.llb/Set Table Column Width.vi"/>
			<Item Name="Build string table (word).vi" Type="VI" URL="../TempRun.llb/Build string table (word).vi"/>
			<Item Name="Excel Import Module.vi" Type="VI" URL="../TempRun.llb/Excel Import Module.vi"/>
			<Item Name="Excel Run Macro.vi" Type="VI" URL="../TempRun.llb/Excel Run Macro.vi"/>
			<Item Name="Excel Remove Module.vi" Type="VI" URL="../TempRun.llb/Excel Remove Module.vi"/>
			<Item Name="Append Report Text.vi" Type="VI" URL="../TempRun.llb/Append Report Text.vi"/>
			<Item Name="Append Report Text (num).vi" Type="VI" URL="../TempRun.llb/Append Report Text (num).vi"/>
			<Item Name="New Report Line.vi" Type="VI" URL="../TempRun.llb/New Report Line.vi"/>
			<Item Name="Append Report Text (str).vi" Type="VI" URL="../TempRun.llb/Append Report Text (str).vi"/>
			<Item Name="Append Table to Report.vi" Type="VI" URL="../TempRun.llb/Append Table to Report.vi"/>
			<Item Name="Append Numeric Table to Report.vi" Type="VI" URL="../TempRun.llb/Append Numeric Table to Report.vi"/>
			<Item Name="HTML Report Labeled Numeric Table.vi" Type="VI" URL="../TempRun.llb/HTML Report Labeled Numeric Table.vi"/>
			<Item Name="Check Serial Numbers.vi" Type="VI" URL="../TempRun.llb/Check Serial Numbers.vi"/>
			<Item Name="Serial Number Dialog.vi" Type="VI" URL="../TempRun.llb/Serial Number Dialog.vi"/>
			<Item Name="Select PPP Filename.vi" Type="VI" URL="../TempRun.llb/Select PPP Filename.vi"/>
			<Item Name="Check Run Schedule.vi" Type="VI" URL="../TempRun.llb/Check Run Schedule.vi"/>
			<Item Name="Read File Lines.vi" Type="VI" URL="../TempRun.llb/Read File Lines.vi"/>
			<Item Name="Add a Run to Schedule.vi" Type="VI" URL="../TempRun.llb/Add a Run to Schedule.vi"/>
			<Item Name="Write line to Schedule file.vi" Type="VI" URL="../TempRun.llb/Write line to Schedule file.vi"/>
			<Item Name="Empty.vi" Type="VI" URL="../TempRun.llb/Empty.vi"/>
			<Item Name="Add Time.vi" Type="VI" URL="../TempRun.llb/Add Time.vi"/>
			<Item Name="Estimate Run Time II.vi" Type="VI" URL="../TempRun.llb/Estimate Run Time II.vi"/>
			<Item Name="Read File and Create String Array.vi" Type="VI" URL="../TempRun.llb/Read File and Create String Array.vi"/>
			<Item Name="Start a FVT Run.vi" Type="VI" URL="../TempRun.llb/Start a FVT Run.vi"/>
			<Item Name="CO2 Dialog.vi" Type="VI" URL="../TempRun.llb/CO2 Dialog.vi"/>
			<Item Name="Create Output and Log File.vi" Type="VI" URL="../TempRun.llb/Create Output and Log File.vi"/>
			<Item Name="Bar Interface Panel III.vi" Type="VI" URL="../TempRun.llb/Bar Interface Panel III.vi"/>
			<Item Name="IssueRunID.vi" Type="VI" URL="../IssueRunID.vi"/>
			<Item Name="FileLockAlert.vi" Type="VI" URL="../../../AutoAge8.0/MainControlsLite v8.0/FileLockAlert.vi"/>
			<Item Name="Read Data From Fixture Files.vi" Type="VI" URL="../Read Data From Fixture Files.vi"/>
			<Item Name="StringToArray.vi" Type="VI" URL="../StringToArray.vi"/>
			<Item Name="Multiline String to 1D String Array.vi" Type="VI" URL="../Multiline String to 1D String Array.vi"/>
			<Item Name="Build Production Sheet.vi" Type="VI" URL="../TempRun.llb/Build Production Sheet.vi"/>
			<Item Name="PreLoad Serial Numbers.vi" Type="VI" URL="../TempRun.llb/PreLoad Serial Numbers.vi"/>
			<Item Name="Create Serial Log Path.vi" Type="VI" URL="../TempRun.llb/Create Serial Log Path.vi"/>
			<Item Name="Bar Interface Panel II.vi" Type="VI" URL="../TempRun.llb/Bar Interface Panel II.vi"/>
			<Item Name="Start a Comp Run.vi" Type="VI" URL="../TempRun.llb/Start a Comp Run.vi"/>
			<Item Name="Start a Compensation Run.rtm" Type="Document" URL="../TempRun.llb/Start a Compensation Run.rtm"/>
			<Item Name="View Runschedule.vi" Type="VI" URL="../TempRun.llb/View Runschedule.vi"/>
			<Item Name="Run Status.vi" Type="VI" URL="../TempRun.llb/Run Status.vi"/>
			<Item Name="Delayed Runs.vi" Type="VI" URL="../TempRun.llb/Delayed Runs.vi"/>
			<Item Name="Create a Runschedule String.vi" Type="VI" URL="../TempRun.llb/Create a Runschedule String.vi"/>
			<Item Name="Is the String NULL.vi" Type="VI" URL="../TempRun.llb/Is the String NULL.vi"/>
			<Item Name="Halt a Delayed Run.vi" Type="VI" URL="../TempRun.llb/Halt a Delayed Run.vi"/>
			<Item Name="Get Output Filename from Schedule File.vi" Type="VI" URL="../TempRun.llb/Get Output Filename from Schedule File.vi"/>
			<Item Name="Remove a Run From Schedule File.vi" Type="VI" URL="../TempRun.llb/Remove a Run From Schedule File.vi"/>
			<Item Name="Configuration Dialog.vi" Type="VI" URL="../TempRun.llb/Configuration Dialog.vi"/>
			<Item Name="Open Data File.vi" Type="VI" URL="../TempRun.llb/Open Data File.vi"/>
			<Item Name="Process the RunProfile.vi" Type="VI" URL="../TempRun.llb/Process the RunProfile.vi"/>
			<Item Name="Convert Multiline String to String Array.vi" Type="VI" URL="../TempRun.llb/Convert Multiline String to String Array.vi"/>
			<Item Name="Extract Temperature Parameter from Runfile Command.vi" Type="VI" URL="../TempRun.llb/Extract Temperature Parameter from Runfile Command.vi"/>
			<Item Name="ArgC and ArgV.vi" Type="VI" URL="../TempRun.llb/ArgC and ArgV.vi"/>
			<Item Name="Write Data to file.vi" Type="VI" URL="../TempRun.llb/Write Data to file.vi"/>
			<Item Name="Soaking.vi" Type="VI" URL="../TempRun.llb/Soaking.vi"/>
			<Item Name="Waiting for Temp.vi" Type="VI" URL="../TempRun.llb/Waiting for Temp.vi"/>
			<Item Name="Remove First Run from Schedule.vi" Type="VI" URL="../TempRun.llb/Remove First Run from Schedule.vi"/>
			<Item Name="Execute Winplot.vi" Type="VI" URL="../TempRun.llb/Execute Winplot.vi"/>
			<Item Name="Check if FVT File.vi" Type="VI" URL="../TempRun.llb/Check if FVT File.vi"/>
			<Item Name="Read Resistance.vi" Type="VI" URL="../TempRun.llb/Read Resistance.vi"/>
			<Item Name="Error Log Recorder.vi" Type="VI" URL="../TempRun.llb/Error Log Recorder.vi"/>
			<Item Name="Test Administration.vi" Type="VI" URL="../TempRun.llb/Test Administration.vi"/>
			<Item Name="Archive Data.vi" Type="VI" URL="../TempRun.llb/Archive Data.vi"/>
			<Item Name="File Header.vi" Type="VI" URL="../TempRun.llb/File Header.vi"/>
			<Item Name="Take Compensation Data.vi" Type="VI" URL="../TempRun.llb/Take Compensation Data.vi"/>
			<Item Name="Get Pullability.vi" Type="VI" URL="../TempRun.llb/Get Pullability.vi"/>
			<Item Name="Iterate to Frequency.vi" Type="VI" URL="../TempRun.llb/Iterate to Frequency.vi"/>
			<Item Name="Calculate HP538x Gate Time.vi" Type="VI" URL="../TempRun.llb/Calculate HP538x Gate Time.vi"/>
			<Item Name="Calculate HP53131x Gate Time.vi" Type="VI" URL="../TempRun.llb/Calculate HP53131x Gate Time.vi"/>
			<Item Name="Converge V_Inject Range.vi" Type="VI" URL="../TempRun.llb/Converge V_Inject Range.vi"/>
			<Item Name="Record Data II.vi" Type="VI" URL="../TempRun.llb/Record Data II.vi"/>
			<Item Name="Get half PPM Data.vi" Type="VI" URL="../TempRun.llb/Get half PPM Data.vi"/>
			<Item Name="Parse Compensation Command.vi" Type="VI" URL="../TempRun.llb/Parse Compensation Command.vi"/>
			<Item Name="Look for SKIP.vi" Type="VI" URL="../TempRun.llb/Look for SKIP.vi"/>
			<Item Name="Set Channel Parameters.vi" Type="VI" URL="../TempRun.llb/Set Channel Parameters.vi"/>
			<Item Name="Set Input Attenuation.vi" Type="VI" URL="../TempRun.llb/Set Input Attenuation.vi"/>
			<Item Name="Set Input Coupling.vi" Type="VI" URL="../TempRun.llb/Set Input Coupling.vi"/>
			<Item Name="Set 100kHz Filter.vi" Type="VI" URL="../TempRun.llb/Set 100kHz Filter.vi"/>
			<Item Name="Set Input Impedance.vi" Type="VI" URL="../TempRun.llb/Set Input Impedance.vi"/>
			<Item Name="Keithley 2000 ACV Config.vi" Type="VI" URL="../TempRun.llb/Keithley 2000 ACV Config.vi"/>
			<Item Name="GPIB Send Message.vi" Type="VI" URL="../TempRun.llb/GPIB Send Message.vi"/>
			<Item Name="Keithley 2000 Single Read Example.vi" Type="VI" URL="../TempRun.llb/Keithley 2000 Single Read Example.vi"/>
			<Item Name="GPIB Receive Message.vi" Type="VI" URL="../TempRun.llb/GPIB Receive Message.vi"/>
			<Item Name="Initialize Run.vi" Type="VI" URL="../TempRun.llb/Initialize Run.vi"/>
			<Item Name="Get Next Run.vi" Type="VI" URL="../TempRun.llb/Get Next Run.vi"/>
			<Item Name="Convert Seconds to HrMinSec.vi" Type="VI" URL="../TempRun.llb/Convert Seconds to HrMinSec.vi"/>
			<Item Name="Format Time - Two Digit String.vi" Type="VI" URL="../TempRun.llb/Format Time - Two Digit String.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="My Application" Type="EXE">
				<Property Name="App_INI_aliasGUID" Type="Str">{F1606BCC-9320-4385-8CA8-BC3B29A187B8}</Property>
				<Property Name="App_INI_GUID" Type="Str">{22335D72-59E3-4F81-AEF4-47290CA01D51}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="App_serverType" Type="Int">1</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{2084E5EB-D7C8-4321-AF1F-B082125BE754}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">My Application</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeTypedefs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../builds/NI_AB_PROJECTNAME/My Application</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{DB1F54C8-377D-4D2F-9EB4-319F6438CCA3}</Property>
				<Property Name="Bld_targetDestDir" Type="Path"></Property>
				<Property Name="Bld_version.major" Type="Int">15</Property>
				<Property Name="Destination[0].destName" Type="Str">T0045_temprun-X.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application/T0045_temprun-X.exe</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application/data</Property>
				<Property Name="Destination[2].destName" Type="Str">Destination Directory</Property>
				<Property Name="Destination[2].path" Type="Path">../builds/NI_AB_PROJECTNAME/My Application</Property>
				<Property Name="DestinationCount" Type="Int">3</Property>
				<Property Name="Source[0].Container.applyDestination" Type="Bool">true</Property>
				<Property Name="Source[0].Container.applyInclusion" Type="Bool">true</Property>
				<Property Name="Source[0].Container.applyProperties" Type="Bool">true</Property>
				<Property Name="Source[0].itemID" Type="Str">{523B9026-E6DB-45FA-B71C-9462DEC7EB64}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/TempRun.vi</Property>
				<Property Name="Source[1].properties[0].type" Type="Str">Remove front panel</Property>
				<Property Name="Source[1].properties[0].value" Type="Bool">false</Property>
				<Property Name="Source[1].properties[1].type" Type="Str">Run when opened</Property>
				<Property Name="Source[1].properties[1].value" Type="Bool">true</Property>
				<Property Name="Source[1].propertiesCount" Type="Int">2</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Bliley Technologies</Property>
				<Property Name="TgtF_internalName" Type="Str">My Application</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright © 2019 Bliley Technologies</Property>
				<Property Name="TgtF_productName" Type="Str">My Application</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{F262689A-DEBC-49D2-8C40-88E718932750}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">T0045_temprun-X.exe</Property>
			</Item>
			<Item Name="My Installer" Type="Installer">
				<Property Name="Destination[0].name" Type="Str">TempRun_v14x</Property>
				<Property Name="Destination[0].parent" Type="Str">{3912416A-D2E5-411B-AFEE-B63654D690C0}</Property>
				<Property Name="Destination[0].tag" Type="Str">{135952D1-C317-427E-88D3-C814A583F764}</Property>
				<Property Name="Destination[0].type" Type="Str">userFolder</Property>
				<Property Name="Destination[1].name" Type="Str">Apple Temprun</Property>
				<Property Name="Destination[1].parent" Type="Str">{624309A2-B0CB-4149-B964-A0FF8B968B6A}</Property>
				<Property Name="Destination[1].tag" Type="Str">{D0840A72-7E0B-4636-8737-5E491732D5F2}</Property>
				<Property Name="Destination[1].type" Type="Str">userFolder</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="DistPart[0].flavorID" Type="Str">DefaultFull</Property>
				<Property Name="DistPart[0].productID" Type="Str">{34D9C224-BFA4-4288-9226-EAF4EEDC48BD}</Property>
				<Property Name="DistPart[0].productName" Type="Str">NI LabVIEW Runtime 2024 Q1 Patch 1 (64-bit)</Property>
				<Property Name="DistPart[0].upgradeCode" Type="Str">{B2695A3E-34C2-3082-9B16-BB16F4DF1A07}</Property>
				<Property Name="DistPartCount" Type="Int">1</Property>
				<Property Name="INST_author" Type="Str">Bliley Technologies, Inc.</Property>
				<Property Name="INST_autoIncrement" Type="Bool">true</Property>
				<Property Name="INST_buildLocation" Type="Path">../Builds/TempRun_v14x/My Installer</Property>
				<Property Name="INST_buildLocation.type" Type="Str">relativeToCommon</Property>
				<Property Name="INST_buildSpecName" Type="Str">My Installer</Property>
				<Property Name="INST_defaultDir" Type="Str">{135952D1-C317-427E-88D3-C814A583F764}</Property>
				<Property Name="INST_productName" Type="Str">TempRun_v14x</Property>
				<Property Name="INST_productVersion" Type="Str">1.0.1</Property>
				<Property Name="InstSpecBitness" Type="Str">64-bit</Property>
				<Property Name="InstSpecVersion" Type="Str">24118001</Property>
				<Property Name="MSI_arpCompany" Type="Str">Bliley Technologies</Property>
				<Property Name="MSI_arpURL" Type="Str">http://www.BlileyTechnologies.com/</Property>
				<Property Name="MSI_distID" Type="Str">{FD0E6E1A-9687-4A1D-9D4A-C993CABD3CFD}</Property>
				<Property Name="MSI_osCheck" Type="Int">0</Property>
				<Property Name="MSI_upgradeCode" Type="Str">{C0CCE344-E6A0-4E79-BC85-E1232AAD1631}</Property>
				<Property Name="RegDest[0].dirName" Type="Str">Software</Property>
				<Property Name="RegDest[0].dirTag" Type="Str">{DDFAFC8B-E728-4AC8-96DE-B920EBB97A86}</Property>
				<Property Name="RegDest[0].parentTag" Type="Str">2</Property>
				<Property Name="RegDestCount" Type="Int">1</Property>
			</Item>
		</Item>
	</Item>
</Project>
