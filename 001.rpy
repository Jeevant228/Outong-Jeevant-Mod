label v001:

    scene black with d
    ". . . . . . . . ."
    $ name = renpy.input("What Is Your Name? (Default Cebong)")
    $ name = name.strip() or "Cebong"
    t "I'm just an ordinary man from a poor family in the country. My parents died three years ago while protecting Scarlet and me from the enemy (Dark Guild)"
    show sc
    $ ss = renpy.input("This is Scarlet she's my? ")
    $ ss = ss.strip() or "Scarlet"
    t "Yeah, I know that she's my [ss]"
    $ br = renpy.input("and I'm Her? ")
    $ br = br.strip() or "Roommate"
    t "So I'm her [br]? Alright then."
    hide sc
    t "At that time my [ss] moved to Big City to become an adventurer"
    t "She's fearless and strong, but I was a coward. I feared the world outside and refused to move with my [ss] to the Big city"
    ".............."
    "........."
    t "Time passed, and after two years my [ss] had some success in becoming an adventurer. She'd joined the guild named \"{b}{i}Outong{/i}{/b}\", so I decided to become an adventurer in Big City,"
    t "Where only the strongest survive and become adventurers..."
    t "I've been in this city for a month, living with my [ss], but I haven't gotten in to any guild yet. "
    t "Sigh... I must be strong enough to join a guild as a member and become an adventurer... Or maybe I can build my own guild, that sounds more fun."
    "................."
    ".........."
    "....."

    scene s1
    with d
    sc "Hey!!, What are you doing there sneaking around?!"
    mc "UHH...I need to use the bathroom?"
    mc "I'm gonna go first."
    scene black with fade
    scene s2
    with d
    sc "STOP!"
    sc "[name] there's only a month left till the guild tournament, did you join a guild yet?"
    sc "Maybe you can join the same guild as me, but you have to be strong enough to join…"
    sc "How are you going to get stronger if you don't start your training?"
    mc "..........."
    t "Sigh... she's right, I was hoping to relax for a while and look for a guild with fewer requirements for membership,"
    t "But now I can't waste any more time, I have to start training hard soon..."
    t "If I stay here doing nothing, Scarlet will kick me out — I can't be a burden for her"
    mc "..........."
    mc "......."
    mc "..."
    mc "."
    sc "[name] are you still there…? Are you ignoring me!?"
    sc "Listen, it's not a problem for you to live here with me, instead. Honestly, I'm happy to have you here with me, but I'm worried about your future, [name]"
    sc "I'm afraid I won't be able to protect you when Dark Guild attacks again after the guild tournament ends."
    sc "Don't think that you're weak just because you haven't joined a guild yet — I believe you've got great potential..."
    mc "..........."
    mc "......."
    mc "..."
    sc "Sigh.. you are ignoring me again. Are you an idiot, [name]?"
    mc "UHH... I wasn't ignoring you, it's just..."
    mc "Scarlet, I'm sorry, but don't waste your time and effort, I'm just not capable of those things. Don't bother with me anymore!"
    mc "I promise I'll help you destroy the Dark Guild who killed our parents."
    "You go to the bathroom and leave Scarlet alone..."
    scene s3
    with d
    tsc "Sigh...I hope he does not think that I'm nagging him. I only want the best for him."
    tsc "I need to take a shower."
    "............."
    scene black with fade

    scene sp
    with d

    tsc "Huh...[name]? Oh shit, I forgot that he's using the bathroom, but why didn't he lock the door?"
    scene mcs
    with d
    tsc "I have to leave. Why am I watching my [br] while he takes a shower? I'm like a pervert, but seeing his cock, I don't remember it being that big when I saw it last time."
    tsc "Ahhh... Fuck, I want to feel that cock in my pussy... (shake head) No... No... No... It's wrong, he's my [br]."
    scene sp
    with d
    tsc "I must leave before he notices."
    scene black with fade
    centered "After while."
    "You decided using your time for meditating and training until nightfall and you're going to sleep and awake in the early morning."
    scene bed
    with d
    mc "Yawn..."
    mc "Ahhh.. shit, it's still early, and my body's sore...maybe taking a walk and getting fresh air will perk me up."
    scene walk
    "You walk alone and look around the quiet neighborhood."
    "(walk - walk - walk....)"

    t "Today the weather is great, and I hope my life is great too."
    t "sigh... I wonder, can I help my [ss] with just my current strength? I want to get stronger."
    "..........."
    "......"
    "..."
    t "Huh, I guess I've walked far enough. It's time to go back home."
    "As you walk, You see something on the ground."
    t "What is that?"
    scene ring
    t " a ring?"
    with flash
    with flash
    with flash
    with d
    t "I don't know why, but that ring feels strange."
    t "Hmm..I'll take it."
    scene walk
    with d
    "You walk to back home"
    "(walk-walk -walk)"
    "KRRRRAAAAKKK"
    "Suddenly you hear a strange noise from the narrow alley"
    mc "Huh... What is that sound? I have to go and check it out."
    scene a1
    play sound "sounds/scream.wav"
    l0 "Argh... Let me go, you bastard!"
    strangeman "Hahaha this time you'll die bitch"
    l0 "In your dreams!"
    strangeman "All of you \"{b}{i}Outong{/i}{/b}\" guild members will die so there is no longer an \"{b}{i}Outong{/i}{/b}\" guild"
    t "What the hell is hapenning? Wait, \"{b}{i}Outong{/i}{/b}\" guild?"
    strangeman "Hahahaha....."
    strangeman1 "Hey boss, I think we should kill that bitch quickly."
    strangeman2 "Right boss, don't waste time, if we take too long, other guild members will come."
    strangeman "Hah... you cowards don't know how to have fun."
    strangeman "I'm going to have fun before I kill this bitch..."
    l0 "Argh... Let me go bastard, or I'll kill all of you!"
    l0 "The Dark Guild must be destroyed."
    strangeman "Hahaha... Say what you like, bitch. You'll die after I have fun with your body."
    l0 "Gasp..kyaaah..."
    scene a2
    strangeman "Hehehe.... quiet, bitch"
    l0 "argh...argh..."
    t "Hmm.. So those guys are members of the Dark Guild, and who's the girl? Why's she been attacked? What should I do?"
    menu:
        "Save Her[lucyp]":
            $ lucy_point += 1
            jump savegirl
        "Keep Watching":
            jump wait



