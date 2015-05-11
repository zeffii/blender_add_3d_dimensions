# blender_add_3d_dimensions
A script to generate a dimension between selected vertices

The original script is by [cwolf3d (Spivak Vladimir)](http://cwolf3d.korostyshev.net/)  
wiki: http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Curve/Dimension  
blender development thread for the file: https://developer.blender.org/T37151#307879  

### Why did I make a repository?

The code is offered as GPL, this permits me to copy and modify the code as long as I also keep it GPL license. My intention is to pep8 the code and experiment a bit more with package structuring in python - the original code as of may 2015 is one massive file (3k+ lines), i'd like to see it modularized. 

A while back (4 years ago from this time of writing) I also wrote a [lightweight calliper script](https://github.com/zeffii/GL-calliper) but it never progressed very far, especially not in the final finesse stage of the leading lines and arrows and 3d text.

### Plan!

first modularize, then make openGL drawing and store drawing information in the objects as json in a string.
