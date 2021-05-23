---
title: Third-person video recording in VR (with avatar)
date: 2021-05-21
---

# Third-person video recording in VR (with avatar)

In traditional games, screen captures can show how the game looks to the player. However, in VR, communicating the feeling of being in an VR experience is hard. Screen captures of the player's first person view in a VR experience fall short because they are limited to 2D, often narrowed field of view, and include the janky head movements of the player. Humans have a remarkable ability to predict the effects of their own head and eye movements, effectively smoothing out their view in their brain. Whilst viewing the recording of a player's first person view, the viewer will not be able to take advantage of this ability and the video will not communicate the true immersiveness of the experience. 

A way to avoid this would be to take advantage another human ability, empathy. Film producers have long known that feelings can be transmitted to a viewer if they see a character experience an event on-screen. So, for VR experiences, we can record experiences from a third person perspective. [LIV](https://www.liv.tv/) has built software to do this, and the "mixed reality" functionality is built into SteamVR and Oculus. When I tackled this issue back in 2017, these tools were less mature. Today, they are still somewhat cumbersome to set up if you are in a hurry. So I built a Unity package that simplifies this, and allows control of a virtual camera with a keyboard and mouse. That way, a friend can control the camera around you (visible as an avatar) and capture the view from that perspective. The package is simple with no dependencies.

<video controls width="500" muted>
  <source src="/static/image/vr-demo-pack.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

[GitHub link](https://github.com/immersivecognition/vr-demo-pack)