---
title: Writing sustainable software for real-time human behaviour experiments
date: 2021-04-12
---

# Writing sustainable software for real-time human behaviour experiments

Software is a core component of modern science. It comes in the form of scripts that can process, visualise, and model data, or, as real-time software that runs during an experiment. When we use experiments to investigate human behaviour, real-time software can automate the experiment procedure, reduce the burden on the researcher in presenting stimuli, as well as making experiments more consistent. When done right, this makes experiments more reproducible, and reduces the risk of external factors interacting with the experiment's effects.

However, software in science is often written to meet a short-term demands, or created by individuals who (though no fault of their own) have little prior experience writing software. As we look towards a future where software and reproducibility become even more crucial in science, it is important we ensure the software we write is "sustainable". Indeed, the [Software Sustainability Institute](https://www.software.ac.uk/about/manifesto) has been set up to lobby for recognition of the role software plays in science.

## Sustainability

My definition of sustainable experiment software is code that not only meets the immediate demands of the task, but is also:

* Readable, allowing researchers to properly interpret their data, cross-referencing with the task mechanics. 
* And maintainable, allowing for future experiments to easily build upon or modify the codebase. 

Let's first look at an example of some typical experiment code. Here, I have created a simple task to investigate the [Stroop effect](https://en.wikipedia.org/wiki/Stroop_effect). Colour words (e.g. "red", "green", "blue") are displayed in a font coloured either matching or not matching the text itself. Participants must respond by speaking aloud the colour of the word. The experiment typically finds that responses from participants take more time when the word does not match the colour itself. The code below is a basic Python script using `pygame` for graphics.

```python
import pygame

# 9 trials numbered 1-9
trial_nums = range(1, 10)

# Setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont(pygame.font.get_default_font(), 96)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

pygame.time.wait(10000)

for trial_num in trial_nums:

    if trial_num in (1, 6, 7):
        colour = (255, 0, 0) # red
    elif trial_num in (2, 5, 8):
        colour = (0, 255, 0) # green
    elif trial_num in (3, 4, 9):
        colour = (0, 0, 255) # blue

    if trial_num in (2, 4, 9):
        text = "red"
    elif trial_num in (1, 6, 8):
        text = "green"
    elif trial_num in (3, 5, 7):
        text = "blue"

    # Create text
    text_img = font.render(text, True, colour)
    text_rect = text_img.get_rect()
    text_rect.center = (320, 240)
    screen.blit(text_img, text_rect)
    
    end_time = pygame.time.get_ticks() + 1000 # 1.0 second
    while pygame.time.get_ticks() < end_time:
        for event in pygame.event.get():
            pass
        pygame.display.flip()

    # Create blank screen
    screen.fill((255, 255, 255))
    
    end_time = pygame.time.get_ticks() + 500 # 0.5 seconds
    while pygame.time.get_ticks() < end_time:
        for event in pygame.event.get():
            pass
        pygame.display.flip()
```

The code does what it needs to. It displays "red", "green" or "blue" in a (seemingly) random order with different colours, for a total of 9 trials. The text displays for 1 second, then a blank screen displays for 0.5 seconds. Here's a video, try to say (out loud) the colour of the text.

<video controls width="500" muted>
  <source src="/static/image/stroop.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

The code for this task isn't very "sustainable". Some criticisms:

* It is not immediately clear what is shown to the participant on each trial. You can work it out, by looking at the `if` code blocks that are run where `trial_num` is `1`, but it may take time and is prone to human error. 
* A naive researcher may change the `trial_nums` to `range(1, 19)` to double the number of trials, but this won't work correctly, and even worse, there will be no error messages to help the researcher!
* Changing the order of the stimuli presentation would require re-coding the internal `if` statements.
* Adding more complexity (new words, colours) would drastically increase the number of lines of code, and break the original version of the experiment.

## Improvements

Even though this is a toy example, there are things we can improve. My ethos when writing experiment software is to separate the experiment code into two parts:

* Experiment specification: Building or describing the experiment structure, including the independent variable values on each trial.
* Experiment implementation: Presenting stimuli according to independent variables using calls to your presentation engine, as well as collecting any dependent variables.

This separation forms a substantial part of the way that my experimental design framework [UXF](http://immersivecognition.com/unity-experiment-framework/) works. 

We can begin with the improvements by creating a means of experiment specification. First, we can store our stimuli as variables, so that they can easily be referenced, or modified.

```python
clr_red = (255, 0, 0)
clr_green = (0, 255, 0)
clr_blue = (0, 0, 255)
txt_red = "red"
txt_green = "green"
txt_blue = "blue"
```

Now for our trials. We want to be able to represent the contents of the trial with code, and we could anything like a Dictionary or instance of a custom class. Here, I simply use a tuple (in Python, a tuple is an immutable list of objects) to define the independent variables (i.e. text and colour) on each trial, and store those in one large tuple containing all trials. 

```python
trials = (
    # colour,   text
    (clr_red,   txt_green),
    (clr_green, txt_red  ),
    (clr_blue,  txt_blue ),
    (clr_blue,  txt_red  ),
    (clr_green, txt_blue ),
    (clr_red,   txt_green),
    (clr_red,   txt_blue ),
    (clr_green, txt_green),
    (clr_blue,  txt_red  )
)
```

Hopefully you can see here how this is much more readable - each row represents a trial, with the two items representing the colour and text respectively. This means we can now simplify the experiment implementation, by looping over the trials, getting rid of the `if` statements inside the stimuli display part of our code:

```python
for trial in trials:
    # Grab independent variables from the trial
    colour = trial[0]
    text = trial[1]

    # Create text
    text_img = font.render(text, True, colour)
    text_rect = text_img.get_rect()
    text_rect.center = (320, 240)
    screen.blit(text_img, text_rect)
    
    end_time = pygame.time.get_ticks() + 1000 # 1.0 second
    while pygame.time.get_ticks() < end_time:
        for event in pygame.event.get():
            pass
        pygame.display.flip()

    # Create blank screen
    screen.fill((255, 255, 255))
    
    end_time = pygame.time.get_ticks() + 500 # 0.5 seconds
    while pygame.time.get_ticks() < end_time:
        for event in pygame.event.get():
            pass
        pygame.display.flip()
```

With this separation now achieved, it should be clear how easy it is for researchers to modify the number of trials or order they are presented in. But this gives us more power than we had before - we can replace our hard-coded trials with more sophisticated means of generating trials. For example, we may want to generate every combination of colour and text, and shuffle the resulting trials. We can easily do this with nested `for` loops:

```python
import random

trials = []
for colour in (clr_red, clr_green, clr_blue):
    for text in (txt_red, txt_green, txt_blue):
        trials.append((colour, text))

random.shuffle(trials)
```

([Full code for updated task](https://gist.github.com/jackbrookes/812ac589f250fbcb27eb8c1522caa6ad))

Notice this change requires no knowledge of `pygame`, and we didn't need to touch the core loop at all. With this separation of specification and implementation, our code is much more robust, and is easy to read and change in the future. 
Hopefully you appreciate how this method has more value as the experiment is scaled up. Imagine the mess of an experiment with dozens of different independent variables, all defined in `if` statements littered throughout the code. Here, a trial object can contain as many variables as required, and the presentation code can access them as needed. The presentation code ("experiment implementation") in a sense has been purposely made to be dumb, and it is unconcerned with which trial it is currently presenting. This way, the experiment specification can change in any way see fit without the presentation code having to be tweaked at all. 

## Further suggestions

To further separate the code, there are a couple more suggestions I would have that could be worth implementing:

* Split the code across (at least) 2 separate files, so that changes to trial order or number do not require accessing of the presentation code.
* Allow for trials to be specified in a `csv` file, which is parsed into a trial list on start-up. Researchers can modify the `csv` file to easily change the trials. 
* Implement a cascading settings system. For example, a setting for a trial would override a setting applied to a block of trials. This type of system [exists in UXF](https://github.com/immersivecognition/unity-experiment-framework/wiki/Settings-system#cascading-requests).
* Some experiments have a closed loop design, where trials may be added or changed based on actions in the previous trials. In this case, only partial separation may be possible.
* You can use the same trial objects to save dependent variables (i.e. participant responses). In UXF, this is done with the [behavioural data collection system](https://github.com/immersivecognition/unity-experiment-framework/wiki/Data-collection#behavioural-data).
* At the end of the task, you can write code to export the trial list (including results) as a `csv` file, so you can easily analyse responses to changes in independent variables.

Happy coding!