define i0 = Character ("???", color="#00ff00", who_outlines=[ (3, "#000") ], image = "iface", window_left_padding=5)
image side iface = "indisface.png"
define ti = Character ("???", color="#00ff00", what_italic=True, what_color="#00ff00", who_outlines=[ (3, "#000") ], image = "iface", window_left_padding=5)
image side iface = "indisface.png"
define i = Character ("Indis", color="#00ff00", who_outlines=[ (3, "#000") ], image = "iface", window_left_padding=5)
image side iface = "indisface.png"

define mv = Character ("Mysterious Voice", color="#8F00FF", who_outlines=[ (3, "#000") ], window_left_padding=5)
define h0 = Character ("???", color="#8F00FF", who_outlines=[ (3, "#000") ], image = "hface", window_left_padding=5)
image side hface = "hface.png"
define h = Character ("Harmonia", color="#8F00FF", who_outlines=[ (3, "#000") ], image = "hface", window_left_padding=5)
image side hface = "hface.png"
define th = Character ("Harmonia", color="#8F00FF", what_italic=True, what_color="#8F00FF", who_outlines=[ (3, "#000") ], image = "hface", window_left_padding=5)
image side hface = "hface.png"

define unq = Character ("???", color="#FF0000", who_outlines=[ (3, "#000") ], image = "qf", window_left_padding=5)
image side qf = "qface.png"
define tunq = Character ("???", color="#FF0000", what_italic=True, what_color="#FF0000", who_outlines=[ (3, "#000") ], image = "qf", window_left_padding=5)
image side qf = "qface.png"

define tz = Character ("Zack", color="#0000FF", what_italic=True, what_color="#0000FF", who_outlines=[ (3, "#000") ], image = "zf", window_left_padding=5)
image side zf = "zackface.png"
define un1 = Character ("???", color="#000", who_outlines=[ (3, "#000") ], window_left_padding=5)
define cr = Character ("Creature", color="#808080", who_outlines=[ (3, "#000") ], window_left_padding=5)

$ alhr = 0