label savegirl:
    t "Yes... I have to save that girl"
    "You look around, see a stick, and pick it up"
    mc "This could be useful..."
    scene a4
    mc "Okay, there is no time — I have to help her immediately."
    mc "STOP!!!"
    mc "Hey, let her go, or I'll beat you all."
    jump sg_done

label wait:
    t "I'll wait and see"
    "..........."
    "Crack....."
    t "Oh fuck, I stepped on something"
    "You accidentally made a sound and they noticed your presence."
    strangeman "Huh, who's there?"
    mc "Shit, they've spotted me."
    jump sg_done

label sg_done:
    scene a2
    strangeman "Hooh... It's a mere ant?."
    scene a3
    l0 "Argh... argh..."
    strangeman "You guys! Go beat up the ant!"
    scene a5
    strangeman1 "Yes, boss! It's easy to step on an ant."
    strangeman2 "Yes, boss! Let's go, buddy!"
    mc "You guys are Dark Guild members, right? So I have to kill you."
    strangeman1 "Oh good, you already know who we are! And you'll die."
    mc "Hah... Let see..come here!"


    scene black with fade
    play sound "sounds/hit.mp3"
    ".........."
    play sound "sounds/hit.mp3"

    "You defeated both of them."

    scene a6
    strangeman1 "Urgh..argghh..."
    strangeman2 "Please don't kill us!"
    mc "I already said I will kill you!"
    strangeman1 "No..no.No ARGGHHh.."
    play sound "sounds/hit.mp3"
    "You killed strange man1"
    strangeman2 "Argh...BOSS HELP ME!! He's killing my buddy."
    mc "And now! It's your time!"
    strangeman2 "Noooo...AAArgh..."
    play sound "sounds/shriek.wav"
    "You killed both of them"
    play sound "sounds/hit.mp3"


    scene a2
    strangeman "Grrr.. You guys suck! Can't beat an ant and get killed instead."
    strangeman "Hey bitch I'll have fun with you later after I kill this ant."
    l0 "Argh....."
    mc "Shit... I forgot there was still one more enemy, but I'm already exhausted."
    scene black with fade
    "Unfortunately, you lose."

    scene a7

    t "Argh fuck..shit..... it hurts.. I'm still too weak"
    t "Turns out he's too strong. I should be more vigilant, and I have to attack his weak point."
    t "But I think it's too late. I can't move anymore."

    strangeman "It's time for you to die."
    "......"
    scene black with fade
    "You close your eyes"
    t "Ugh... It's over. I'll lose. I'll die."
    t "Weak people like me never seem to be able to become an adventurer"
    t "I'm sorry, [ss], I can't keep my promise."
    "..........."
    "......"

    scene black with fade

    scene a8
    play sound "sounds/slash.ogg"
    strangeman "AARRGHH... you bi...tch."
    l0 "Hey, are you okay?"
    mc "Ugh....."
    scene black with fade
    centered "You passed out."
    "..................."
    "............"
    "....."
    mc "Huh... Where am I? Why can't I see anything? It's all black."
    un "congrats, my boy! You're the chosen one."
    mc "Who's that? And where am I?"
    t "Am I still alive? "
    t "I remember the girl killed a strange man from the Dark Guild,"
    t "But what happened after that?"
    t "Or maybe I'm dead, and this is the afterlife?"
    "................."

    with flash
    un "Haha..haha.. don't worry, my boy! You're in my spatial world, and you're still alive. This is not the afterlife — you'll be safe here! "
    mc "Huh..you can read my mind? Really?"
    mc "So this must a dream, right?"
    un "Yes and no, it's not just a dream."
    mc "HEY, where are you? And who are you?"
    with flash
    show mg1
    un "I'm here, my boy, I'm Zerocus, a Mage, but this is only my soul and memories!"
    mc "Only your soul and memories? So you are not here? Then where is your body?"
    zr "I am nowhere. I died tens of years ago. I was killed by my apprentice. Her name was 'Sinta', she fell into darkness,"
    zr "she was blinded by power, at one time she asked me to teach her strong destructive magic, but I refused because she was not suitable."
    zr "And oh... I'm sorry, my boy, I don't have much time for this story."
    zr "The short version of my story is that she stabbed me in the back "
    zr "Because you have found that my special ring, it means you have the potential to become my successor."
    mc "the ring?"

    show ring
    with flash
    with d
    hide ring
    with flash
    mc "Oh yeah, I remember, that strange ring."
    zr "Listen, my boy! I don't have much time left."
    zr "Here, I'll give you all my power as a gift before I vanish."
    mc "Power? What's the power you'll give to me?"
    zr "I'll start now!"
    mc "Wait...wait...wait... what should I do?"
    hide mg1
    show mg


    zr "(start casting spell)...HAAAAaaahh.....take it, my boy!"
    mc "What are you doing?"
    hide mg
    show mg2

    mc "what? Arghh...argh...!!! Huh... Wait, I can feel the power flowing in my veins, but it also hurts."
    mc "Aaaarghhh....arghhh... How long will this keep coming? I can't... I can't resist anymore. It hurts... argh..."
    hide mg2
    show mg3
    play sound "sounds/quake.ogg"
    mc "AAAAArrrGGGhhhh.........."
    scene black with fade
    centered "somewhere."
    scene ms0
    tms0 "Hmm... I feel someone, somewhere, has awakened his magic power."
    tms0 "And I'm afraid his power will exceed my current power."
    tms0 "I must immediately find whoever this person is, I will make him an ally. Otherwise, I have to kill him."
    scene black with fade
    un "excuse me..."
    scene lin0
    un "Mistress Sinta, I have news for you!"
    scene ms1
    ms "What's the news, Lin?"
    scene lin0
    li "Three of our members have been killed!"
    scene ms1
    ms "Hooh... whoever dares to oppose our Dark Guild will perish."
    scene lin0
    li "Two of them were killed by an Unknown man, and one was killed by a member of \"{b}{i}Outong{/i}{/b}\"."
    scene ms1
    tms "An unknown man. Is this a coincidence?"
    ms "Hmm... Interesting. Quickly investigate who this unknown man is! And immediately report to me with the results."
    scene lin0
    li "Yes, Mistress Sinta..."

    scene black with fade
    "..............."
    centered "Day passed"
    scene s4
    tsc "It's already afternoon — why hasn't [name] come out of his room yet?"
    tsc "I'll check. Maybe he's still sleeping"
    scene s5
    play sound "sounds/knock.mp3"
    "KNOCK... KNOCK... KNOCK..."
    sc "[name] Are you awake?"
    play sound "sounds/knock.mp3"
    "KNOCK... KNOCK... KNOCK..."
    sc "..........."
    sc "[name] are you there? Hello... Listen, I'm sorry for what I said yesterday, I just worry about you."
    sc "Please answer me, my [br]."
    "........"
    tsc "Strange, why isn't he answering? Is he still sleeping?"
    "........"
    tsc "Arghh...enough!"
    sc "[name]! I'm come in."
    scene s6
    sc "Huh... He's not here?"
    tsc "Did he run away?"
    tsc "No, his stuff is still here. And he promised to help me to destroy the Dark Guild, but he is still weak. If he's in danger because of me, I won't be able to forgive myself."
    tsc "Sigh... I hope you become stronger soon, [name], I can't protect you if the Dark Guild attacks again."
    scene s7
    tsc "I'll try to call him"
    "...."
    tsc "Weird. His phone is off, I'm starting to worry about you [name]? Was he offended by what I said yesterday?"
    sc "Oh shit..it's my fault."
    scene black with fade
    "................"
    label galleryscene1:
    scene lroom2
    t "Huh, what a weird dream! And where am I now?"
    t "I don't remember why I'm here."
    scene lroom
    "You look your side and you see a girl sleeping naked"
    t "What..? Who is she? Why's she sleeping naked beside me?"
    t "Well... Not bad to see a beautiful naked body by my side ha-ha..."
    "......."
    with vpunch
    mc "{b}ARGH!{/b}... My head hurts!"

    scene lroom3

    l0 "Hmmm..?"
    l0 "Oh … you're awake? Are you okay?"
    scene lroom1
    l0 "Yaaaaaaawnnn...."
    mc "Oh…uh…sorry if I woke you up."
    t "Fuck, she's hot! And I've got a boner. I want to fuck her right now, ."
    t "But I barely know who she is."
    scene lroom4
    l0 "Hey, are you okay? You look tense!"
    mc "Well, you know I'm a normal guy, and seeing such a beautiful girl naked in front of me, well...Uhm, I mean...uhm, you know."
    l0 "Oh… I'm sorry, this is my fault. I'll fix this, don't worry, I'll help release your tension."
    l0 "Lay down, please! I'll take care of you."
    mc "O…ok, but it's not necessary."
    l0 "Shhhhh.."
    scene lroombj
    tl0 "Wow, this is so big, I didn't expect it to be this big"
    tl0 "This makes me horny, I want to fuck him, but I don't know who he is yet."
    l0 "Don't worry, I'll help you."
    mc "Uhm...I have a question, I..."
    scene lroombj1
    l0 "Shh...hold on, handsome!"
    l0 "I promise I'll answer all your questions after this, okay?"
    "......."
    mc "O..ok then.."
    scene lroombj
    t "Ohh, fuck! This feels so good, ohhhh..."
    mc "Aaargh... I'm going to cum"
    play sound "sounds/Ejaculate.wav"
    scene lbj
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash

    mc "Aaaaaaahhh yes, Thank you."
    l0 "Okay, I think it's fine, I'll clean up this mess, and we'll talk"
    scene black with fade
    scene ltalk
    l0 "Are you okay?"
    mc "... Yeah, just a little dizzy."
    mc "Uhm.. Why were you sleeping naked beside me? Who are you? And why am I here?"
    mc "How long did I sleep?"
    l0 "Oh.. I'm sorry, I always sleep naked. I'm Lucy, and you are in my room."
    l "I brought you to my house because you were unconscious three days ago."
    mc "What! three days? Are you serious?"
    l "Yes, I'm serious. It's been three days since you fell unconscious."
    mc "Hmm... Wait"
    t "I remember that I was about to die, and then she killed that bastard."
    "......."
    t "Oh shit, I've been unconscious for three days, I hope my [ss] is not worried."
    l "Thank you for saving me. What's your name, my handsome hero?"
    mc "My name's [name]. You can call me [name]."
    l "So [name]... Are you also an adventurer or a member of a guild?"
    mc "No... Not yet..."
    l "Do you know that I am an \"{b}{i}Outong{/i}{/b}\" guild member!"
    mc "Yeah, I heard it from that strange man from Dark Guild three days ago."
    l "Oh right, that bastard, I only killed one of them."
    l "Hey, I have to introduce you to my best friend, Scarlet, later. She's also an \"{b}{i}Outong{/i}{/b}\" guild member."
    mc "Wait, you know Scarlet?"
    t "Of course. She is an \"{b}{i}Outong{/i}{/b}\" guild member."
    t "But I didn't know that they're best friends. "
    scene ltalk1
    with d
    l "Of course I know her — Scarlet and I are best friends. You know Scarlet too?"
    mc "Um, yeah, I know her."
    t "Better not tell her that she is my [ss] "
    l "You know because we are... blah blah blah...."
    t "Wow, looking at her I can see her pussy"
    scene ltalk1
    pause (2.0)
    t "Wait, is she's doing that on purpose?"
    t "Fuck, I'm getting a hard-on again, shit I want fuck her right here, right now."
    l "And then we went.....blah... blah... blah...."
    t "Shit...she's drive me crazy, Aaaargh... What should I do?"

