default trust_jessy = 0
default trust_joshua = 0

define j = Character("Jessy", what_slow_cps=30)
define m = Character("Joshua", what_slow_cps=30)
define narrator = Character(None, what_slow_cps=34)

# --- SIMPLE, STABLE TRANSFORM ---
transform sprite_normal:
    zoom 0.33
    xalign 0.5
    yalign 1.0

label start:

    # Act 1 - Arrival

    # Soft music
    $ renpy.music.set_volume(0.30, channel="music")
    play music "bgm.ogg" fadein 2.0

    # Scene 1
    scene bg room at bg_full
    with fade

    narrator "It’s quiet… too quiet. The air feels heavy, like the room has been holding its breath for far too long."

    show jessy normal at sprite_center
    with dissolve

    j "Oh…"
    pause 0.4
    extend " hey. I didn’t hear you come in."

    j "I’m Jessy."
    pause 0.5
    j "You look a little lost."

    narrator "Her voice is soft, unsure. She keeps glancing at you, trying to figure out who you are."

    j "This place can be overwhelming at first."
    pause 0.6
    j "Honestly… it overwhelmed me too."

    narrator "She tries to smile, but something about her expression feels tired."

    pause 0.8

    # Scene 2
    scene bg park at bg_full
    with fade

    narrator "Later, outside… the world feels colder. The wind carries a strange stillness."

    show joshua happy at sprite_center
    with dissolve

    m "Hey."
    pause 0.4
    extend " You met Jessy, right?"

    m "She’s sweet, but… she’s been through a lot."

    narrator "His voice drops. Something weighs on him too."

    show joshua sad at sprite_center
    with dissolve

    m "It’s been a rough day. For both of us. For a while now, actually."

    narrator "He looks away, as if searching for something he lost a long time ago."

    pause 1.0

    narrator "And just like that… the night grows darker."

    # Act 2 - The Unraveling

    scene bg room at bg_full
    with fade

    narrator "Later that night… the room feels different. Smaller. Like the walls moved closer."

    show jessy sad at sprite_center
    with dissolve

    j "Joshua shouldn’t have said that."

    pause 0.5

    j "He worries too much."

    narrator "She says it quickly. Too quickly."

    j "Things are fine here. They have to be."

    pause 0.8

    narrator "She avoids your eyes."

    j "You ever get that feeling?"
    pause 0.4
    j "Like something already happened…"
    extend " but nobody talks about it?"


    narrator "Silence stretches between you."

    show jessy annoyed at sprite_center
    with dissolve

    j "Why are you looking at me like that?"

    pause 0.4

    j "I’m serious. Don’t."

    narrator "Her voice sharpens — not anger, but fear."

    pause 0.6

    j "If you’re here…"
    pause 0.3
    j "then that means it’s starting again."

    narrator "Again?"

    play sound "door_knock.ogg"

    narrator "A knock. Sudden. Loud."

    show jessy sad at sprite_left
    with dissolve

    j "…Don’t answer."

    pause 0.5

    narrator "Another knock. Firmer."

    show joshua sad at sprite_right
    with dissolve

    m "Jessy. Open the door."

    pause 0.6

    m "It’s not safe pretending anymore."


    narrator "The lights flicker."

    pause 0.5

    narrator "Outside, something moves."

    narrator "And for the first time, you realize—"

    narrator "This place isn’t quiet."

    narrator "It’s waiting."

    narrator "The door stays closed."

    pause 0.6

    narrator "Joshua doesn’t knock again."

    show jessy sad at sprite_left
    with dissolve

    j "He’s right."

    pause 0.4

    j "I just hoped…"
    pause 0.3
    j "maybe this time would be different."

    narrator "Her shoulders sink, like she’s been holding herself together out of habit."

    j "People don’t arrive here by accident."

    narrator "The room feels colder."

    show jessy annoyed at sprite_left
    with dissolve

    j "When it starts, everyone reacts the same way."

    j "They deny it."
    pause 0.3
    j "They hide."
    pause 0.3
    j "They wait for someone else to fix it."

    narrator "She finally looks at you."

    j "You didn’t come here to visit."

    show joshua sad at sprite_right
    with dissolve

    m "Jessy."

    pause 0.4

    m "We don’t have time anymore."

    narrator "There’s urgency in his voice — not panic, but certainty."

    m "If they’re here…"
    pause 0.3
    m "then it’s already begun."

    scene bg park_night at bg_full
    with fade

    narrator "Outside, the park is empty."

    narrator "Too empty."

    narrator "Streetlights hum softly, casting long shadows that don’t quite line up with anything."

    narrator "The world looks normal."
    narrator "That’s the problem."

    show jessy sad at sprite_left
    with dissolve

    j "Last time…"
    pause 0.4
    j "we ran."

    narrator "Her voice trembles."

    j "It didn’t save anyone."

    show joshua sad at sprite_right
    with dissolve

    m "This time, we stay."

    pause 0.6

    narrator "Both of them look at you."

    narrator "Not waiting for permission."

    narrator "Waiting for confirmation."

    narrator "You finally understand."

    narrator "This place doesn’t trap people."

    narrator "It gathers them."

    narrator "And now—"

    narrator "It has you."