label v008:
    centered "Next Day."

    scene 0080
    with d
    a "Wow, this is so different from what I expected."
    mc "Hmm...what do you mean, Alice?"
    a "I'm surprised that the inside of this guild building is so different from what the outside looked like and it's really big."
    mc "I forgot to tell you that it looks like an old building on the outside because that was the taste of the guild master."
    mc "He likes ancient things, and when I first came to the guild, I even felt like I was in another building once I came inside."
    "........."
    a "I hope the Guild Master is willing to help me."
    mc "Believe me, he will definitely help you."
    mc "Are you nervous, Alice?"
    scene 0081
    with d
    a "Yeah, I'm a little nervous."
    mc "You don't need to be nervous, Alice! I'm here with you."
    scene 0082
    with d
    a "Yes, thank you, [name], and I hope I'm accepted into this guild."
    mc "Oh come on I told you, you will definitely be accepted here."
    mc "Let's go to see the guild master."
    a "Ok..."
    scene 0083
    with d
    tz "Isn't that [name]? Who is the girl with him."
    tz "Damn I don't want to meet him now, but he must have seen me."
    scene black with fade
    scene 0084
    with d
    z "Hi, um... Senior how are you."
    mc "Oh hi Zack, I'm fine how about you? I heard from the guild master that you were injured in our duel. I hope it's not too bad."
    scene 0085
    with d
    z "Yeah it's not a serious wound."
    mc "I'm sorry I wasn't able to control my strength at that time."
    scene 0087
    with d
    z "Don't worry — anyway it was my own fault."
    tz "To be honest my wound is still not healed, but I'm ashamed to tell him."
    scene 0086
    with d
    z "I mean I shouldn't have challenged you at that time. Because you were personally invited by Viona, I should have known that you have great power."
    z "As far as I know, Viona has never invited someone personally, and usually she's always cold to people she hasn't known for long. She is always cold to me, even though I've been a Guild member for quite a while."
    mc "Oh is that true?"
    z "Yes that's true."
    t "Hmm... always cold to people she hasn't known for a long time, huh? But she's always been nice to me."
    z "By the way who is this girl next to you?"
    mc "Oh yes, I forgot to introduce her to you. This is Alice. She is my friend and I asked her to join our guild, so I want her to meet the Guild Master."
    mc "Alice, this is Zack. He is an elite member in our guild."
    scene 0088
    with d
    a "Uhm...hi, nice to meet you."
    scene 0087
    with d
    tz "Looks like she doesn't have any special abilities. If she doesn't have the ability, for sure she won't be accepted here, could this girl also be a mage?"
    tz "Ah, never mind — it doesn't matter to me. The most important thing for me right now is to quickly heal my wounds."
    scene 0086
    with d
    z "If you want to meet with the Guild Master you should do it immediately, because he said that today he will attend a meeting with the other Guilds."
    z "Okay, I'll leave now, see you later senior..."
    scene black with fade
    scene 0088
    with d
    a "Is he really an elite member here?"
    mc "Yes sure, don't you believe it?"
    a "I didn't mean that, it's just that he actually calls you senior. Shouldn't the senior be the one who joined first?"
    mc "I told you."
    scene black with fade
    scene 0089
    with d
    mc "Let's go."
    "........."
    scene 00810
    with d
    mc "Hey look! It's Guild Master. He seems to be talking with Viona about something."
    mc "Let's go meet him."
    scene 00811
    with d
    v "Yes, I'll ask them to come here right away."
    g "It is not necessary — they are already here."
    scene 00812
    with d
    v "Hmm... what?"
    scene 00813
    with d
    v "Oh hi, [name]."
    scene 00814
    with d
    v "Hi, Alice."
    scene 00813
    with d
    v "I'm glad you two are here."
    v "You know I about to go see you two and ask you to come here."
    scene 00815
    with d
    mc "Oh really? Then you're in luck haha..."
    scene 00813
    with d
    v "Yes I am,"
    v "But I'm glad you're fine."
    scene 00815
    with d
    mc "What do you mean, Viona? Of course I'm fine."
    scene 00813
    with d
    v "Well, I thought you'd still be laying in bed after your fight with the dragon yesterday."
    scene 00815
    with d
    mc "Come on it was just an ordinary fight."
    scene 00813
    with d
    v "Ordinary fight, huh? Are you serious? Yesterday you looked totally wiped out."
    scene 00815
    with d
    mc "I... sigh, okay I admit it, it was a tough fight for me because it was my first experience, but it didn't kill me because you helped me, right?"
    scene 00813
    with d
    v "Well, however I was amazed with you, [name]."
    scene 00814
    with d
    v "Hey Alice, how are you?"
    scene 00816
    with d
    a "Oh, thanks for asking, I'm fine, thanks to the guild members who helped me."
    scene 00817
    with d
    v "I'm glad you're fine, and I think I know why you came here."
    v "You definitely want to meet the Guild Master, right?"
    scene 00816
    with d
    a "Uhm...yeah."
    scene 00817
    with d
    v "Then you've met him now because the person next to me is the Guild Master, and his name is {i}Kampretus."
    scene 00816
    with d
    a "Nice to meet you Guild Master {i}Kampretus."
    scene 00818
    with d
    g "So you are Alice? I've heard about you from Viona."
    g "And you came here wanting me to help you to find out about something inside you?"
    scene 00819
    with d
    a "Yes, that's true Guild Master {i}Kampretus{/i} are you willing to help me?"
    a "And besides that, if you allow me, I also want to join 'The Outong'."
    scene 00818
    with d
    g "Hmm... alright, of course I will help you, but first, just call me Guild Master while in the Guild."
    g "And whether you can join the Guild or not it depends on you — if you don't have ability or talent, I can't allow you to join my Guild because this Guild only accepts certain people."
    g "Do you understand, Alice?"
    scene 00815
    with d
    mc "But Guild Master! I asked her to join the Guild. Is it true that if she doesn't have the ability she won't be allowed to become a member?"
    scene 00820
    with d
    g "That's right, even though you personally invited her, she can only be accepted as a member if she passes the test of her ability or talent."
    scene 00815
    with d
    mc "Then why did you immediately accept me without giving me any test?"
    scene 00820
    with d
    g "I accepted you because you demonstrated your ability by defeating Zack. I considered that to be a test for you."
    g "Do you understand, [name]? And after all, you are also a Mage. Everyone knows that a Mage has sufficient ability."
    scene 00815
    with d
    mc "But even if she doesn't have the ability could you make an exception for her so she can become a member of the guild?"
    scene 00820
    with d
    g "I can't. It's the rule. I know that you asked her to become a member of the Guild because you want her to be safe, right?"
    g "Even so, I don't think you listened carefully to what I said before."
    scene 00815
    with d
    mc "Huh? what do you mean?"
    scene 00820
    with d
    g "I told you that in order to become a member, a person must at least have a good ability or talent and pass the test from me."
    g "Which means even if she doesn't have the ability, as long as she has good talent I can help train her and I will of course accept her as a member."
    g "You don't have to worry anyway — you guys said that Alice has something special in her, right?"
    scene 00815
    with d
    mc "But..."
    scene 00821
    with d
    a "I understand Guild Master, even though I don't have the ability I will accept a test from you."
    scene 00818
    with d
    g "Well, I will not test your abilities because I know you haven't the ability yet. Instead I will only test your talents, while also helping you to find out about something inside you."
    g "I will use my magic power, but I warn you that this may be painful for you, are you ready?"
    scene 00822
    with d
    "Alice is looking at you."
    menu:
        "Nod to her[alicep]":
            scene 00823
            with d
            $ alice_point += 1
            a "(Smile)"
            a "Yes, I'm ready."
        "Do nothing":
            a "Uhm..yes.."
    scene 00824
    with d
    g "I'll start, get ready."
    scene 00825
    with d
    a "Yes."
    scene 00826
    with d
    play sound "sounds/aura.ogg"
    ""
    scene 00827
    with d
    "........."
    "......"
    "..."
    mc "Hey Viona! How long does this sort of thing usually take to finish?"
    scene 00828
    with d
    v "I'm not sure. It depends on each person, sometimes it can be long sometimes it can be short."
    v "In this process, they can't be bothered, so we have to wait for them to finish."
    scene 00829
    with d
    mc "If we talk like this will it bother them?"
    scene 00828
    with d
    v "Don't worry, they won't be influenced by something from outside so they won't hear what we say."
    scene 00829
    with d
    mc "Are you sure about that?"
    scene 00828
    with d
    v "Yes, I am very sure. By the way, how is your [ss]'s condition, has she recovered?"
    scene 00829
    with d
    mc "Yes, she said she only needs one more day of rest and she will be back to normal."
    mc "What about Lucy? Is she okay?"
    scene 00828
    with d
    v "Ho ho ho, are you worried about her?"
    scene 00829
    with d
    mc "What do you mean, Viona? Of course I'm worried, she's my friend."
    scene 00828
    with d
    v "Don't worry, she's fine. The last time I saw her she was enjoying her time."
    a "(Groan)"
    mc "Alice!?"
    scene 00825
    with d
    ""
    scene 00830
    with d
    a "Hngg..."
    scene 00827
    with d
    mc "Viona! Will Alice be alright...?."
    scene 00828
    with d
    v "Don't worry, she's fine, something like this is normal."
    scene 00829
    with d
    mc "Oh really? I thought something bad was happening to her."
    scene black with fade
    "A few minutes later."
    scene 00818
    with d
    g "I've finished testing your talent. You have good talent so I accepted you as a member of the Guild."
    scene 00819
    with d
    a "Oh really? Thanks, Guild Master. What talent do I have?"
    scene 00818
    with d
    g "According to my observations, your talent is that you can become a Mage like us."
    g "Because I see you have great potential in that area."
    g "From now on you should come here every day to practice. In our Guild library we have some good books it will be very useful for you to study."
    g "And of course I'll help you myself."
    scene 00817
    with d
    v "I'll help you too, Alice."
    scene 00819
    with d
    a "Thank you."
    scene 00815
    with d
    mc "Then about something that is inside Alice, do you already know about it, Guild Master?"
    scene 00820
    with d
    g "About that, to be honest I'm still not sure just what it is, but there is definitely something special."
    g "Since Alice doesn't have a foundation in mana control, it's hard for me to be sure, so I want Alice to practice first, and later I will try to find out again."
    scene 00815
    with d
    mc "If you have trouble finding it out, how can the enemy know and want something that is inside Alice?"
    scene 00820
    with d
    g "I'm sure they have something that can detect a certain kind of power."
    scene 00818
    with d
    g "Alice! Go with Viona — she will show you the Guild library and I will get some relics from the storage room to help you."
    scene 00820
    with d
    g "And [name], would you wait for me in my training room? I have a special mission for you."
    mc "Special mission?"
    g "Yes."
    scene black with fade
    scene 00831
    with d
    t "Well at least I'll go to the toilet first."
    ca "Hey [name]!"
    scene 00832
    with d
    mc "Oh, hi Carol, how are you?"
    scene 00833
    with d
    ca "I'm fine, how is Scarlet's current condition?"
    scene 00834
    with d
    mc "She's fine, she told me she only need a day of rest before she can go back to her usual activities."
    scene 00833
    with d
    ca "That's good, so [name] do you have free time today?"
    scene 00834
    with d
    mc "I don't think so. It looks like I'll be busy today. Guild Master told me he has a special mission for me today."
    mc "Why do you ask?"
    scene 00833
    with d
    if carol_point >=1:
        ca "Oh well, I just wanted to treat you to a few drinks, you know, as my thanks for helping save Cindy."
        ca "Since you'll be busy today, how about another time? That is if you want to have a drink with an old woman like me."

        menu:
            "Accept her offer[carolp]":
                $ carol_point += 1
                mc "Of course I will accept your offer."
                ca "Great."
            "Reject her offer":
                mc "Hmm... I will think about your offer after I complete the mission."
                ca "Oh, Okay."
    else:
        ca "Oh it's nothing — Cindy told me that she wanted to meet you."
    scene 00833
    with d
    ca "Well, hey [name]! You said you got a special mission today?"
    scene 00834
    with d
    mc "Yes that's what I said."
    scene 00833
    with d
    ca "Because you are new, I guess you don't know about the mission levels in this guild."
    scene 00834
    with d
    mc "Mission levels?"
    scene 00835
    with d
    ca "Yes, basically all missions in the Guild have a level. The lowest level of mission is level {i}'F'{/i} and the highest is level {i}'S'{/i}."
    ca "For example, a level {i}'F'{/i} is a simple mission that all guild members are sure to easily complete."
    ca "And your special mission is rated level {i}'B'{/i}, where only members who meet the special requirements can get this mission."
    ca "And you should know that usually new members only get missions with a maximum level of {i}'D'{/i}, but because you are a Mage it's no wonder you get a mission with a {i}'B'{/i} level."
    ca "Because mission levels are based on the level of difficulty and potential danger that exists."
    scene 00834
    with d
    mc "Oh I see, now I know that there are levels on a mission."
    mc "If a special mission is rated at level {i}'B'{/i}, then how difficult and dangerous is a level {i}'S'{/i} mission?"
    scene 00835
    with d
    ca "For mission level {i}'S'{/i} I do not know how difficult and dangerous it is, because I have never been on a mission at level {i}'S'{/i}, what is clear is the difficulty and danger exceeds almost anyone's ability."
    ca "It has been widely reported that many people from various guilds fail to complete missions at level {i}'S'{/i}, and as a result they never come back alive."
    ca "For our guild, there is only one person who has ever successfully completed a level {i}'S'{/i} mission."
    scene 00834
    with d
    mc "What? Only one person? Who is this strong person that you mean? Is it {i}Viona?"
    scene 00836
    with d
    ca "No, it wasn't Viona. Her name is {i}'Yola'."
    ca "If she was still here you could definitely meet her."
    ca "Unfortunately she's no longer in our guild."
    scene 00837
    with d
    mc "What happened to her?"
    scene 00836
    with d
    ca "I don't know. It's weird because when she successfully completed the mission she looked the same as usual."
    ca "We had a party inside the Guild to celebrate her success in completing a level {i}'S'{/i} mission."
    ca "She was here in the Guild among the guild members at the party when suddenly she disappeared without a trace."
    ca "All the guild members have searched for her but no one has found her."
    scene 00837
    with d
    mc "Did the Guild Master know at that time?"
    scene 00835
    with d
    ca "I'm not sure about that, but right before she disappeared I saw her talking with him."
    ca "So I asked the Guild Master about this, and he said he didn't know anything about Yola's disappearance. It's just that I felt like the Guild Master was hiding something."
    scene 00837
    with d
    t "Hmm... it sounds strange. How could someone disappear without a trace in a crowd without anyone knowing what had happened."
    t "......"
    t "Ah shit, I can't stand it anymore, I have to go to the toilet right away."
    scene 00834
    with d
    mc "Uhm... hey Carol, sorry, actually I still want to talk with you, but I have to go to the toilet first, so see you later."
    scene black with d
    centered "After a while"
    scene 00838
    with d
    t "I remember that when I was unconscious after the duel with Zack, the Guild Master brought me here. So this is his special training ground."
    "........."
    "......"
    "..."
    t "Hmm... why is the Guild Master not here yet? Am I waiting in the wrong place? No, surely he is still busy helping Alice."
    t "Alright then, while I wait for him, I will practice improving my magic. After all, he said this is a training ground, right?"
    t "Looks like a suitable place under the tree."
    scene black with fade
    scene 00839
    with d
    t "Well it's time to practice."
    "........."
    "......"
    "..."
    t "Hmm... weird. Why can't I absorb the mana in here? Let's try again."
    "........."
    "......"
    "..."
    t "This is really weird. I can't absorb the mana here even though I feel it is so abundant."
    scene 00840
    with d
    t "I remember when the Guild Master helped me when I was lying on that black stone — maybe if I move there I could absorb mana."
    t "Alright then I'll move there."
    scene black with fade
    scene 00841
    with d
    t "Well, let's try again."
    "........."
    "......"
    "..."
    t "What the heck, it's the same here too! I really can't absorb the mana."
    scene 00842
    with d
    g "Looks like you can't absorb the mana here? Correct?"
    scene 00843
    with d
    mc "Oh, Guild Master ehm...yeah I was trying to train my magic power a little here, but I really can't absorb the mana here."
    mc "Can you tell me about this, Guild Master?"
    scene 00844
    with d
    g "Of course."
    g "You will not be able to absorb the mana in this place because of the black stone you are sitting on."
    scene 00843
    with d
    mc "What's wrong with this black stone I'm sitting on?"
    mc "I don't feel anything strange about this stone at all."
    scene 00844
    with d
    g "I will tell you that the black stone is not an ordinary stone but a magic stone."
    g "The stone contains earth elements as well as natural elements which are very strong. With the black stone here, the amount of mana here increases."
    scene 00843
    with d
    mc "Where did this stone come from? And what is the connection why I can't practice here with this stone here?"
    scene 00844
    with d
    g "I accidentally found the stone in an adventure and I brought it here."
    g "The reason you can't train here is because your main magic element isn't earth element or natural element so..."
    scene 00843
    with d
    mc "But I can use magic with those two elements and..."
    scene 00844
    with d
    g "If you're still curious then you better let me finish talking first."
    scene 00843
    with d
    mc "Oh, I'm sorry."
    scene 00844
    with d
    g "So as I said before, the reason you can't practice here is because your main magic element isn't earth element or natural element."
    g "Even though you can use all kinds of magic element it will be useless if your main element is not earth element or natural element."
    g "Besides, that black stone naturally seals this room so if you want to practice here you must have at least one of the two elements I mentioned earlier."
    g "Seeing the results of your duel with Zack when you lost control, I can conclude that your magic has the main element of fire, and luckily at that time Viona there was who has water elemental magic so she could suppress your magic power."
    scene 00843
    with d
    t "Hmm... I see. That must be why I was in so much pain when Viona tried to stop me because her main magic element is water while my main magic element is fire."
    t "Two opposing elements of magic."
    mc "Guild Master I have a question, can the main magic element change if we continue to train the other elements?"
    mc "I mean the main element of my magic is fire, but if I continue to train other elements such as earth or water elements, can my main magic element change?"
    scene 00844
    with d
    g "I understand your question and the answer is no. You can't change your main magic element because it is the basis of magic for a Mage."
    g "Even though you can use other magic elements, still your main magic element will not change."
    scene 00843
    with d
    mc "Ok I understand now. What special mission will you give me?"
    scene 00844
    with d
    g "Actually I was not sure about giving you this mission because it might be dangerous."
    g "But after seeing your ability, I again considered giving this mission to you because maybe only you can do it."
    scene 00843
    with d
    mc "Tell me what mission it is?"
    scene 00844
    with d
    g "Well, your mission is..."
    scene black with fade
    "..........."
    "......."
    "..."
    scene 00843
    with d
    mc "I understand, and I will accept the mission."
    scene 00844
    with d
    g "Then get ready because you will leave now. The place is so far you won't get there until tomorrow."
    scene black with fade
    "........."
    "......"
    "..."
    scene 00845
    with d
    un "Is this the right place? I don't see anything dangerous here."
    scene 00846
    with d
    un1 "Yes this is the place, don't be careless, stay focused."
    scene 00845
    with d
    un "Come on dude there's nothing here. It's just a waste of time. We better go back and report that the mission has been completed even though we haven't done anything here."
    scene 00846
    with d
    un1 "We can't do that. Would you be willing to take the risk of getting caught making a fake report?"
    scene 00847
    with d
    un1 "Not only would we be kicked out of the Guild, but we'd also be punished. I don't want that."
    un1 "Besides, if there was nothing here, there's no way this would be a high-paying quest."
    scene 00845
    with d
    un "But isn't it a little strange? They say that people always go missing in this place. Moreover, cases of missing people only occur in adult males."
    scene 00847
    with d
    un1 "Yes ,to be honest I also feel a little strange about this quest, but I believe that they were not kidding."
    un1 "Refocus and look for helpful hints."
    scene 00848
    with d
    un "Sigh... Okay I understand I'll... huh?"
    un "Ughh... What happened to me? Hey dude! what happened? I can't move!"
    un "HEY! HELP ME!"
    scene 00849
    with d
    un1 "What's wrong? Why are you screaming?"
    un1 "Huh? What's wrong with my body? I... I can't move."
    un1 "Oh, damn is this the enemy's doing? Ughh..."
    scene black with fade
    "........."
    "......"
    "..."
    scene 00850
    with d
    t "Hmm... according to reports this is the place."
    t "From the reports I received a lot of people go missing here, and all of them are adult males."
    t "If you look around here it's nothing, but I can feel the magic energy fluctuating here."
    t "Maybe this is illusion magic or disguise magic — I will try to use magic on my eyes to improve my eyesight."
    play sound "sounds/aura.ogg"
    scene 00851
    with d
    t "Huh...! I can't move my body!"
    t "Damn it looks like this will be a little difficult. I will ignore that my body can't move, for the time being I have to focus on finding the cause."
    scene 00852
    with d
    "........"
    play sound "sounds/aura.ogg"
    scene 00853
    with flash
    t "Aha! Found you, so this is your doing huh?"
    scene 00854
    with d
    ti "There's another person here."
    ti "Will this time also end as usual?"
    scene 00855
    with d
    i0 "Sigh...I can only hope this time it will work."

    scene 00853
    with d
    mc "HEY! You over there! Is this your doing?"
    scene 00855
    with d
    i0 "Now I'm starting to feel that person talking to me."
    mc "HEY!"
    i0 "Could this be the effect of being here too long? I want this to end soon."
    mc "HEY! can you hear me?"
    i0 "Wait a minute — it looks like he did talk to me."
    mc "HEY! You on the tree, I'm talking to you! Can you hear me?"
    scene 00857
    with d
    i0 "You...you...talked to me?"
    scene 00856
    with d
    mc "Yes, I'm talking to you."
    scene 00857
    with d
    i0 "Can you see me?"
    mc "Of course I can see you."
    scene 00858
    with d
    ti "In the long time I've been here, this is the first time anyone has talked to me or been able to see me."
    scene black with fade
    scene 00859
    with d
    i0 "Hop."
    scene 00860
    with d
    i0 "Hey I ask you one more time can you really see me? And also are you a human?"
    i0 "I know I asked before, but I just wanted to confirm."
    scene 00861
    with d
    t "This woman is starting to piss me off. Doesn't she believe I can see her?"
    t "Wait a minute, I used my magic power to increase my eyesight before, so now I can see what ordinary humans can't see."
    scene 00860
    with d
    i0 "Hey why are you silent?"
    scene 00861
    with d
    t "Hmm... maybe she doesn't know that I'm a Mage?"
    scene 00860
    with d
    i0 "If you won't answer, it's okay, I'll just start as usual."
    scene 00861
    with d
    t "What is she going to do with me? Wait a minute is she going to kill me? Damn I still can't move."
    mc "Hey, wait! Wait a minute, I'll answer you."
    t "I'll try to buy time and distract her while trying to break free."
    mc "You asked if I can see you right? The answer is yes, I can see you, and I am a human, does that answer your questions?"
    scene 00862
    with d
    i0 "So you can really see me and you are human too?"
    scene 00863
    with d
    ti "Hmm... it's strange he can see me and he is also a human, this has never happened before."
    ti "Is the curse getting weaker?"
    t "Looks like I managed to distract her, now I'll take this opportunity to break free using my magic."
    scene 00851
    with d
    play sound "sounds/aura.ogg"
    t "Yeah it worked. Now I can move again."
    scene 00863
    with d
    t "Now to see what she will do to me, I'll pretend I still can't move."
    scene 00862
    with d
    i0 "You know I actually don't want to do this to you because you are the first human who could see me. I actually want to talk to you a little longer."
    mc "What are you going to do to me? Why have you made me unable to move?"
    scene 00863
    with d
    i0 "What am I going to do with you?"
    ti "Hmmm... what should I do with him now? It's quite difficult to determine. If I do as usual maybe he will immediately disappear."
    ti "But if I leave him, he will be taken by a wild animal."
    t "Shit... I won't take the risk that maybe she wants to do something bad to me right now. Fine, I'll take action first."
    scene black with fade
    scene 00864
    with d
    i0 "(Gasp) you...! How can you move? Shouldn't you be unable to move? How is that possible? You can even touch me and not disappear."
    scene 00865
    with d
    mc "Why are you so shocked? I guess you've never met a Mage like me before."
    mc "I tell you I'm not an ordinary human, I have magic power that let me see you and also break free from your traps."
    scene 00864
    with d
    i0 "A Mage? Magic power?"
    scene 00865
    with d
    mc "Yes, so you don't know what a mage is huh?"
    i0 "I know about magic but..."
    mc "Do you think a little illusion and some lowly restraint magic can beat me? I tell you that your trap will be of no use on me."
    scene 00864
    with d
    i0 "But I didn't do that."
    scene 00865
    with d
    mc "And I'm supposed to believe that?"
    scene 00866
    with d
    i0 "(Smile)"
    mc "Hmm... why are you smiling."
    t "Did I say something wrong?"
    scene 00867
    with d
    i0 "I don't care if you believe me or not, I'm just happy that this curse will end soon."
    scene 00866
    with d
    mc "Curse?"
    i0 "Uh-huh..."
    mc "What curse do you mean? Explain it to me!"
    scene 00867
    with d
    i0 "I'll explain it to you, but first I want to know what your name is."
    scene 00866
    with d
    mc "Name? Is that necessary?"
    scene 00867
    with d
    i0 "Yes, because I want to thank the person who will end this curse soon."
    scene 00866
    with d
    mc "Sigh... Ok you can call me [name]."
    scene 00867
    with d
    i "[name], my name is Indis and I am an elf."
    scene 00866
    with d
    mc "Well, enough for the introductions, can you explain about the curse now?"
    scene 00867
    with d
    i "Well, first of all I want to tell you that what makes me invisible to ordinary people and puts restraint magic on them is not me."
    i "It was a curse in this place that happened because I accidentally offended a Demon Queen, and it almost caused war between my people and the demon nation."
    i "To avoid war, I personally came to the Demon Queen to ask for peace and she agreed on one condition that I must accept her curse, and without thinking I immediately agreed to it."
    i "And long story short I was not personally cursed but I was just made to live in this cursed place, but it feels the same to me."
    scene 00866
    with d
    mc "So it's not you who is cursed but this place, and you are forced to live in this place?"
    scene 00867
    with d
    i "Yes, it is true."
    scene 00866
    with d
    mc "If you're not the cursed one why don't you leave here?"
    scene 00867
    with d
    i "I can't leave this place. I've tried many times, but I still can't do it. It is like there is a chain that binds me here."
    i "And I even once thought to end my own life, but that didn't work either."
    scene 00866
    with d
    mc "Then why did the restraint magic activate and attack me?"
    scene 00867
    with d
    i "To be honest, I don't know all about it, but what the Demon Queen told me before I was sent here, is that if I want this curse to be over, I have to have sex with a human or I have to die."
    i "But every time there a human is trapped here, it is always an adult male, and when I touch the trapped person he suddenly disappears without a trace."
    i "So until now I couldn't get out of this place because I've never had sex with humans."
    scene 00866
    with d
    t "Hmm... isn't this really weird, she offended someone from the Demon race and she should be the one who was cursed, but she didn't get cursed and was instead sent to this place."
    t "And what's even weirder is that if she wants the curse to end she has to have sex with a human, but she has never succeeded because when a person trapped here is touched by her, he suddenly disappears."
    t "I think someone who is called the Demon Queen is using Indis to kidnap humans, and naturally Indis will try to meet the requirements to be free so she continues to do it."
    t "I suspect that this Demon Queen must want to get a lot of humans from this place via Indis."
    t "I'm sure this place must have some kind of teleportation array that will activate if Indis touches a trapped person."
    t "Well, this is beginning to make sense. If it's true, I think I understand the cause of the disappearance of people in this place."
    scene 00867
    with d
    i "Hey [name]! I don't care whether you believe in my words or not, but I ask your help to end this curse."
    scene 00866
    with d
    mc "So you want me to have sex with you? To end this curse."
    scene 00867
    with d
    i "Yes that's true, but if you don't want to I won't force you, but instead, please just kill me. If I die this curse will also end. I don't want the humans who come here always disappear."
    i "So please grant one of my requests."
    i "I will not mind and will still be grateful to you even if you kill me."
    scene 00868
    with d
    t "Hmm... what should I do to end this curse? Should I have sex with her or kill her?"
    t "I guess now I know why the Guild Master told me that this mission was only suitable for me."
    menu:
        "I will.."
        "Fuck her":
            mc "Okay I will have sex with you because I don't want to kill you."
            scene 00867
            with d
            i "Do you really want to do that for me?"
            scene 00866
            with d
            mc "Yes, of course I'll free you."
            jump if_start
        "Kill her":

            scene 00869
            with d
            mc "I'm sorry I thought I was going to kill you."
            scene black with fade
            jump if_end


