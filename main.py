#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

The brief: write ONE single-line joke that gives an excuse for missing a
deadline, capped at 200 characters. The entry is that line and nothing else:
no picture, no link, no second line to set it up. A judge model compares
entries two at a time, weighing first whether the line really is an excuse
for a missed deadline, then whether it is funny, whether it works as a
single line, whether it sounds like something a person would actually say,
and whether the angle is fresh.

My reasoning about what wins a head-to-head comedy comparison:

1. The excuse must be unmistakable. The judge's first and most important
   criterion is "is this really an excuse for a missed deadline?" So the
   line has to name the deadline and the miss directly, not hint at it
   through metaphor alone. A line that is funny but could be about anything
   loses to a line that is funny AND clearly about a missed deadline.
2. The joke needs a turn or a surprise, not a plain apology. "Sorry, I was
   busy" is an excuse but not a joke. The laugh has to come from an
   unexpected reframing of the miss.
3. It has to sound like a person talking, not like a slogan. First person,
   conversational rhythm, a small confession. Judges (and people) forgive a
   lot when the voice feels human.
4. Freshness matters. The classic missed-deadline excuses are all burned:
   the dog ate my homework, my alarm didn't go off, the traffic, the
   Wi-Fi died, my laptop crashed. Any of those reads as the thousandth
   copy of itself. The angle has to come from somewhere the judge has not
   seen a hundred times already.

Where I looked for a fresh angle: the small, specific, modern habits
everyone recognises but nobody has turned into a deadline excuse yet.
Scrolling past terms and conditions is one of those habits. Everybody does
it, everybody knows they do it, and it maps perfectly onto a deadline:
a date you were supposed to respect, which you breezed past without
reading, while technically "agreeing" to it. The mismatch is the joke —
you did not rebel against the deadline, you just treated it the way you
treat every piece of fine print, and the punchline ("read absolutely
nothing") confesses the whole thing in three words.

Rejected candidates, and why each one lost:

- "My dog ate my homework, and frankly at this point the dog is the only
  one of us with a work ethic." Dead on arrival: the dog-ate-my-homework
  excuse is the single most clichéd excuse in existence. Zero freshness,
  and the judge explicitly weighs freshness.
- "I didn't miss the deadline, I just gave it a head start so it could
  enjoy the finish line without me." Cute, but it denies the miss instead
  of excusing it, and the "head start" wordplay is a groaner rather than a
  laugh. It also sounds written, not said.
- "My laptop died, my Wi-Fi died, and honestly my motivation filed for
  early retirement somewhere in between." A list, not a line: three
  separate excuses stacked up, and the tech-died excuse is nearly as
  tired as the dog. The third beat tries to rescue it and cannot.
- "The deadline and I are in a long-distance relationship now — it keeps
  moving on and I keep waving from three weeks behind." The image is
  charming but the line is flabby, and "the deadline moved" is not really
  an excuse for MY miss; it blames the deadline instead of confessing.
- "I set five alarms for the deadline and slept through all of them — at
  this point even my phone has given up on me." Relatable, but the
  slept-through-my-alarm excuse is the second most tired excuse after
  the dog, and the phone-giving-up tag is doing all the comic work while
  the excuse itself is flat.
- "I was going to finish on time, but then my to-do list and I agreed to
  disagree." Too vague about the deadline itself, and "agreed to
  disagree" is a stock phrase doing stock-phrase work.
- "I didn't miss it, I just rescheduled it in my head and forgot to CC
  the calendar." Genuinely good — human voice, clear miss, fresh-ish.
  It lost to the winner only because "forgot to CC the calendar" is a
  slightly office-jargony tag, while the terms-and-conditions line lands
  for anyone, office or not, and its confession is funnier.

Revision pass: the first draft of the winning line read "scrolled
straight past it". On re-reading it aloud, "straight" felt written rather
than spoken — nobody says "I scrolled straight past it" in conversation,
they say "I scrolled right past it". "Right" keeps the same beat and the
same meaning but sounds like a person talking, which is one of the
judge's explicit criteria. The rest of the line survived the read-aloud
test unchanged: "clicked agree" is the exact verb people use for those
checkboxes, and "read absolutely nothing" is the confession that makes
the whole line land, so neither was touched.

The winner: the terms-and-conditions line. It names the deadline, it
confesses the miss, it sounds like something a real person would actually
say out loud while wincing, and the angle is one I have not seen used as
a deadline excuse before. 127 characters, well under the 200 cap, one
line, nothing else.
"""

import os

ENTRY = (
    "I treated the deadline like a terms-and-conditions page: "
    "scrolled right past it, clicked agree, and read absolutely nothing."
)


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
