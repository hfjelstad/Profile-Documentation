

### ServiceCalendarFrame

```
# NeTEx annotation: 
***A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. that may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| List | dayTypes | [DayType](/10-Objects/DayType.md) | ***A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays.*** | 
| List | operatingPeriods | [OperatingPeriod](/10-Objects/OperatingPeriod.md) | ***A continuous interval of time between two OPERATING DAYs which will be used to define validities.*** | 
| List | dayTypeAssignments | [DayTypeAssignment](/10-Objects/DayTypeAssignment.md) | ***Associates a DAY TYPE with an OPERATING DAY within a specific Calendar. A specification of a particular DAY TYPE which will be valid during a TIME BAND on an OPERATING DAY.*** | 
| List | operatingDays | [OperatingDay](/10-Objects/OperatingDay.md) | ***A day of public transport operation in a specific calendar. An OPERATING DAY may last more than 24 hours.*** | 