label if_start:
    scene 00870
    with d
    i "So shall we start?"
    scene black with fade
    scene 00871
    with d
    i "Ah..."
    scene 00872
    with vpunch
    with d
    i "Yeah."
    scene 00873
    with vpunch
    with d
    i "Aahh, this feels good, yeah."
    scene 00874
    with vpunch
    with d
    mc "I'm cumming."
    with vpunch
    with flash
    mc "Hngh..."
    play sound "sounds/Ejaculate.wav"
    with vpunch
    with flash
    scene black with fade
    scene 00875
    with d
    ""
    scene black with fade
    scene 00876
    with d
    i "Thank you, [name]. I hope you don't regret having sex with me because this is my first experience doing it."
    mc "I don't regret it. I just wanted to get rid of the curse."
    i "Yes, and now I'm sure the curse is gone."
    mc "How can you be sure the it's really gone?"
    i "I can feel something different in my body now. I feel like there is nothing that binds me to this place anymore."
    scene black with fade
    scene 00877
    with d
    i "Thanks again [name]. Now I can go back to my country."
    mc "How do you go back to your country?"
    i "I will go with my wings."
    scene black with fade
    scene 00878
    with d
    i "Look! Now I can use my wings, which confirms that the curse in this place has completely disappeared because before I could not use my wings at all."
    mc "So you're going to fly back to your country?"
    i "No, I don't need to fly there because with my wings I can go right back there."
    mc "How come?"
    i "It's a secret, if we meet again one day maybe I'll tell you the secret."
    i "Alright, it's time to go."
    scene 00879
    with d
    mc "Hey, did you shrink?"
    i "Yes, it is true."
    scene 00880
    with d
    i "Goodbye [name], I will always remember your name."

    scene 00881
    with d

    scene 00882
    with d

    scene 00883
    with d
    mc "Huh? she disappeared? How could she do that? Forget it, she said it was a secret, and I think she's really left."


