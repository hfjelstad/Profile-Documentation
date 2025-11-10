This content is added from a manually generated file: 

# DatedServiceJourney
  
>[!NOTE]
>A particular [ServiceJourney](/10-Objects/ServiceJourney.md) of a vehicle on a particular [OperatingDay](/10-Objects/OperatingDay.md).
>
>Operational details of the DatedServiceJourney is derived from a referenced generic [ServiceJourney](/10-Objects/ServiceJourney.md). The generic Journey cannot specify [dayTypes](/10-Objects/DayType.md) when this is defined by the [OperatingDay](/10-Objects/OperatingDay.md) of the DatedServiceJourney.
>
>
>Defined in PublicationDelivery/dataObjects/[TimetableFrame](/01-Frames/TimetableFrame.md)/vehicleJourneys 


<br>

<details open>
<summary>
  <b>Full overview</b>
</summary>

| Type | Name | Description | Cardinality 
|-|-|-|:-:|
| Attribute | <b>version | Object version numbering |<font color="green"> <b>1:1|
| Attribute | <b>id | Identifier |<font color="green"> <b>1:1|
| Attribute | <b>created | DateTime describing when the object was created |<font color="yellow"> <b>0:1|
| Element   | <b>ServiceAlteration | Enumeration: [planned, replaced, extraJourney], "planned" is default if no data provided | <font color="yellow"> <b>0:1 |
| Reference | <b>BlockRef | Reference to Block or TrainBlock |<font color="yellow"> <b>0:1| 
| Reference | <b>ServiceJourneyRef | Reference to the [ServiceJourney](/10-Objects/ServiceJourney.md) template |<font color="green"> <b>1:1|
| Reference | <b>DatedServiceJourneyRef| Referencing a Service the current objekt is reinforcing or replacing |<font color="yellow"> <b>0:*|
| Reference | <b>OperatingDayRef| Reference to the [OperatingDay](/10-Objects/OperatingDay.md) dating  the object |<font color="green"><b>1:1|

</details>
<br>

>[!TIP]
>Have a look at the guide describing the simple usage of [DatedServiceJourney](/04-Guides/Timetable_DatedServiceJourney.md), or the [deviation handling](/05-Use%20case/DSJ.md)



 --------------------------- 



 This content is automaticly generated using NAP as source: 



### DatedServiceJourney

```
# NeTEx annotation: 
A particular journey of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff. 

The VIEW includes derived ancillary data from referenced entities.
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Element | ServiceAlteration |  |  | 
| Reference | [ServiceJourneyRef](ServiceJourney.md) |  | Reference to a SERVICE JOURNEY. | 
| Reference | [OperatingDayRef](OperatingDay.md) |  | Reference to an OPERATING DAY. | 
| Reference | [DatedServiceJourneyRef](DatedServiceJourney.md) |  |  | 