menu:
    "Fuck Her":
        if lucy_point >= 1:
            jump fucklu
        else:
            jump lucystop
    "Resist":
        $ renpy.end_replay()
        jump resist
label lucystop:
    scene lm
    play sound "sounds/Gasp.wav"
    l "Gasp...[name]! What are you doing?"
    mc "I'm sorry, Lucy, I couldn't help myself anymore."
    l "No! please stop it! I'm sorry [name], but I can't. Please stop it"
    l "What if Viona comes in?"
    mc "Viona?"
    l "Yes, she's my sister"
    mc "But she's not here now, so maybe we can have fun"
    l "No I can't! please leave me alone! [name], I'm sorry but can you leave?"
    jump fl_done
label resist:
    t "No, I can't, she's my [ss]'s best friend"
    mc " I'm sorry Lucy, I think I have to go, see you later."
    l "But I haven't introduced you to Viona yet."
    mc "Who's Viona?"
    l "She's my sister."
    mc "Maybe next time."
    l "Oh...ok then, see you later, [name]."
    jump fl_done

label fucklu:
    scene lm
    with d
    play sound "sounds/Gasp.wav"
    l "Gasp...[name]! What are you doing?"
    mc "I'm sorry, Lucy, I can't help myself anymore."
    mc "You're driving me crazy with your pussy in front of me. I know you're doing that on purpose, right?"
    "........."
    "....."
    l "I.....I....yes…yes [name] yes, I did that because I want you, [name]. I want your big cock, please fuck me, [name]!"
    mc "Your wish is my command."
    scene lm1
    with d

    l "Oooohh... Finally, I can feel this big cock inside me."
    l "Yesss, fuck me harder....deeper ooh.."
    scene lm2
    with d
    l "Aaaaaahhhh..... [name], I can't think anymore hah hah...."
    l "fFuuuuckkk..ohhhh I'm cumming I'm cummiiiinggg...."
    scene lmf
    with d
    mc "You know Lucy? You're a beautiful girl, and your body's hot, I like you, Lucy."
    l "So...aahhh..you like ahhh..me? Maybe we can... hah..ahh... hang out together, and we can invite my best friend, Scarlet."
    l "Oh yes, just like that, fuck me...fuck me..."
    mc "Let's change position!"
    label fucklucy:
        menu:
            "Doggy style":

                jump lucydoggy
            "Missionary":

                jump lucymissionary
            "Standing":
                jump lucystanding
            "Skip...":
                $ renpy.end_replay()
                jump fucklucy_end
    label lucydoggy:

        play movie "mov/lucydoggy.webm" loop
        play music "<loop 0.0>sounds/lucy.mp3"
        show movie with d
        l "Ah.... ah.... fuck me...fuck ah... ah... yessss..."
        l "Ooohhh....this feels so gooood.. faster faster please fuck me faster"

        menu:
            "Faster":
                play movie "mov/lucydoggyfaster.webm" loop
                show movie with d
                l "Aaahhh.... yeeesssss... fuuuuckk..."
                l "Oh yeah... just like that"
                l "It feels so gooooddd aahhhh....."
                l "Fuck me... harder faster ah......fuuck yes..."
                l "Your cock is Aaahh...mazing... ohhh...."
                l "Yes.. yes.. fuck me [name]! I love your big cock"


        jump fucklucy
    label lucymissionary:
        play movie "mov/lucymissionary.webm" loop
        show movie with d
        l "Fuck me... fuck me.. fuck me..."
        l "Ooohhhh... yess [name] fuck me..."
        l "Fuck...ohhh yeah...."
        jump fucklucy



    label lucystanding:
        play movie "mov/lucy.webm" loop
        show movie with d
        l "Ooohhhh... yess [name] fuck me harder faster..."
        l "Fuck...ohhh yeah...."
        l "Fuck me... fuck me.. fuck me..."

        l "Ah.... ah.... fuck me... ah... yessss..."
        l "Ooohhh....this feels so gooood.."
        l "I'm going to cum again, I'm cumming, I'm cumming, I'm cummiiiiiiingg.."
        $ renpy.end_replay()
        "...."
        jump fucklucy
