#! /bin/bash


# Based on https://stackoverflow.com/a/5789674.
# Supposedly, every AoC has a solution that can run within 15 seconds..
# But not this one. Run the program for about two minutes each time.
interval=120

executeInterval() {
  # Execute the program, dumping any output to the appropriate file.
  exec python launcher.py > output.txt &

  # Get the process ID to kill with SIGINT after a few seconds.
  processId=$!

  # Wait for an interval.
  sleep $interval

  # Terminate with an interrupt.
  # Adjusted based on https://stackoverflow.com/a/5722850.
  { kill -2 $processId && wait $processId; } 2>/dev/null
}

# Can you see the do-while being built?
executeInterval

# If there is an interruption, we can look for the 'extra' file as
# a kind of guard against future intervals.
# Ref: https://stackoverflow.com/a/20148469.
interruptedFile="one/three/interrupted.txt"

while [[ -e $interruptedFile ]]; do

  echo "Target command did not complete within $interval second(s)..."

  # Let us do some inspection, while the next iteration occurs..
  cp "output.txt" "lastOutput.txt"
  cp $interruptedFile "lastInterrupted.txt"

  # Let the CPU take a short break, so we may perform said inspection..
  sleep 30

  executeInterval

done

# Got tired of this just going. Hopped onto reddit, as linked on AoC's page,
# clicked on the calendar for day 13, saw there was an animation, clicked on
# it, and now I has feel dumb. https://streamable.com/tojflp

# I would never have thought to do it that way, but now I'm going to try and
# implement an algorithm like that, without looking at code, just the anim.

# Ugh.

