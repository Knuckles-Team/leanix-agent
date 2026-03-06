##  Intended Usage
PULL webhooks are intended to be used in a loop:
  1. Make a request to retrieve some events.
  2. Process events.
  3. On success, make a request to advance the cursor or use the autoCommit option. Move the cursor forward only after you've processed the current batch of events. Once the cursor is moved, you can't fetch events from previous batches.
  4. Repeat the above steps.
