This content is added from a manually generated file: 

# CompositeFrame
CompositeFrame can be used to group frames that shares the same ValidityConditions, e.g. the ValidityCondition must be the same for all frames below it. This means that this is not set per frame, but is controlled implicitly from the CompositeFrame.

![CompositeFrame](/01-Frames/images/CompositFrame.png)

(iMAGE TOBE UPDATED!)

 --------------------------- 



 This content is automaticly generated using NAP as source: 



### CompositeFrame

```
# NeTEx annotation: 
*** A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. ***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | created |  | ***  *** | 
| Attribute | version |  | ***  *** | 
| Attribute | id |  | ***  *** | 
| List | validityConditions | [AvailabilityCondition](/10-Objects/AvailabilityCondition.md) | *** VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. *** | 
| List | codespaces | [Codespace](/10-Objects/Codespace.md) | *** A system for uniquely identifying objects of a given type. Used for the distributed management of objects from many different sources. For example eachregion of a country may be given a different codespace to use when allocating stop identifieres which will be unique within a country. *** | 
| List | FrameDefaults | [DefaultLocale](/10-Objects/DefaultLocale.md) | ***  *** | 
| List | frames | [ServiceFrame](ServiceFrame.md) | *** A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. *** | 
| List | frames | [TimetableFrame](TimetableFrame.md) | *** A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. *** | 
| List | frames | [ResourceFrame](ResourceFrame.md) | *** A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs, VEHICLE TYPEs etc that have a common validity, as specified by a set of frame VALIDITY CONDITIONs. Used to define common resources that will be referenced by other types of FRAME. *** | 
| List | frames | [ServiceCalendarFrame](ServiceCalendarFrame.md) | *** A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. that may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES. *** | 
| List | frames | [SiteFrame](SiteFrame.md) | *** A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned. *** | 
