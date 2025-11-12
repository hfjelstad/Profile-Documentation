

### JourneyPattern

```
# NeTEx annotation: 
***An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles. A JOURNEY PATTERN may pass through the same POINT more than once. The first point of a JOURNEY PATTERN is the origin. The last point is the destination.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Element | Name |  |  | 
| Element | Description |  |  | 
| Element | PrivateCode |  | ***A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems.*** | 
| Reference | [RouteRef](Route.md) |  | ***Reference to a ROUTE.*** | 
| List | pointsInSequence | StopPointInJourneyPattern |  | 
| List | linksInSequence | ServiceLinkInJourneyPattern |  | 
