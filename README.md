# CV_SVG_Arranger

## History (Dramatic)

It all started with the ardent desire to work. 

```
You've got to be brave, bold, different from the crowd
```

That's what every CV website will tell you.

```
Splash it with pink, 
Make it unique, 
Use split-page formatting, 
To be amazing
```

or something along those lines. 

And many newbies believe that companies give a damn about the shade of purple they're using for their borders.  Now they're enticed and they truly believe that if their CV isn't the color of clown barf, they're social rejects and no company will ever take them. Capitalizing on this fear, CV websites are there to give everybody who cares a quick solution: 

```
Why not use our CV tool?
```

And use the CV tool they do; they swap around colors, they rewrite lines, mess around with fonts. THEY ADD A HOBBY SECTION, as if corporate cared about our unicycle riding lessons from 4th grade.

And what a work of art did it end up being. That Helvetica lookalike font is worth every cent. You've found a shade of grey which no other candidate ever used for their text, and, just to make yourself stand out from the crowd, YOU SPLIT YOUR CV INTO THIRDS! THIRDS! 

I think you're ready to work. Hell, with such a CV, you shouldn't even need to work. The fact that HR had the opportunity to read such a finely crafted work of art should earn you at least 40 per hour as a CV guru. All you have to do is click that download button...

BUT ALAS, PERIL! The letters materialize before your eyes, oh, those horrid letters. AND THEY ASK YOU TO PAY. TO PAY THE COST. THE ULTIMATE COST. THE COST OF 1$ (and, after 2 weeks, 14.99$ recurring monthly, by purchasing this product you waive your right to vote and reproduce).

But what about all that work? The hours you spent choosing the squiggles for your H's. The careful phrasing and arrangement on the page! You MUST pay. You've already done so much. 

And you shall pay... unless you've got a friend like me ;)

## History (Less Dramatic)

Look. Websites suck. They make you waste hours of your life without any mention of them being paid services, and, after you've sunken god knows how many hours, they bet on the sunken cost fallacy and try to sell you 
the CV you've created ( plus whatever other hidden costs ). I'm all for paying, as long as the price IS WRITTEN ON THE FRONT OF THE PRODUCT. No caveats, no gimmicks, no "pay to be subscribed to a CV writing tool".
It's a glorified TEX editor with some Javascript to make it look all nice for crying out loud, you don't even
need to use it for an entire year. 

My friend came across one of these websites, and pretty much everything i've described above happened. 

## Solution

In order to entice you to buy the product, these scummy companies will dangle the CV right in front of your face. You cannot download it or interact with it, and they bet that if you were dumb enough to think colors
make your CV stand out, then you're dumb enough to pay 1 buck ( plus a recurring subscription in small print).

The CV, however, doesn't need to be downloaded. You've already got it on your web page. Sure, it's an SVG 
embedded in the HTML code and not readily accesible, but it's there. Why not use their editor for free, then
snatch it from the website. 

The issue with that is that the SVG on your computer will look terrible. However, not terrible enough that it 
wouldn't be fixable with a Python Script :)

## How to

1. You write your CV using the tool offered by the website.
2. "Inspect Element" on the displayed CV, and copy the entire SVG element. Copy in a text file and repeat for all the pages.
3. (Optional) Save both files as HTML. Maybe open them up and see how terrible they look.
4. Use Prettier (high chance you're using it already if you got to this obscure GitHub page) to format HTML code with a cap of 10000000000 characters per line. 
5. Use my script on the formatted files.
6. Throw it under a PDF converter if you want it in PDF, then merge the 2 PDFs using a PDF merger.

Voila. You just saved yourself a buck, go buy yourself some orange juice :)

There are some examples thrown in here, have a look at my friend's CV for inspiration :) (names and various details changed for anonimity's sake).

Btw, SVG_Converter is what you want to use. I might end up rewriting some of that stuff to make it look more pleasing, but I likely won't.
