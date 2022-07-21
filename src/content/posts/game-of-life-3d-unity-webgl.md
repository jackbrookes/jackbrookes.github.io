---
title: Game of Life 3D in Unity WebGL
date: 2022-07-22
---

# Game of Life 3D in Unity WebGL

I created a 3D Game Of Life in Unity WebGL. It includes several changes from the 2D Game Of Life:

* It uses a 3D grid instead of a 2D grid.
* Neighbourhood is now a cube instead of a square (up to 28 neighbours).
* Thresholds for the rules are set to more sensible values for 3D, but can be customised.
* We render cells as small spheres so that we can see them better.
* You can move around and rotate the camera with WASD/Mouse.

<video controls width="700" muted>
  <source src="/static/image/game-of-life.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

Each cell is initially occupied based on a probability. You can try the demo in browser with the link below:

[Play Game of Life 3D](/fun/game-of-life-3d)

The source code is on GitHub:

[View on GitHub](https://github.com/jackbrookes/game-of-life-3d-unity/tree/main/Assets/Scripts)