label act2_start:

    play music "bgm.ogg" fadein 2.0
    $ renpy.music.set_volume(0.18, channel="music")


    narrator "No one speaks for a while."

    narrator "The park doesn’t feel hostile."
    narrator "It feels patient."

    show jessy sad at sprite_left
    show joshua sad at sprite_right
    with dissolve

    narrator "Jessy watches you carefully."

    narrator "Joshua looks away, giving you space."

    narrator "For the first time since arriving here—"
    narrator "the silence feels directed at you."

menu:
    "Ask Jessy what happens if you stay":
        $ trust_jessy += 1
        jump act2_jessy

    "Ask Joshua what happens if you try to leave":
        $ trust_joshua += 1
        jump act2_joshua

    "Say nothing and observe":
        jump act2_silent

label act2_jessy:

    j "If you stay…"
    pause 0.4
    j "things stop hurting so sharply."

    narrator "She chooses her words carefully."

    j "You still remember why you came."
    j "It just stops defining you."

    narrator "She meets your eyes."

    j "Some people need that."

    narrator "Joshua says nothing."

    jump act2_converge

label act2_joshua:

    m "Leaving isn’t impossible."

    pause 0.4

    m "But it’s not physical."

    narrator "He finally looks at you."

    m "You don’t walk out."
    m "You let go of what brought you in."

    narrator "Jessy tenses slightly."

    m "Most people aren’t ready for that."

    jump act2_converge

label act2_silent:

    narrator "You stay quiet."

    narrator "You watch."

    narrator "Jessy notices first."

    j "That’s also an answer."

    narrator "Joshua exhales slowly."

    m "Silence usually means fear."

    narrator "Neither of them pushes you."

    jump act2_converge

label act2_converge:

    narrator "The air shifts."

    narrator "Not dramatically."
    narrator "Just enough to notice."

    narrator "The park lights flicker once—"
    narrator "then steady."

    show jessy sad at sprite_left
    show joshua sad at sprite_right
    with dissolve

    j "The place listens."

    pause 0.4

    m "It always does."

    narrator "You feel it now."

    narrator "The longer you stay undecided—"
    narrator "the harder it becomes to choose at all."

    narrator "This place doesn’t rush people."

    narrator "It waits for them to settle."

label act3_start:

    narrator "The park feels quieter than before."

    narrator "Not empty."
    narrator "Focused."

    show jessy sad at sprite_left
    show joshua sad at sprite_right
    with dissolve

    narrator "They are no longer watching the place."

    narrator "They are watching you."

    narrator "You notice something strange."

    narrator "The questions in your head don’t feel like yours anymore."

    narrator "They feel… invited."

menu:
    "Ask why this place exists":
        jump act3_why_place

    "Ask why you were brought here":
        jump act3_why_you

    "Ask what happens if you refuse everything":
        jump act3_refuse

label act3_why_place:

    narrator "You ask the question carefully."

    narrator "The answer doesn’t come from them."

    narrator "It comes from the silence."

    j "Because people don’t know where to put things they can’t fix."

    pause 0.4

    j "This place holds them."

    jump act3_converge

label act3_why_you:

    narrator "You already know the answer."

    narrator "You just haven’t said it out loud."

    m "You didn’t come here by mistake."

    pause 0.4

    m "You came because something followed you."

    narrator "Not footsteps."

    narrator "Weight."

    jump act3_converge

label act3_refuse:

    narrator "You say you don’t want any of this."

    narrator "No place."
    narrator "No role."
    narrator "No waiting."

    j "That’s allowed."

    pause 0.4

    j "It’s just… rarely honest."

    jump act3_converge

label act3_converge:

    narrator "Something shifts again."

    narrator "Not outside."

    narrator "Inside."

    narrator "The place isn’t reacting to your words."

    narrator "It’s reacting to your certainty."

    if trust_jessy > trust_joshua:
        jump act3_jessy_path
    elif trust_joshua > trust_jessy:
        jump act3_joshua_path
    else:
        jump act3_neutral_path

label act3_jessy_path:

    j "You can stay."

    pause 0.4

    j "Not forever."
    j "Not safely."

    narrator "She doesn’t promise comfort."

    narrator "She promises stability."

    jump act3_end

