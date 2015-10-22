# classAnalysis

1. Go login and do a course search across all the CS courses (so it returns the classes and everything)
2. Save the page
3. Put this .py file in the same folder as the BuzzPort.htm file
4. Inside the .py file, you can add to 'classes I've taken' etc to remove classes from search.
5. Run in command line (I redirect to file but your call).
6. Note the classes you can sign up for and go sign up.
7. Classes that have openings in waitlist are there too.

This can be modified to look at ALL OMSCS classes and pull out only the ones that have waitlist capacity, or are not full, and should be pretty trivial (maybe you want to do that?).

Initially I was going based on ID's but came across stuff that used the same ID for different courses, so I tried course titles, but the titles aren't the same as what you find on the OMSCS cirriculum page. (I.E. Machine Learning for Trading is now Mach Learn For Trade I think).

Up to you if you want to fiddle more with things, but I'd love to have pull requests :)