label if_end:
    scene 00883
    with d

    mc "I think this mission is over and it's time to go back and report on it."
    mv "{size=-17} Help!"
    mc "What?"
    mv "{size=-17} [name]! Help!"
    mc "Who? Who called me?"
    mc "There's nobody here."
    mv "{size=-17} [name]! Help me!"
    mc "The sound came from over there. I'll go check it out."
    scene black with fade
    ".........."
    "......"
    "..."
    scene 00884
    with d
    ung "My Queen, our field has been ruined."
    scene 00885
    with d
    unq "Yes, I already know about that. You don't have to panic. I will find a solution for this problem."
    unq "What about the last two humans we got?"
    scene 00884
    with d
    ung "For now they still can't be used because they are still unconscious, my Queen."
    scene 00886
    with d
    unq "Then you just wait for them, and once they're ready, use them right away!"
    unq "And one more thing — in the near future I may go to the human world, so please you take care of all the business that is here while I'm away, you understand?"
    scene 00887
    with d
    ung "I understand my Queen, then I'll go back to watch them."
    unq "....."
    tunq "Hmm... how could my curse be removed? Is Indis dead? Or maybe she managed to have sex with a human, but that shouldn't be possible."
    tunq "After I finish my business here with that old bastard, I will immediately go to the human world. I'm so curious to investigate this now."
    scene black with fade
    scene 00888
    with d
    ung "Now all I have to do is wait for them."
    un1 "....."
    un "....."
    scene black with fade
    scene 00889
    with d
    mv "{size=-14} [name]! Help me!"
    t "I think the voice came from within this forest, but if I'm not mistaken, according to the existing reports this is a forbidden forest, and the local people even call it the forest of death."
    mv "{size=-9} [name]! help me!"
    t "Sigh...I actually don't want to go into this forest, but the voice is calling my name and asking for help, so I can't ignore it."
    t "Alright then, I'll go into the forest."
    scene 00890
    pause (0.3)
    scene black with fade
    "..."
    scene 00891
    with d
    cr "(sniff)...(sniff)... grr..."
    scene 00892
    with d
    cr "Grrr...(sniff)...(sniff)..."
    scene 00893
    with d
    cr "Grrr..."
    scene 00894
    with d
    cr "Grrr..."
    mc "What? what creature is that? This is the first time I've seen one, and it looks like it's about to attack me."
    scene 00895
    with d
    play sound "sounds/Fireball.wav"
    mc "Shit, Fireball!"
    cr "Grrr...."
    scene 00894
    with d
    mc "Huh? it didn't work."
    cr "Grrr...."
    mc "So you're quite strong, huh? then try this one!"
    scene 00896
    with d
    play sound "sounds/Fireball.wav"
    mc "FIREBALL!"
    scene black with fade
    scene 00897
    with d
    mc "Phew... I didn't expect that creature to be so strong that I had to use my strongest attack to kill it."
    mv "{size=-8}[name]! Help me!"
    mc "The sound is getting louder, I will soon find the source of the voice."
    scene 00898
    with d
    mc "This place is very foggy."
    scene 00899
    with d
    mc "And here there is a swamp. If I'm not careful I will definitely end up in this swamp."
    mc "Damn, the fog here is getting thicker and blocking my vision."
    scene 008100
    with d
    mv "{size=-5} [name]! Help me!"
    mc "How much farther do I have to go into this forest? But the sound is getting closer."
    scene black with fade
    "After a while you finally found the source of the sound."
    scene 008101
    pause (0.5)
    scene 008102
    pause (0.5)
    scene 008101
    pause (0.5)
    scene 008101
    pause (0.5)
    scene 008102
    pause (0.5)
    mv "[name]! Help me!"
    scene 008101
    pause (0.5)
    mc "Is that purple stone talking? Hey, purple stone! Are you the one talking?"
    scene 008102
    pause (0.5)
    mv "Yes, that's me. Please help me."
    scene 008101
    pause (0.5)
    t "How can the stone talk? Is it some kind of magic stone? Obviously it's not an ordinary stone."
    mc "Hey, how do you know my name?"
    scene 008102
    pause (0.5)
    mv "That's not important, the most important thing right now is please help me."
    scene 008101
    pause (0.5)
    mc "Help you? How and why should I help you?"
    scene 008102
    with d
    mv "Please take me away from here. Believe me, if you help me you will not regret it."
    scene 008101
    with d
    t "It seems like there's nothing to lose if I get the stone."
    mc "Ok I will help you."
    scene 008102
    with d
    mv "STOP! Don't come closer!"
    scene 008101
    with d
    mc "Huh? What's wrong? If I don't come close how can I get you?"
    scene 008102
    with d
    mv "Believe me! please don't move any closer, if you want to take me away it's easy enough. The way is to use your magic power to attack my direction."
    mc "Huh? But..."
    mv "Trust me! Just do it!"
    mc "Hmmm... okay."
    scene 008101_
    with d
    mc "Then take this!"
    play sound "sounds/aura.ogg"
    scene 008103_
    with d
    mc "Huh? So there is some kind of barrier here?"
    scene 008102
    with d
    mv "Yes that's right, and that's why I forbid you to move closer. If you touch the barrier your strength will disappear, so you don't touch it. The only way to remove this barrier is by destroying it from outside."
    scene 008101
    with d
    mc "I can see there is a barrier like this, but if my attack just now didn't work, how can I break through it?"
    scene 008102
    with d
    mv "You have to attack again and again."
    scene 008101
    with d
    mc "Hmm... well, if there is no other choice..."
    scene black with fade
    "After you attacked the barrier again and again, you finally managed to destroy it."
    scene 008101
    with d
    mc "Yeah, I finally made it (pant...) (pant...)."
    t "How can the barrier be this strong? I've completely run out of mana and my body is so tired."
    mc "Hey, I broke the barrier what should I do now?"
    scene 008102
    with d
    mv "Great, now stay there."
    scene 008101
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008103
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008101
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008103
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008101
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008103
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008101
    pause (0.2)
    scene 008102
    pause (0.2)
    scene 008103
    pause (0.2)
    with flash
    with flash
    with flash
    play sound "sounds/quake.ogg"
    scene 008104
    with d
    h0 "Finally."
    scene 008105
    with d
    h0 "After a long time."
    scene 008106
    with d
    h0 "I'm free."
    scene 008107
    with d
    h0 "......"
    scene 008108
    with d
    h0 "......"
    scene 008109
    with d
    h0 "Hey, thanks for helping me."
    mc "Wait...!wait...! You're too close."
    h0 "Oh sorry."
    scene 008110
    with d
    t "Oh fuck, why is she naked, and fuck she's hot? That makes it hard to stay focused."
    h0 "So since you've helped me I'll be your master."
    scene 008111
    with d
    mc "What? Wait a minute! Wait a minute."
    mc "I don't know who you are, and I also don't know how you could emerge from that purple stone, and also why you suddenly offered yourself to be my master. What do you mean by that?"
    scene 008110
    with d
    h0 "Alright, I'll introduce myself to you first."
    h "My name is Harmonia, and actually the purple stone is a seal that I made myself, but unfortunately this seal has a side effect, once the seal is active there is a barrier protecting it, and that is what kept me trapped here."
    scene 008111
    with d
    mc "What? Wait a minute! It doesn't make any sense. If you made it yourself, why did you need to ask for my help, and also why did you decide to seal yourself in that purple stone?"
    scene 008110
    with d
    h "Well, I honestly don't want to tell you about this because it is my personal business, but if you want to know I can tell you."
    menu:
        "I want to know":
            scene 008111
            with d
            mc "Tell me everything! I want to know why you sealed yourself."
            scene 008110
            with d
            h "Okay if you really want to know I'll tell you, but I'll keep it short."
            h "At that time I was in a life or death battle, and because there were too many enemies, I could not survive — I was seriously injured and almost killed."
            h "Fortunately, I had a special relic that helped me to escape from the enemy, but my wound was so serious I would not have lasted much longer. I really almost died at that time."
            h "So I sealed my own body in the purple stone and within that stone I could heal my own wounds. Unfortunately the seal I made was not perfect."
            h "So it caused side effects like I said."
            scene 008111
            with d
            mc "And the side effect is the appearance of a barrier that can only be destroyed from the outside? So if no one outside helped you, you would stay inside that barrier forever? And that's why you asked for my help?"
            scene 008110
            with d
            h "Yes, that's right, and the barrier also suppresses my strength, so I can't destroy it myself."
            h "The only way to get out of the barrier is to destroy it from the outside."
        "I am not interested ":
            scene 008111
            with d
            mc "Well, if you don't want to say, it doesn't matter because I'm not interested in your story."
            h "Sure."
    scene 008111
    with d
    mc "Well now I've helped you, I have two questions for you."
    mc "The first is how could you know my name and call me from a distance?"
    mc "And second, isn't it a little strange that I helped you, but you want to be my master — shouldn't I be your master?"
    scene 008110
    with d
    h "I will answer your questions."
    h "First, I can know your name and call you from a distance because of my abilities, and I used this ability when I felt someone with magic power was near me who might be able to help me. That person was you."
    scene 008111
    with d
    t "So that's her ability. If I could learn it, maybe it would be of use to me."
    mc "What is that ability? Can you teach me?"
    scene 008110
    with d
    h "Unfortunately, even if I tried to teach it to you, this ability can't be learned, so don't expect to be able to do it."
    h "And for your second question it is clear that I will be your master, because I am much stronger than you."
    scene 008111
    with d
    t "Damn, it's getting hard to focus because of her naked body, and I'm starting to think about fucking her."
    t "Shit, I gotta focus."
    mc "So you're much stronger than me? Really?"
    scene 008110
    with d
    h "Of course, and I will not argue with you."
    scene 008111
    with d
    mc "Why are you so eager to be my master? What's in it for you?"
    scene 008110
    with d
    h "The first reason is you're still too weak."
    h "The second reason is this is a gift that you get out of my gratitude for releasing me, so I will make you even stronger."
    h "And the third reason is, after you get stronger, I want you to find something that is missing from me."
    h "For those reasons, I have decided that starting today I will be your master, so you should call me master hehe..."
    scene 008111
    with d
    mc "When did I approve of you as my master? After all...."
    scene 008110
    with d
    h "Enough!" with vpunch
    t "Huh? What happened? I feel intimidated."
    h "You know? I've been watching you. You look so tense. What are you thinking?"
    scene 008111
    with d
    t "Of course I'm tense. It's because you're naked in front of me, and it makes me horny."
    t "Shit should I say that?"
    scene 008112
    with d
    h "Hmmm...?"
    th "Oh, I didn't realize I was naked right now. This must be a side effect of that seal, so that my clothes are gone, so I've been talking to him while naked?"
    scene 008111
    with d
    h "Hmm... hmm... hmm..."
    scene 008110
    with d
    h "Could it be that you became aroused by seeing my naked body?"
    t "Oh fuck, is that obvious? Wait, is she teasing me?"
    h "Do you want to have fun with me?"
    t "What!? Is she serious?"
    h "Don't worry, I know you want to do it."
    scene 008113
    with d
    h "(Snapping finger)"
    mc "Huh? Why am I naked? Where are my clothes?"
    h "Come on you don't need them right now, right? Don't you want to do it with me?"
