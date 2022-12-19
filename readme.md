*This project is in pre-alpha and part of my 2023 new years Resolution to 
create an original project each month throughout the year. The main purpose
is for my self-education. At this stage, this readme provides an high level
description of the intended product and some context around its design.


I feel like my brain works differently from most people.

I do know that I have Aphantasia - a difference in neurology which means I
cannot picture things in my head.
More accurately I guess this would be described as an inability to artificially
recreate the experience of the senses within my imagination - when I close my
eyes I see nothing, except, I can only describe as 'conceptually'. The same is
true for sounds, smells, touch and so on. People with Aphantasia often derive
unique or novel methods to interpret and understand the world in which we live,
and as it is a feature (not a condition) of our perception, many people with
Aphantasia do not realise until late in life that they have it - this includes
me. Therefore, they may have created highly competent alternative methods to
perform common tasks of the brain, which a 'minds-eye sighted' person would not
have needed to do, where instead they could have used the ability to simply
'see' things in their head. As you can imagine, this could affect how memory and
recall works, as well as many other functions of the mind - I am by no means a
scientist and have no deep understanding of neurology or other related
disciplines, so it would be remiss of me to assert beyond this, however I feel
the fact I have Aphantasia is likely the most impactful feature of my psyche
which explains the feeling I have; that I think differently from most others.
I have also pondered on other things, such as do I have ADHD for example, but
never taken any official tests.

This information is likely irrelevant to you and you are probably wondering why
I'm divulging this; well basically it is to provide some context into the
purpose behind this project. In other words, I feel it's necessary context,
though admittedly, I do not know how well it will translate my feeling and
understanding, and intentions, as well as I would like.

With that said, the main point of this project is to create, yet another - 
ideas tracking/notepad/to-do list/project planning app etc etc.
More accurately, I am to develop a datastructure and API to fasciliate
numerous front end projects from a db of 'my ideas', with a heavy focus
on linking 'idea' to one another in order to aid tracking of those
ephemeral ideas which come in a brief moment of inspiration but when you
do not have the time, oportunity, momentum etc to develop the idea further,
or when the idea is something you feel highly positive about, but you don't
quite know where it could apply.

In this project, I aim to create a basic API and well defined data structure,
where 'ideas/notes/projects/targets/goals' etc are all instances of one
universal data class/object. Some of the attributes will obviously have to be
optional to allow such a wide range of categories of thought/information to 
be distilled into one such generic data structure, with a lot of how you
categorise these objects being left to the front end via specific SQL querying
as well as tables recording the relations between these (same class) objects
of varying contextual meanings. In this way I hope to be able to build a sort
of 'web' of my mind, rather than a strictly vertical hyerarchical structure
in classifying and organising my thoughts. I have no idea if any of this 
makes sense to anyone else, but if you're still with me, I shall dig a little
into how I (at the very early stages) plan to structe this technilogically
speaking.

First though, I want to outline some of my main intended use cases for this,
shall we say, 'data structure platform for human thoughts'.

The first problem I aim to solve with this is to be able to capture fleeting
ideas and thoughts in daily life in form which can be usefully recalled and
applied later in time.

This will include some basic UI entry points in the form of note-taking, 
dashboards, calendar/planning app and some poject basic management tools.
An example of how to solve the problem above will be to provide some sort
of gamified process of past ideas review - where the system will make
decisions of which ideas/thoughts from the past to present on a daily basis
for further consideration/review. This would likely be a simple 5 minute a 
day sort of application, where user input deadlines/reminder dates, quality
of connections to other ideas/notes/projects (both high linkage for inspiring
development of ideas, and low linkage for pruning ideas from the system)

I also plan a system of dependency between ideas, where one 'idea object'
can depend on the completion of another, be that a project, a to-do item,
a technology goal to learn etc. This, I hope would help focus priorities
at times when I feel like I want to learn something but don't know what to
do at that moment in time (I have a bad habit of starting projects/learning
new subjects before finishing others)

The rough idea for the data structure I have at current would be something 
along these lines:

python class/object structure:

class Idea(stuff):
    def __init__(self):
        self.id              #autogen by db
        self.title           #self explanitory
        self.content         #text content of the idea/note
        self.files           #dict of files owned by the idea object
        self.category        #user defined categorisation of idea objs
        self.type            #data structure defined types of object
                             #instances - i.e. idea,project,to-do,note,
                             #research-reference,problem,solution
        self.external_links  #links to external resources
        self.links           #internal link system - dict of links to
                             #and from other objects (db will record only
                             #links to in specific table called links)
        self.deadline        #hard deadline for completion if applicable
        self.reminders       #list of reminder objects (date and some text)
        self.dependencies    #list of objects required before this can be
                             #completed
        self.dependents      #list of objects requiring this one to be
                             #completed
        self.active          #indicator of whether this is active i.e.
                             #is an active project, skill patch etc
        self.archived        #not deleted, but not to be worked on
                             #currently
        self.priority        #a metric of priority over other objects, details tbc
        self.frontend_id     #id of front end which created object
Note, different front end apps will use combinations of the above attributes/
fields to derive uniqueness of categories and classification as well as build
connections between objects.
