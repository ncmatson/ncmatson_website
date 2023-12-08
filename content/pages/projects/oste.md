Title: OSTE (open source terrain extraction)
[< back to Projects]({filename}../projects.md)

This project was my senior design project which I worked with my frined [Danny Zhao](https://www.linkedin.com/in/dannyzh/).  The goal was to create an open source replacement for LIDAR datasets that one of the professors at SMU was using to predict wireless environments without having to do the traditional drive testing.  We didn't get quite that far but we did end up putting a pretty cool project together.  We developed a simple web app that allowed users to select regions on Google Maps they wanted analyzed.  We then processed satelite images two ways: a deep neural net (which we didn't write, we just built some publicly available code) to classify pixels as buildings, and a contour detection algorithm to get building outlines.  We then took the identified buildings and, using some simple geometry, estimated the ground footprint/area of the identified buildings, which was then highlighted on the map.

One of the interesting things that happened on this project was that we signed early in the semester on for an free academic license with a certain remote sensing/satelite imaging company.  That licesnse was very generous.  It allowed us to request and download thousands of images per minute or something like that.  Later on in the semester, another sr. design team asked us where we were getting our satelite images from because they wanted to use it for their project.  When they went to the website, there was no option for a free academic license, and the cheapest tier that was available only allowed for a few dozen requests per hour!  Fortunately our licesnse didn't seem to have been effected, so we really lucked out!

You can see the code on [github](https://github.com/ncmatson/OSTE).

<div>
    <img src="{static}/images/projects/oste_flowgraph.png" alt="block diagram with example images" width=600px height=auto>
</div>