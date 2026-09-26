---
titulo: Can blender have more combing tools for hair?
autor: BrandonD
url: https://blenderartists.org/t/can-blender-have-more-combing-tools-for-hair/1199022
data: 2020-01-01
idioma: en
coletado_em: 2026-09-26
---

### Post #1 — BrandonD — 2020-01-01T12:40:01.308Z

I’ve been working with blender hair for a while now and I was wondering if we could get more tools to make our workflow a lot easier and faster. I’m creating female hair with a ponytail and I was thinking how much easier it would be if there was a pinch combing tool. Just a thought. Let me know what you guys think and if there are ways of doing this or any addons.

---

### Post #2 — pasi — 2020-01-03T09:08:57.430Z

I’ve been working with hair recently and what I’d really like is for lack of a better name, a Moses brush (because parting oceans…). Something I could apply between hair strands to push them away from each other. I often want to manually clump strands especially around edges and it would be cool to be able to push from the outside towards the model, parting hair along the way.

---

### Post #3 — Musashidan — 2020-09-08T12:35:35.187Z

There’s a brand new hair system in the very early stages, proposed and being developed by Daniel Bystedt and a few devs. I asked him about it(because I use Maya Xgen) and he’s also experienced in Xgen and a number of other production hair systems over the years and he assured me it will be designed as a node based system that should stack up against the likes of Xgen and Ornatrix. In the meantime, you’re stuck with Blender’s pretty bad current solution. Future is bright in this regard though, it’s just goung to take time.

---

### Post #4 — Piotr_Adamowicz — 2020-09-08T13:06:36.756Z

Yes! It can!
But it won’t any time soon

---

### Post #5 — mod1 — 2020-09-08T13:37:51.506Z

but for now you can use addons / long waiting for new features (

---

### Post #6 — Magnavis — 2020-09-08T13:50:25.501Z

anywhere we can read/hear more about that? Sounds super interesting.

---

### Post #7 — Musashidan — 2020-09-08T14:02:29.644Z

https://developer.blender.org/T78515

---

### Post #8 — SidV — 2020-09-13T14:02:50.248Z

I’m ok with the amount of brushes available. It probably depends on your workflow. I like to add one hair at the time and then brush it, which gives me total control over each strand.
What i’m missing is a snapshot option for simulated hair. Specially when you deal with long hair i would like to run the simulation once, snapshot it and work from there.
The  simulation department is urgently in need of some attention. Using cloth simulation to simulate hair was definately the right decision but everyone who actually tried to simulate long hair probably knows what i’m talking about.
I’m getting the weird feeling that this ‘everything nodes’ dilemma is welcome excuse to delay everything as in ‘It would make no sense to improve that certain field right now since everything will be ‘everthing nodes’ some day’. Thats what led to the animation 2020 project delay and also affect other fields like hair particles for example. I’m getting tired of it.

---

### Post #9 — thomas_p — 2020-09-13T14:51:02.896Z

My most sought after feature at the moment is actually the ability to convert curves to hair guides and vice versa.
Without that you end up losing styling changes all too easily, cannot refit/conform existing hairstyles to different assets, etc etc.

---

### Post #10 — zeauro — 2020-09-13T15:57:26.337Z

IMO, animation 2020 project was more delayed by underestimation of amount of work to spend on basics of 2.8 design (UI, Viewport, EEVEE, View Layers & Collections, Library Overrides, etc…).
Work on NLA editor has started with few improvements that should end-up in 2.91 as announced by roadmap of animation module. Most of improvements of NLA should happen for 2.92. But intuitiveness improvements should happen during 2.92 development with work on visual keying and be released in 2.93.
Everything Nodes project to begin, had to wait that a certain amount of basics were restored, too. Since the moment, concept was proposed, particles nodes are announced as first target of the project.
And people can currently test Jacques Lucke work. That is tangible.
About the 10 targets defined in january for year 2020, developers made significant progress on half of them. The year is not finished. At the end of the year, they probably will respect most of their promise. That is not so bad.
They made the volume object and point clouds object. The third one that is supposed to be added is the hair object.
According to roadmap, work on new hair should start, soon.
If that does not happen for this end of year, it should happen in first half of 2021.

---

### Post #11 — SidV — 2020-09-14T11:11:56.893Z

You talking about the new hair type. I dont know where you get that schedule from. When i take a look at the
milestones
planed this year i can’t find anything about hair even the task clearly give no info when this is gonna happen
Work plan
Time estimate: ?
Besides that the hair object type is a new feature i couldn’t find anything on hair fixes and improvements. That said, i know the Blender team is working their butt off and i dont criticize their work ethic or competence,  just their priorities. I just think there are more important things than to add new features at the moment.
thomas_p:
My most sought after feature at the moment is actually the ability to convert curves to hair guides and vice versa.
Without that you end up losing styling changes all too easily, cannot refit/conform existing hairstyles to different assets, etc etc.
I think the hair tool addon can help you with that:
https://joseconseco.github.io/HairToolDocs_28/convert_generate_hair/

---

### Post #12 — zeauro — 2020-09-14T16:20:54.808Z

SidV:
When i take a look at the
milestones
planed this year i can’t find anything about hair even the task clearly give no info when this is gonna happen
Because of hair dynamics, that is under Nodes and Physics module.
blender.org
Blender Developer - developer.blender.org
Join the global community of Blender developers.
SidV:
That said, i know the Blender team is working their butt off and i dont criticize their work ethic or competence, just their priorities. I just think there are more important things than to add new features at the moment.
One goal of developing a new hair system is to get rid of problems of old system with its abandon.

---

### Post #13 — thomas_p — 2020-09-14T22:19:49.530Z

SidV:
I think the hair tool addon can help you with that:
https://joseconseco.github.io/HairToolDocs_28/convert_generate_hair/
Hey thanks, yeah I know about that. Interpolation between guide curves is the issue for me though, if I bring in curves from some other source and run them through that the resulting particles end up pretty uneven looking, a bit like when you try to cut your own hair first time.
Same guide curves in other software give a smooth looking result with nicely interpolating length and orientation.
But cheers for reminding me about this function, I’ll try and bug the author to see if something on his end can be done to improve the result. So close!

---

### Post #14 — NoahMuiruri54 — 2020-10-14T15:15:02.588Z

hey am Noah…for sure to achieve realistic hair in blender is a painful thing,so i suggested to the ornatrix devs if they could manage creating a plugin for blender…but they said they cant becoz of blender licence model…but i wasnt satisfied with their answer(since some commercial render engines have overcome that)…so do you guys think its possible to intergrate it??

---

### Post #15 — stargeizer — 2020-10-14T16:54:07.203Z

You need to understand that for a commercial developer, viral licenses like the GPL are a kind of “cancer” (Notion promoted by the old head of Microsoft), and should be avoided like the plague: Any developer that wants to keep their code closed, cannot legally offer code for such platform, unless they have lots of money to get lawyers involved (E.g.: Nvidia, Broadcom), or they want to open their code, but in such case, they also need lawyers involved, more so if they live in the US and any country that recognizes software patents to approve and clear the code for open release (E.g. AMD, Intel).
For small ventures/developers, that’s a full no-go.
Render Engines bypass the problem using an open “shim” to export the data from Blender to RAM/Hard drive and from them, the closed software can take the data and does their magic. For geometry like hair, probably is possible to do that too, but closed source developers usually doesn’t want to invest time/money for that. It’s just not viable, from a economic viewpoint.

---

### Post #16 — NoahMuiruri54 — 2020-10-15T14:39:54.591Z

ooh thanks for the clarification

---