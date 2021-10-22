import csv, json

# Step 1: Open CSV and read
# Step 2: Select first row
# Step 3: Identify if this is a header or a detail
# Step 4: 
# # For a header: 
# # # Clear out previous headers array
# # # Iterate through each field
# # # If this field is "Event", append an auto increment number
# # # Add to a headers array
# # For a detail:
# # # Place all details into an array
# # # Zip details with the previous headers
# # # Turn the new arrays into a dictionary
# # # Add them into a JSON array
# Step 5: Loop through JSON array

# IF field = Id: name lowercase to "id", should I convert unix timestamp?
# IF field = Tz: name to "timezone" (formatting?)
# IF field = From: name to "tracking_start", convert to proper datetime with timezone | option for original, unix timestamp
# IF field = To: name to "tracking_end", convert to proper datetime with timezone | option for original, unix timestamp
# IF field = Sched: name to "alarm_scheduled", convert to proper datetime with timezone | option for original, unix timestamp
# IF field = Hours: name to "tracking_hours"
# IF field = Rating: name lowercase
# IF field = Comment: name lowercase, maybe split into multiple fields as tags, allow for non-tags
# IF field = Framerate: ?
# IF field = Snore: ?
# IF field = Noise: ?
# IF field = Cycles: ?
# IF field = DeepSleep: ? Is this a percent?
# IF field = LenAdjust: ?
# IF field = Geo: ?
# IF field = digit-type: actigraphy, learn about it and how to display
# IF field = Event #: [Types: DHA, HR, AWAKE_START, LIGHT_START, LUX, AWAKE_END, LIGHT_END, DEEP_START, 
#   DEEP_END, REM_START, REM_END, DEVICE, TRACKING_STOPPED_BY_USER, ALARM_LATEST, ALARM_STARTED, ALARM_DISMISSED, others?]
#       IF type = DHA: event type, timestamp (what is DHA?)
#       IF type = HR: event type, timestamp, value
#       IF type = LUX: event type, timestamp, value
#       IF type = AWAKE_START: event type, timestamp
#       IF type = AWAKE_END: event type, timestamp
#       IF type = LIGHT_START: event type, timestamp
#       IF type = LIGHT_END: event type, timestamp
#       IF type = DEEP_START: event type, timestamp
#       IF type = DEEP_END: event type, timestamp
#       IF type = REM_START: event type, timestamp
#       IF type = REM_END: event type, timestamp
#       IF type = DEVICE: event type, timestamp (what is this?)
#       IF type = TRACKING_STOPPED_BY_USER: event type, timestamp
#       IF type = ALARM_LATEST: event type, timestamp
#       IF type = ALARM_STARTED: event type, timestamp
#       IF type = ALARM_DISMISSED: event type, timestamp
# IF field = any other fields?
