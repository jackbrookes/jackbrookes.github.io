---
title: My Work
---

# My Work

## Software portfolio

My open sourced work can be found at my [GitHub](http://github.com/jackbrookes).

## Research publications

Up-to-date list available on [Google Scholar](https://scholar.google.com/citations?user=0kwtpyoAAAAJ&hl=en).

## Projects

The [Unity Experiment Framework (UXF)](http://immersivecognition.github.io/unity-experiment-framework) is a software framework for developing virtual reality human behaviour experiments in Unity. It gives researchers easy-to-use tools to create applications to investigate how humans learn, move, and think. UXF includes complex systems for experiment flow and data collection in a set of simple Unity components. It supports virtual reality experiments, web browser based experiments, traditional screen-based experiments, and remote data collection by storing data in the cloud. I developed it during my PhD, made it open source, and have been continually updating it since then. 

<img src="/static/image/uxf.png"/>

Core skills & technologies:

* Unity C# API design
* Custom Unity Editor tools
* Multithreaded file I/O
* Communication with cloud databases (AWS)
* WebGL
* Dynamic user interfaces
* Unit testing
* Extensive documentation

During my PhD and beyond I have developed several virtual reality experiments to examine human behaviour, mostly in the area of human sensorimotor decision making. All were developed in Unity and with UXF.

### VR Threat Toolkit

I previously worked at UCL building a Unity platform for studying human movement within threatening VR scenarios. Alongside building statistical models of cognitive processes, this allows researchers to study how humans act so quickly in the face of fear, despite the complexity of the required movements. With this platform, one can easily create sequences of pre-planned events, including interactive elements, which allows each participant to experience a controlled encounter with a virtual threat, whilst collecting movement and physiological data.

<img src="/static/image/vrthreat-panther.jpg" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/>

Core skills & technologies:

* Virtual Reality physics & interaction
* Procedural animation (i.e. movement of animal 3D models)
* Custom shaders
* Performance optimisation (material combining, static batching, occlusion culling)
* Complex coroutine systems for dynamic event sequencing 
* Custom Unity Editor tools
* Spatialised virtual audio
* Screen, camera, and microphone recording from Unity
* Unity Post Processing Stack v2 

### VR / AR Surgical training

Part of my PhD involved research into how surgical simulator systems could be improved with haptic technology in order to enhance learning outcomes. I developed algorithms to apply assistive or disruptive forces to allow for practice matching an individual's skill level.

I also developed software for the MOOG Simodont Dental Trainer, which replicates the haptic sensations of many dental procedures. My software allows creation of "tasks" - blocks of virtual material with different levels of softness, which trainee dentists must learn to discriminate and drill out. My software is available [open source](https://github.com/jackbrookes/simodont-model-builder).

<img src="/static/image/simodont.bmp" width="500" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/> 
<img src="/static/image/smb.PNG" width="500" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/> 

### Interceptive timing

This task examines the interceptive timing ability of children and adults. Crucially, VR allows the task to be made 3D - which means we can more reliably discern spatial and temporal errors separately. The gamification of the interceptive timing task means children enjoy taking part in the studies.

<video controls width="500" muted>
  <source src="/static/image/interceptive-timing-vr.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

### Golf training

A great challenge in learning is understanding generalisation. Humans and other animals manage to quickly generalise abilities learned in one domain to another one. Virtual Reality poses a massive opportunity for training of skills ranging from surgery to customer service. For this to be useful, the skills learned in VR need to transfer to the real world. We are using this virtual reality golf task I developed to examine how we generalise skills learned in one medium to another.

<img src="/static/image/golf.png" width="500" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/> 

### Intrinsic vs extrinsic costs in sensorimotor decision making

Here we present participants with a series of choices between two objects. These objects differ in their *extrinsic* costs in terms of number of stars (i.e. points), and also their *intrinsic* costs because they have certain distance and timing constraints.

<img src="/static/image/bubbles.jpg" width="500" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/>

### Postural sway assessment tool

This task measures the participant's head position across three conditions: vision, no vision, and the oscillating room intervention. VR makes these manipulations easy, and allows researchers to examine the participants ability to use vision to adjust balance. This project is available free & [open source](https://github.com/immersivecognition/posture-assessment-vr). 

<video controls width="500" muted>
  <source src="/static/image/sway.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

### Action-bandits

In my PhD I study how different types of errors (selection error, movement error) change the way we learn about our world. In this experiment, participants must physically swipe through one of two targets. Virtual Reality allows me to easily manipulate the rate of movement errors the participant believes they are making, by hiding the position of the hand when needed.  

<video controls width="500" muted>
  <source src="/static/image/action-bandits.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

### Prehension

Reach-to-grasp behaviours have been studied for decades, but only recently VR has allowed new experiments to be created. Here, we examine the effects of removing haptics or vision of the hand when reaching for an object using the VR experiment I developed.

<video controls width="500" muted>
  <source src="/static/image/prehension-vr.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>


### Robotic rehabilitation

During my Masters project I developed a snake clone which is played by a robotic arm that communicates with Unity using real-time multiplayer networking technologies (TCP/UDP).

<video controls width="500" muted>
  <source src="/static/image/snake.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

### Haptic Handwriting

Handwriting is an important life skill, but many children underperform. Here I developed a simple handwriting task that allows children to virtually practice handwriting with haptic interventions that potentially improve learning rate. The Unity application communicates to a Phantom Omni haptic pen system. We tested this in a primary school, which was then featured on the BBC Inside Out program.

<img src="/static/image/handwriting.png" width="500" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/> 
<img src="/static/image/bbc-vr-children-handwriting.png" width="500" onclick="window.open(this.src, '_blank').focus()" style="cursor: pointer;"/> 

### Treasure chest bandits

Continuing the work done in my PhD on learning in the context of movement errors, I developed a similar task that removed the motor aspect of the task, and transformed it into a 2-stage decision making task. This is done on a computer monitor rather than in VR.

<video controls width="500" muted>
  <source src="/static/image/treasure.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

### Visuomotor adaptation

A common motor learning experiment paradigm involves applying a transformation to the environment, such that movements are mapped to a cursor position in a novel way. Here I developed a VR version of this task, which opens up the possibility of developing interesting new interventions, and running these types of experiments on a larger scale.

<video controls width="500" muted>
  <source src="/static/image/vmr.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

### Paired associates memorisation

Memorising a pair of objects, and then recalling the second object after being prompted with the first, is a common way of measuring memory. I developed a VR version of this task, which uses realistic 3D objects rather than the classic image or word based tests in an attempt to be more ecologically valid. We use this task to examine the effects of sleep interventions on memory performance.

<video controls width="500" muted>
  <source src="/static/image/paired-associates.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

# Other 3D/VR software:

* [VR Demo Pack](https://github.com/immersivecognition/vr-demo-pack) - Unity package that allows developers to add an avatar, viewable in 3rd person, to their task for presentation and video purposes.
* [BounceBeat](https://github.com/jackbrookes/bouncebeat) - VR musical physics sandbox game made in Unity.
* [Unnamed concept VR game](https://github.com/jackbrookes/vr-graph-intersection) - VR puzzle game where the goal is to create faces from nodes that do not create intersections in a 3D graph.
* [Eyeballs VR Demo](https://github.com/jackbrookes/eyeballs-vr-demo) - VR demo made in Unity that allows you to detach your eyes from your head.
* [Isometricism](https://jackbrookes.itch.io/isometricism) - Concept puzzle game where the visual perspective alters the paths the player can take.

<video controls width="500" muted>
  <source src="/static/image/isometricism.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

* [Halo custom gametype scripts](https://github.com/jackbrookes/halo-reach-custom-gametypes) - Collection of my custom scripted gametypes for Halo: Reach, written in a Lua-like language.