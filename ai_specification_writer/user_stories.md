# User Stories

### User Story 1
As a passenger, I want to search for nearby drivers so that I can find a quick ride.

**Acceptance Criteria**:
- User enters pickup and destination coordinates.  
- System displays available drivers within a 5 km radius.  
- Ride can be booked in under 2 minutes.  

**Priority**: MVP

### User Story 2
As a driver, I want to post my travel route and departure time so that passengers can find me.

**Acceptance Criteria**:
- Driver can input start location, destination, and exact departure time.  
- System validates that the input time is in the future.  
- Route becomes immediately visible to passengers searching that trajectory.  

**Priority**: MVP

### User Story 3
As a passenger, I want to link my credit card or digital wallet so that payment is handled automatically after the ride.

**Acceptance Criteria**:
- User can input and securely save payment credentials.  
- System performs a $1 authorization charge to validate the payment method.  
- Payment is automatically deducted upon ride completion.  

**Priority**: MVP

### User Story 4
As a driver, I want to see a passenger's safety rating before accepting a ride request so that I can maintain personal safety.

**Acceptance Criteria**:
- Passenger rating is displayed directly on the incoming ride request notification.  
- Driver can tap the rating to see detailed behavioral feedback comments.  
- Driver can decline requests from passengers with ratings below 4.0 stars.  

**Priority**: High

### User Story 5
As a passenger, I want to track the driver's real-time vehicle location on a map so that I know exactly when to walk outside.

**Acceptance Criteria**:
- Map screen updates the vehicle marker position every 3 seconds once the trip starts.  
- Estimated Time of Arrival (ETA) recalculates dynamically based on live traffic data.  
- Passenger receives a push notification when the driver is within 500 meters.  

**Priority**: High

### User Story 6
As a user, I want to see my historical carbon emissions saved on a dashboard so that I can track my environmental footprint reduction.

**Acceptance Criteria**:
- Dashboard calculates metrics based on distance traveled compared to solo driving benchmarks.  
- System updates figures immediately after each completed carpool journey.  
- User can share their monthly eco-badge statistics directly to social media profiles.  

**Priority**: Medium

### User Story 7
As a passenger, I want to split the ride cost evenly with other passengers in the same vehicle so that transport remains highly affordable.

**Acceptance Criteria**:
- Fare calculation engine splits total route costs automatically between all active passengers.  
- Users can view individual adjusted fare breakdown amounts prior to trip confirmation.  
- Transaction splits execute concurrently upon single arrival checkpoints.  

**Priority**: Medium

### User Story 8
As a driver, I want to set a recurrent weekly commuting schedule so that I do not have to manually input my routine shifts every single day.

**Acceptance Criteria**:
- UI provides selection checkboxes for days of the week (Monday through Friday options).  
- Routine template populates future weekly cycles automatically.  
- System sends alert updates to preferred match histories 24 hours prior to launch.  

**Priority**: Low

### User Story 9
As a user, I want to filter my potential ride matches by music and conversation preferences so that my commuting environment is pleasant.

**Acceptance Criteria**:
- Profile creation workflow includes toggles for cabin environment tags (e.g., Quiet, Chatty, Pop Music).  
- Matching grid automatically boosts compatibility ranking for users with matching preferences.  
- System flags conflicting cabin styles during selection previews.  

**Priority**: Low
