

### TimetableFrame

```
# NeTEx annotation: 
***A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| List | vehicleJourneys | [ServiceJourney](/10-Objects/ServiceJourney.md) | ***A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN. The VIEW includes derived ancillary data from referenced entities.*** | 
| List | vehicleJourneys | [DatedServiceJourney](/10-Objects/DatedServiceJourney.md) | ***A particular journey of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff. The VIEW includes derived ancillary data from referenced entities.*** | 
| List | noticeAssignments | [NoticeAssignment](/10-Objects/NoticeAssignment.md) | ***The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively.*** | 
| List | journeyInterchanges | [ServiceJourneyInterchange](/10-Objects/ServiceJourneyInterchange.md) | ***The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs.*** | 
