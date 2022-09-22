This is a program that allows a streamlined workflow for the bridge scour project.
The idea is after gathering sonar data, this program should return 3 things
-A point shape file of the sonar
-An interpolated tiff that is masked by a predifined polygon shapefile
-Logged stats about the kriging project, including a semivariogram, variogram stats, and stats about the kriging
To use the tool, define a domain and range, and enter it into the prompt
load the csvs into the program
load the shapefile into the program
The program should run and output the above 3 things.

KRIGING TYPES:
Best Results: Spherical(nlag ~= 20), *Exponential(nlag ~= 8), Power(n~=20)
Ok Tesult: **Gaussian (nlags ~=20)
Don't bother result: Linear (nlag ~=15)
*Breaks at high value, best result is nlag number before breaking
**Breaks at low values, for example nlag=6
--Recomended to keep weights on (makes a big difference), and exact values equal to true (tho exact values on or off dont effect the result noticably)

VARIOGRAM NOTES:
Variograms are nice, as they allow you to see the interpolation preformance before the execution
If you have a returned bad variogram, you can return to the main page, as executing the interpolation is processor heavy

WORKFLOW
FILES ARE INPUTED -> THE SHAPE FILE IS REPROJECTED TO EPSG 4326 -> THE SONAR DATA CSV'S ARE CONCATINATED ->  A POINT
SHAPEFILE IS MADE FROM THE CSV -> THE KRIGING IS DONE -> THE INTERPOLATION IS CLIPPED BY THE POLYGON SHAPEFILE AND
OUTPUTTED AS A TIFF.