label act3_joshua_path:

    m "If you leave…"
    pause 0.3
    m "you’ll feel everything again."

    narrator "He doesn’t soften it."

    narrator "He respects you too much for that."

    jump act3_end

label act3_neutral_path:

    narrator "You haven’t chosen yet."

    narrator "The place notices."

    narrator "So does the silence."

    jump act3_end

label act3_end:

    narrator "For the first time, the question is clear."

menu:
    "Stay, and let the place hold things for you":
        jump act3_stay_response

    "Leave, and carry everything back with you":
        jump act3_leave_response

    "Say you need more time":
        jump act3_wait_response

label act3_stay_response:
    narrator "The park grows still."
    narrator "Not relieved."
    narrator "Accepting."
    jump act4_start

label act3_leave_response:
    narrator "The silence tightens."
    narrator "Not angry."
    narrator "Prepared."
    jump act4_start

label act3_wait_response:
    narrator "The place does not argue."
    narrator "It never does."
    jump act4_start


label act4_start:

    narrator "Something has changed."

    narrator "The place hasn’t moved."
    narrator "The walls are the same."
    narrator "The park is the same."

    narrator "But the quiet no longer feels gentle."

    scene bg room at bg_full
    with fade

    show jessy sad at sprite_left
    show joshua sad at sprite_right
    with dissolve

    narrator "Jessy looks exhausted."

    narrator "Joshua looks uncertain."

    narrator "Neither of them notices it at first."

    narrator "You do."

    if trust_jessy > trust_joshua:

        narrator "Staying has dulled the sharp edges."

        narrator "Memories feel distant."
        narrator "Feelings feel softer."

        narrator "Too soft."

        j "I can keep it steady."
        pause 0.4
        j "For a while."

        narrator "She doesn’t say forever."

        narrator "She never does."

    elif trust_joshua > trust_jessy:

        narrator "Leaving feels closer now."

        narrator "And heavier."

        narrator "Thoughts you avoided return in full detail."

        m "I didn’t tell you the worst part."
        pause 0.4
        m "It hurts more before it gets better."

        narrator "He looks away."

        narrator "For the first time, he isn’t sure."

    else:

        narrator "Indecision has a weight."

        narrator "It presses inward."

        narrator "Thoughts loop."
        narrator "Questions repeat."

        j "The place notices when people wait too long."

        m "It always has."

    scene bg park_night at bg_full
    with fade

    narrator "The park no longer feels patient."

    narrator "It feels strained."

    show jessy sad at sprite_left
    show joshua sad at sprite_right
    with dissolve

    j "I stay because someone has to."

    pause 0.4

    j "If I leave… it falls apart."

    m "And if no one ever leaves—"
    pause 0.3
    m "nothing ever changes."

    narrator "Their voices stay calm."

    narrator "That’s what makes it worse."

    narrator "You feel it now."

    narrator "Staying still is no longer neutral."

menu:
    "Accept the place and what it asks of you":
        $ act4_choice = "stay"

    "Commit to leaving, no matter the cost":
        $ act4_choice = "leave"

    "Take responsibility for others caught here":
        $ act4_choice = "bridge"

narrator "The place does not react."
narrator "It never does."
narrator "It only remembers."

jump act5_start


label act5_start:

    scene bg park at bg_full
    with fade

    narrator "Morning."

    narrator "The first time you see the place like this."

    narrator "Nothing is different."

    narrator "Everything is."

    if act4_choice == "stay":

        show jessy sad at sprite_center
        with dissolve

        j "You understand it now."

        narrator "You don’t feel proud."

        narrator "You feel ready."

        narrator "Jessy steps back."

        narrator "For the first time, she rests."

        narrator "Joshua leaves quietly."

        narrator "The place still holds people."

        narrator "Now, you help it do so."

        narrator "Not forever."

        narrator "Just long enough."

        jump act5_end

    elif act4_choice == "leave":

        show joshua sad at sprite_center
        with dissolve

        m "It won’t be easy."

        narrator "You nod."

        narrator "You don’t expect it to be."

        narrator "Jessy watches as you go."

        narrator "She doesn’t stop you."

        narrator "You leave with everything you came with."

        narrator "And something new."

        narrator "The choice to carry it."

        jump act5_end

    elif act4_choice == "bridge":

        show jessy sad at sprite_left
        show joshua sad at sprite_right
        with dissolve

        narrator "You refuse the extremes."

        narrator "You stay long enough to help."

        narrator "You leave when it’s time."

        narrator "Others begin to do the same."

        narrator "The place loosens its grip."

        narrator "Not gone."

        narrator "Changed."

        jump act5_end

label act5_end:

    narrator "The place still exists."

    narrator "But it no longer defines you."

    stop music fadeout 2.0

    return