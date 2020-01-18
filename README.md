# temp_percent_withGUI
GUI that let's you easily calculate percentages of melting points in Celsius.

While working at Yale, I used a process called thermomechanical nanomolding. Essentially, you place a metal on top of a mold and heat it until it becomes slightly soft. Then you apply a massive amount of pressure and hope it finds its way into the mold. The driving force for this process is not well understood (at least at the time of this writing), though we suspected it was a diffusion based. 

Anyway, because these metals typically soften enough for molding at 40% of their melting point, I needed to do this calculation many times. Melting points are easy to find in C and the heating element was in celsius as well. Because converting to kelvin, multiplying by 0.40 and then converting back to celsius was annoying and something I had to do many times, I wrote a quick program with a gui and lots of useful defaults to make this task easier.

## Useful features
- default percentage (pre-filled in) is 40%
- curser starts in temperature box
- hitting tab moves to next box (% box)
- hitting enter runs the calculation

## Screenshot of program
![program sample](/program_screenshot.png)
Format: ![Alt Text](url)
