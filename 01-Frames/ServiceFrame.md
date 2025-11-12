

### ServiceFrame

```
# NeTEx annotation: 
***A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned.***
```

| Type | Name | SubElement | NeTEx annotation | 
| --- | --- | --- | --- | 
| Attribute | version |  |  | 
| Attribute | id |  |  | 
| Attribute | modification |  |  | 
| List | routes | [Route](/10-Objects/Route.md) | ***An ordered list of located POINTs defining one single path through the Road (or rail) network. A ROUTE may pass through the same POINT more than once.*** | 
| List | lines | [Line](/10-Objects/Line.md) | ***A group of ROUTEs which is generally known to the public by a similar name or number.*** | 
| List | lines | [FlexibleLine](/10-Objects/FlexibleLine.md) | ***A group of FLEXIBLE ROUTEs of which is generally known to the public by a similar name or number and which have common booking arrangements.*** | 
| List | journeyPatterns | [JourneyPattern](/10-Objects/JourneyPattern.md) | ***An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles. A JOURNEY PATTERN may pass through the same POINT more than once. The first point of a JOURNEY PATTERN is the origin. The last point is the destination.*** | 
| List | noticeAssignments | [NoticeAssignment](/10-Objects/NoticeAssignment.md) | ***The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively.*** | 
| List | routePoints | [RoutePoint](/10-Objects/RoutePoint.md) | ***A POINT used to define the shape of a ROUTE through the network.*** | 
| List | destinationDisplays | [DestinationDisplay](/10-Objects/DestinationDisplay.md) | ***An advertised destination of a specific JOURNEY PATTERN, usually displayed on a head sign or at other on-board locations.*** | 
| List | scheduledStopPoints | [ScheduledStopPoint](/10-Objects/ScheduledStopPoint.md) | *** A POINT where passengers can board or alight from vehicles.*** | 
| List | serviceLinks | [ServiceLink](/10-Objects/ServiceLink.md) | ***A LINK between an ordered pair of STOP POINTs. Service links are directional - there will be separate links for each direction of a route.*** | 
| List | stopAssignments | [PassengerStopAssignment](/10-Objects/PassengerStopAssignment.md) | ***Assignment of a SCHEDULED STOP POINT to a STOP PLACE and QUAY, etc.*** | 
| List | stopAssignments | [FlexibleStopAssignment](/10-Objects/FlexibleStopAssignment.md) | ***Assignment of a SCHEDULED STOP POINT to a FLEXIBLE STOP PLACE and quay. etc.*** | 
| List | notices | [Notice](/10-Objects/Notice.md) | ***A note or footnote about any aspect of a service, e.g. an announcement, notice, etc. May have different DELIVERY VARIANTs for different media.*** | 
| List | additionalNetworks | [Network](/10-Objects/Network.md) | ***A named grouping of LINEs under which a Transport network is known.*** | 