menu:
    "[jeegreen]Yes":
        mc "Yeah, I do."
        h "If so then..."
        jump hf_start
    "No":
        mc "I'm sorry, but I can't do this with you. Can you return my clothes to me?"
        h "Really? Okay then, I'll return your clothes."
        h "(Snapping fingers)"
        jump hf_end

label hf_start:
    scene black with fade
    scene 008114
    with d
    mc "Hey, what are you doing?"
    h "Don't worry! I know you're tired after using all your magic to destroy the barrier earlier, so I'll do it for you and you don't have to do anything."
    scene 008115
    with d
    h "Oh, wow you're already so hard. You must have been holding it for a long time."
    th "Looking at the size, it looks big enough for me."
    th "And... to be honest I've never done this."
    scene 008116
    with d
    h "Then let's start with this first."
    scene 008117
    with d
    scene 008118
    with d
    scene 008117
    with d
    scene 008116
    with d
    scene 008117
    with d
    scene 008118
    pause (0.4)
    scene 008117
    pause (0.4)
    scene 008116
    pause (0.4)
    scene 008119
    with d
    h "Well I think this is enough — let's start fucking."
    th "You will be my first."
    mc "......."
    scene 008120
    with d
    h "You see! Mine is getting wet."
    h "As I told you, this is the first time for me."
    scene 008121
    with d
    h "Oh aahh this...it's already in."
    scene 008122
    with d
    h "Aaahh...."
    th "I can feel it. So this is how a cock feels? It really rips me ups."
    play movie "mov/gh.webm" loop
    show movie with d
    h "Ohh, yeah..."
    h "Aaahhhh, I can feel it this is really tearing me apart."
    mc "Ugh...I'm going to cum, your pussy is so tight."
    h "You already want to cum? Me too then, let's cum together."
    mc "Ugh... I'm cumming!"
    h "Me too, let's cum!"
    stop movie
    scene 008123
    with d
    h "Aaahhh I'm cummiiiiing...."
    mc "Hng..."
    play sound "sounds/Ejaculate.wav"
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash
    scene 008124
    with d
    h "Pant... pant...this is the best I've ever felt, I can feel your warm cum inside of me."
    h "Aaah..."
    scene 008125
    with d
    ""
    scene black with fade
    scene 008113
    with d
    h "(Snapping finger) There, I returned your clothes."
    mc "Oh, thank you."