label fucklucy_end:
    scene black with fade
    stop movie
    stop music
    centered "Meanwhile"

    scene viona1
    with d
    v0 "Haaah, finally I'm home. A week away from home feels like forever."
    v0 "I'm home... Lucy! Where are you?"
    v0 "I want to take a shower and relax, but where's Lucy? She's must be home at this time of day."
    v0 "I wonder, is she in her room? I'll check in there."
    v0 "But first thing first, I need a shower.."
    scene black with fade
    scene viobath
    with d
    tv0 "Hmm.. It's nice, I needed this so much. "
    tv0 "After a week on a mission when I rarely got a bath"
    tv0 "And hardly ever slept in a bed — mostly sleeping on the ground in the middle of a forest. "
    tv0 "Taking a shower like this feels like paradise"
    v0 "Hmm...hmm...hmm"
    scene viobath1
    with d
    tv0 "I wonder why Lucy didn't greet me, she must be home right?"
    tv0 "Or maybe she's on a mission?... No! If she was on a mission I'd have heard from the guild, except if the mission is level 'S'."
    tv0 "But for now she doesn't have power enough for level 'S' mission, because it's too dangerous. Even I'm still too weak to get those missions."
    tv0 "No.. no.. no.. maybe she's still asleep? So she's won't hear me coming, I'll surprise her later hehe..."
    v0 "..........."
    tv0 "Okay, I think that's enough, let's check Lucy's room!"
    scene black with d
    scene viona2
    with d
    tv0 "I'll see if she's in her room or not."
    play sound "sounds/lucy.mp3"
    l "Ahhh....ahhh yeesss..... yess....fuuuuck "
    play sound "sounds/lucy.mp3"
    tv0 "Hmmm, wait.... sounds like she's masturbating in her room, but why didn't she lock the door."
    l "Oooohhh yeeeeaahh....."
    ".........."
    "......"
    "..."
    tv0 "I think she's done, I'll go in. Let's see what are you doing Lucy? Hehe..."
    scene lmf1
    with d
    mc "Ah...."
    t "Shit I'm going to cum"
    l "Yes, give it to me...."
    l "Cum on my face! Cover me with your semen..."
    scene lmf3
    with d
    play sound "sounds/Ejaculate.wav"
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash
    scene black with d

    scene viona3
    with d
    play sound "sounds/Gasp.wav"
    v0 "Gasp... Lucy! What the fuck are you doing? You're fucking a stranger? Really?"
    v0 "We're sisters, and you tell me everything, but you never told me you have a boyfriend?"
    mc "Ehmmm... I'm not...."
    scene lmf2
    with d
    l "Viona...? I can explain! And don't you know how to knock?"
    v "Lucy! We have to talk seriously. I'll leave you two alone…"
    play sound "sounds/door.wav"
    "Viona slams the door and leave."
    mc "So... She's your sister?"
    l "Yes, she is my sister, don't worry, I'll talk with her about this, and you can stay here."
    mc "I'm sorry Lucy, I think I should go, see you later."
    l "Oh...ok then, see you later [name]."
    $ renpy.end_replay()
    jump fl_done


