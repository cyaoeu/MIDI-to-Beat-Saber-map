# MIDIbeat (v0.091 (pre-alpha))
Use the DAW Reaper to make MIDI files, then convert those files to Beat Saber map data (JSON).

Read the code for now, very WIP...

Input: .mid file (hardcoded as beatsaber.mid for now)

Output: .json file (hardcoded as Expert.json for now)

Change the path and outputpath variables in settings.py to the location of your .mid file.

TODO:
- Work on UX DAW side (shareable template with custom keys/theme and so on) (70%)
- Add GUI that calls map generation script and remove hard coded paths. (20%)
- Create a beatmap using the tool to fix various issues.
- Add visualization feature for events (lighting).
- Add patterns for pattern insertion feature.
- Clean up code.
- Create simple video tutorials/wiki page (or similar).
