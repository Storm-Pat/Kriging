This is a program that allows a streamlined workflow for the bridge scour project.
The idea is after gathering sonar data, this program should return 3 things
-A point shape file of the sonar
-An interpolated tiff that is masked by a predifined polygon shapefile
-Stats about the kriging project, including a semivariogram, variogram stats, and stats about the kriging
To use the tool, define a domain and range, and enter it into the prompt, as well as the kriging option
load the csvs into the program
load the shapefile into the program
The program should run and output the above 3 things.
NOTE: csvs inputted should be the same as an SLG file converted in ReefMaster.