label fl_done:
    scene black with fade
    centered "You get dressed and leave"

    scene walk
    with d
    t "I remember about my dream with the Mage... And he said I've got potential to become his successor because I could find that ring..."
    t "And he gave me such powerful magic. I can feel it, but I wonder how to use that power. He didn't say anything about how to use it."
    with flash
    t "Oh… Yeah, the ring!"
    t "I almost forgot, it must be still in my pocket."
    scene ring
    with d
    t "Hmm... This ring still looks strange to me..."
    t "But he said this ring is special."
    t "Maybe if I wear this ring, I'll know how the power in my body works."

    scene ring1
    with d

    mc "Nothing happened..."
    "............"
    "......"
    with flash
    mc "Wait... my head... argh... It's hurt again."
    mc "It feels like the time when Old Mage Zerocus gave me magical power, argghhh.. but this time I'm just feeling like..."
    with flash
    with vpunch
    with flash
    with vpunch
    with flash
    scene ring2
    with d
    play sound "sounds/bolt.ogg"
    mc "Aaargghhh....."
    play sound "sounds/bolt.ogg"
    with flash
    with vpunch
    with flash
    with d
    scene black with fade
    scene ring3
    with d

    t "Huh… What happened to my clothes? Wait... I can feel it, I can remember everything, and I know how to use my power, and this is my magical clothing."
    t "With this outfit, physical attacks can't hurt me very much... So it's like bulletproof."
    t "Now I'm a Mage, and I have such powerful magic."
    t "I'll ask Scarlet about the guild tournament! But first I have to ask to join the guild."
    t "With my new power, from now on everything will be easier."
    mc "MuaHahaHAhaha....oops I'm laughing too loud, like an evil lord haha..."
    t "Okay, let's go home. Scarlet must be worried."
    t "Actually, I have the power to fly, but if I do, it will attract too much attention."

    scene black with fade
    centered "You got home at night."
    mc "Scarlet, I'm home!"
    "....."
    t "Hmm...maybe she's already sleeping"
    "As you walk to your room you hear a sound"

    menu:
        "Investigate":
            label galleryscene2:
            t "Hmm... It's coming from Scarlet's room. I'll open her door"
            scene sm2
            with d
            t "Oh fuck... she's masturbating! Should I watch this?"
            menu:
                "Yes!":
                    scene sm
                    with d
                    sc "Oh..."
                    scene sm_
                    with d
                    sc "Yeah....ehmm"
                    play movie "mov/sm.webm" loop
                    show movie with d

                    play music "<loop 0.0>sounds/scarlet.mp3"

                    sc "Oh... fuck yeesss...fuck me fuck me ooooohhh...."
                    sc "Yes yes yes give it to me... fuck me harder!"
                    t "I wonder who she's imagining?"
                    sc "Yes, I'm cumming. I'm cumming."
                    sc "Please cum with me! Cum with me...cum inside my pussy [name]!"
                    stop music
                    t "{b}WHAT THE FUCK!{b} She's imagining me!"
                    t "It's too weird. I have to go to sleep."

                    scene black with fade
                    stop movie
                    "You head off to bed."
                    scene sm_
                    with d
                    sc "Ahhh....."
                    sc "It feels so good."
                    scene black with fade

                    scene sm1
                    with d
                    tsc "Sigh... I did it again, I imagined my [br] fucking me again."
                    tsc "Since I saw his cock in the bathroom, I can't stop thinking about it."
                    tsc "Shit... it's wrong, but why does it feel so good when I imagine it with him?"
                    tsc "But now he left me alone, sigh... I hope you come back. Please don't leave me, my [br] "
                    sc "......................"
                    sc "............."
                    sc "......."

                    sc "yaaaawnn..."
                    tsc "I'm exhausted, I'll going to sleep"
                    scene black with fade
                    $ renpy.end_replay()
                "Leave it be":
                    t "Nah...it'd be weird watching my [ss] masturbating. I'm tired, and I'm going to sleep."
                    scene black with fade
                    $ renpy.end_replay()
        "Leave it be":
            t "I don't care, I'm tired, and I'm going to sleep"
    scene black with fade
    centered "MORNING"
    scene bed
    with d
    mc "Yaaawnn...I slept like a log, and my head's not hurting anymore."
    mc "Okay, I'll see Scarlet."
    mc "I need to talk with her"
    mc "But, first thing first, I need a shower. I stink like a pig."
    scene mcs
    with d
    t "I hope Scarlet wasn't too worried about my being away. It was just three days."
    t "But I left without a word. "
    scene black with fade
    centered "Meanwhile"
    scene s9
    with d
    sc "Yaaaaawnn...it's morning."
    sc "I need to take a shower and then get some breakfast. I wonder if [name] is back?"
    scene s10
    with d
    sc "Yawnn...I didn't get enough sleep."
    sc "I can't stop worrying about [name]. What if he's in danger? And what if he never comes back?"
    sc "Sigh... I'm overthinking, no! He's fine, and he'll be back."
    sc "Alright, let's take a shower."
    scene black with fade
    scene mcs1
    with d
    mc "So... Lucy and Scarlet are best friends."
    mc "I wonder how Lucy will react when she finds out that Scarlet is my [ss]."
    mc "But Lucy's hot as hell, and thinking about her gives me a hard-on"
    mc "......"
    mc "I think I'll go to Scarlet's room and ask her about the guild."
    scene black with fade
    scene s11
    with d
    sc "[name]? [name]!!! You back?"
    mc "What? Scarlet, what are you doing here? I just got out of the shower!"
    mc "Hey... Wait... Wait... Wait... What?"
    "She runs to you and gives you a big hug."

    scene mchug
    with d
    mc "Hmm... Scarlet? I'm naked! What's wrong? "
    sc "What's wrong? You are an idiot! I was worried about you, you idiot... You've been gone for three days without a word, and I couldn't even call you by phone."
    mc "Don't worry, I'm here!"
    scene mchug1
    with d
    sc "I thought you might be in danger or that the Dark Guild had attacked again and… And… (sniff…) they killed you? Just because they know that you're my [br]."
    sc "And I was afraid you'd left me alone forever."
    mc "Don't worry Scarlet, I'll never leave you."
    t "I think I'll have to tell her that the reason I've been gone for three days was the Dark Guild attack on [l]."
    t "But not right now, it's too much for her."
    mc "Wait! Why would they want to kill me if they know that I'm your [br]?"
    sc "You idiot, of course, because of my position as a guild deputy in the \"{b}{i}Outong{/i}{/b}\""
    mc "Guild deputy? You? Really? Why didn't you tell me?"
    sc "Because if you knew about my position, you might think I'd give you an easy way to join the guild."

    "........."
    "...."
    sc "Huh....!"
    mc "Hmm... Scarlet?"
    t "Fuck... My cock still hard from before, did she notice?"
    sc "I'm sorry, I got carried away."
    sc "Give me a second."
    scene black with fade
    scene s12
    with d
    sc "Hey... You got a boner just because I hugged you? I am your [ss]! You know! "
    mc "Uhm..it's not what you think,"
    sc "Okay, I'll leave you alone then, but we must have a serious talk after this!"
    mc "Okay, and I have a question for you too."

    scene black with fade
    "You finish your shower and then you have breakfast with Scarlet"

    scene s8
    with d
    mc "I'm sorry Scarlet, I made you worry, so I want to make it up to you!"
    sc "It's okay, now that you're back safe and sound, I'm relieved."
    sc "So...[name] will you explain to me why you were gone for three days without a word, making me worry?"
    mc "Okay, ehm..."
    t "I'm not sure if I can tell her about Dark Guild yet because she might think that I'm still weak. Shit...what should I do?"
    menu:
        "Tell her the truth[scarletp]":
            $ scarlet_point += 1
            mc "Three days ago while I was walking around, I fought with Dark Guild members."
            sc "WHAT... Really? You fighting with Dark Guild members! Were you alone, and how many were there?"
            mc "Well, actually as I walked by, I saw your best friend, Lucy. She was being attacked by three of them."
            sc "Lucy? You know that she's my best friend?"
            mc "Well, yes, she mentioned about you."
            sc "So… does Lucy know that you're my [br]?"
            mc "No, she's doesn't!"
            sc "Okay, what happened? "
            mc "So I helped her, and I killed two of them, but I was exhausted. Luckily Lucy saved me, by killing the last one, and I fell unconscious."
            mc "I didn't know what happened after that, but when I'm woke up, I was in Lucy's house."
            t "I can't tell her that I'm a Mage, and of course, about me sleeping with Lucy in her room, she doesn't need to know those things for now."
            sc "I'll talk with Lucy later."
        "Lie":
            mc "Well, as I was walking around, I went into a forest, and got lost."
            mc "And it took me three days to find my way back."
            sc "Really? Do you think I'll believe that? I know you aren't telling me the truth, but whatever. I'm sure you have your reasons for keeping it to yourself. "



    sc "Listen, [name], I have to go on a mission, and I'll be back tonight."
    mc "Okay then, good luck."
    scene black with fade
    "......."
    mc "Oh fuck... I forgot to ask her about the Guild, but I can ask her tonight."
    "(Beep beep...) you got a message"
    scene mcp
    with d
    mc "Oh, it's from Lucy! She wants me to come to the park right now?"
    t "hmm... I wonder what she wants?"
    mc "I think I'll go see her."
    scene black with fade
    "............"
    scene prk
    with d
    mc "There she is, and who's that sitting next to her? "
    mc "Let see!"
    ".........."
    scene prk0
    with d
    t "Looks like Lucy's sister"
    ".........."
    t "If I remember, Lucy said her name is... vonia? vonvon?... viona?"
    scene black with fade

    scene prk1
    with d
    mc "Hey, Lucy! And...?"
    v "Viona, my name's Viona."
    mc "Nice to meet you Viona my name's [name]"
    l "Hey [name] I invited you here for my sister, she wants to talk with you!"
    mc "So...Viona, what do you want to talk with me about?"
    v "hmmm....hey [name], I just want to say thank you — my sister told me that you saved her from the Dark Guild."
    scene black with fade
    "Beep Beep..."
    scene prk2
    with d
    "........."
    l "I'm sorry guys, Scarlet says that she needs my help, so I have to go. I leave you two alone bye-bye..."
    v "Hey... Lucy, wait!"
    v "Sigh.....!"
    scene black with fade
    scene prk3
    with d
    v "You know what? Lucy told me she was investigating Dark Guild members' activity, but she got caught."
    v "And when the Dark Guild wanted to kill her, you came and saved her. As adventurers we know well that the danger is always there."
    v "But still, she's my sister."
    scene prk4
    with d
    v "I'm very grateful that she's safe! You know she's important to me! "
    v "I don't know what would have happened to my sister if you hadn't come to save her."
    mc "Well, I can't just ignore a damsel in distress."
    v "Oh, such a gentleman, I think you're a nice person. I wonder if I was in danger would you want to save me too?"
    menu:
        "Yes Of Course[vionap]":
            $ viona_point += 1
        "Maybe":
            $ viona_point += 0
        "No[vionan] ":
            $ viona_point -=1


    v "Hahaha... Don't worry. I'm just kidding. I'm stronger than Lucy."
    "........"
    "...."

    scene black with fade
    "You chatted with Viona for a while."
    scene prk5
    with d
    v "Hey [name], I'm sorry you ended up endangering your own life for the sake of saving my sister."
    v "And I'm so sorry I didn't know you were in Lucy's room at that time because I'm still on mission and not at home.."
    v "I mean ehm... You slept in her room, and Lucy said that you and her....?"
    mc "Ehmmm... we're not...."
    v ".........."
    mc ".........."
    v ".........."
    mc ".........."
    t "Shit... this is awkward "
    mc "Viona! I think I have to go..."
    scene prk4
    with d
    v "WAIT!"
    v "I want to show you my secret. It's not something that I'll show to anyone, even my sister."
    t "Hmm... show her secret to me, but not to anyone, even her sister, could this be...? No... No, it's not something like that"
    mc "So what do you want to show me?"
    v "Follow me!"
    mc "Okay, lead the way."
    jump v002
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
