# Boat_Localisation

This is extension of a fun project I did for the [MASM12](https://www.maths.lth.se/matstat/kurser/fms110mas222/) course at Lund University. It was quite nice to tinker with, so I decided to extend it. 

## Project description

Assume you are out fishing on a lake (or in an archipelago), whatever floats your boat. After an intense morning of fishing (I don't know how fishing works) you take a nap. You wake up several hours later, completely disoriented. You can safely assume that you have drifted around *quite* a lot. Due to currents and wind, we can assume the drift has zero mean, however variance can be assumed to be proportional to time. 

What’s even more troubling is that a think fog has settled over the water. You approximate the visibility to about maybe five meters. Consequently, you have no idea where you are. Looking around in your boat, you find the following objects:

* One topological map of the lake (or archipelago).
* One laptop running your favourite IDE and programming language, with all the slickest libraries dowloaded.
* One depth gauge of lower quality. The instructions on the back reveal ”Measurement error ±15%”. Aight.
* (Optional) Compass

**Goal:** Using only the equipment found in the boat, try to locate yourself.