label hf_end:
    scene 008110
    with d
    h "So are you ready?"
    scene 008111
    with d
    mc "Ready for what?"
    scene 008110
    with d
    h "Of course, ready to get out of this forest."
    scene 008111
    with d
    mc "Yes I'm ready, but before that, can you cover your body with something? Because it makes it difficult to focus."
    scene 008126
    with d
    h "Ohoho... so you can't focus when you can see my beautiful body?"
    mc "....."
    h "Don't want to answer? Then, what if I do this."
    scene 008127
    with d
    h "You see? What do you think?"
    mc "What do you mean?"
    h "I mean what do you think of the pose I'm making, is this sexy tehehe...?"
    mc "Come on, stop teasing me. We have to go — I think it will be dark soon."
    scene 008113
    with d
    h "Alright... alright... I understand. I'll wear my clothes (snapping finger)."
    scene 008128
    with d
    h "All done."
    scene 008129
    with d
    h "You see? What do you think? Does this outfit work for me?"
    scene 008130
    with d
    ""
    menu:
        "Yes, it looks good(Goddess+1)":
            $ goddess_point +1
            mc "I think it's good and suits you. You look beautiful with it."
            scene 008129
            with d
            h "Really? I was expecting you would say that tehehe..."
        "I don't care":
            mc "Honestly I don't care what you wear."
            scene 008129
            with d
            h "You shouldn't say things like that to your master."
            h "Hmph..."


    scene 008131
    with d
    h "You know, in this forest there are many dangerous creatures and as your master, I will take care of you until we get out of here."
    mc "I can take care of myself."
    h "You're almost out of mana, and I think you will find it difficult to get out of this forest, so you should be behind me."
    mc "I told you I can take care of myself, let's go!"
    scene black with fade
    scene 008132
    with d
    mc "Hmm... Harmonia?"
    t "Where did she go?"
    mc "Harmonia...! Where are you?"
    t "Is she hiding?"
    mc "HARMONIA!"
    scene 008133
    with d
    h "Boo... are you looking for me?" with vpunch
    mc "Ah, shit! You startled me."
    h "Oh really? That means I did it."
    scene 008134
    with d
    h "Tehehe..."
    mc "Come on, stop playing, we have to get out of this forest."
    scene black with fade
    "As you and Harmonia walked on the way out, a strange creature appeared and confronted you."
    scene 008135
    with d
    mc "Harmonia! Get away, those creatures are dangerous. I'll face them."
    t "Shit, it's the same kind of creature I fought before, they are quite strong especially now that there are three of them and that one looks even bigger."
    t "I'm not sure I can beat them all, if I can't overcome them, do I have no other choice but to break the Guild Master's seal again?"
    mc "Harmonia! Listen to me! I'll fight these three. When you hear my signal, run away from here, you understand?"
    scene 008136
    with d
    h "Hey... hey... hey... what are you talking about? You want to protect me?"
    mc "Of course."
    h "I feel touched that you want to protect me, but are you looking down on me? I am your master. I do not need your protection."
    h "Besides, I doubt if you can protect me or even protect yourself I'm not very sure you will survive."
    h "Earlier you doubted I was stronger than you, right?"
    mc "Yes, but now's not the time to talk about that."
    h "Hey listen! How strong do you think those creatures are?"
    scene 008135
    with d
    mc "They are quite strong, I fought one of them before so I already know how strong they are."
    scene 008136
    with d
    h "Oh really? But to me they look very weak. Let me show you a little of my strength."
    scene 008137
    with d

    scene 008138
    with d
    h "(Snapping finger)"
    scene 008135
    with d
    scene 008139
    with d
    with vpunch
    with vpunch
    with vpunch
    scene 008140
    with d
    with vpunch
    with vpunch
    with vpunch
    with flash
    scene 00890
    with d
    t "What? How could she do that? She just snapped her fingers, they all died, and they even left no trace, is she actually a human?"
    t "I think she is really strong — maybe there is nothing wrong with her becoming my master."
    scene 008141
    with d
    h "What do you think about my abilities."
    scene 008136
    with d
    h "Now, do you want to accept me as your master?"
    scene 008136_
    with d
    mc "How did you do that? Are you a human?"
    th "Of course I'm not a human. I am a goddess, but in my current condition I may not be too different from humans."
    th "I must immediately get back what is missing from me."
    mc "Hmm... Harmonia? Harmonia! Hello?"
    scene 008136
    with d
    h "What?"
    mc "Are you okay? You're silent for a while."
    h "Of course I'm fine I'm just a little daydreaming."
    mc "That was amazing, how did you do it? As a Mage I never saw magic like that. You just snapped your fingers, and those creatures all died and disappeared without a trace."
    h "Oh really? I mean of course I'm great. I'm your master after all. If you want to be able to do as I have done, from now on you have to listen to what I tell you."
    scene 008136_
    with d
    th "Damn, it looks like I overdid it, even though I only used a little of my strength. I thought those creatures would only faint after being hit by my attack."
    th "I think from now on I will be careful when showing him my strength, otherwise this will be bad for his development."
    th "I have to make [name] stronger so he can help me in the future."
    mc "Then let's get out of this forest soon."
    scene black with fade
    "After a while, you finally made it out of the forbidden forest."
    scene 008142
    with d
    h "Hey, [name]! Why are you walking so fast?"
    h "Wait for me!"
    scene 008143
    with d
    h "Can't you slow down a little?"
    h "I haven't walked like this in a long time."
    mc "It will be dark soon, so we have to hurry."
    h "If you want to go fast why don't you just fly and take me with you? Can't you fly?"
    mc "I could've done it earlier, but did you forget I ran out of mana, so I can't fly for now."
    mc "After all, aren't you so strong? If you just walk it shouldn't be a problem, right?"
    h "It's a different thing. Anyway I don't like walking — can at least you carry me?"
    mc "......"
    scene 008144
    with d
    th "Hmmm... he ignored me."
    th "If I had not lost my flying ability I would have used it and would not have complained like this."
    th "Just wait until I get all my abilities back."
    scene 008145
    with d
    "..........."
    mc "Come on we gotta hurry! it's going to get dark."
    h "ARGHHH...."
    mc "Huh?"
    scene 008146
    with d
    mc "Harmonia! What happened?"
    mc "Hey, what happened to you? Please say something."
    h "(Groans)"
    scene 008147
    with d
    h "I'm sorry [name], it looks like this is not going as I expected."
    mc "What do you mean? What's happening to you?"
    scene 008148
    with d
    h "Something bad has happened."
    mc "Can you explain it to me?"
    scene 008149
    with d
    play music "<loop 0.0>sounds/bg.mp3"
    h "I'm sorry [name]. I shouldn't have called you at that time to help me. Now you've wasted your time and energy."
    scene 008150
    with d
    mc "What's going on, Harmonia? Why do you say that?"
    scene 008151
    with d
    h "Long ago, before I sealed myself in a purple stone, I was almost killed several times. To avoid death, I was forced to split myself into several shards and gave each shard its own ability to protect itself."
    h "Unfortunately, each shard only has one original ability. Right now the shards are scattered all over the world and what just happened is that one of the shards has died or disappeared."
    scene 008152
    with d
    mc "Then what will happen to you?"
    scene 008151
    with d
    h "When a shard dies or disappears it causes the same thing to my original body — in other words I will also die or disappear unless I can get a large amount of magic power to restore my body."
    scene 008150
    with d
    mc "Has something like this happened before?"
    scene 008149
    with d
    h "Yes this did happen before, and actually it's the third time, but this time it's different."
    scene 008150
    with d
    mc "Different? What's different?"
    scene 008151
    with d
    h "During the first and second incident I was still in the purple stone seal so I could restore my body, but now that the seal has broken I can't restore my body."
    scene 008152
    with d
    mc "Is there no other way to restore your body?"
    scene 008151
    with d
    h "Unfortunately the only way is for me to get a large amount of magic power."
    scene 008152
    with d
    mc "Can't you make that purple stone seal again? If you make it and get trapped again I promise to help you again."
    scene 008151
    with d
    h "Unfortunately it's really impossible for me to do at this time."
    h "Maybe this is the time for us to part, even though we haven't even known each other long enough to teach you anything."
    h "Haha... as a master I'm really pathetic."
    scene 008152
    with d
    mc "Hang on! I'll take you to the Guild Master soon. Surely he can save you. He knows many things about magic."
    scene 008151
    with d
    h "Thank you [name], but I don't think that will make it. I only have a few minutes left before I disappear."
    scene 008152
    with d
    mc "Is there really nothing I can do to help you this time?"
    t "Fuck, shit, what do I do now?"
    scene 008153
    with d
    h "Huh...!?"
    stop music
    scene 008154
    with d
    h "Wait, what is this?"
    mc "What do you mean? Are you asking about this ring?"
    scene 008155
    with d
    h "Where did you get your ring?"
    scene 008156
    with d
    mc "I found this ring somewhere far from here."
    scene 008155
    with d
    h "Do you know what ring this is?"
    mc "Of course, this ring is a special magic ring, and it made it possible for me to become a Mage."
    h "Do you know the use of this ring?"
    mc "The use of this ring? I... uhm..."
    t "What is the use of this ring? I got some memories from old Mage Zerocus about his magic, but regarding this ring I really don't have any information."
    mc "I honestly don't know much about this ring."
    h "I thought you didn't know, so I'll tell you that this ring is basically a magic ring that can store various things, including someone's soul."
    t "Hmm... this ring can do that? That means the old Mage Zerocus had stored his own soul in this ring before meeting me."
    scene 008157
    with d
    h "[name], listen to me! There is just one way if you really want to save me."
    mc "Just tell me! What should I do?"
    h "You don't need to do anything, I'll do it myself, it's just that I need your consent to..."
    mc "I agree, so just do it."
    h "Hey, I'm not done talking. I need your consent, because it will take all your magic power. Do you really agree?"
    mc "Wait, what?"
    h "Yes I said I will take all your magic power to restore myself."
    mc "If you take all my magic power, will I be able to use magic again?"
    h "Yes that's true you won't be able to use magic. That's why I'm asking your consent."
    t "Damn, if I lose all my magic power then I will become an ordinary human again, but since this is the only way to save her, there is no more time to think."
    mc "Hey Harmonia, I agree you can take all my magic power, but after you take my magic power, will I stop being a Mage forever?"
    h "Of course you will be a Mage, because I will only use your magic for a time. Once I've restored my body, then you will be free to use magic again. You could say I will be only borrowing your magic."
    mc "That's great, then how long do you need to recover?"
    h "It can take several days, weeks, months, even years, depending on how much magic power you have. The greater your magic power, the faster it will be."
    mc "Okay do it! As long as it can save you. How do you take my magic power?"
    h "I will take your magic power through this ring. Listen to me — whatever happens to me, you don't have to do anything, I'll put myself into your ring."
    mc "I understand."
    h "Alright, I'll start it."
    scene 008158
    with d
    ""
    scene 008159
    with d
    play sound "sounds/aura.ogg"
    t "Hmm... the ring is shining with red light?"
    scene 008160
    with d
    play sound "sounds/aura.ogg"
    t "And now a purple color?"
    scene 008159
    pause (0.2)
    scene 008160
    pause (0.2)
    scene 008159
    pause (0.2)
    scene 008160
    pause (0.2)
    scene 008159
    pause (0.2)
    scene 008160
    pause (0.2)
    scene 008159
    pause (0.2)
    scene 008160
    pause (0.2)
    t "Oh, it blinked a few times. I don't know what happened but I feel my magic power starting to fade."
    scene 008161
    with d
    t "Huh? My magic coat?"
    scene 008162
    with d
    ""
    scene 008163
    with d
    ""
    scene 008164
    with d
    t "My magic coat has completely disappeared. Is this a sign that my magic power has been taken away?"
    scene 008165
    with d
    t "Huh?"
    mc "Harmonia! Your body is fading."
    t "Wait, she said whatever happens, I don't have to do anything, but still her body is..."
    scene 008166
    pause (0.2)
    scene 008167
    pause (0.2)
    mc "Harmonia!"
    scene 008168
    with d
    mc "She really disappeared, but this ring is still shining."
    th "Hey, [name]! can you hear me?"
    mc "Harmonia? Where are you?"
    th "I'm in your Ring."
    mc "In my ring? are you okay?"
    th "Of course not, I'm almost dead, you know?"
    th "I will start my recovery. I want to tell you when the light on this ring has gone out it means I have started the recovery process and you won't be able to use your magic at all."
    th "And in addition, you also won't be able to talk to me without your magic. I guess that's all I need to say, alright bye bye."
    mc "Hey wait!"
    scene 008168
    pause (0.4)
    scene 008169
    pause (0.4)
    scene 008170
    pause (0.4)
    scene 008171
    pause (0.4)
    t "The light on the ring has gone out. It means Harmonia is in the process of recovering."
    t "I wonder if I really can't use magic right now."
    scene 008172
    with d
    t "I'll try if what Harmonia said is true — I'll try to make a fireball."
    "......"
    t "Yep, what she said was true — I can't use magic at all."
    t "Sigh... that means I've become an ordinary human again, I hope the recovery process will be completed soon so I can use magic again."
    t "Alright, I better get back to the Guild immediately."
    scene black with fade
    "You returned to the guild and reported on your mission."
    scene black with fade
    centered "After a few days."
    scene bed
    with d
    mc "Yaaawn.... ah it's morning."
    show hand2
    with d
    mc "Harmonia!"
    "......"
    mc "Harmonia!"
    "......"
    t "Yep still nothing happen, I guess she still hasn't finished recovering herself. It's been four days since my magic disappeared. I wonder how long it will take until she recovers and my magic can return?"
    t "Today I still can't practice magic, and my body is still sore from doing physical exercise every day. Maybe today I'll just relax."
    hide hand2
    with d
    t "Oh, I remember I heard that today Alice is not training and I often see Alice looking sad. I should use this opportunity to take her to the beach — I'm sure that will help her feel better."
    t "I should take Scarlet too. I hope she's not busy today."
    scene black with fade
    scene 008173
    with d
    t "I don't know why she always looks sad even though I always try to cheer her up. I think she still remembers about her dead family, or maybe she's worried that the enemy will come to her again."
    mc "Hi, Alice!"
    scene 008174
    with d
    a "Oh, hi [name]."
    scene 008175
    with d
    mc "How are you?"
    scene 008176
    with d
    a "I'm fine."
    scene 008175
    with d
    mc "Really? but it looks like you are having a problem."
    mc "Come on, if you have a problem you can tell me! Is this about the Guild? Are any of the members bullying you? Just tell me so I can help you."
    scene 008176
    with d
    a "No, [name]! I'm really fine, and absolutely none of the Guild members bully me — actually, they are quite friendly to me."
    scene 008175
    with d
    mc "Oh well then, I heard you're off today, huh?"
    scene 008176
    with d
    a "Yes that's right, the Guild Master asked me to take a day off from training today because he wants me to do an awakening test in a few days."
    scene 008175
    with d
    mc "Since you're off training how about we go to the beach together?"
    scene 008176
    with d
    a "The beach?"
    scene 008175
    with d
    mc "Yes, I also asked Scarlet to go with us, but unfortunately she's busy today, so it's just the two of us, what do you think?"
    scene 008176
    with d
    a "Of course I want to, you know I always want to go to the beach."
    scene 008175
    with d
    mc "Then let's go now."
    a "Yes."
    scene black with fade
    "You and Alice go to the beach together."
    scene 008177
    with d
    a "You know, [name], I'm so glad you brought me to the beach. Since I was a kid, I always loved it."
    mc "Really? When was the last time you were at the beach, Alice?"
    a "I don't know. I can't remember anymore because it's been so long."
    scene 008178
    with d
    a "I want to go there, let's go there it looks like it will be fun."
    t "I've never seen Alice this happy before, maybe I should take her on vacation more often."
    mc "Then let's go."
    scene black with fade
    "........."
    "......"
    "..."
    scene 008179
    with d
    a "This mission was not that difficult. In fact it was quite fun, don't you think, [name]?"
    mc "Uhm yeah sure."
    t "The days go by so fast, a week has passed since I met Harmonia and she still hasn't finished recovering, which means I still can't use my magic power."
    t "Until now, I still kept my lost power a secret from everyone. Even the Guild Master didn't know about it, and the Guild Master offered me some quite difficult missions, but I always refused them."
    t "The reason, of course, is because I'm currently without my magic power, so I won't take the risk of taking on a dangerous mission."
    t "All I can do right now is train my physical strength and carry out low-level missions with Alice."
    scene black with fade
    "........."
    "......"
    "..."
    scene 008180
    with d
    t "Sigh... I feel like today is very long and tiring."
    t "Oh yeah, today is the day Alice performs her magic awakening test, she must have come home by now. I'll ask her about the results of the test she did, but I'd better take a shower first."
    scene black with fade
    "After you take a shower you go straight to Alice's room."
    "Knock...Knock...Knock..."
    a "Come in."
    scene 008181
    with d
    mc "Oh I'm sorry, I didn't know you hadn't changed your clothes."
    mc "I'll come back later."
    scene 008182
    with d
    a "Wait!"
    a "It's okay, come here please."
    mc "But... well okay."
    scene 008183
    with d
    mc "Well, I actually wanted to ask you the results of your magic awakening test."
    scene 008184
    with d
    a "Oh..."
    mc "What's wrong, Alice?"
    t "What's going on with her expression? Could it be that she failed to awaken her magic power?"
    a "...."
    mc "Uhm... Alice? do you not want to talk about it with me?"
    scene 008185
    with d
    a "No! That's not it, I actually want to tell you about the test results."
    mc "So...?"
    scene 008186
    with d
    a "I will tell you, but beforehand may I lean on you, [name]?"
    mc "Huh? You want to lean on me? O...okay that's not a problem I guess."
    scene 008187
    with d
    a "Thank you, [name]."
    scene 008188
    with d
    mc "No problem, so what were the results of your magic awakening test?"
    a "...."
    mc "Uhm...Alice...?"
    t "Wait, did she actually fail and is afraid to make me disappointed?"
    mc "Listen Alice! to be honest I don't really care about the results of your magic awakening test. I just want to know because I'm curious."
    mc "But if you don't want to say it now that's okay I won't force you."
    scene 008187
    with d
    a "[name], I told you I wanted to tell you about it, it's just that..."
    scene 008188
    with d
    mc "Did you fail?"
    scene 008187
    with d
    a "No! I did not fail, I have succeeded in awakening my magic, but it is..."
    scene 008188
    with d
    mc "You managed to awaken your magic that means now you are a Mage."
    mc "That's great, Alice! Then why did you not say it from the beginning?"
    scene 008187
    with d
    a "It's because... uhm... it's because... (sigh...) as I thought it will be hard to say."
    scene 008188
    with d
    mc "Okay calm down you don't need to hurry try to say one by one and slowly."
    scene 008187
    with d
    a "(Inhales)... (exhales)... okay I'll try."
    a "It started after I succeeded in awakening my magic after. Guild Master taught me various types of basic magic which he thought were the easiest."
    scene 008188
    with d
    mc "Hmm...okay then what's the problem?"
    scene 008187
    with d
    a "The problem is that I couldn't use a single one of the magic techniques the Guild Master taught me. I failed to do them all."
    a "Then the Guild Master realized there was something different about my power. Finally he used his magic to check the magic in my body and was quite surprised by what he found."
    a "He said the reason I couldn't use the magic he taught me was because his method didn't match with something in me, because when my magic awoke, something else that was in me was also active."
    scene 008188
    with d
    mc "So what exactly is that thing in you."
    scene 008187
    with d
    a "That something is a power that can be used to fortify the strength of an object or can even be used on living being like humans, and that's why I can't use the magic taught by the Guild Master."
    scene 008188
    with d
    mc "I see, that means all this time what the enemy wants from you is that power? If the enemy gets it then they can strengthen themselves and become much stronger, huh?"
    scene 008187
    with d
    a "Yes, the Guild Master also said that."
    scene 008188
    with d
    mc "Then isn't it good because you have that power?"
    scene 008187
    with d
    a "The problem is that our Guild doesn't have anyone to teach me and there aren't any manuals or anything that can help me use this magic."
    scene 008188
    with d
    mc "Don't worry Alice! I'll help you find something or someone who can help you."
    scene 008187
    with d
    a "Actually, you don't have to do that for me."
    scene 008188
    with d
    mc "Why not?"
    scene 008187
    with d
    a "Because the Guild Master has found someone who can teach me and help me use the magic I have."
    scene 008188
    with d
    mc "Isn't that great? Then why do you look displeased?"
    scene 008187
    with d
    a "That's because the person who will teach me requires that I stay and practice at her place."
    scene 008188
    with d
    mc "Hmm... that means you're going to leave this house?"
    a "Yeah."
    mc "Then where does that person live?"
    scene 008187
    with d
    a "She lives on the top of a mountain in a place that is very remote. You could say that it is isolated from the outside world. The Guild Master said it was a very suitable place for me to train."
    scene 008188
    with d
    mc "Then what's your decision? are you really going to go?"

    if alice_point >=0:
        scene 008187
        with d
        a "I still haven't decided."
        scene 008188
        with d
        mc "Why?"
        scene 008187
        with d
        a "Because on the one hand I want to go, and on the other hand I also don't want to go."
        scene 008188
        with d
        t "Hmm... I wonder what keeps her from going? Isn't this a good opportunity for her?"
        mc "Alice, can I know exactly what is keeping you from going?"
        scene 008187
        with d
        play music "<loop 0.0>sounds/bg.mp3"
        a "What keeps me from wanting to go is... because..."
        scene 008188
        with d
        mc "Yes...?"
        scene 008189
        with d
        a "It's because of you, [name]!"
        mc "Me?"
        a "You're the reason I don't want to go."
        mc "Why?"
        a "Do you remember when you fought to save me from Omkadal?"
        mc "Yes...?"
        a "At that time you risked your life to save me, and then, when I had nowhere to go and didn't know what to do, you took me and let me live with you."
        a "And as long as I live her, when I'm sad because I still remember my family, you always try to comfort me and you even invite me to go to the beach with you."
        a "And that's when I felt something had been wrong with me. It really felt like something different, I felt like I found a new family and even more than that."
        a "I have never felt this feeling before, and when you are by my side like this, I really feel at ease."
        scene 008190
        with d
        a "[name], I think I've really fallen in love with you."
        t "So all this time Alice has had feelings for me? Why did I never realize it? But do I also love Alice?"
        menu:
            "[jeegreen]Yes":
                $ alhr = True
                mc "Alice...!"

                jump alh
            "No":
                stop music
                mc "Alice we better not continue this conversation."
                mc "I'm sorry Alice, but I don't have the same feelings as you."
                scene 008187
                with d
                a "(sad...) I understand."
                mc "Then what is your decision?"
                jump alnh
    else:

        jump alnh

