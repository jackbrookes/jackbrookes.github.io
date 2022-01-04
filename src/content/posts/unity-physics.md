---
title: Notes on Unity Physics
date: 2022-01-04
---

* Unity uses the PhysX system developed by Nvidia for 3D physics.
* High level functions are available for creating rigid bodies, adding forces, and coupling bodies with joints and springs.
* Inherently discrete, so errors will occur, and it is not always deterministic.

## Manual spring/damper calculations

* A spring/damper system is an example of PD controller, and are used to correct for some error (difference between desired and actual position). The spring applies a force **p**roportional to the error, and the damper applies a force proportional to the **d**erivative of the error (velocity), relative to a desired velocity. Constants (`Kp` and `Kd`) are used to control this force. Usually you want `Kp` to be positive (to correct the error) and `Kd` to be negative (to slow the system down - simulating drag or friction)
* If you want to manually calculate a drag force using a Rigidbody's velocity, you will always be one frame behind any forces you apply, since velocity only gets updated when the physics simulation is updated (i.e. during `FixedUpdate`. Try to use the built-in drag parameters where you can.
* For rotational/torsion springs, the [Rigidbody Inertia Tensor](https://docs.unity3d.com/ScriptReference/Rigidbody-inertiaTensor.html) property describes how the mass of the object is distributed in 3D space. It is conceptually equivalent to the [Moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia). Along with the Inertia Tensor Rotation property, these can be use to change how much torque is required to rotate an object. These are approximated by Unity if left unchanged, but you can manually assign these to make an object more resistant to rotation in a particular direction.
* Classical calculations for PD controllers can cause issues such as overshooting and oscillations in discrete physics calculation. A more stable Spring/Damper system has been helpfully typed up in [this article](https://digitalopus.ca/site/pd-controllers/) by Digital Opus. With this you can create critically damped systems which smoothly correct for error with no oscillation.

## Configurable Joints

* When an axis is set to limited, all external forces/torques applied to the axis seem to be ignored.

## Unity's drag calculation

* The drag value assigned in the inspector is quite opaque, and it is not clear what the units are. It seems that the drag is [simply a multiplier for the velocity](https://forum.unity.com/threads/drag-factor-what-is-it.85504/#post-2005882), which asymptotes the velocity to zero as drag increases. To simulate it yourself:

```cs
body.velocity *= Mathf.Clamp01(1f - drag * Time.fixedDeltaTime);
```
