Guide: Exchanging Timetable data
Implementation guide for timetable data producers
This guide provides a practical description of the data needed to describe a passenger timetable and how to structure the data for exchange as xml files according to NeTEx. The required data includes the network topology, the possible journey patterns along the stops in the network, the actual journeys and timing, and the calendar that describe on which days the journeys are run.
PublicationDelivery root element
As with any NeTEx dataset, the timetable data must be structured into PublicationDelivery xml elements with frames that contain the timetable data. Figure 1 PublicationDelivery example. The actual timetable data is indicated the example but omitted for brevity
The PublicationDelivery element is the root element of the xml document. It contains required information about the publication in addition to the ‘payload’ elements, i.e. the timetable data structured as different types of frame elements. For an in depth description of PublicationDelivery, see PublicationDelivery
Organise the data into frames
  
Figure 2 A timetable dataset consists of one or more files containing data structured into frames, some are always required, some are required under certain circumstances, and some are optional
The CompositeFrame is an optional wrapper frame that contains other frames. The frames in a CompositeFrame must have the same validity conditions. The validity period stated on the outermost CompositeFrame is considered the dominant validity of all data in the dataset.  
The JourneyPatterns for each line in the network should be placed in a separate ServiceFrame, and the ServiceJourneys making up the schedule for each line in a separate TimetableFrame. Each line in the network thus is described with such a pair of one ServiceFrame and one TimetableFrame. TBD See [link] for further details on the contents of these frames.
The other frames contain common data that can be referenced by all lines in a timetable publication.
Calendar data is placed in a ServiceCalendarFrame. The calendar contains OperatingDays or DayTypes that describe when the services run. The calendar days can be used by more than one line, and the schedules for the different lines in the network will typically refer to the same calendar days.
Common resources are placed in a ResourceFrame. For timetable data this must include the participating Organisations and Authorities.
The timetable relies on the stop data, which must be available in a SiteFrame. When the stops are available from a national register, there is usually a separate publication containing the stop data. TBD how to tie timetables to stops
Split the data into separate files
To reduce the size of the files it is recommended to split the timetable datasets into several files. The preferred way to do so in this guide is:
⦁	One file with frames containing common data for all lines in the network. The file name must start with _ (underscore), e.g. _shared_data.xml
⦁	One file per line in the network with the TimetableFrame and ServiceFrame containing the schedule and patterns for the line. The file name must follow the convention (…TBD) eg. RUT_RUT-Line-4_4_Vestli---Bergkrystallen.xml

 
Figure 3 Example of a Timetable dataset with several PublicationDeliveries in separate files
All files should be exchanged together as a single zip archive. 
All files must conform to the requirements of a PublicationDelivery (TBD link here).
Only complete timetable datasets can be exchanged. A timetable publication must replace any previous version entirely.
Detailed description of the contents of the common data and the line specific data:
Common information in _Shared_File.xml
One line in _Line_File.xml

Submit and validate
When the dataset is produced, the last step is to validate the compliance of the dataset to ensure that trip planning applications and other consumers will be able to use them. TBD last opp dataset …. 
Checklist? Bør vi ha en sjekkliste med krav til innhold? 
Er det her vi bør beskrive at data må tilpasses det konsumentene skal bruke data til, f.eks. grunnlag for billett til avgang og håndtering av avvik?


Further reading
TBD Hvor mye skal med?
DestinationDisplays
Interchanges
Routes
Notices
Different ways of representing Calendars
Flexible Lines