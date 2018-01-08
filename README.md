# TREEMAKER

## Description:

## Department: Layout/matte paint

For shots that required trees with leaves of different colors to be laid out in a large area. This work was done based on an artwork that suggested there were some areas with similar color trees but some areas with variations in the tree leaves.

The plan was to let the matte painting department to create color maps that would have spots of colors on a black background that would decide the color of tree leaves in that area.


## Getting Started
This Code is based on a Tree OTL from Houdini orbolt.
This code brings in an Otl called deciduous tree.So you would need the Otl to get started.
This shelf tool has 2 parts:

		1. Otl importing - IMPORT_TREE_OTL.py

		2. Building GUI - TREE_MAKER.py

## OTL importing
On clicking the shelf tool after selecting the ground plane with enough subdivision the Otl gets imported into the code using
hou.hda.installFile('../tree.otl')

## Building the GUI
This part is to graphically change the ground or repaint or select new image for the ground and to vary the growth, orientation, trunk width etc.
Inaddition to that I have tried to bring randomness in height and orientation of trees

    
## Prerequisites
This tool is built for Houdini
It is tested on Linux and OSX
This code is written using Python 2.7 and PySide
Houdini 15.5 supports Pyside by default.



## Features of the tool

		1.The Tool allows matte paints color map to be projected 
  		on layout’s ground, creating trees with leaves of color based on the painted color

		2.The Tool allows other departments to add paint in houdini to 
  		add/remove a particular color tree using Houdini’s inbuilt paint tool.

		3.The Tool works with all form of terrains.The tree would be created based on normals of surface

		4.The Tool allows the user to change the ground.

		5.The Tool has additional controls to set the orientation, trunk width, growth

		6.The Tool automatically ensures that no tree is created on top of each other

## STEPS:

		1. Select the node in the geometry geometry level which will be the ground plane

		2. Click on the ‘import tree otl’ shelf tool. It create 2 nodes: 
				1. Deciduoustree1 - import tree 
				2. Geo1 - contains all nodes to make tree grow based on the color 
				
## Geo node creation:

		1. Checks for selection of ground if not will display message.
				sel_node = hou.selectedNodes()
				if len(sel_node) < 1:
		   			 hou.ui.displayMessage('select a ground')
					 
		2. Create nodes 
				obj_ctxt = hou.node('obj')
		   		obj = hou.node('obj')
		    		geo = obj.createNode('geo', run_init_scripts=False)
				node=geo.createNode(“nodename”)
				
		3. Set input to all created nodes
				node.setInput(0,node)
				
		4. Set parameter of nodes
				parameter=node.parm(“parm_name”)
				parameter.set(value)
				Or if it is an expression:
				parameter.setExpression(“expression”)
				
		5. Create vop node to grow tree on the image based ground

		6. Two wrangle nodes created named :
				1.Attribwrangle_pscale -for height randomness
				2.Attribwrangle_rotation -for orientation randomness

## Creation of GUI:

		1. Created graphical user interface with pyside

		2. Window title is 'Tree Maker' with a tree icon

		3. Created label for ground path line edit, tree height, fruit on/off,  
		orientation, trunk width, random height and random orientation. Size and position of label is set using setGeometry. Text color style is done by setStyleSheet
				label=QLabel("text")
				self.grnd_path_label = QtGui.QLabel('GROUND PATH', self)
				self.grnd_path_label.setGeometry(5, 120, 200, 30)
				self.grnd_path_label.setStyleSheet('QLabel{color:rgb(200,80,80)}')

	        4. Button to select ground
	        		self.grnd_path_btn = QtGui.QPushButton('SELECT GROUND', self)
	        opens a houdini tree view
	         		grnd = hou.ui.curDesktop().createFloatingPanel(hou.paneTabType.TreeView)
	        selecting new ground and on pressing 'confirm' selects new ground.
	        'Ground path' line edit text takes new path.

	        5. Paint button select paint tool and allows you to paint on the ground
	         		paint_node = hou.node('/obj/geo1//paint1')
	        		paint_node.setSelected(True, True, True) 

	        6. Select image button open 'file open window' and allows to select new image 
	        image for the ground
	        		fl = QtGui.QFileDialog.getOpenFileName()

	        7. Reset button will clear image or painting done on the ground

	        8. Tree growth, fruit on/off, orientaion and trunk width is controlled by a
	        slider and its value is displayed in a spin box
	        		self.tree_orint_slider = QtGui.QSlider(self)
	        		self.tree_orint_val = QtGui.QSpinBox(self)
	        		slider_value = int(self.sender().value())
	        		tree_orint_parm = hou.parm(
		        		                     '/obj/deciduoustree1/treesys1_lsystem1_randseed')
		        	tree_orint_parm.set(slider_value)
		        	self.tree_orientation_val.setValue(slider_value)	                  
		    9. For do on/off randomness on tree height and orientaion checkbox is provided
		    		self.pscale = QtGui.QCheckBox(self)
		    		if state == QtCore.Qt.Checked:
			            x = hou.parm('/obj/geo1/attribwrangle_pscale/snippet')
			            x.set('@pscale=rand(@ptnum)+.3;')
		        	else:
			            x = hou.parm('/obj/geo1/attribwrangle_pscale/snippet')
			            x.set('')
                                           


## FINAL RESULT:

		Reel : ( https://vimeo.com/249388964 )

		Password: reel2018

		Reel Time: 0-1 min


## LIVE SYSTEM
This tool can be easily used in production, as it is built using Houdini and Python
It has been tested and used on Linux and OSX
The tree Otl the tool uses, can be change to any in house asset otl. 

## Built With
		sublime text 2

		github for versioning

## Authors
This code is entirely written by Meera George.
It was developed in production for my previous company,
This is a simplified version of the same code.

## Acknowledgments
I would like to thank
GITHUB, CODEFIGHTS.COM, UDEMY, ODFORCE SCRIPTING FORUM,CG SOCIETY,
SIDEFX FORUM which helped me complete this tool.


