# Data Schema

Each row represents a single pitch

## Columns
### game_id
Unique identifier for each game
Example: 2026-05-12_GAME1

### date
Game date in YYYY-MM-DD format

### pitcher_name
Always LastName_FirstName

### pitcher_hand
Pitchers throwing hand
Allowed values: R, L

### batter_name
Always LastName_FirstName

### batter_hand
Batter hitting side
Allowed values: R, L, S

### inning 
Inning number (Integer)
Allowed values: 1+

### pitch_number
Pitch number within the at-bat
Always starts with 1

### pitch_type
Only use these exact abbreviations. No variations allowed.
Allowed values: 
-FB (Fastball)
-CH (Change-up)
-CV (Curveball)
-SL (Slider)
-SI (Sinker)
-SP (Splitter)
-FC (Cutter)
-KN (Knuckleball)

### x
Raw horizontal pitch location (will be normalized later)

### y
Raw vertical pitch location (will be normalized later)

### result
Only use these exact abbreviations. No variations allowed.
Allowed values:
-whiff
-foul
-in_play
-ball
-called_strike

### balls
Number of balls in the count (0 - 3)

### strikes
Number of strikes in the count (0-2)