label alh:
    scene 008189
    with d
    a "Listen, [name]! I don't care if you don't have feelings for me and I don't even care if one day you marry someone else or have several wives — I don't care either."
    mc "Alice...!"
    a "As long as I can always be by your side and you don't throw me out."
    mc "Alice...!"
    a "I mean if you..."
    mc "ALICE! listen to me! I honestly have the same feelings for you."
    scene 008191
    with d
    a "Really? You also have feelings for me?"
    mc "Yes that's right."
    a "Then prove it!"
    mc "Prove what?"
    a "Prove that you love me too."
    mc "How do I prove it?"
    a "Kiss me!"
    scene 008192
    with d
    mc "Okay, then, I will give you what you ask for."
    ""
    scene 008190
    with d
    mc "But is it really okay if I have multiple wives one day?"
    scene 008191
    with d
    a "Yes of course, I have no problem with that, because my father used to have several wives including my mother, even though they are all dead now."
    scene 008190
    with d
    mc "Oh! Then how about your decision? Have you chosen now?"
    scene 008191
    with d
    a "Yes, I have decided. I will depart tomorrow. I want to be stronger, and I also want to be able to help you in the future, so I will go to that isolated place and train there."
    scene 008190
    with d
    mc "Then how long are will you be there? When will you come back to the Guild?"
    scene 008191
    with d
    a "I don't know for sure, but I may be there for a few months."
    scene 008190
    with d
    mc "Okay then you better get some rest. I also want to get some sleep soon."
    stop music
    scene 008189
    with d
    a "Uhm... [name]! Before you go, I want you to do something for me, but this might be a little bit uhm..."
    mc "Just say it, Alice! What is it can I do for you?"
    a "You know, today is the last day I will be here with you, because I will leave tomorrow morning."
    a "And after I leave, I won't see you for the next few months, so before I go I want to... I want to..."
    mc "Want...?"
    a "I want you to take my virginity."
    t "What?"
    ta "Oh no, I really said it. This is really embarrassing."
    mc "Are you serious? I mean you're still a virgin? And you want me to be your first?"
    a "Yes."
    mc "Well then, I will be happy to fulfill your wish."
    scene black with fade
    scene 008193
    with d
    mc "Alice, you know? Your green eyes are so beautiful."
    scene 008194
    with d
    a "Thank you, [name]."
    a "So what should I do now? I mean this is the first time I'm going to do this so I don't know what to do."
    scene 008193
    with d
    mc "You don't have to do anything Alice, just try to relax."
    a "Uh-huh."
    mc "Okay, I'll start by taking off your towel first."
    scene 008195
    ""
    scene 008196
    pause(0.3)
    scene 008197
    pause(0.3)
    scene 008198
    pause(0.3)
    scene 008199
    with d
    ""
    scene 008200
    with d
    a "Ah..."
    mc "What is it, Alice?"
    scene 008201
    with d
    a "Nothing. I'm just a little nervous and I feel a little embarrassed about showing my body to you."
    a "Even though it's not your first time seeing it, I'm still not used to it."
    mc "Not the first time?"
    a "Yes, did you forget when we were in the abyss that time? We were both naked there, remember?"
    mc "Oh yeah, that time, huh? I almost forgot about that incident."
    mc "Don't worry you'll get used to it now, just relax."
    scene 008202
    with d
    play movie "mov/allick.webm" loop
    show movie with d
    a "Ah...[name]."
    mc "Hmm...."
    a "I don't know how you did it, but it feels good."
    stop movie
    scene 008203
    with d
    a "Oh...yeah, please don't stop."
    a "Keep going aah..."
    a "Eh...? Why did you stop?"
    scene 008204
    with d
    mc "Because I want to do something else."
    play movie "mov/alfinger.webm" loop
    show movie with d
    a "Ah...yeah, this is as good as before."
    mc "Really?"
    a "Uh-huh."
    stop movie
    scene 008205
    with d
    mc "Then are you ready to lose your virginity?"
    a "Yeah. I think I'm ready."
    scene 008206
    with d
    mc "Okay I'll start slowly, if you feel pain just tell me, and I'll stop."
    scene 008207
    with d
    ""
    scene 008208
    with d
    a "Ah..."

    ""
    scene 008209
    with d

    a "Hnggh..."
    mc "Do you want me to stop, Alice?"
    a "No, you can keep going!"
    mc "Okay."
    scene 008210
    with d
    ""
    scene 008209
    with d
    a "Aah..."
    scene 008211
    with d
    ""
    scene 008209
    with d
    a "Now I'm not virgin anymore?"
    mc "Yes, Alice now you've become a woman, and you are my woman from now on."
    scene 008205
    with d
    a "(Smile...)"
    t "Fuck yeah! virgin pussy is really the best! I'll be cumming in no time."
    a "You know [name]? I'm so happy to hear you claim me and say I'm your woman."
    mc "Really?"
    t "Oh fuck I'm cumming."
    scene 008212
    with d
    mc "Alice, I'm cumming."
    with flash
    scene 008213
    with d
    play sound "sounds/Ejaculate.wav"
    with flash
    play sound "sounds/Ejaculate.wav"
    with flash
    scene 008205
    with d
    mc "Alright Alice, I'll go back to my room to sleep, you should sleep, too, because you're leaving tomorrow morning, right?"
    a "[name], wait! Would you sleep here with me tonight?"
    mc "Me sleep with you?"
    a "Will you? I just don't want to be alone tonight because this is the last night I'll stay here before I leave tomorrow morning."
    menu:
        "Fulfill her request[alicep]":
            $ alice_point + 1
            mc "Of course I'll stay with you, Alice."
            scene black with fade
            scene 008214
            with d
            a "Thank you [name], for agreeing to stay here and sleep with me."
            scene 008215
            with d
            mc "How could I refuse a request from a girl like you, Alice?"
            scene 008214
            with d
            a "Actually I really don't want to go away from you, but I do want to be strong so that I will not be just a burden to you."
            a "Believe in me, [name]! I will definitely be able to use my magic soon, and come back to you."
            scene 008215
            with d
            mc "I'll definitely believe in you, Alice."
            mc "Okay, it's time to sleep, good night."
            scene 008214
            with d
            a "Good night, [name]."
            scene 008216
            with d
            "......."
            "....."
            "..."
            scene black with fade
        "Reject her request":

            mc "Sorry, Alice, but I can't."
            a "Alright then good night."
            mc "Good night."
            scene black with fade

    jump tbc
label alnh:
    scene 008187
    with d
    a "I've decided, I'm leaving tomorrow morning."
    mc "Then how long will you be there? And when will you come back to the Guild?"
    a "I don't know for sure, but I may be there for a few months."
    mc "Okay then, you better get some rest soon, and I also want to go to sleep."
    a "Yeah."
    jump tbc
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
