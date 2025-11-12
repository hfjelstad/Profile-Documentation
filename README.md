![NeTEx](/11-Resources/Images/NeTEx3.jpg)

# Profile-Documentation
Test for collaborative profile documentation <br>
Notes / ideas for structure: <br>
TODO: Check and harnonice towards Transmodel and NeTEx standard for naming <br>
Align structure with Transmodel and NeTEx <br>

# Table of Contents
- [Introduction](#Introduction) - Get to know NeTEx, its Terms, common usage and tools (like XSD) provided
- [Frames](#frames) - Deep dive into the NeTEx structure and the basic usage of frames 
- [Guides](#guides) - Where can i start? How should i model my data? See no further, these guides will help you a long way
- [Use Cases](#use-case) - If you have some very perticular needs, maybe they are showcased here?
- [Reference Data examples](#reference-data-examples) - How have others solved the issue with external data sources?

# Introduction

<details open>
<summary>Introduction to NeTEx</summary>
NeTEx (CEN TS 16614-1, 16614-2 og 16614-3) is a CEN-standard which defines the data format and description for public transport data exchanges. The standard is based on Transmodel (EN 12896), and the reference model for permanent objects required for access to public transport: IFOPT (Identification of Fixed Objects in Public Transport, EN 28701).

NeTEx supports the exchange of data necessary for stop place information, journey planning, and ticketing, and is divided into three main categories:

1. Network Topology (CEN TS 16614-1)
2. Scheduled Timetables Plan data (CEN TS 16614-2)
3. Fare Information (CEN TS 16614-3)

NeTEx was created by CEN / TC278 / WG3 / SG9 lead by France. The final part of the format was published in 2015. The format was created to support the needs of a collection of public transport data providers in Europe, among others ERA (European Rail Agency) and UIC (International Union of Railways).

NeTEx is a general-purpose XML format that facilitates the exchange of complex public transport data between distributed systems. Data in the NeTEx format should be used to effectively update various information and operational applications through both file-based services and web service architectures. The official website contains a detailed explanation of the intention underlying the standard, data models and publicly available standard documentation. In particular, "NeTEx White Papers", available under the website's Downloads-section provides a good introduction to how different concepts in public transport can be modelled using NeTEx.

NeTEx is a comprehensive data format intended to describe different concepts for public transport data in various ways. In many cases, there will be parts of the specification that exceed requirements in actual implementation. Therefore, the extraction of necessary objects, which constitute a so-called NeTEx profile, should be made. Such a profile should be used to specify which parts of the NeTEx format are expected to be exchanged between systems in a given context.
</details>

<details>
<summary>Profiles</summary>
</details>
<details>
<summary>XSD</summary>
<br>
You can use XSD (XML Schema Definition) to validate XML files by linking the XML document to an XSD schema and running a validation process that checks whether the XML structure, elements, and data types conform to the rules defined in the schema.

* ☕ Java: Use SchemaFactory and Validator classes.
* 🐍 Python: Use xmlschema.XMLSchema("person.xsd").is_valid("person.xml").
* ⚙️ .NET: Use XmlReaderSettings with XmlSchemaSet.

Click [here](https://github.com/NeTEx-CEN/NeTEx/tree/master/xsd) for the offical and current NeTEx XSD
</details>
<details>
<summary>Terms</summary>
</details>
<details>
<summary>Common</summary>
<br>
**TODO:** Short intro to Common

- [DateFormats](/02-Common/01-DateFormats.markdown)
- [Calendars](/02-Common/02-Calendars.markdown)

</details>
<details>
<summary>Standard (NeTEx) vs Profile</summary>
</details>
<br/>

# Frames
Frames are used for logical grouping of different NeTEx concepts:
- 🧩 [CompositFrame](/01-Frames/CompositFrame.md) - Grouping of multiple frames
- 🛠️ [ResourceFrame](/01-Frames/ResourceFrame.md) - frame for common objects, i.e. organisations, responsibilities, equipments etc.
- 📍 [SiteFrame](/01-Frames/SiteFrame.md) - frame for information regarding stop places and places of interest.
- 🗺️ [ServiceFrame](/01-Frames/ServiceFrame.md) - frame for information regarding networks lines, routes, planned stops etc.
- 📅 [ServiceCalendarFrame](/01-Frames/ServiceCalendarFrame.md) - frame for defining calendar-information - types of days, operating days, and their relations etc.
- 🕒 [TimetableFrame](/01-Frames/TimetableFrame.md) - frame for describing the actual journeys, such as calendar references, departure times, and waiting times etc.prop
- 🚍 [VehicleScheduleFrame](/01-Frames/07-VehicleScheduleFrame.markdown) - frame for vehicle usage planning with vehicle information, equipment and blocks.
- 👨‍✈️ [DriverScheduleFrame](/01-Frames/08-DriverScheduleFrame.markdown) - frame for planning of personnel scheduling 
- 🎟️ [FareFrame](/01-Frames/FareFrame.md) - frame for fare definitions and price information including products and sales offers.

# Guides:
- [Using DatedServiceJourney as a calendar](/04-Guides/Timetable_DatedServiceJourney.md) 📅

# Use Cases
- [Handling deviations with DatedServiceJourneys](/05-Use-case/DSJ.md)

Use Cases and descriptions


Proposed Use Cases to be modeled in examples and seperate doc files her:
- Stops
	- Accesibility - examples with pictures (as Johan is doing with stops)
- Organisations
- Timetable
- Timetable when booking
- FareZones
- Fares
	- Documentation of objects and fields to use

# Reference Data examples
Some data may not be contained in the exchanged dataset but provided trough a external source. Here are some implementation examples of referenced data:

- [Stops](/03-ReferrenceData/01-Stops.markdown)
- [Organisations](/03-ReferrenceData/02-Organisations.markdown)
- [VehicleType](/03-ReferrenceData/03-VehicleType.markdown)
- [Vehicle](/03-ReferrenceData/04-Vehicle.markdown)